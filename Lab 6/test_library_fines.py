import pytest
from library_fines import late_fine, can_borrow, renewal_status

# --- Tests for late_fine ---

def test_returned_on_time():
    # Student returns on time (within 14 days)
    assert late_fine("student", 10, False) == 0

def test_faculty_late_fine_under_limit():
    # Faculty returns within 30 days, no damage (35 days kept - 30 loan days = 5 days overdue * 1 = 5)
    assert late_fine("faculty", 35, False) == 5

def test_guest_late_fine_capped():
    # Guest overdue long enough to hit the 200 fine cap
    # 14 days loan -> 64 days kept = 50 days overdue * 5 = 250 -> capped at 200
    assert late_fine("guest", 64, False) == 200

def test_fine_with_damage():
    # Student late with damage (+150)
    # 20 days kept -> 6 days overdue * 2 = 12 + 150 = 162
    assert late_fine("student", 20, True) == 162

def test_invalid_member_raises_error():
    with pytest.raises(ValueError, match="unknown member"):
        late_fine("unknown", 10, False)

def test_invalid_days_raises_error():
    with pytest.raises(ValueError, match="invalid days"):
        late_fine("student", -5, False)


# --- Tests for can_borrow ---

def test_can_borrow_student_valid():
    assert can_borrow(1, 0, "student") is True

def test_can_borrow_student_limit_reached():
    assert can_borrow(3, 0, "student") is False

def test_can_borrow_faculty_valid():
    assert can_borrow(5, 50, "faculty") is True

def test_can_borrow_faculty_limit_reached():
    assert can_borrow(10, 0, "faculty") is False

def test_can_borrow_excessive_pending_fine():
    # Pending fine > 100 should block borrowing regardless of books held
    assert can_borrow(0, 105, "student") is False


# --- Tests for renewal_status ---

def test_renewal_status_success():
    assert renewal_status(0, False, 5) == "renewed"

def test_renewal_status_denied_due_to_reservation():
    assert renewal_status(0, True, 5) == "denied"

def test_renewal_status_limit_reached():
    assert renewal_status(2, False, 5) == "limit reached"

def test_renewal_status_overdue():
    assert renewal_status(1, False, -1) == "overdue"

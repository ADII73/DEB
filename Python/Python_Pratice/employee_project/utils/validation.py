# is_valid_employee(employee)
# Returns True only when:
# 1. The name is not empty after removing surrounding spaces.
# 2. The salary is greater than 0.
# Otherwise, returns False.

# utils/validation.py

def is_valid_employee(employee):
    return employee['name'].strip() != "" and employee['salary'] > 0

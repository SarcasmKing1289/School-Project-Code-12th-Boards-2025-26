"""Print employee data according to employee ID via nested dictionaries."""
EMPLOYEES = {
    101: {"name": "Alice", "role": "Engineer"},
    102: {"name": "Bob", "role": "Designer"},
    103: {"name": "Carol", "role": "Manager"},
}

def get_employee(eid):
    return EMPLOYEES.get(eid)

if __name__ == "__main__":
    try:
        eid = int(input("Enter employee ID: ").strip())
        emp = get_employee(eid)
        if emp:
            print(emp)
        else:
            print("Employee not found.")
    except ValueError:
        print("Invalid ID.")

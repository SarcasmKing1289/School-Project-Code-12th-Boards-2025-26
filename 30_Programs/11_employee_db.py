"""Add/remove employees to/from an in-memory employee database (dictionary)."""
def add_employee(db, eid, name, role):
    if eid in db:
        raise KeyError("Employee ID exists.")
    db[eid] = {"name": name, "role": role}

def remove_employee(db, eid):
    db.pop(eid, None)

if __name__ == "__main__":
    db = {}
    while True:
        cmd = input("Command (add/remove/list/quit): ").strip().lower()
        if cmd == "add":
            try:
                eid = int(input("ID: ").strip())
                name = input("Name: ").strip()
                role = input("Role: ").strip()
                add_employee(db, eid, name, role)
                print("Added.")
            except Exception as e:
                print("Error:", e)
        elif cmd == "remove":
            try:
                eid = int(input("ID to remove: ").strip())
                remove_employee(db, eid)
                print("Removed if existed.")
            except ValueError:
                print("Invalid ID.")
        elif cmd == "list":
            for k, v in sorted(db.items()):
                print(k, v)
        elif cmd == "quit":
            break
        else:
            print("Unknown command.")

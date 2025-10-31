"""Store sample user data via nested tuples and print summary."""
def sample_data():
    # (id, (first_name, last_name), (age, country))
    users = (
        (1, ("Alice", "Smith"), (30, "USA")),
        (2, ("Bob", "Jones"), (25, "UK")),
        (3, ("Carol", "Wu"), (28, "Canada")),
    )
    return users

if __name__ == "__main__":
    for uid, name, info in sample_data():
        print(f"ID: {uid}, Name: {name[0]} {name[1]}, Age: {info[0]}, Country: {info[1]}")

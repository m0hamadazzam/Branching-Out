import json


def load_users():
    """Load users from the JSON file."""
    try:
        with open("users.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Error: users.json file not found.")
        return []
    except json.JSONDecodeError:
        print("Error: Invalid JSON format in users.json.")
        return []


def filter_users_by_name(users, name):
    """Return users whose name matches (case-insensitive)."""
    return [user for user in users if user.get("name", "").lower() == name.lower()]


def filter_users_by_age(users, age):
    """Return users whose age matches."""
    return [user for user in users if user.get("age") == age]


def filter_users_by_email(users, email):
    """Return users whose email matches exactly."""
    return [user for user in users if user.get("email") == email]


def print_results(results):
    """Display filtered users in a clear formatted layout."""
    if not results:
        print("\n⚠️  No users found matching your criteria.\n")
        return

    print(f"\n✅ Found {len(results)} user(s):")
    print("-" * 40)

    for i, user in enumerate(results, start=1):
        print(f"User #{i}")
        print(f"  Name : {user.get('name', 'N/A')}")
        print(f"  Age  : {user.get('age', 'N/A')}")
        print(f"  Email: {user.get('email', 'N/A')}")
        print("-" * 40)


def main():
    users = load_users()
    if not users:
        return

    while True:
        filter_option = input("\nFilter by (name, age, or email): ").strip().lower()

        if filter_option not in {"name", "age", "email"}:
            print("Filtering by that option is not supported.")
        else:
            value = input(f"Enter {filter_option}: ").strip()

            if filter_option == "age":
                try:
                    value = int(value)
                except ValueError:
                    print("Age must be a number.")
                    continue

            if filter_option == "name":
                results = filter_users_by_name(users, value)
            elif filter_option == "age":
                results = filter_users_by_age(users, value)
            else:
                results = filter_users_by_email(users, value)

            print_results(results)

        retry = input("\nWould you like to filter again? (y/n): ").strip().lower()
        if retry != "y":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()

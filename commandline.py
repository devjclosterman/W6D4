def main():
    while True:
        print("\nOptions:")
        print("1. Create User")
        print("2. Retrieve Users by Criteria")
        print("3. Update User Profile")
        print("4. Delete Users by Criteria")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")

        if choice == '1':
            create_user()
        elif choice == '2':
            retrieve_users()
        elif choice == '3':
            update_user()
        elif choice == '4':
            delete_users()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose a number from 1 to 5.")

def create_user():
    username = input("Enter username: ")
    age = int(input("Enter age: "))
    gender = input("Enter gender: ")
    address = input("Enter address: ")

    user_id = create_user_with_profile(username, age, gender, address)
    print(f"User created with ID: {user_id}")

def retrieve_users():
    criteria = input("Enter criteria to retrieve users (e.g., age > 25 AND gender = 'Male'): ")
    users = retrieve_users_by_criteria(criteria)
    print("\nRetrieved Users:")
    for user in users:
        print(user)

def update_user():
    user_id = int(input("Enter user ID to update: "))
    age = int(input("Enter new age (press Enter to skip): ") or -1)
    gender = input("Enter new gender (press Enter to skip): ")
    address = input("Enter new address (press Enter to skip): ")

    update_user_profile(user_id, age=age if age != -1 else None, gender=gender or None, address=address or None)
    print("User profile updated successfully.")

def delete_users():
    criteria = input("Enter criteria to delete users (e.g., gender = 'Female'): ")
    delete_users_by_criteria(criteria)
    print("Users deleted successfully.")

if __name__ == "__main__":
    main()


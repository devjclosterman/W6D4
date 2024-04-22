from advanced_user_operations import AdvancedUserOperations
# Initialize AdvancedUserOperations instance
advanced_user_ops = AdvancedUserOperations()
# Test creating a new user with profile information
print("Creating a new user...")
result_create = advanced_user_ops.create_user_with_profile('John Doe', 'john.doe@example.com', 'test123', age=30, gender='Male', address='123 Main St')
print("User creation result:", result_create)
# Test retrieving users based on specified criteria
print("\nRetrieving users...")
users = advanced_user_ops.retrieve_users_by_criteria(min_age=25, max_age=40, gender='Male')
print("Retrieved users:", users)
# Test updating user profile information
print("\nUpdating user profile...")
result_update = advanced_user_ops.update_user_profile('john.doe@example.com', age=35, address='1234 roger rd')
print("User profile update result:", result_update)
# Test deleting users based on specified criteria
print("\nDeleting users...")
result_delete = advanced_user_ops.delete_users_by_criteria(gender='Female')
print("User deletion result:", result_delete)


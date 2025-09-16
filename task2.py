# Task 2: Personalized Greeting

# Take user's first and last name as input
first_name = input("Enter your first name: ").strip()
last_name = input("Enter your last name: ").strip()

# Concatenate to get full name
full_name = f"{first_name} {last_name}"

# Print personalized greeting
print(f"Hello, {full_name}! Welcome to the Python world.")

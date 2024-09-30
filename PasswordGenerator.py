import random
import string

def generate_password(length, complexity):
    if complexity == 1:
        # Low complexity: Digits only
        characters = string.digits
    elif complexity == 2:
        # Medium complexity: Digits and Letters (uppercase and lowercase)
        characters = string.ascii_letters + string.digits
    elif complexity == 3:
        # High complexity: Digits, Letters (uppercase and lowercase), and Special characters
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        print("Invalid complexity level. Please choose 1, 2, or 3.")
        return None
    
    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("=====================================================================")
print("======================== Password Generator =========================")
print("=====================================================================")

while True:
    try:
        length = int(input("Enter your password length: "))
        if length <= 0:
            print("Password length must be greater than 0.")
            continue

        print("=====================================================================")
        print("Choose the complexity of the password:")
        print("1 - Low (Only digits)")
        print("2 - Medium (Letters and digits)")
        print("3 - High (Letters, digits, and special characters)")
        complexity = int(input("Enter complexity level (1, 2, or 3): "))

        password = generate_password(length, complexity)
        if password:
            print("=====================================================================")
            print("Your password: " + password)
            print("=====================================================================")
        
    except ValueError:
        print("Please enter a valid number for password length and complexity.")

    play_again = input("Do you want to generate another password? (yes/no): ").lower()
    if play_again != "yes":
        break
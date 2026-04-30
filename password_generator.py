import random 
import string

def generate_password(length, use_upper, use_digits, use_symbols):
    characters = string.ascii_lowercase
    
    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters or length <= 0:
        return None

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


# Run only if file is executed directly (optional CLI support)
if __name__ == "__main__":
    try:
        length = int(input("Enter password length: "))
        use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_digits = input("Include digits? (y/n): ").lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

        result = generate_password(length, use_upper, use_digits, use_symbols)

        if result:
            print("Generated Password:", result)
        else:
            print("Invalid input or no options selected.")

    except ValueError:
        print("Please enter a valid number.")
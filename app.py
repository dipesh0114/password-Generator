import random
import string

def generate_password(length, use_digits=True, use_symbols=True, use_uppercase=True):
    if length < 3:
        length = 3  # Ensure minimum length
    
    # Base character pool
    characters = string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    if use_uppercase:
        characters += string.ascii_uppercase

    if not characters:
        raise ValueError("Character set is empty. Enable at least one character type.")

    # Ensure at least one character from each enabled set
    password = []

    if use_digits:
        password.append(random.choice(string.digits))
    if use_symbols:
        password.append(random.choice(string.punctuation))
    if use_uppercase:
        password.append(random.choice(string.ascii_uppercase))

    # Fill the rest of the password
    while len(password) < length:
        password.append(random.choice(characters))

    # Shuffle to avoid predictable patterns
    random.shuffle(password)
    return ''.join(password)


def main():
    try:
        num_passwords = int(input("How many passwords do you want to generate? "))
    except ValueError:
        print("Invalid input. Generating 1 password.")
        num_passwords = 1

    print("Minimum password length is 3")

    password_lengths = []
    for i in range(num_passwords):
        try:
            length = int(input(f"Enter the length of Password #{i+1}: "))
            if length < 3:
                print("Too short. Setting to minimum length (3).")
                length = 3
        except ValueError:
            print("Invalid input. Using default length (8).")
            length = 8
        password_lengths.append(length)

    # Feature preferences
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'

    print("\nGenerated Passwords:")
    for i in range(num_passwords):
        password = generate_password(password_lengths[i], use_digits, use_symbols, use_uppercase)
        print(f"Password #{i+1}: {password}")


if __name__ == "__main__":
    main()

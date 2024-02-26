import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def main():
    try:
        num_passwords = int(input("How many passwords do you want to generate? "))
        min_length = int(input(f"Minimum length of password should be  3: ") or 3)

        if min_length < 3:
            min_length = 3

        print(f"Generating {num_passwords} passwords with a minimum length of {min_length}")

        for i in range(num_passwords):
            length = int(input(f"Enter the length of Password #{i+1}: "))
            length = max(length, min_length)
            password = generate_password(length)
            print(f"Password #{i+1}: {password}")

    except ValueError:
        print("Please enter valid integers for the number of passwords and password length.")

if __name__ == "__main__":
    main()

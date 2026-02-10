import secrets
import string
from datetime import datetime

# Simple, interactive and secure password tool

LAST_GENERATED = []

def generate_password(length=12, use_lower=True, use_upper=True, use_digits=True, use_symbols=True):
    chars = ""
    if use_lower: chars += string.ascii_lowercase
    if use_upper: chars += string.ascii_uppercase
    if use_digits: chars += string.digits
    if use_symbols: chars += string.punctuation
    if not chars:
        raise ValueError("No characters selected.")
    return ''.join(secrets.choice(chars) for _ in range(length))

def check_strength(password):
    length = len(password)
    categories = sum([
        any(c.islower() for c in password),
        any(c.isupper() for c in password),
        any(c.isdigit() for c in password),
        any(c in string.punctuation for c in password)
    ])
    if length < 8 or categories < 2:
        return "Weak"
    elif length < 12 or categories < 3:
        return "Medium"
    else:
        return "Strong"

def save_passwords(passwords, filename=None):
    if not passwords:
        print("No passwords to save.")
        return
    if filename is None:
        filename = f"passwords_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    try:
        with open(filename, "w", encoding="utf-8") as f:
            for pwd in passwords:
                f.write(pwd + "\n")
        print(f"\n✅ Passwords saved to {filename}")
    except Exception as e:
        print(f"Error saving file: {e}")

def prompt_bool(prompt, default=True):
    resp = input(prompt).strip().lower()
    if resp == "":
        return default
    return resp not in ("n", "no", "0")

def prompt_int(prompt, default, min_value=None, max_value=None):
    try:
        resp = input(prompt).strip()
        val = int(resp) if resp != "" else default
    except ValueError:
        print("Invalid integer input; using default.")
        val = default
    if min_value is not None and val < min_value:
        print(f"Value too small; using min {min_value}.")
        val = min_value
    if max_value is not None and val > max_value:
        print(f"Value too large; using max {max_value}.")
        val = max_value
    return val

def generate_single_interactive():
    length = prompt_int("Enter password length (default 12): ", 12, 4, 256)
    use_lower = prompt_bool("Include lowercase letters? (Y/n): ", True)
    use_upper = prompt_bool("Include uppercase letters? (Y/n): ", True)
    use_digits = prompt_bool("Include digits? (Y/n): ", True)
    use_symbols = prompt_bool("Include symbols? (Y/n): ", True)

    pwd = generate_password(length, use_lower, use_upper, use_digits, use_symbols)
    strength = check_strength(pwd)
    print(f"\nGenerated Password: {pwd}  |  Strength: {strength}")
    LAST_GENERATED.clear()
    LAST_GENERATED.append(pwd)

    if prompt_bool("Save this password to a TXT file? (y/N): ", False):
        save_passwords(LAST_GENERATED)

def generate_multiple_interactive():
    count = prompt_int("How many passwords to generate? (default 5): ", 5, 1, 1000)
    length = prompt_int("Enter password length (default 12): ", 12, 4, 256)
    use_lower = prompt_bool("Include lowercase letters? (Y/n): ", True)
    use_upper = prompt_bool("Include uppercase letters? (Y/n): ", True)
    use_digits = prompt_bool("Include digits? (Y/n): ", True)
    use_symbols = prompt_bool("Include symbols? (Y/n): ", True)

    passwords = []
    for _ in range(count):
        pwd = generate_password(length, use_lower, use_upper, use_digits, use_symbols)
        strength = check_strength(pwd)
        print(f"\nGenerated Password: {pwd}  |  Strength: {strength}")
        passwords.append(pwd)

    LAST_GENERATED.clear()
    LAST_GENERATED.extend(passwords)

    if prompt_bool("Save these passwords to a TXT file? (y/N): ", False):
        save_passwords(passwords)

def validate_user_password():
    pwd = input("\nEnter the password to validate: ")
    strength = check_strength(pwd)
    print(f"Password Strength: {strength}")

def main():
    print("\n=== Password Tool: generate, validate, save ===\n")
    print("1. Generate a single password")
    print("2. Generate multiple passwords")
    print("3. Validate an existing password")
    print("4. Save last generated passwords to TXT")
    print("5. Exit")

    choice = input("\nEnter your choice (1-5): ").strip()
    if choice == "1":
        generate_single_interactive()
    elif choice == "2":
        generate_multiple_interactive()
    elif choice == "3":
        validate_user_password()
    elif choice == "4":
        if LAST_GENERATED:
            save_passwords(LAST_GENERATED)
        else:
            print("No generated passwords in this session to save.")
    elif choice == "5":
        print("\nExiting. Bye!\n")
        return False
    else:
        print("Invalid choice.")
    return True

if __name__ == "__main__":
    while True:
        cont = main()
        if not cont:
            break
        again = input("\nDo you want to perform another action? (Y/n): ").strip().lower()
        if again == "n":
            print("\nExiting. Bye!\n")
            break

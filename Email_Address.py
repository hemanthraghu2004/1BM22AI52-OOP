import re

def is_valid_email(email):
    # Regular expression for a simple email validation
    email_pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

    # Use the re.match() function to check if the email matches the pattern
    if email_pattern.match(email):
        return True
    else:
        return False

# Example usage:
email_address = "example@email.com"
result = is_valid_email(email_address)

if result:
    print(f"{email_address} is a valid email address.")
else:
    print(f"{email_address} is not a valid email address.")

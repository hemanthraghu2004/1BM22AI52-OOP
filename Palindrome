def is_palindrome(substring):
    # Check if the substring is a palindrome
    return substring == substring[::-1]

def get_palindromes(input_string):
    palindromes = []

    # Iterate through all possible substrings
    for i in range(len(input_string)):
        for j in range(i + 1, len(input_string) + 1):
            substring = input_string[i:j]

            # Check if the substring is a palindrome and not an empty string
            if is_palindrome(substring) and len(substring) > 1:
                palindromes.append(substring)

    return palindromes

# Example usage:
input_string = "level radar python deed civic"
palindromes_result = get_palindromes(input_string)

print(f"Input String: {input_string}")
print(f"Palindromes: {palindromes_result}")

def validate_input(user_input):
    if user_input and isinstance(user_input, str):
        return True
    return False

def convert_to_binary(text):
    """Convert text or number into binary format."""
    # Check if it's a number (like age)
    if text.isdigit():
        return bin(int(text))  # Binary for integers
    else:
        # Convert each character to binary using ASCII
        return " ".join(format(ord(char), "08b") for char in text)


def create_message(name, age, name_binary, age_binary):
        message = (
        f"Hello {name}, you are {age} years old!\n"
        f"Name in binary: {name_binary}\n"
        f"Age in binary: {age_binary}")
        return message
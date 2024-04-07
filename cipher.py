# Define the caesar cipher function.
def caesar_cipher(text):
    """
    Encrypts a message using the Caesar cipher method with a right shift of 5.

    Parameters:
    - text (str): The input text to be encrypted.
    
    Returns:
    - str: The encrypted message.
    """
    # Initialize the empty string. This will be used to accumulate the encoded characters.
    result = ""
    # Define the alphabet used for the cipher.
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    # Define the shift value.
    shift = 5
    
    # Iterate over each character in the input text. This loop goes through each character (char) in the text string one by one.
    for char in text:
        # Check if the current character, converted to lowercase, is in the alphabet string. This is to ensure we only try to shift letters and ignore other characters (like punctuation).
        if char.lower() in alphabet:
            # Find the current position of the character in the alphabet.
            position = alphabet.find(char.lower())
            # Calculate the new position of the character by adding the shift value to its original position. The % 26 ensures that the new position wraps around if it goes beyond the alphabet length.
            new_position = (position + shift) % 26
            # Encrypt the character by finding its new position in the alphabet.
            encrypted_char = alphabet[new_position]
            # If the original character was uppercase, convert the shifted character to uppercase to preserve case.
            if char.isupper():
                encrypted_char = encrypted_char.upper()
            result += encrypted_char
        else:
            # If the character is not a letter, add it to the result without shifting.
            result += char
    
    # Return the final encrypted message.
    return result

# Prompt the user for the text.
text = input("Please enter a sentence: ")

# Print the result of the Caesar cipher function.
print("The encrypted sentence is:", caesar_cipher(text))
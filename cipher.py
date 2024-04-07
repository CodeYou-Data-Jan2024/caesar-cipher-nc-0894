# Define the caesar cipher function.
def caesar_cipher(text, shift, direction):
    """
    Encrypts or decrypts a message using the Caesar cipher method.
    
    Parameters:
    - text (str): The input text to be encrypted or decrypted.
    - shift (int): The number of positions each letter should be shifted.
    - direction (str): Specifies the operation: 'encode' to encrypt, or 'decode' to decrypt.
    
    Returns:
    - str: The encrypted (encoded) or decrypted (decoded) message.
    """
    # Initialize the empty string. This will be used to accumulate the encoded or decoded characters.
    result = ""
    # Define the alphabet used for the cipher.
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    # Iterate over each character in the input text. This loop goes through each character (char) in the text string one by one.
    for char in text:
        # Check if the current character, converted to lowercase, is in the alphabet string. This is to ensure we only try to shift letters and ignore other characters (like punctuation).
        if char.lower() in alphabet:
            # Find the current position of the character in the alphabet.
            position = alphabet.find(char.lower())
            # Shift the character's position based on the direction.
            if direction == 'encode':
                # For encoding, shift forward by 'shift' positions. The % 26 ensures that the new position wraps around if it goes beyond the alphabet length.
                new_position = (position + shift) % 26
            elif direction == 'decode':
                # For decoding, shift backward by 'shift' positions. The % 26 ensures that the new position wraps around if it goes beyond the alphabet length.
                new_position = (position - shift) % 26
            else:
                # If the direction is not recognized, return an error message.
                return "Invalid direction"
            # Add the shifted character to the result string.
            # If the original character was uppercase, convert the shifted character to uppercase.
            if char.isupper():
                result += alphabet[new_position].upper()
            else:
                # Otherwise, keep it lowercase.
                result += alphabet[new_position]
        else:
            # If the character is not a letter, add it to the result without shifting.
            result += char
    
    # Return the final encrypted or decrypted message.
    return result

# Example usage:
# Prompt the user for the text, shift amount, and whether they want to encode or decode.
text = input("Enter the text: ")
shift = int(input("Enter the shift number: "))
direction = input("Encode or Decode? ").lower()

# Print the result of the Caesar cipher function based on user input.
print(caesar_cipher(text, shift, direction))


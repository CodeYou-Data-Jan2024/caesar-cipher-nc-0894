# Define the caesar cipher function.
def caesar_cipher(text):

    # Initialize the empty string. This will be used to accumulate the encoded or decoded characters.
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

# Prompt the user for the text.
text = input("Please enter a sentence: ")

# Print the result of the Caesar cipher function.
print("The encrypted sentence is:", caesar_cipher(text))


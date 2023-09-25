#HERE IS THE KEY
PlainText = "monarchy"

#PlainText = "instruments"
#PlainText = "helloe"

def find_letter_coordinates(letter, matrixlists):
    for row_idx, row in enumerate(matrixlists):
        for col_idx, char in enumerate(row):
            if char == letter:
                return (row_idx, col_idx)
    return None  # Return None if the letter is not found



PlanTextPairs = []

#print(PlainText)
#print(len(PlainText) % 2)


#print(PlainText)
for i in range(0,len(PlainText),2):
    if PlainText[i] == PlainText[i+1]:
        PlainText = PlainText[:i+1] + 'x' + PlainText[i+1:]

if (len(PlainText) % 2 == 1):
     PlainText = PlainText + "z"

for i in range(0,len(PlainText), 2):
        PlanTextPairs.append(PlainText[i] + PlainText[i+1])

#print(PlainText)
#print(PlanTextPairs)


# Your alphabet list
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

letters_in_string = []

for char in PlainText:
    if char.isalpha() and char.lower() not in letters_in_string:
        letters_in_string.append(char.lower())

for char in letters_in_string:
    if char in alphabet:
        alphabet.remove(char)


#print(letters_in_string + alphabet)

matrix = letters_in_string + alphabet

matrixlists = [[],[],[],[],[]]

for i in range (0, 25):
     if i < 5:
        matrixlists[0].append(matrix[i])
     elif i < 10:
        matrixlists[1].append(matrix[i])
     elif i < 15:
        matrixlists[2].append(matrix[i])
     elif i < 20:
        matrixlists[3].append(matrix[i])
     else:
        matrixlists[4].append(matrix[i])

#print(matrixlists)
#print(PlanTextPairs[0][1])

#print(find_letter_coordinates(PlanTextPairs[0][1], matrixlists))

#for i in range (0,5):
#    print(matrixlists[i])

# Existing code for creating the matrix and preparing the plaintext message

# ...

def playfair_encrypt(plaintext, matrixlists):
    # Function to encrypt a plaintext using the Playfair cipher

    # Preprocess the plaintext (same code as before)
    for i in range(0, len(plaintext), 2):
        if plaintext[i] == plaintext[i + 1]:
            plaintext = plaintext[:i + 1] + 'x' + plaintext[i + 1:]

    if (len(plaintext) % 2 == 1):
        plaintext = plaintext + "z"

    plaintext_pairs = [plaintext[i] + plaintext[i + 1] for i in range(0, len(plaintext), 2)]
    
    ciphertext = []

    for pair in plaintext_pairs:
        row1, col1 = find_letter_coordinates(pair[0], matrixlists)
        row2, col2 = find_letter_coordinates(pair[1], matrixlists)

        if row1 == row2:
            ciphertext.append(matrixlists[row1][(col1 + 1) % 5] + matrixlists[row2][(col2 + 1) % 5])
        elif col1 == col2:
            ciphertext.append(matrixlists[(row1 + 1) % 5][col1] + matrixlists[(row2 + 1) % 5][col2])
        else:
            ciphertext.append(matrixlists[row1][col2] + matrixlists[row2][col1])

    return ''.join(ciphertext)

def playfair_decrypt(ciphertext, matrixlists):
    # Function to decrypt a ciphertext using the Playfair cipher

    ciphertext_pairs = [ciphertext[i] + ciphertext[i + 1] for i in range(0, len(ciphertext), 2)]
    
    plaintext = []

    for pair in ciphertext_pairs:
        row1, col1 = find_letter_coordinates(pair[0], matrixlists)
        row2, col2 = find_letter_coordinates(pair[1], matrixlists)

        if row1 == row2:
            plaintext.append(matrixlists[row1][(col1 - 1) % 5] + matrixlists[row2][(col2 - 1) % 5])
        elif col1 == col2:
            plaintext.append(matrixlists[(row1 - 1) % 5][col1] + matrixlists[(row2 - 1) % 5][col2])
        else:
            plaintext.append(matrixlists[row1][col2] + matrixlists[row2][col1])

    return ''.join(plaintext)

# Example plaintext message
plaintext_message = "griffinpwill"

# Encrypt the plaintext
ciphertext = playfair_encrypt(plaintext_message, matrixlists)


# Decrypt the ciphertext
decrypted_message = playfair_decrypt(ciphertext, matrixlists)
print("Decrypted Message:", decrypted_message)
print(f"Encrypting using key: {PlainText}")
print("Making Matrix:")
for i in range (0,5):
    print(matrixlists[i])
print("Encrypted Message:", ciphertext)

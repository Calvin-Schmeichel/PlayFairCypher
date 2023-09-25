#PlainText = "instruments"
#PlainText = "helloe"

def find_letter_coordinates(letter, matrixlists):
    for row_idx, row in enumerate(matrixlists):
        for col_idx, char in enumerate(row):
            if char == letter:
                return (row_idx, col_idx)
    return None  # Return None if the letter is not found

PlainText = "monarchy"

PlanTextPairs = []

#print(PlainText)
#print(len(PlainText) % 2)


print(PlainText)
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

for i in range (0,5):
    print(matrixlists[i])
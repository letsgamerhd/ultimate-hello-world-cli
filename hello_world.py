import time

targetText = "Hello, World!"
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
currentText = ""

for character in targetText:
    if character.isalpha():
        for char in alphabet:
            print(currentText + char)
            time.sleep(0.01)

            if char == character:
                currentText += character
                break
    else:
        currentText += character
        print(currentText)
        time.sleep(0.01)

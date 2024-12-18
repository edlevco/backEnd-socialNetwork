from random import randint

def encrypt(password):
    encrypted = ""
    for char in password:
        encrypted += str((ord(char)*2)+88) + "."

    
    moreLetters = 10 - len(password)
    encrypted += ":"
    if moreLetters > 0:
        for i in range(moreLetters):
            encrypted += str(randint(10, 99))

    return encrypted

def decrypt(password):
    numbers = password.split(".")
    numbers.pop()
    letterArray = []
    for num in numbers:
        letter = chr(int((int(num)-88)/2))
        letterArray.append(letter)
    word = "".join(letterArray)

    return word





        


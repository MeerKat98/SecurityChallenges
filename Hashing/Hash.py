#MeerKat

import hashlib

key = "68e109f0f40ca72a15e05cc22786f8e6"
correct = False
while (correct == False):
    password = input("Enter Password: ")
    password = hashlib.md5(password.encode('utf-8'))
    password = password.hexdigest()
    if (key == password):
        print("Correct! :)")
        correct = True
    else:
        print("Incorrect!!!\nTry again!")

'''
_____________________________________________________________
A very small, very inefficient, but still a working
cracker for MD5 hashes consisting of numbers and letters

Author: An0ny
_____________________________________________________________
'''


import hashlib as h
import random as r
from random import choices
from string import ascii_letters

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print("")
print("_____________________________________________________________\nA very small, very inefficient, but still a working\ncracker for MD5 hashes consisting of numbers and letters\n \nAuthor: An0ny\n_____________________________________________________________")
print("")


#Function for getting the mask to guide the cracking process
def get_mask():
    mask = []
    howmany = int(input("Enter number of total letters here: "))
    for counter in range(0, howmany):
        mask.append(str(input("Enter next mask letter type (str OR int) here: ")))
    print(mask)
    return mask


#Function for cracking all MD5 hashes containing only numbers and letters
def bruteforce():
    wrong = True
    mask = get_mask()
    hash = str(input("Enter md5 hash to crack here: "))
    while wrong:

        guess = ""
        for x in range(0, len(mask)):
            if mask[x] == "str":
                guess += r.choice(ascii_letters)
            if mask[x] == "int":
                guess += str(r.choice(numbers))

        #guess = str(str(r.choice(numbers)) + str(r.choice(numbers)) + str(r.choice(numbers)) + str(r.choice(numbers)))
        #guess = "".join([r.choice(ascii_lowercase) for _ in range(0, len(mask))])
        print("Guessed result: " + guess)
        guess_hash = h.md5(guess.encode('UTF-8'))
        print("Guessed hash: " + guess_hash.hexdigest())
        if guess_hash.hexdigest() == hash:
            wrong = False
    print("")
    print(" >> Cracked hash result: " + guess + " <<")
    print("")
    menu()


#Function for cracking 4 digit pins only
def bruteforce_digit_pin():
    wrong = True
    hash = str(input("Enter md5 hash to crack here: "))
    while wrong:
        guess = str(str(r.choice(numbers)) + str(r.choice(numbers)) + str(r.choice(numbers)) + str(r.choice(numbers)))
        #guess = "".join([r.choice(ascii_lowercase) for _ in range(0, len(mask))])
        print("Guessed result: " + guess)
        guess_hash = h.md5(guess.encode('UTF-8'))
        print("Guessed hash: " + guess_hash.hexdigest())
        if guess_hash.hexdigest() == hash:
            wrong = False
    print("")
    print(" >> Cracked hash result: " + guess + " <<")
    print("")
    menu()

#Menu function for asthetics ;-)
def menu():
    print("This is a simple, ineffective but working tool to crack MD5 hashes using simple python calculations.")
    mode = str(input("What do you want to crack ? (1 = numbers & letters / 2 = 4-digit-pin): "))
    if mode == "1":
        bruteforce()
    if mode == "2":
        bruteforce_digit_pin()
    else:
        menu()


menu()




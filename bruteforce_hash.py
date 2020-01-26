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
blacklist = []

print("")
print("_____________________________________________________________\nA very small, very inefficient, but still a working\ncracker for MD5 hashes consisting of numbers and letters\n \nAuthor: An0ny\n_____________________________________________________________")
print("")


#Function for getting the mask to guide the cracking process
def get_mask():
    mask = []
    howmany = int(input("Enter number of total letters here: "))
    for counter in range(0, howmany):
        mask.append(str(input("Enter next mask letter type (s OR i) here: ")))
    print(mask)
    return mask

#"blacklist" is being used
#Function for cracking all MD5 hashes containing only numbers and letters
def bruteforce():
    wrong = True
    guess_counter = 0
    blacklist_mode = ""
    mask = get_mask()

    if len(set(mask)) == 1:
        if mask[0] == "s":
            blacklist_mode = "string only"
        if mask[0] == "i":
            blacklist_mode = "int only"
    if len(set(mask)) != 1:
        blacklist_mode = "mixed"

    hash = str(input("Enter md5 hash to crack here: "))
    while wrong:
        guess = ""
        for x in range(0, len(mask)):
            if mask[x] == "s":
                guess += r.choice(ascii_letters)
            if mask[x] == "i":
                guess += str(r.choice(numbers))
        if guess not in blacklist:
            blacklist.append(guess)
            guess_counter += 1
            #guess = str(str(r.choice(numbers)) + str(r.choice(numbers)) + str(r.choice(numbers)) + str(r.choice(numbers)))
            #guess = "".join([r.choice(ascii_lowercase) for _ in range(0, len(mask))])
            print("Guessed result: " + guess)
            guess_hash = h.md5(guess.encode('UTF-8'))
            print("Guessed hash: " + guess_hash.hexdigest())

            if blacklist_mode == "string only":
                if len(blacklist) >= 10000:             #Change hard limit of blacklist depending on hardware
                    blacklist.clear()
            if blacklist_mode == "int only":
                if len(blacklist) >= 10000:             #Change hard limit of blacklist depending on hardware
                    blacklist.clear()
            if blacklist_mode == "mixed":
                if len(blacklist) >= 10000:             #Change hard limit of blacklist depending on hardware
                    blacklist.clear()

            if guess_hash.hexdigest() == hash:
                print("")
                print("Blacklist mode: " + blacklist_mode)
                print("")
                print("Wrong guesses: " + str(guess_counter))
                blacklist.clear()
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




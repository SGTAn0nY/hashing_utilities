import random, hashlib
from string import ascii_letters

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
length = 4



def menu():
    print("Dictionary attacks!")
    print("ATTENTION:")
    print(">> Change 'length' for different data length <<")
    operation = str(input("what do you want to do ?\n1 --- Initialise new dictionary\n2 --- Test dictionary\n3 --- Bruteforce hash using dictionary\n4 --- Change mode\n5 --- Change mask\n99 --- Exit\n=> "))
    if operation == "1":
        create_dict()
    if operation == "2":
        test_dict()
    if operation == "3":
        bruteforce()
    if operation == "4":
        set_mode()
    if operation == "5":
        set_mask()
    if operation == "99":
        exit()
    else:
        menu()

def set_mode():
    mode = str(input("1 --- Numbers only\n2 --- String only\n3 --- Mixed string and numbers\n=> "))
    return mode

def set_mask():
    mask = []
    for counter in range(0, length):
        mask.append(str(input("Enter next character of data (i for int / s for string): ")))
    return mask

def create_dict():
    #file = open("D:\coding_etc\projects\python\hashing_utilities\dictattack\i_4_md5.txt", "w+")
    file_path = input("Enter new dictionary path: ")
    file_full_path = file_path + "i_" + str(length) + "_md5.txt"
    file = open(file_full_path, "w+")


    for i in range(0, pow(10, length)):

        guess = ""
        for y in range(0, length):
             guess = guess + str(random.choice(numbers))
        if guess not in file.read():
            print(guess)
            file.write(guess)

            guess_hash = hashlib.md5(guess.encode('UTF-8'))
            file.write(str(guess_hash.hexdigest()))

    file.close()
    menu()

def test_dict():
    wrong = True
    counter = 0
    blacklist = []
    file_open = open("D:\coding_etc\projects\python\hashing_utilities\dictattack\dicts\int_only\i_4_md5.txt", "r")
    file = file_open.read()
    while wrong:
        guess = ""
        for y in range(0, length):
             guess = guess + str(random.choice(numbers))
        if guess not in blacklist:
            blacklist.append(guess)
            print(counter)
            if guess not in file:
                wrong = False
            counter += 1
        if guess in blacklist:
            if len(blacklist) == 10000:
                print("")
                print(">> Checked ", counter, "guesses! <<")
                print(">> Entire file checked, it is complete! <<")
                print("")
                wrong = False
    menu()


def bruteforce():
    file_open = open("D:\coding_etc\projects\python\hashing_utilities\dictattack\dicts\int_only\i_4_md5.txt", "r")
    file = file_open.read()
    index = []
    result = ""
    hash = str(input("Enter hash to crack here:\n=> "))
    try:
        for y in range(0, length):
            index.append(file.index(hash) - length + y)
        for x in range(0, len(index)):
            result = result + file[index[x]]
        print("")
        print(">> Cracked hash result: ", result, " <<")
        print("")
    except:
        print("Failure!")
    menu()


mode = set_mode()
mask = set_mask()

menu()
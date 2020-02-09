import random, hashlib

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
length = 4

def menu():
    print("Dictionary attacks!")
    print("ATTENTION:")
    print(">> Change 'length' for different data length <<")
    operation = str(input("what do you want to do ?\n1 --- Initialise new dictionary\n2 --- Test dictionary\n3 --- Bruteforce hash using dictionary"))
    if operation == "1":
        create_dict()
    if operation == "2":
        test_dict()
    if operation == "3":
        bruteforce()
    else:
        menu()


def create_dict():
    #file = open("D:\coding_etc\projects\python\hashing_utilities\dictattack\i_4_md5.txt", "w+")
    file_path = input("Enter new dictionary path: ")
    file_full_path = file_path + "i_" + str(length) + "_md5.txt"
    file = open(file_full_path, "w+")
    blacklist = []

    while len(blacklist) <= pow(10, length):

        guess = ""
        for y in range(0, length):
             guess = guess + str(random.choice(numbers))
        if guess not in blacklist:
            print(guess)
            file.write(guess)
            blacklist.append(guess)

            guess_hash = hashlib.md5(guess.encode('UTF-8'))
            file.write(str(guess_hash.hexdigest()))

    file.close()
    menu()

def test_dict():
    wrong = True
    counter = 0
    blacklist = []
    file_open = open("D:\coding_etc\projects\python\hashing_utilities\dictattack\i_4_md5.txt", "r")
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
    file_open = open("D:\coding_etc\projects\python\hashing_utilities\dictattack\i_4_md5.txt", "r")
    file = file_open.read()
    index = []
    result = ""
    hash = str(input("Enter hash to crack here: "))
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



menu()
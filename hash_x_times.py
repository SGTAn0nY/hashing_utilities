import hashlib

def hash():
    times = str(input("How many times to hash: "))
    i = int(times)

    data = str(input("Enter data here: "))
    data_bytes = data.encode('UTF-8')
    hash = hashlib.md5(data_bytes)
    print(hash.hexdigest())

    for x in range(0, i-1):
        hash = hashlib.md5(hash.hexdigest().encode('UTF-8'))
        print(hash.hexdigest())
    print("Final hash: ", hash.hexdigest())

hash()
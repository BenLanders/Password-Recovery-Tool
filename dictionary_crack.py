import hashlib

f = open ('dictionary.txt', 'r')
passwordLength = input('Enter password length:')
md5Hash = input('Enter md5 hash:')
salt = input('Enter a salt, if any:')
number = input('Enter number of words in dictionary:')
inputFile = f.read().splitlines()

for i in range(0,int(number)):
    password = inputFile[i]
    print (password)
    passwordSalt = password+salt
    h = hashlib.md5(passwordSalt.encode())
    testHash = str(h.hexdigest())
    print (testHash)
    if testHash == md5Hash:
        print ('Password is: ' + password)
        break

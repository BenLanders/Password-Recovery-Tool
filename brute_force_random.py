import random
import string
import hashlib

letters = string.ascii_letters
passwordLength = input('Enter password length:')
md5Hash = input('Enter md5 hash:')
salt = input('Enter a salt, if any:')

while True:
    testPassword = str( ''.join(random.choice(letters) for i in range(int(passwordLength))))
    print (testPassword)
    testing = testPassword+salt
    h = hashlib.md5(testing.encode())
    testHash = str(h.hexdigest())
    print (testHash)
    
    if testHash == md5Hash:
        print ('Password is ' + testPassword)
        break

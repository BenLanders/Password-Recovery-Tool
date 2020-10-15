import binascii
import itertools
import random
import string
import hashlib
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

def lowerCase(inputHash):
    return inputHash.lower()

def randomPasswordCrack():
    char = (options2.get())
    if char == 'All':
        chars = string.printable
    elif char == 'Lower case':
        chars = string.ascii_lowercase
    elif char == 'Upper case':
        chars = string.ascii_uppercase
    elif char == 'Mixed letters':
        chars = string.ascii_letters
    else:
        chars = string.printable
        
    passwordLength = (e1.get())
    hashType = (options1.get())
    passwordHash = lowerCase(e2.get())
    saltHead = (e3.get())
    saltTail = (e4.get())
    
    while True:
        guess = str( ''.join(random.choice(chars) for i in range(int(passwordLength))))
        guessSalt = saltHead+guess+saltTail
        if hashType == 'md5':
            h = hashlib.md5(guessSalt.encode())
            guessHash = str(h.hexdigest())
        elif hashType == 'SHA256':
            h = hashlib.sha256(guessSalt.encode())
            guessHash = str(h.hexdigest())
        elif hashType == 'SHA1':
            h = hashlib.sha1(guessSalt.encode())
            guessHash = str(h.hexdigest())
        elif hashType =='NTLM':
            guessHash = hashlib.new('md4',guessSalt.encode('utf-16le')).hexdigest()
        else:
            h = hashlib.md5(guessSalt.encode())
            guessHash = str(h.hexdigest())
        print (guess, guessHash)
   
        if guessHash == passwordHash:
           print ('Password is: ' + guess)
           tk.Label(master,text=guess,foreground='red',font=1).grid(row=8, column=1,sticky=tk.W)
           break

def dictionaryCrack():
    tk.Label(master,text='              ',foreground='red',font=1).grid(row=8,column=1,sticky=tk.W)
    master.directory = filedialog.askopenfilename()
    path = master.directory
    f = open (path, 'r')
    passwordLength = (e1.get())
    passwordHash = lowerCase(e2.get())
    hashType = (options1.get())
    saltHead = (e3.get())
    saltTail = (e4.get())
    inputFile = f.read().splitlines()
    count = 0

    for i in inputFile:
        if i:
            count += 1

    for i in range(0,8):
        guess = inputFile[i]
        guessSalt = saltHead+guess+saltTail
        if hashType == 'md5':
            h = hashlib.md5(guessSalt.encode())
            guessHash = str(h.hexdigest())
        elif hashType == 'SHA256':
            h = hashlib.sha256(guessSalt.encode())
            guessHash = str(h.hexdigest())
        elif hashType == 'SHA1':
            h = hashlib.sha1(guessSalt.encode())
            guessHash = str(h.hexdigest())
        elif hashType =='NTLM':
            guessHash = hashlib.new('md4',guessSalt.encode('utf-16le')).hexdigest()
        else:
            h = hashlib.md5(guessSalt.encode())
        print (guess,guessHash)

        if guessHash == passwordHash:
            print ('Password is: ' + guess)
            tk.Label(master,text=guess,foreground='red',font=1).grid(row=8,column=1,sticky=tk.W)
            break

        
def bruteForce():
        tk.Label(master,text='              ',foreground='red',font=1).grid(row=8,column=1,sticky=tk.W)
        passwordLength = int((e1.get())) + 1
        minimum = passwordLength -1
        hashType = (options1.get())
        passwordHash = lowerCase(e2.get())
        saltHead = (e3.get())
        saltTail = (e4.get())
        charSelect = (options2.get())
        if charSelect == 'All':
            chars = string.printable
        elif charSelect == 'Lower case':
            chars = string.ascii_lowercase
        elif charSelect == 'Upper case':
            chars = string.ascii_uppercase
        elif charSelect == 'Mixed letters':
            chars = string.ascii_letters
        else:
            chars = string.printable
            
        for password_length in range(minimum, passwordLength):
            for guess in itertools.product(chars, repeat=password_length):
                guess = ''.join(guess)
                guessSalt = saltHead+guess+saltTail
                if hashType == 'md5':
                    h = hashlib.md5(guessSalt.encode())
                    testHash = str(h.hexdigest())
                elif hashType == 'SHA256':
                    h = hashlib.sha256(guessSalt.encode())
                    testHash = str(h.hexdigest())
                elif hashType == 'SHA1':
                    h = hashlib.sha1(guessSalt.encode())
                    testHash = str(h.hexdigest())
                elif hashType =='NTLM':
                    testHash = hashlib.new('md4',guess.encode('utf-16le')).hexdigest()
                print(guess, testHash)
                
                if testHash == passwordHash:
                    print('Password is: ' + guess) 
                    tk.Label(master,text=guess,foreground='red',font=1).grid(row=8,column=1,sticky=tk.W)
                    break
                

def instructions():
    instruct = tk.Tk()
    instruct.geometry("400x350") 
    instruct.title('Password Recovery: Instructions')
    T = tk.Text(instruct, height = 100, width = 100) 
    l = tk.Label(instruct, text = "Instructions") 
    l.config(font =("Courier", 14)) 
  
    info = """The tool includes three modes.
-Random: generates random passwords until target
 password found.
-Dictionary: enables users to input passwords
 from an external file.
-Brute: iterates through every password
 combination.

Steps
1. Enter the number of characters in the
   password. Not required for Dictionary mode.
2. Enter the password hash.
3. Enter a salt at the head or tail of the
   password. Leave empty if password does not
   contain a salt.
4. Select the hash type.
5. Select the character type.
6. Press either ‘Random’, ‘Dictionary’ or
   ‘Brute’."""

    l.pack() 
    T.pack(side=tk.LEFT)  
  
    T.insert(tk.END, info) 
  
master = tk.Tk()
master.geometry('400x450')
master.title('Password Recovery')

tk.Label(master,foreground='black',font=1,height=1,padx=8,pady=15, 
         text="Password length").grid(row=0,sticky=tk.W)
tk.Label(master,foreground='black',font=1,height=1,padx=8,pady=10,anchor='w', 
         text="Hash").grid(row=1,sticky=tk.W)
tk.Label(master,foreground='black',font=1,height=1,padx=8,pady=10,
         text="Salt (head)").grid(row=2,sticky=tk.W)
tk.Label(master,foreground='black',font=1,height=1,padx=8,pady=10,
         text="Salt (tail)").grid(row=3,sticky=tk.W)
tk.Label(master,foreground='black',font=1,height=1,padx=8,pady=10,
         text="Hash type").grid(row=4,sticky=tk.W)
tk.Label(master,foreground='black',font=1,height=1,padx=8,pady=15, 
         text="Character set").grid(row=5,sticky=tk.W)
tk.Label(master,foreground='black',font=1,height=1,padx=8,pady=10,
         text="Password...").grid(row=8,sticky=tk.W)
 

e1 = tk.Entry(fg='black',bg='yellow',width=20,font=1)
e2 = tk.Entry(fg='black',bg='yellow',width=20,font=1)
e3 = tk.Entry(fg='black',bg='yellow',width=20,font=1)
e4 = tk.Entry(fg='black',bg='yellow',width=20,font=1)


e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)


tk.Button(master, 
          text='Random',font=1,width=9,bg='red',fg='yellow', 
          command=randomPasswordCrack).grid(row=6, 
                                    column=0, 
                                    sticky=tk.W,
                                    padx=10,
                                    pady=5)

tk.Button(master, 
          text='Dictionary',font=1,width=9,bg='red',fg='yellow', 
          command=dictionaryCrack).grid(row=6, 
                                    column=1, 
                                    sticky=tk.W,
                                    padx=0,
                                    pady=5)

tk.Button(master, 
          text='Brute',font=1,width=9,bg='red',fg='yellow', 
          command=bruteForce).grid(row=7, 
                                    column=0, 
                                    sticky=tk.W,
                                    padx=10,
                                    pady=5)

tk.Button(master, 
          text='Instructions',font=1,width=9,bg='red',fg='black', 
          command=instructions).grid(row=7, 
                                    column=1, 
                                    sticky=tk.W,
                                    padx=0,
                                    pady=5)

options1 = tk.StringVar(master)
options1.set('md5') # default value

options2 = tk.StringVar(master)
options2.set('Printable') # default value

om1 =tk.OptionMenu(master, options1, 'md5','SHA256','SHA1','NTLM')
om1.grid(row=4,column=1,sticky=tk.W)

om2 =tk.OptionMenu(master, options2, 'All','Lower case','Upper case','Mixed letters')
om2.grid(row=5,column=1,sticky=tk.W)

tk.mainloop()



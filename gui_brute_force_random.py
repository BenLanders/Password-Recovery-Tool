import random
import string
import hashlib
import tkinter as tk

def crack():
    letters = string.ascii_letters
    passwordLength = (e1.get())
    md5Hash = (e2.get())
    salt = (e3.get())

    while True:
        testPassword = str( ''.join(random.choice(letters) for i in range(int(passwordLength))))
        print (testPassword)
        testing = testPassword+salt
        h = hashlib.md5(testing.encode())
        testHash = str(h.hexdigest())
        print (testHash)
    
        if testHash == md5Hash:
            print ('Password is ' + testPassword)
            tk.Label(master,text=testPassword,font=1).grid(row=3, column=1)
            break

master = tk.Tk()
master.geometry('400x200')
tk.Label(master,foreground='black',font=1,height=1,pady=5, 
         text="Password length").grid(row=0)
tk.Label(master,foreground='black',font=1,height=1,pady=5,anchor='w', 
         text="md5 hash").grid(row=1)
tk.Label(master,foreground='black',font=1,height=1,pady=5,
         text="Salt").grid(row=2)
tk.Label(master,foreground='black',font=1,height=1,pady=5,
         text="Password...").grid(row=3)

e1 = tk.Entry(fg='black',bg='yellow',width=20,font=1)
e2 = tk.Entry(fg='black',bg='yellow',width=20,font=1)
e3 = tk.Entry(fg='black',bg='yellow',width=20,font=1)


e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)


tk.Button(master, 
          text='Crack',font=1,bg='red',fg='yellow', 
          command=crack).grid(row=4, 
                                    column=0, 
                                    sticky=tk.W, 
                                    pady=4)

tk.mainloop()



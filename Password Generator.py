import random as r
import tkinter as tk
chs, pw, l, cl = r'''ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~?''', '', r.randrange (8, 16), [0, 0, 0]
def pw_generate ():
    global pw
    for i in range (l):
        pw += chs [r.randrange (len (chs))]
        ch = pw [i]
        if ch in chs [:26]:
            cl [0] = 1
        elif ch in chs [52:62]:
            cl [1] = 1
        elif ch in chs [62:]:
            cl [2] = 1
pw_generate ()
while sum (cl) != 3:
    pw = ''
    pw_generate ()
print ('Your password is:', pw, sep = '\n')
rt = tk.Tk ()
rt.withdraw ()
rt.clipboard_clear ()
rt.clipboard_append (pw)
rt.update ()
rt.destroy ()
print ('\nand has been copied to clipboard!')

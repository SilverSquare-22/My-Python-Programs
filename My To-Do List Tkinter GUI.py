from tkinter import *
from tkinter import messagebox
import csv
import random as r

# Colour palette
fb = [[['#003D66', '#1AA3FF'], '#99D6FF'], [['#660000', '#FF6666'], '#FFB3B3'], [['#2D2640', '#966CF9'], '#CBB6FC'], [['#004D1C', '#00CC44'], '#66FF99'], [['#4D4D00', '#CCCC00'], '#FFFF66'], [['#4D0040', '#FF80EA'], '#FFC9F6']]
rc = r.randrange (len (fb))

# Creating window
win = Tk ()
win.title ('To-Do List by Anagha')
win.config (bg = fb [rc] [1])
win.geometry ('+0+0')
win.resizable (False, False)
L, N, tl, b, v, bf, c = [], [], [], [], [], [], 0

# Creating label and frame
lab = Label (win, text = 'My To-Do List', font = ('Trebuchet MS', 30), fg = fb [rc] [0] [0], bg = fb [rc] [1])
lab.pack (anchor = 'w', padx = 30, pady = (30, 10))
fr = Frame (win, bg = fb [rc] [1], padx = 30, pady = 30)
fr.pack ()

# Functions
def win_create ():
    global labr, winr, entr
    winr = Toplevel (win)
    winr.config (bg = fb [rc] [1])
    winr.resizable (False, False)
    labr = Label (winr, font = ('Trebuchet MS', 12, 'bold'), fg = fb [rc] [0] [0], bg = fb [rc] [1])
    labr.pack (anchor = 'w', padx = 15)
    entr = Entry (winr, width = 30, font = ('Trebuchet MS', 12))
    entr.pack (anchor = 'w', padx = 15)
def active_disabled ():
    cu = 0
    for i in range (len (L)):
        if L [i] [1] == 1:
            cu += 1
            N [i].config (font = ('Trebuchet MS', 15, 'overstrike'), fg = fb [rc] [0] [1])
        else:
            N [i].config (font = ('Trebuchet MS', 15, 'bold'), fg = fb [rc] [0] [0])
    if cu == len (L):
        butt2.config (state = DISABLED)
    else:
        butt2.config (state = ACTIVE)
    labt.config (text = str (cu) + '/' + str (len (L)) + ' tasks completed')
    cu = 0
def butt_create ():
    global butt2, butt3, labt
    butt2 = Button (fr, text = 'Mark all as done', command = check_all, font = ('Trebuchet MS', 12, 'bold'), fg = fb [rc] [0] [0], activeforeground = fb [rc] [0] [0], width = 15, height = 1)
    butt2.grid (row = 1, column = 3, sticky = 'e', padx = (30, 0))
    butt3 = Button (fr, text = 'Delete All', command = delete_all, font = ('Trebuchet MS', 12, 'bold'), fg = fb [rc] [0] [0], width = 15, height = 1)
    butt3.grid (row = 2, column = 3, sticky = 'e', padx = (30, 0))
    labt = Label (fr, font = ('Trebuchet MS', 12, 'bold'), fg = fb [rc] [0] [0], bg = fb [rc] [1])
    labt.grid (row = 3, column = 3)
    active_disabled ()
def butt_destroy ():
    butt2.destroy ()
    butt3.destroy ()
    labt.destroy ()
def buttd_create ():
    menu = Menu (fr, tearoff = 0)
    buttd = Button (fr, text = '···', font = ('Trebuchet MS', 15), fg = fb [rc] [0] [0], bg = fb [rc] [1], compound = 'right', borderwidth = 0, highlightthickness = 0)
    buttd.grid (row = c - 1, column = 1, sticky = 'e', padx = (120, 20), pady = 5)
    if c == 1:
        for i in range (5):
            dfr = Frame (fr, width = 1, bg = fb [rc] [0] [0])
            dfr.grid (row = i, column = 2, sticky = 'ns')
            bf.append (dfr)
    elif c > 5:
        dfr = Frame (fr, width = 1, bg = fb [rc] [0] [0])
        dfr.grid (row = c - 1, column = 2, sticky = 'ns')
        bf.append (dfr)
    def show_menu ():
        menu.post (buttd.winfo_rootx (), buttd.winfo_rooty ())
    buttd.config (command = show_menu)
    b.append (buttd)
    def rename_task (i = c - 1):
        win_create ()
        winr.title ('Rename Task')
        labr.config (text = 'Enter new name:')
        ot = tl [i] [len (str (tl [i].split ('.') [0])) + 2 :]
        entr.insert (0, ot)
        def rename ():
            if not (entr.get ().isspace () or entr.get () == '' or entr.get () == ot):
                tb = str (i + 1) + '. ' + entr.get ()
                N [i].config (text = tb)
                L [i] [0] = tb
                with open ('To-Do List.csv', 'w', newline = '') as f:
                    csv.writer (f).writerows (L)
                winr.destroy ()
        def abort_rename ():
            winr.destroy ()
        Button (winr, text = 'Cancel', command = abort_rename, font = ('Trebuchet MS', 12, 'bold'), fg = fb [rc] [0] [0], width = 7, height = 1).pack (anchor = 'nw', side = 'right', padx = (0, 10), pady = 10)
        Button (winr, text = 'Rename', command = rename, font = ('Trebuchet MS', 12, 'bold'), fg = fb [rc] [0] [0], width = 7, height = 1).pack (anchor = 'nw', side = 'right', padx = (0, 10), pady = 10)
    def delete_task (i = c - 1):
        global c
        if messagebox.askyesno (title = 'WARNING!', message = 'Delete task no. ' + str (i + 1) + '?', icon = 'warning'):
            N [i].destroy ()
            b [-1].destroy ()
            if i == 0:
                for j in range (5, len (bf)):
                        bf [j].destroy ()
                        bf.pop (j)
            elif i > 4:
                bf [i].destroy ()
                bf.pop (i)
            L.pop (i)
            N.pop (i)
            tl.pop (i)
            b.pop ()
            v.pop (i)
            for j in range (i, len (N)):
                num = str (int (L [j] [0].split ('.') [0]) - 1)
                L [j] [0] = num + L [j] [0] [len (num) :]
                N [j].grid_configure (row = j)
                N [j].config (text = L [j] [0])
            with open ('To-Do List.csv', 'w', newline = '') as f:
                csv.writer (f).writerows (L)
            c -= 1
            active_disabled ()
            if c == 0:
                for j in range (len (bf)):
                    bf [j].destroy ()
                bf.clear ()
                butt_destroy ()
    menu.add_command (label = 'Rename', command = rename_task, font = ('Trebuchet MS', 12, 'bold'))
    menu.add_command (label = 'Delete', command = delete_task, font = ('Trebuchet MS', 12, 'bold'))
def add_task ():
    win_create ()
    winr.title ('Add Task')
    labr.config (text = 'Enter task name:')
    def add ():
        if not (entr.get ().isspace () or entr.get () == ''):
            global L, c, var, labt
            L.append ('')
            c = len (L)
            var, tb = IntVar (value = 0), str (c) + '. ' + entr.get ()
            def check (var = var):
                v [N.index (cb)] = var
                L [N.index (cb)] [1] = var.get ()
                with open ('To-Do List.csv', 'w', newline = '') as f:
                    csv.writer (f).writerows (L)
                active_disabled ()
            cb = Checkbutton (fr, text = tb, variable = var, command = check, font = ('Trebuchet MS', 15, 'bold'), fg = fb [rc] [0] [0], bg = fb [rc] [1])
            cb.grid (row = c - 1, column = 0, sticky = 'w')
            N.append (cb)
            tl.append (tb)
            v.append (var)
            L [N.index (cb)] = [tb, var.get ()]
            with open ('To-Do List.csv', 'w', newline = '') as f:
                csv.writer (f).writerows (L)
            if c == 1:
                butt_create ()
            else:
                active_disabled ()
            buttd_create ()
            winr.destroy ()
    def abort_add ():
        winr.destroy ()
    Button (winr, text = 'Cancel', command = abort_add, font = ('Trebuchet MS', 12, 'bold'), fg = fb [rc] [0] [0], width = 7, height = 1).pack (anchor = 'nw', side = 'right', padx = (0, 10), pady = 10)
    Button (winr, text = 'Add', command = add, font = ('Trebuchet MS', 12, 'bold'), fg = fb [rc] [0] [0], width = 7, height = 1).pack (anchor = 'nw', side = 'right', padx = (0, 10), pady = 10)
def check_all ():
    for i in v:
        i.set (1)
        L [v.index (i)] [1] = 1
        N [v.index (i)].config (font = ('Trebuchet MS', 15, 'overstrike'), fg = fb [rc] [0] [1])
        with open ('To-Do List.csv', 'w', newline = '') as f:
            csv.writer (f).writerows (L)
        labt.config (text = str (len (L)) + '/' + str (len (L)) + ' tasks completed')
        butt2.config (state = DISABLED)
def delete_all ():
    global c
    if messagebox.askyesno (title = 'WARNING!', message = 'Are you sure you want to delete all tasks?\nNote that this action cannot be undone.', icon = 'warning'):
        for i in range (len (L)):
            N [i].destroy ()
            b [i].destroy ()
            bf [i].destroy ()
        L.clear ()
        N.clear ()
        tl.clear ()
        b.clear ()
        bf.clear ()
        v.clear ()
        c = 0
        butt_destroy ()
        with open ('To-Do List.csv', 'w', newline = '') as f:
            pass

# Creating buttons
butt1 = Button (fr, text = 'Add Task', command = add_task, font = ('Trebuchet MS', 12, 'bold'), fg = fb [rc] [0] [0], width = 15, height = 1)
butt1.grid (row = 0, column = 3, sticky = 'e')

# Creating checkboxes
try:
    with open ('To-Do List.csv') as f:
        for i in csv.reader (f):
            c += 1
            var, tb = IntVar (value = int (i [1])), i [0]
            cb = Checkbutton (fr, text = tb, variable = var, font = ('Trebuchet MS', 15, 'bold'), fg = fb [rc] [0] [0], bg = fb [rc] [1])
            cb.grid (row = c - 1, column = 0, sticky = 'w')
            def check (cb = cb, var = var):
                v [N.index (cb)] = var
                L [N.index (cb)] [1] = var.get ()
                with open ('To-Do List.csv', 'w', newline = '') as f:
                    csv.writer (f).writerows (L)
                active_disabled ()
            cb.config (command = check)
            N.append (cb)
            tl.append (tb)
            v.append (var)
            L.append ([tb, var.get ()])
            buttd_create ()
        if c != 0:
            butt_create ()
except FileNotFoundError:
    c = 0

win.mainloop ()

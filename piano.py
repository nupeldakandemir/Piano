import tkinter as tk
import pygame

pygame.mixer.init()

def play_sound(note):
    pygame.mixer.music.load(note)
    pygame.mixer.music.play()

def do(event=None):
    b1.config(relief=tk.SUNKEN)
    play_sound("otalar/nota-do.wav")
    b1.after(50, lambda: b1.config(relief=tk.RAISED))

def re(event=None):
    b2.config(relief=tk.SUNKEN)
    play_sound("otalar/nota-re.wav")
    b2.after(50, lambda: b2.config(relief=tk.RAISED))

def mi(event=None):
    b3.config(relief=tk.SUNKEN)
    play_sound("otalar/nota-mi.wav")
    b3.after(50, lambda: b3.config(relief=tk.RAISED))

def fa(event=None):
    b4.config(relief=tk.SUNKEN)
    play_sound("otalar/nota-fa.wav")
    b4.after(50, lambda: b4.config(relief=tk.RAISED))

def sol(event=None):
    b5.config(relief=tk.SUNKEN)
    play_sound("otalar/nota-sol.wav")
    b5.after(50, lambda: b5.config(relief=tk.RAISED))

def la(event=None):
    b6.config(relief=tk.SUNKEN)
    play_sound("otalar/nota-lya.wav")
    b6.after(50, lambda: b6.config(relief=tk.RAISED))

def si(event=None):
    b7.config(relief=tk.SUNKEN)
    play_sound("otalar/nota-si.wav")
    b7.after(50, lambda: b7.config(relief=tk.RAISED))

def oto():
    f = open('nota.txt')
    s = f.readlines()
    def notalar(i):
        if i < len(s):
            satir = s[i].split()
            def nota(j):
                if j < len(satir):
                    if satir[j].lower() == 'do':
                        do()
                    if satir[j].lower() == 're':
                        re()
                    if satir[j].lower() == 'mi':
                        mi()
                    if satir[j].lower() == 'fa':
                        fa()
                    if satir[j].lower() == 'sol':
                        sol()
                    if satir[j].lower() == 'la':
                        la()
                    if satir[j].lower() == 'si':
                        si()
                    j = j + 1
                    pencere.after(200, lambda: nota(j))
            nota(0)
            i = i + 1
            pencere.after(200 * len(satir) + 1000, lambda: notalar(i))
    notalar(0)

pencere = tk.Tk()
pencere.title('Piano')
pencere.geometry('520x400')

b1 = tk.Button(pencere, text='Do', font='Verdana 14 bold', bg='white', fg='pink', height=10, width=3, command=do)
b1.place(x=50, y=20)
b2 = tk.Button(pencere, text='Re', font='Verdana 14 bold', bg='pink', fg='white', height=10, width=3, command=re)
b2.place(x=110, y=20)
b3 = tk.Button(pencere, text='Mi', font='Verdana 14 bold', bg='white', fg='pink', height=10, width=3, command=mi)
b3.place(x=170, y=20)
b4 = tk.Button(pencere, text='Fa', font='Verdana 14 bold', bg='pink', fg='white', height=10, width=3, command=fa)
b4.place(x=230, y=20)
b5 = tk.Button(pencere, text='Sol', font='Verdana 14 bold', bg='white', fg='pink', height=10, width=3, command=sol)
b5.place(x=290, y=20)
b6 = tk.Button(pencere, text='La', font='Verdana 14 bold', bg='pink', fg='white', height=10, width=3, command=la)
b6.place(x=350, y=20)
b7 = tk.Button(pencere, text='Si', font='Verdana 14 bold', bg='white', fg='pink', height=10, width=3, command=si)
b7.place(x=410, y=20)
b8 = tk.Button(pencere, text='Otomatik', font='Verdana 14 bold', bg='pink', fg='white', height=1, width=10, command=oto)
b8.place(x=200, y=300)

pencere.bind('<a>', lambda event: on_key(event, 'do'))
pencere.bind('<s>', lambda event: on_key(event, 're'))
pencere.bind('<d>', lambda event: on_key(event, 'mi'))
pencere.bind('<f>', lambda event: on_key(event, 'fa'))
pencere.bind('<g>', lambda event: on_key(event, 'sol'))
pencere.bind('<h>', lambda event: on_key(event, 'lya'))
pencere.bind('<j>', lambda event: on_key(event, 'si'))
pygame.mixer.init()

def play_sound(note):
    pygame.mixer.music.load(note)
    pygame.mixer.music.play()

def on_key(event, note):
    play_sound(f"otalar/nota-{note}.wav")

pencere.mainloop()

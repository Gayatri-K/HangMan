from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

window = Tk()

window.title("HANGMAN! His life is in your hands")
window.geometry("900x700")
chances=5;
image_paths=['h6.png','h5.png','h4.png','h3.png','h2.png','h1.png']
img = Image.open(image_paths[chances])
img = img.resize((200, 200), Image.ANTIALIAS)
img= ImageTk.PhotoImage(img)
panel = Label(window, image = img)
panel.grid(column=0, row=0)
answer_arr=[]
def clicked(alphabet):
    global chances
    answer= "TECHNOPATHS";
    if alphabet in answer: #Its checks whether the albpbet is there in the answer

        if alphabet=="T":
            btn01["text"] =btn09["text"]= alphabet;
        elif alphabet=="E":
            btn02["text"] = alphabet;
        elif alphabet=="C":
            btn03["text"] = alphabet;
        elif alphabet=="H":
            btn04["text"] =btn010["text"]= alphabet;
        elif alphabet=="N":
            btn05["text"] = alphabet;
        elif alphabet=="O":
            btn06["text"] = alphabet;
        elif alphabet=="P":
            btn07["text"] = alphabet;
        elif alphabet=="A":
            btn08["text"] = alphabet;
        elif alphabet=="S":
            btn011["text"] = alphabet;
          
    else:
        chances = chances - 1;
        txt="Chances remaining "+str(chances);
        label1.configure(text=txt)
        image = Image.open(image_paths[chances])
        image = image.resize((200, 200), Image.ANTIALIAS)
        imgnew = ImageTk.PhotoImage(image)
        panel.configure(image=imgnew)
        panel.image = imgnew
        
        if chances<1:
            messagebox.showinfo("Loose to guess","Hanged!"+"\nCorrect word : TECHNOPATHS")
            window.destroy()
    if btn01["text"]=="T" and btn02["text"]=="E" and btn03["text"]=="C" and btn04["text"]=="H" and btn05["text"]=="N" and btn06["text"]=="O" and btn07["text"]=="P" and btn08["text"]=="A" and btn09["text"]=="T" and btn010["text"]=="H" and btn011["text"]=="S":
        messagebox.showinfo("congratulations", "You Won! Great Buddy!")
        window.destroy()
    print(chances)


btn01 = Button(window, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
btn01.grid(column=2, row=0)
btn02 = Button(window, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
btn02.grid(column=3, row=0)
btn03 = Button(window, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
btn03.grid(column=4, row=0)
btn04 = Button(window, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
btn04.grid(column=5, row=0)
btn05 = Button(window, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
btn05.grid(column=6, row=0)
btn06 = Button(window, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
btn06.grid(column=7, row=0)
btn07 = Button(window, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
btn07.grid(column=8, row=0)
btn08 = Button(window, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
btn08.grid(column=9, row=0)
btn09 = Button(window, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
btn09.grid(column=10, row=0)
btn010 = Button(window, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
btn010.grid(column=11, row=0)
btn011 = Button(window, text=" ",bg="white", fg="Black",width=3,height=1,font=('Helvetica','20'))
btn011.grid(column=12, row=0)


btn1 = Button(window, text="A",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("A"))
btn1.grid(column=3, row=1)
btn2 = Button(window, text="B",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("B"))
btn2.grid(column=4, row=1)
btn3 = Button(window, text="C",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("C"))
btn3.grid(column=5, row=1)
btn4 = Button(window, text="D",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("D"))
btn4.grid(column=6, row=1)
btn5 = Button(window, text="E",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("E"))
btn5.grid(column=7, row=1)
btn6 = Button(window, text="F",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("F"))
btn6.grid(column=8, row=1)
btn7 = Button(window, text="G",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("G"))
btn7.grid(column=9, row=1)
btn8 = Button(window, text="H",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("H"))
btn8.grid(column=10, row=1)

btn9 = Button(window, text="I",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("I"))
btn9.grid(column=3, row=2)
btn10 = Button(window, text="J",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("J"))
btn10.grid(column=4, row=2)
btn11= Button(window, text="K",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("K"))
btn11.grid(column=5, row=2)
btn12 = Button(window, text="L",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("L"))
btn12.grid(column=6, row=2)
btn13 = Button(window, text="M",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("M"))
btn13.grid(column=7, row=2)
btn14 = Button(window, text="N",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("N"))
btn14.grid(column=8, row=2)
btn15= Button(window, text="O",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("O"))
btn15.grid(column=9, row=2)
btn16 = Button(window, text="P",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("P"))
btn16.grid(column=10, row=2)

btn17 = Button(window, text="Q",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("Q"))
btn17.grid(column=4, row=3)
btn18 = Button(window, text="R",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("R"))
btn18.grid(column=5, row=3)
btn19 = Button(window, text="S",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("S"))
btn19.grid(column=6, row=3)
btn20 = Button(window, text="T",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("T"))
btn20.grid(column=7, row=3)
btn21 = Button(window, text="U",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("U"))
btn21.grid(column=8, row=3)
btn22 = Button(window, text="V",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("T"))
btn22.grid(column=9, row=3)

btn23 = Button(window, text="W",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("W"))
btn23.grid(column=5, row=4)
btn24 = Button(window, text="X",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("X"))
btn24.grid(column=6, row=4)
btn25 = Button(window, text="Y",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("Y"))
btn25.grid(column=7, row=4)
btn26 = Button(window, text="Z",bg="skyBlue", fg="Black",width=3,height=1,font=('Helvetica','20'),command=lambda: clicked("Z"))
btn26.grid(column=8, row=4)






label1=Label(window,text="Total Chances are : 5")
label1.grid(row=5,column=0)

window.mainloop()


from random import *
from tkinter import *

num="1234567890"
alphanum="abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
spalphanum="abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*(){}"

#passlen=int(input("Enter password length\n"))
#randPass=[ ]

#print("Select the password\n1. Number\n2. Alphabet\n3. Special alpha num\n")
#selecttype=int(input())

#if selecttype==1:
    #for i in range(passlen):
      # randPass.append(choice(num))
#elif(selecttype==2):
    #for i in range(passlen):
       # randPass.append(choice(alphanum))
#else:
    #for i in range(passlen):
      # randPass.append(choice(spalphanum))
        
#result="".join(randPass)

#print("Your random password is :"+result)

def Create_Pass():

    TheChoice=Tchoice.get()
    

    if  TheChoice=="":
        resultBox.delete(0.0,END)
        resultBox.insert(END,"\n Select the type of password you'd like")

    length=int(pass_length.get())
    randPass=[ ]
    for i in range(length):
        randPass.append(choice(TheChoice))

    result="".join(randPass)

    TheResult="\n ***Your Password is : "+result+"  *** \n"

    resultBox.delete(0.0,END)
    resultBox.insert(END,TheResult)


window=Tk()
window.geometry("800x500")
window.title("Ashwin's  Password Generator ")
progName=Label(window,font=('Stencil', 15,'bold'), text="Ashwin 's Password Generator (^_^)", fg="indigo")
progName.grid(row=1,column=3,padx=200,pady=30)

chooseType=Label(window,font=('Times New Roman',15,'bold'),text='Choose a type among the 3')
chooseType.place(relx=.03, rely=.25)

Tchoice= StringVar ( )
Numchoice=Radiobutton(window,font=('corbel',10,'italic'),text="Numeric",variable=Tchoice,value=num)
Numchoice.place(relx=.3,rely=.35)
AlphaNumchoice=Radiobutton(window,font=('corbel',10,'italic'),text="Alphabetic",variable=Tchoice,value=alphanum)
AlphaNumchoice.place(relx=.3,rely=.4)
Salphachoice=Radiobutton(window,font=('corbel',10,'italic'),text="Special",variable=Tchoice,value=spalphanum)
Salphachoice.place(relx=.3,rely=.45)

size=Label(window,text='Size',font=('copperplate Gothic',10, 'bold'))
size.place(relx=.65,rely=.4 )

pass_length=Spinbox(window,from_=8,to=100)
pass_length.place(relx=.73,rely=.4) 
pass_length.config(state='readonly')


GenButton=Button(window,text='Generate',command=Create_Pass)
GenButton.place(relx=.45, rely=.57)

resultBox=Text(window,height=6, width=70)
resultBox.place(relx=.14, rely=.7)




























    

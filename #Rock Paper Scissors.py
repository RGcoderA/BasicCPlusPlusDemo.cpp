#Rock Paper Scissors
import random
from tkinter import Text
from tkinter import Tk, Button, Label,StringVar

window = Tk()
window.title("Rock Paper Scissors") 

USER_SCORE = 0
COMP_SCORE = 0
USER_CHOICE = ""
COMP_CHOICE = ""

def choice_to_number(choice):
    rps = {'rock':0,'paper':1,'scissors':2}
    return rps[choice]

def number_to_choice(number):
    rps={0:'rock',1:'paper',2:'scissors'}
    return rps[number]

def random_computer_choice():
    return random.choice(['rock','paper','scissors'])

def result(human_choice,comp_choice):
    global USER_SCORE
    global COMP_SCORE
    
    user=choice_to_number(human_choice)
    comp=choice_to_number(comp_choice)
    
    if(user==comp):
        print("Tie")
    elif((user-comp)%3==1):
        print("You win")
        USER_SCORE+=1
    else:
        print("Computer wins")
        COMP_SCORE+=1
    text_area = Text(master=window,height=12,width=30)
    text_area.grid(column=0,row=4)
    text_area.insert(END, "Your Choice: "+human_choice+"\nComputer's Choice: "+comp_choice)
    text_area.insert(END, "\nYour Score: "+str(USER_SCORE)) 
    text_area.insert(END, "\nComputer Score: "+str(COMP_SCORE))

def rock():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE='rock'
    COMP_CHOICE=random_computer_choice()
    result(USER_CHOICE, COMP_CHOICE)

def paper():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE='paper'
    COMP_CHOICE=random_computer_choice()
    result(USER_CHOICE, COMP_CHOICE)

def scissors():
    global USER_CHOICE
    global COMP_CHOICE
    USER_CHOICE='scissors'
    COMP_CHOICE=random_computer_choice()
    result(USER_CHOICE, COMP_CHOICE)

button1 = Button(text="       Rock       ",bg="skyblue", command=rock)
button1.grid(row=1,column=0)

button2 = Button(text="       Paper      ",bg="pink", command=paper)  
button2.grid(row=1,column=1)

button3 = Button(text="     Scissors     ",bg="lightgreen", command=scissors)
button3.grid(row=1,column=2)

window.mainloop()


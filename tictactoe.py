from tkinter import *
from tkinter import messagebox

ui=Tk()
ui.geometry('450x480')
ui.config(bg='sienna')

buttons=[

]

def winner(b,currentplayer):
    for row in range(3):
        if b[row][0]==b[row][1]==b[row][2]==currentplayer:
            return True
    for column in range(3):
        if b[0][column]==b[1][column]==b[2][column]==currentplayer:
            return True
    if b[0][0]==b[1][1]==b[2][2]==currentplayer:
        return True
    if b[2][0]==b[1][1]==b[0][2]==currentplayer:
        return True

def checkfull(b):
    for i in range(3):
        for j in range(3):
            if b[i][j]==' ':
                return False
    return True

def game():
    b=[[' ' for _ in range(3)] for _ in range(3)]
    currentplayer='x'
    def handleclick(row,column):
        nonlocal currentplayer
        print(row,column)
        if b[row][column]==' ':
            b[row][column]=currentplayer
            button=buttons[row][column]
            button['text']=currentplayer
            button['state']='disabled'
            if winner(b,currentplayer)==True:
                messagebox.showinfo('winner','The winner is '+currentplayer)
            elif checkfull(b):
                messagebox.showinfo('tie','The game is a tie')

            else:
                if currentplayer=='x':
                    currentplayer='o'
                else:
                    currentplayer='x'
    for i in range(3):
        row=[]
        for j in range(3):
            button=Button(ui,text='',width=20,height=10,command=lambda row=i,column=j:handleclick(row,column))
            print(i,j)
            button.grid(row=i,column=j)
            row.append(button)
        buttons.append(row)
game()



ui.mainloop()

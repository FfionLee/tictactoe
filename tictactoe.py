from tkinter import *

ui=Tk()
ui.geometry('450x480')
ui.config(bg='sienna')

buttons=[

]

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
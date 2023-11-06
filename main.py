
import tkinter as tk
import random
global player


tk.window = tk.Tk()
tk.window.title("Tic-Tac-Toe")
players = ["◯","⚫"]
player = random.choice(players)
buttons = [[0,0,0],
           [0,0,0],
           [0,0,0]]


def newgame():
    player = random.choice(players)
    label.config(text=player+"'s Turn")
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="",bg="#F0F0F0")
            
            
label = tk.Label(text=player + "'s Turn", font=('consolas',40))
label.pack(side="top")

reset_button = tk.Button(text="restart", font=('consolas',20), command=newgame)
reset_button.pack(side="bottom")


def checkthewin():
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="green")
            buttons[row][1].config(bg="green")
            buttons[row][2].config(bg="green")
            return True
    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="green")
            buttons[1][column].config(bg="green")
            buttons[2][column].config(bg="green")
            return True
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][2].config(bg="green")
        return True
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="green")
        buttons[1][1].config(bg="green")
        buttons[2][0].config(bg="green")
        return True
    elif empty() is False:
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="yellow")
        return "Tie"

    else:
        return False
    
    
def taketurns(row, column):
    global player
    if buttons[row][column]['text'] == "" and checkthewin() is False:
        if player == players[0]:
            buttons[row][column]['text'] = player
            if checkthewin() is False:
                player = players[1]
                label.config(text=(players[1]+"'s Turn"))
            elif checkthewin() is True:
                label.config(text=(players[0]+" Wins!"))
            elif checkthewin() == "Tie":
                label.config(text="It's a Tie!")

        else:
            buttons[row][column]['text'] = player
            if checkthewin() is False:
                player = players[0]
                label.config(text=(players[0]+"'s Turn"))
            elif checkthewin() is True:
                label.config(text=(players[1]+" Wins!"))
            elif checkthewin() == "Tie":
                label.config(text="It's a Tie!")
      
                
def empty():
    spaces = 9
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] != "":
                spaces -= 1
    if spaces == 0:
        return False
    else:
        return True
    
frame = tk.Frame(tk.window)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = tk.Button(frame, text="",font=('consolas',40), width=5, 
        height=2, command= lambda row=row, column=column: taketurns(row,column))
        
        buttons[row][column].grid(row=row,column=column)


tk.window.mainloop()


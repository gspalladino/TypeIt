import random
import string
import tkinter as tk


class TypeItGame:
    def __init__(self):
        self.mainWin = tk.Tk()
        self.mainWin['bg'] = 'ivory'
        self.startButton = tk.Button(bg = 'green', text = 'Start Game', padx = 10, pady = 10, command = self.openGameWin)
        self.startButton.grid(row = 0, column =0)

    def openGameWin(self):
        self.gameWin = tk.Toplevel(self.mainWin)
        self.promptCanvas = tk.Canvas(self.gameWin, bg = 'green')
        self.promptCanvas.grid(row = 0, column = 0)
        self.gameWin.bind("<KeyPress>", self.typeIt)
        self.canvasText = self.promptCanvas.create_text(100, 50, text = 'hi')
        # self.promptEntry = tk.Entry(self.gameWin,bg = 'ivory', fg = 'black')
        # self.promptEntry.grid(row=1,column=0)
        self.pointTally = 0
        self.pointTallyLabel = tk.Label(self.gameWin,bg = 'ivory', fg = 'black', text = 0)
        self.pointTallyLabel.grid(row=0,column=1)
    def typeIt(self,event):
        keysym = event.keysym
        if self.pointTally == 0 and keysym in string.ascii_lowercase:
            self.pointTally += 1
            self.labelName(random.choice(string.ascii_lowercase))
            return print('game started')
        while self.pointTally <= 100 and self.pointTally > 0:
            # inpStr = "type " + self.prompt + ":"
            # userInp = input(inpStr)
            if keysym == self.prompt:
                self.pointTally += 1
                self.pointTallyLabel['text'] = self.pointTally
                self.labelName(random.choice(string.ascii_lowercase))
                return print('point total:', self.pointTally)
            else:
                print("you scored ", self.pointTally," points")
                self.gameWin.destroy()
        while self.pointTally > 100 and self.pointTally <= 200:
            prompt = random.choice(string.ascii_letters)
            inpStr = 'type ' + prompt + ":"
            userInp = input(inpStr)
            if userInp == prompt:
                self.pointTally += 1
                print(self.pointTally)
            else:
                print("you scored ", self.pointTally, " points")
                self.gameWin.destroy()
    def labelName(self,prompt):
        self.prompt = prompt
        self.promptCanvas.itemconfig(self.canvasText, text=self.prompt)

    def go(self):
        self.mainWin.mainloop()

if __name__ == '__main__':
    game = TypeItGame()
    game.go()
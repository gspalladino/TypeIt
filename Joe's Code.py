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
        self.promptCanvas.bind("<KeyPress>", self.typeIt)
        self.canvasText = self.promptCanvas.create_text(100, 50, text = '')
        self.promptEntry = tk.Entry(self.gameWin,bg = 'ivory', fg = 'black')
        self.promptEntry.grid(row=1,column=0)
        self.pointTally = 0
        self.pointTallyLabel = tk.Label(self.gameWin,bg = 'ivory', fg = 'black', text = 0)
    def typeIt(self,event):
        keysym = event.keysym
        if self.pointTally == 0 and keysym in string.ascii_lowercase:
            self.pointTally += 1
        while self.pointTally <= 100 and self.pointTally > 0:
            self.prompt = random.choice(string.ascii_lowercase)
            self.canvasText['text'] = self.prompt
            # inpStr = "type " + self.prompt + ":"
            # userInp = input(inpStr)
            if keysym == self.prompt:
                self.pointTally += 1
                self.pointTallyLabel['text'] = self.pointTally
            else:
                print("you scored ", self.pointTally," points")
                break
        while self.pointTally > 100 and self.pointTally <= 200:
            prompt = random.choice(string.ascii_letters)
            inpStr = 'type ' + prompt + ":"
            userInp = input(inpStr)
            if userInp == prompt:
                self.pointTally += 1
                print(self.pointTally)
            else:
                print("you scored ", self.pointTally, " points")
                break
    def go(self):
        self.mainWin.mainloop()

if __name__ == '__main__':
    game = TypeItGame()
    game.go()
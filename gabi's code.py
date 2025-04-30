import random
import string
import tkinter as tk
import PIL.Image as Image
import PIL.ImageTk as ImageTk
from pygame import mixer



class TypeItGame:
    def __init__(self):
        '''makes opening window and references game window'''
        self.mainWin = tk.Tk()
        self.mainWin.geometry("350x450")
        self.mainWin['bg'] = 'ivory'
        self.startButton = tk.Button(bg = 'green', text = 'Start Game', padx = 10, pady = 10, fg='red', font="Comfortaa 40", command = self.openGameWin)
        self.startButton.grid(row = 1, column =0)


        photoOpen = Image.open("images/typeit3.png")


        self.tracPic = ImageTk.PhotoImage(photoOpen)
        imgLabel = tk.Label(self.mainWin, image=self.tracPic)
        imgLabel.grid(row=0, column=0)

    def openGameWin(self):
        '''This is the main game window. Theres a canvas with the bopit image on it.
        There is also a point tally label.'''
        self.gameWin = tk.Toplevel(self.mainWin)

        bgBopit = Image.open("images/bopitbg3.png")
        self.bg_image = ImageTk.PhotoImage(bgBopit)

        mixer.init()
        mixer.music.load("music/beepboop.wav")
        mixer.music.play(-1)


        # self.promptCanvas = tk.Canvas(self.gameWin, bg = 'green', width="350", height="400")
        self.promptCanvas = tk.Canvas(self.gameWin, width="350", height="300", bg="gainsboro")
        self.promptCanvas.grid(row = 0, column = 0)

        self.promptCanvas.create_image(50, 0, image=self.bg_image, anchor='nw')

        self.gameWin.bind("<KeyPress>", self.typeIt)
        self.canvasText = self.promptCanvas.create_text(205, 138, text = 'type to start!', fill='red', font="Comfortaa 40" )
        # self.promptEntry = tk.Entry(self.gameWin,bg = 'ivory', fg = 'black')
        # self.promptEntry.grid(row=1,column=0)

        pointtallyLabelLabel = tk.Label(self.gameWin, bg='ivory', fg='black', text="Points:")
        pointtallyLabelLabel.grid(row=0, column=1, sticky="e")

        self.pointTally = 0
        self.pointTallyLabel = tk.Label(self.gameWin, bg='ivory', fg='black', text=str(self.pointTally))
        self.pointTallyLabel.grid(row=0, column=2, sticky="w")
    def typeIt(self,event):
        '''This function takes a key press as input and checks to see if it matches the prompt given.
        If it does match, it generates a new prompt, if it doesn't it ends the game and opens the death screen'''
        keysym = event.keysym
        lowkeysym = keysym.lower()
        self.position = [(205,138), (205,20), (205,240), (105,175), (320,75)]
        if keysym == 'Shift_L' or keysym == 'Shift_R':
            capital = True
            return print('Shift entered')
        else:
            capital = False
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
                self.openDeathScreen()
                # mixer.music.stop()
                return
        while self.pointTally > 100 and self.pointTally <= 200:
            # prompt = random.choice(string.ascii_letters)
            # inpStr = 'type ' + prompt + ":"
            # userInp = input(inpStr)
            # if userInp == prompt:
            #     self.pointTally += 1
            #     print(self.pointTally)
            # else:
            #     # print("you scored ", self.pointTally, " points")
            #     self.openDeathScreen()
            #     return
            if keysym == self.prompt or lowkeysym == self.prompt.lower() and capital == True:
                self.pointTally += 1
                self.pointTallyLabel['text'] = self.pointTally
                self.labelName(random.choice(string.ascii_letters))
                x, y = random.choice(self.position)
                self.promptCanvas.moveto(self.canvasText, x=x, y=y)
                return print('point total:', self.pointTally)
            else:
                print("you scored ", self.pointTally, " points")
                self.openDeathScreen()
                # mixer.music.stop()
                return
    def labelName(self,prompt):
        '''Renames the prompt on the canvas to the new prompt'''
        self.prompt = prompt
        self.promptCanvas.itemconfig(self.canvasText, text=self.prompt)

    def openDeathScreen(self):
        '''Is called when the user loses. Opens the death screen which shows final point tally.
        Restart button calls playAgain function. Quit button calls quitGame function. '''
        print("Death screen should appear!")
        self.deathScreen = tk.Toplevel(self.mainWin)
        self.deathScreen.title("Game Over")
        self.deathScreen.geometry("350x480")
        self.deathScreen['bg'] = 'gainsboro'

        mixer.music.stop()
        mixer.music.load("music/death.mp3")
        mixer.music.play(-1)

        gameOverLabel = tk.Label(self.deathScreen, text=f"Game over :(\nYou scored {self.pointTally} points.", bg='gainsboro', fg="red",
                                 font="Comfortaa 20")
        gameOverLabel.pack(pady=10)

        brokentypeit = Image.open("images/broken3.png")
        self.broken_image = ImageTk.PhotoImage(brokentypeit)
        brokenImageLabel = tk.Label(self.deathScreen, image=self.broken_image, bg='gainsboro')
        brokenImageLabel.pack(pady=5)

        buttonFrame = tk.Frame(self.deathScreen, bg='gainsboro')
        buttonFrame.pack(pady=10)

        playAgainButton = tk.Button(buttonFrame, text="Play Again!", command=self.playAgain, bg='green', fg='green', font="Comfortaa")
        playAgainButton.pack(side='left', padx=5)

        quitButton = tk.Button(buttonFrame, text="Quit", command=self.quitGame, bg='red', fg='black', font="Comfortaa")
        quitButton.pack(side='left', padx=5)

    def playAgain(self):
        '''Resets game for player by destroying the game window and the death window,
        and reopening the openGameWin'''
        self.gameWin.destroy()
        self.deathScreen.destroy()
        self.openGameWin()

    def quitGame(self):
        '''Destroys the main window'''
        self.mainWin.destroy()

    def go(self):
        '''Begins game play'''
        self.mainWin.mainloop()

if __name__ == '__main__':
    game = TypeItGame()
    game.go()
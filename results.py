from tkinter import *
import answers
from answers import *
from tkinter import ttk

#Constants for window
GAME_WIDTH = 520
GAME_HEIGHT = 520
BG_COLOR = ("#009DDC")
F_COLOR = ('#0D1F2D')
F = ('Raleway', 25,)
BTN_F = ('Raleway', 15)
QF = ('Ubuntu', 15,)

window = Tk()

#set window icon
icon = PhotoImage(file='media/bg_quiz_game.png')
window.iconphoto(True, icon)

#tk button style
style = ttk.Style()
style.theme_use('alt')
style.configure('TButton',
                background = "#004965",
                foreground = 'white',
                relief='flat',
                )
style.map('TButton',  background=[('active','#00425C')])


                    #########################  WINDOW CONFIGURATIONS  #########################


window.title('Simpsons Quiz Game')
window['bg'] = BG_COLOR

#fixed window size
window.geometry("520x520")
window.resizable(0, 0)

#window height and width
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

#window movement on x and y axis
x = int((screen_width / 2) - (GAME_WIDTH / 2))
y = int((screen_height / 2) - (GAME_HEIGHT / 2))

#centralise window to screen
window.geometry("{}x{}+{}+{}".format(GAME_WIDTH, GAME_HEIGHT, x, y))

try:
    score = "You scored \n" + str(int((correct_guesses/(guesses))*100)) + "%"
except ZeroDivisionError:
    score = "Doh! \n You scored Zero."

    ########################  FUNCTIONS  #########################


#Button Function \\quit game
def exit():
    window.destroy()


#show score
question_label = Label(
    window,
    text=score,
    padx=500,
    pady=500,
    bg=BG_COLOR,
    fg="#FFFFFF",
    font=F,
    anchor='center', ).pack()


                              #########################  BUTTONS  #########################


#btn quit
Button(
    window,
    text= "Quit".upper(),
    font=BTN_F,
    command=exit,
    bg=F_COLOR,
    activebackground=F_COLOR,
    fg=F_COLOR,
    height=3
).pack(fill=X, anchor='s',expand=TRUE, side=LEFT, )

window.mainloop()
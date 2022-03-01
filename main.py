from tkinter import *
from tkinter import ttk


#Constants for window
GAME_WIDTH = 520
GAME_HEIGHT = 520
xVelocity = 3
yVelocity = 2
BG_COLOR = ("#009DDC")
F_COLOR = ('#0D1F2D')
F = ('Raleway', 25,)
BTN_F = ('Raleway', 15)

window = Tk()

#Button Function \\quit game
def start_game():
    window.destroy()
    import question1

#tk button style
style = ttk.Style()
style.theme_use('alt')
style.configure('TButton',
                background = "#004965",
                foreground = 'white',
                relief='flat',
                )
style.map('TButton',  background=[('active','#00425C')])

#set window icon
icon = PhotoImage(file='media/bg_quiz_game.png')
window.iconphoto(True, icon)

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

#create canvas
canvas = Canvas(window, width=GAME_WIDTH, height=GAME_HEIGHT)
#btn quit
Button(
    window,
    text= "START".upper(),
    font=BTN_F,
    command=start_game,
    bg=F_COLOR,
    activebackground=F_COLOR,
    fg=F_COLOR,
    height=3
).pack(fill=X, anchor='s',expand=TRUE, side=BOTTOM, )

canvas.pack()

#background photo
bg_photo = PhotoImage(file="media/bg_quiz_game.png")
background = canvas.create_image(0,0, image=bg_photo, anchor=NW)

window.mainloop()
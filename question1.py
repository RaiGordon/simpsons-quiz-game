from tkinter import *
import answers
from answers import *
from tkinter import ttk
from tkinter import messagebox
import time

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


                     ########################  FUNCTIONS  #########################


#Button Function \\next page
def nextPage():
    window.destroy()
    import question2
#Button Function \\quit game
def exit():
    window.destroy()

def choice():
    pass

#Questions function \\Radio buttons
def questions_one():
    global x
    x = StringVar()

    # Question text
    question_label = Label(
        window,
        text=questions[0].upper(),
        padx=500,
        pady=50,
        bg=BG_COLOR,
        fg="#FFFFFF",
        font=F,
        anchor='center', ).pack()

    #Radio button Options
    for i in (options[0]):
        radiobutton = Radiobutton(window,
                    text=i,
                    variable = x,
                    value=i,
                    font=QF,
                    width=100,
                    command=choice(),
                    anchor="w",
                    padx=30,
                    pady=10,
                    bg='#009DDC',
                                  )
        radiobutton.pack(anchor=W, )
#seperator after each option
        canvas = Canvas(window, width=GAME_WIDTH, height=0.2)
        canvas.pack()

#submit button function
def make_choice():
    selection = x.get()
    if selection == "":
        messagebox.showerror(title="ERROR", message="Make a selection.")
    elif selection == options[0][0]:
        answers.correct_guesses +=1
        answers.guesses +=1
        window.destroy()
        import question2
    elif selection == options[0][1]:
        answers.guesses +=1
        window.destroy()
        import question2
    elif selection == options[0][2]:
        answers.guesses +=1
        window.destroy()
        import question2
    else:
        answers.guesses +=1
        window.destroy()
        import question2

#place questions
Label(
    window,
    text=questions_one(),
    bg='#009DDC',
    anchor ='center',).pack()
                              #########################  BUTTONS  #########################

# submit button
submit_button = ttk.Button(
    window,
    text="Submit",
    command=make_choice)

submit_button.pack(
    anchor="center",
    padx=5,
    pady= 0,
    expand=True)
#
# #btn quit
# Button(
#     window,
#     text= "Quit".upper(),
#     font=BTN_F,
#     command=exit,
#     bg=F_COLOR,
#     activebackground=F_COLOR,
#     fg=F_COLOR,
#     height=3
# ).pack(fill=X, anchor='s',expand=TRUE, side=LEFT, )
#
# #btn next page
# Button(
#     window,
#     text="Skip question".upper(),
#     font=BTN_F,
#     command=nextPage,
#     height=3
# ).pack(fill=X, anchor='s', expand=TRUE, side=RIGHT,)

window.mainloop()
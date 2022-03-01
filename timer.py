# ##Countdown Timer
#
#
# class Countdown_timer:
#     for seconds in range(15, 0, -1):
#         # countdown timer label
#         Label(window, text=seconds,  bg=BG_COLOR, padx=3, font=(F, 14, "bold")).grid(row=1, column=1)
#         Label(window, text="seconds left",bg=BG_COLOR, font=(F, 14,)).grid(row=1, column=2, )
#         window.update()
#         time.sleep(1)
#     messagebox.showerror(title="Time's up", message="You ran out of time \n Continue to next question.")
#     window.destroy()
#     import question2
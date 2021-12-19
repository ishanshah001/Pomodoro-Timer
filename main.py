'''
 Pomodoro Technique: The Pomodoro Technique is a time management method.
 It uses a timer to break work into intervals, traditionally 25 minutes in length, separated by short breaks.
 The original technique has six steps:
 1. Decide on the task to be done.
 2. Set the pomodoro timer (typically for 25 minutes).[1]
 3. Work on the task.
 4. End work when the timer rings and take a short break (typically 5–10 minutes).
 5. If you have fewer than three breaks, go back to Step 2 and repeat until you go through all three breaks.
 6. After three breaks are done, take the fourth break and then take a long break (traditionally 20 to 30 minutes).
    Once the long break is finished, return to step 2.
'''

from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer_window=None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    start["state"]=NORMAL
    global timer_window
    global reps
    reps=0
    label.config(text="Timer")
    canvas.itemconfig(timer, text=str("00:00"))
    check_mark.config(text="Work cycles: ")
    window.after_cancel(timer_window)

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    start["state"]=DISABLED
    global reps
    reps+=1
    if reps%8==0:
        tick=check_mark["text"]
        tick+="\u2713"
        check_mark.config(text = tick)
        label.config(text="Long break")
        counter(LONG_BREAK_MIN * 60)
    elif reps%2==0:
        tick = check_mark["text"]
        tick += "\u2713"
        check_mark.config(text=tick)
        label.config(text="Short break")
        counter(SHORT_BREAK_MIN * 60)
        #counter(5)
    else:
        label.config(text="Work")
        counter(WORK_MIN * 60)
        #counter(5)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def counter(count):
    global timer_window
    min=count//60
    sec=count%60
    if sec<10:
        sec="0"+str(sec)
    canvas.itemconfig(timer,text=(str(min)+":"+str(sec)))
    if count>0:
        timer_window=window.after(1000, counter,count-1)
    else:
        start_timer()





# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro App")
window.config(bg=YELLOW,padx="50",pady="50")

label=Label(text="Timer",font=("Arial",45,"bold"))
label.grid(column=1,row=0)

canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
photo=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=photo)
timer=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)

check_mark=Label(text="Work cycles: ",font=20,padx=10,pady=10)
check_mark.grid(column=1,row=3)

start=Button(text="Start",command=start_timer)
start.grid(column=0,row=2)

reset=Button(text="Reset",command=reset_timer)
reset.grid(column=2,row=2)

window.mainloop()

from tkinter import*
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    window.after(1000,count_down,count-1)


# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Pomodoro")
window.config(padx=110,pady=50,bg=YELLOW)

def say_Something(thing):
    print(thing)

canvas=Canvas(width=220,height=225,bg=YELLOW,highlightthickness=0)
tm_img=PhotoImage(file="tomato.png")
canvas.create_image(110,100,image=tm_img
                    )
canvas.create_text(110,112,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(column=2,row=2)

time=Label(text="Timer",fg=GREEN,font=(FONT_NAME,50),bg=YELLOW)
time.grid(column=2,row=0)


Btn1=Button(text="Start",bg=YELLOW,highlightthickness=0)
Btn1.grid(column=0,row=3)

Btn2=Button(text="Reset",bg=YELLOW,highlightthickness=0)
Btn2.grid(column=3,row=3)

check_marks=Label(text="✔",fg=GREEN,bg=YELLOW)
check_marks.grid(column=2,row=3)

window.mainloop()
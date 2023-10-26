from tkinter import *

window = Tk()
window.config(bg="white")
window.geometry("600x800+1100+150")
window.title("TIME TABLE")

'''Main Title'''
can = Canvas(window, width=600, height=110, bg="#01c0bc")
can.pack()
title = Label(window, text="STUDY PLANNER", font=("Norasi", 35))
title.config(bg="#01c0bc", fg="white", width=20, height=1)
title.place(x = 65, y = 15)

'''CANVAS''' 
can = Canvas(window, background="#f5f5f5", width=600, height=800)
can.pack()
can.create_rectangle(25, 380, 350, 135, fill= "#f5f5f5")   #left box
can.create_line(443, 45, 570, 45, fill="lightgrey")   #right time box
can.create_line(420, 75, 570, 75, fill="lightgrey")
can.create_line(455, 105, 570, 105, fill="lightgrey")
can.create_rectangle(370, 390, 580, 160, fill= "#f5f5f5") #right box
can.create_rectangle(370, 555, 580, 433, fill= "#f5f5f5") #right tommorow's box
can.create_rectangle(370, 680, 580, 595, fill= "#f5f5f5") #reminders

'''label'''
lb = Label(window, text="Date      /     /", bg="#f5f5f5")
lb.place(x=40, y=156)
lb.config(font=('Rasa', 17))

lb = Label(window, text="Start Time:", foreground="#01c0bc", bg="#f5f5f5", font=("Norasi", 15))
lb.place(x=363, y=126)
lb = Label(window, text="End Time:", fg="#01c0bc", bg="#f5f5f5", font=("Norasi", 15))
lb.place(x=370, y=156)
lb = Label(window, text="Time Spend:", fg="#01c0bc", bg="#f5f5f5", font=("Norasi", 15))
lb.place(x=350, y=186)
lb = Label(window, text="To Do:", fg="black", bg="#f5f5f5", font=("Norasi", 15))
lb.place(x=40, y=208)  #3 left side box
lb = Label(window, text="Color Code",fg="black",background="#f5f5f5", font=("Norasi", 15))  #right side box
lb.place(x=375, y=275)
lb = Label(window, text="Timetable:", fg="black", bg="#f5f5f5", font=("Norasi", 15))
lb.place(x=50, y=500)  #left timetable
lb = Label(window, text="Tomorrow's task:", fg="black", bg="#f5f5f5", font=("Norasi", 15))
lb.place(x=370, y=505)  #Tomorrow's task
lb = Label(window, text="Reminders:", fg="black", bg="#f5f5f5", font=("Norasi", 15))
lb.place(x=370, y=668) #reminders
lb = Label(window, text="Reading",fg="grey",background="#f5f5f5", font=("Norasi", 15))  #right side box
lb.place(x=393, y=312)
lb = Label(window, text="Exercise",fg="grey",background="#f5f5f5", font=("Norasi", 15))  #right side box
lb.place(x=393, y=343)
lb = Label(window, text="Typewriting",fg="grey",background="#f5f5f5", font=("Norasi", 15))  #right side box
lb.place(x=393, y=372)
lb = Label(window, text="Yt",fg="grey",background="#f5f5f5", font=("Norasi", 15))  #right side box
lb.place(x=393, y=402)
lb = Label(window, text="Homework",fg="grey",background="#f5f5f5", font=("Norasi", 15))  #right side box
lb.place(x=393, y=433)
lb = Label(window, text="Other",fg="grey",background="#f5f5f5", font=("Norasi", 15))  #right side box
lb.place(x=393, y=462)

'''date entry'''
date = Entry(window, bd = 1, borderwidth=0, highlightthickness=0, bg = "#f5f5f5", width=2)
date.place(x = 90, y = 160)
date = Entry(window, bd = 1, borderwidth=0, highlightthickness=0, bg = "#f5f5f5", width=2)
date.place(x = 125, y = 160)
date = Entry(window, bd = 1, borderwidth=0, highlightthickness=0, bg = "#f5f5f5", width=4)
date.place(x = 160, y = 160)
entry = Entry(window, highlightthickness=0, borderwidth=0, bg="#f5f5f5")
entry.place(x=460, y=138, width=100)
entry = Entry(window, highlightthickness=0, borderwidth=0, bg="#f5f5f5")
entry.place(x=460, y=168, width=100)
entry = Entry(window, highlightthickness=0, borderwidth=0, bg="#f5f5f5")
entry.place(x=460, y=198, width=100)

'''timetable'''
entry = Entry(window, width=5, borderwidth=0, highlightthickness=0, bg = "white")
entry.insert(0, "02:00")
entry.place(x=30, y=550)
entry = Entry(window, width=5, bd = 0, border=0, highlightcolor="#fffefe", highlightthickness=0)
entry.place(x=30, y=580)
entry = Entry(window, width=5, bd = 0, border=0, highlightcolor="#fffefe", highlightthickness=0)
entry.place(x=30, y=610)
entry = Entry(window, width=5, bd = 0, border=0, highlightcolor="white", highlightthickness=0)
entry.place(x=30, y=640)
entry = Entry(window, width=5, bd = 0, border=0, highlightcolor="white", highlightthickness=0)
entry.place(x=30, y=670)
entry = Entry(window, width=14, borderwidth=0, highlightthickness=0, bg = "white")
entry.insert(0, "your text here")
entry.place(x=75, y=550)
entry = Entry(window, width=14, bd = 0, border=0, highlightcolor="white", highlightthickness=0)
entry.place(x=75, y=580)
entry = Entry(window, width=14, bd = 0, border=0, highlightcolor="white", highlightthickness=0)
entry.place(x=75, y=610)
entry = Entry(window, width=14, bd = 0, border=0, highlightcolor="white", highlightthickness=0)
entry.place(x=75, y=640)
entry = Entry(window, width=14, bd = 0, border=0, highlightcolor="white", highlightthickness=0)
entry.place(x=75, y=670)
entry = Entry(window, width=5, bd = 0, border=0, highlightcolor="white", highlightthickness=0)
entry.place(x=196, y=550)
entry = Entry(window, width=5, bd = 0, border=0, highlightcolor="white", highlightthickness=0)
entry.place(x=196, y=580)
entry = Entry(window, width=5, bd = 0, border=0, highlightcolor="white", highlightthickness=0)
entry.place(x=196, y=610)
entry = Entry(window, width=5, bd = 0, border=0, highlightcolor="white", highlightthickness=0)
entry.place(x=196, y=640)
entry = Entry(window, width=5, bd = 0, border=0, highlightcolor="white", highlightthickness=0)
entry.place(x=196, y=670)
entry = Entry(window, width=14, bd = 0, border=0, highlightcolor="white", highlightthickness=0)
entry.place(x=241, y=550)
entry = Entry(window, width=14, bd = 0, border=0, highlightcolor="white", highlightthickness=0)
entry.place(x=241, y=580)
entry = Entry(window, width=14, bd = 0, border=0, highlightcolor="white", highlightthickness=0)
entry.place(x=241, y=610)
entry = Entry(window, width=14, bd = 0, border=0, highlightcolor="white", highlightthickness=0)
entry.place(x=241, y=640)
entry = Entry(window, width=14, bd = 0, border=0, highlightcolor="white", highlightthickness=0)
entry.place(x=241, y=670)
entry = Entry(window, width=20, bd = 0, border=0, highlightcolor="white", highlightthickness=0)
entry.place(x=148, y=713)
lb = Label(window, text="Enjoyment Score:", background="white")  #right side box
lb.place(x=30, y=712)
lb = Label(window, text="/10", background="white")  #right side box
lb.place(x=280, y=712)
entry = Entry(window, width=19, bd = 0, border=0, highlightcolor="white", highlightthickness=0)
entry.place(x=156, y=742)
lb = Label(window, text="Productivity Score:", background="white")  #right side box
lb.place(x=30, y=741)
lb = Label(window, text="/10", background="white")  #right side box
lb.place(x=280, y=741)
entry = Entry(window, width=18, bd = 0, border=0, highlightcolor="white", highlightthickness=0)
entry.place(x=166, y=770)
lb = Label(window, text="Time to Finish work:", background="white")  #right side box
lb.place(x=30, y=769) 

'''checkbutton'''
int = Checkbutton(window, background="#f5f5f5",fg="maroon", highlightthickness=0, borderwidth=0)
int.place(x=372, y=323)
int = Checkbutton(window, background="#f5f5f5",fg="blue", highlightthickness=0, borderwidth=0)
int.place(x=372, y=355)
int = Checkbutton(window, background="#f5f5f5",fg="lightgreen", highlightthickness=0, borderwidth=0)
int.place(x=372, y=385)
int = Checkbutton(window, background="#f5f5f5",fg="black", highlightthickness=0, borderwidth=0)
int.place(x=372, y=415)
int = Checkbutton(window, background="#f5f5f5",fg="yellow", highlightthickness=0, borderwidth=0)
int.place(x=372, y=445)
int = Checkbutton(window, background="#f5f5f5",fg="orange", highlightthickness=0, borderwidth=0)
int.place(x=372, y=474)

entry = Entry(window, highlightthickness=0, borderwidth=0, background="#f5f5f5", width=23)   #inside reminders
entry.place(x=380, y=708)
entry = Entry(window, highlightthickness=0, borderwidth=0, background="#f5f5f5", width=23)   #inside reminders
entry.place(x=380, y=730)
entry = Entry(window, highlightthickness=0, borderwidth=0, background="#f5f5f5", width=23)   #inside reminders
entry.place(x=380, y=753)
can.create_line(380, 615, 570, 615, fill="#99dad9")  #inside reminders
can.create_line(380, 638, 570, 638, fill="#99dad9")
can.create_line(380, 661, 570, 661, fill="#99dad9")
entry = Entry(window, highlightthickness=0, borderwidth=0, background="#f5f5f5", width=23)   #Tomorrow's tasks
entry.place(x=380, y=553)
can.create_line(380, 460, 570, 460, fill="#99dad9")
entry = Entry(window, highlightthickness=0, borderwidth=0, background="#f5f5f5", width=23)   #Tomorrow's tasks
entry.place(x=380, y=578)
can.create_line(380, 485, 570, 485, fill="#99dad9")
entry = Entry(window, highlightthickness=0, borderwidth=0, background="#f5f5f5", width=23)   #Tomorrow's tasks
entry.place(x=380, y=603)
can.create_line(380, 510, 570, 510, fill="#99dad9")
entry = Entry(window, highlightthickness=0, borderwidth=0, background="#f5f5f5", width=23)   #Tomorrow's tasks
entry.place(x=380, y=628)
can.create_line(380, 535, 570, 535, fill="#99dad9")

  #left box
can.create_oval(38, 150, 53, 165, fill="#01c0bc", width=1, outline="skyblue")
can.create_oval(38, 185, 53, 200, fill="#01c0bc", width=1, outline="skyblue")
can.create_oval(38, 220, 53, 235, fill="#01c0bc", width=1, outline="skyblue")
can.create_oval(38, 253, 53, 267, fill="#01c0bc", width=1, outline="skyblue")
can.create_oval(38, 285, 53, 300, fill="#01c0bc", width=1, outline="skyblue")
can.create_oval(38, 318, 53, 333, fill="#01c0bc", width=1, outline="skyblue")
can.create_oval(38, 351, 53, 366, fill="#01c0bc", width=1, outline="skyblue")
can.create_oval(183, 150, 198, 165, fill="#f5f5f5", width=1, outline="skyblue")
can.create_oval(183, 220, 198, 235, fill="#f5f5f5", width=1, outline="skyblue")
can.create_oval(183, 253, 198, 267, fill="#f5f5f5", width=1, outline="skyblue")
can.create_oval(183, 185, 198, 200, fill="#f5f5f5", width=1, outline="skyblue")
can.create_oval(183, 285, 198, 300, fill="#f5f5f5", width=1, outline="skyblue")
can.create_oval(183, 318, 198, 333, fill="#f5f5f5", width=1, outline="skyblue")
can.create_oval(183, 351, 198, 366, fill="#f5f5f5", width=1, outline="skyblue")
can.create_line(35, 167, 340, 167, fill="#99dad9")
can.create_line(35, 202, 340, 202, fill="#99dad9")
can.create_line(35, 237, 340, 237, fill="#99dad9")
can.create_line(35, 269, 340, 269, fill="#99dad9")
can.create_line(35, 302, 340, 302, fill="#99dad9")
can.create_line(35, 335, 340, 335, fill="#99dad9")
can.create_line(35, 368, 340, 368, fill="#99dad9")

'''left box entry'''
entry = Entry(window, bg="#f5f5f5",width=15, borderwidth=0, highlightthickness= 0)
entry.place(x=58, y=295)
entry = Entry(window, bg="#f5f5f5",width=15, borderwidth=0, highlightthickness= 0)
entry.place(x=58, y=330)
entry = Entry(window, bg="#f5f5f5",width=15, borderwidth=0, highlightthickness= 0)
entry.place(x=58, y=362)
entry = Entry(window, bg="#f5f5f5",width=15, borderwidth=0, highlightthickness= 0)
entry.place(x=58, y=395)
entry = Entry(window, bg="#f5f5f5",width=15, borderwidth=0, highlightthickness= 0)
entry.place(x=58, y=428)
entry = Entry(window, bg="#f5f5f5",width=15, borderwidth=0, highlightthickness= 0)
entry.place(x=58, y=461)
entry = Entry(window, bg="#f5f5f5",width=15, borderwidth=0, highlightthickness= 0)
entry.insert(0, "Your text here")
entry.place(x=58, y=260)
entry = Entry(window, bg="#f5f5f5",width=17, borderwidth=0, highlightthickness= 0)
entry.place(x=203, y=260)
entry = Entry(window, bg="#f5f5f5",width=17, borderwidth=0, highlightthickness= 0)
entry.place(x=203, y=295)
entry = Entry(window, bg="#f5f5f5",width=17, borderwidth=0, highlightthickness= 0)
entry.place(x=203, y=330)
entry = Entry(window, bg="#f5f5f5",width=17, borderwidth=0, highlightthickness= 0)
entry.place(x=203, y=362)
entry = Entry(window, bg="#f5f5f5",width=17, borderwidth=0, highlightthickness= 0)
entry.place(x=203, y=395)
entry = Entry(window, bg="#f5f5f5",width=17, borderwidth=0, highlightthickness= 0)
entry.place(x=203, y=428)
entry = Entry(window, bg="#f5f5f5",width=17, borderwidth=0, highlightthickness= 0)
entry.place(x=203, y=461)

window.mainloop()
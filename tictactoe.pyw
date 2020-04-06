from tkinter import *
from tkinter import messagebox
import sys

root = Tk()

my_canvas = Canvas(width=190, height=177, bg='white')
my_canvas.place(x=0, y=0)

my_canvas.create_line(61,0, 61, 200, width=5)
my_canvas.create_line(126,0, 126, 200, width=5)
my_canvas.create_line(0,57, 200, 57, width=5)
my_canvas.create_line(0,117, 200, 117, width=5)

circle_ = PhotoImage(file='zero.png')
cross_ = PhotoImage(file='cross.png')

i = 0 # кол-во ходов
a = 0 #переменная, определяющая, рисовать крестик или кружок


p1 = ''
p2 = ''
p3 = ''
p4 = ''
p5 = ''
p6 = ''
p7 = ''
p8 = ''
p9 = ''



def check():
	global i
	i += 1
	if ((p1 == 'o' and p2 == 'o' and p3 == 'o')
	or(p4 == 'o' and p5 == 'o' and p6 == 'o')
	or (p7 == 'o' and p8 == 'o' and p9 == 'o')
	or (p1 == 'o' and p4 == 'o' and p7 == 'o')
	or (p2 == 'o' and p5 == 'o' and p8 == 'o')
	or (p3 == 'o' and p6 == 'o' and p9 == 'o')
	or (p1 == 'o' and p5 == 'o' and p9 == 'o')
	or (p3 == 'o' and p5 == 'o' and p7 == 'o')
	):
		messagebox.showinfo("Win", 'Нолики победили')
		sys.exit()
	elif ((p1 == 'x' and p2 == 'x' and p3 == 'x')
	or(p4 == 'x' and p5 == 'x' and p6 == 'x')
	or (p7 == 'x' and p8 == 'x' and p9 == 'x')
	or (p1 == 'x' and p4 == 'x' and p7 == 'x')
	or (p2 == 'x' and p5 == 'x' and p8 == 'x')
	or (p3 == 'x' and p6 == 'x' and p9 == 'x')
	or (p1 == 'x' and p5 == 'x' and p9 == 'x')
	or (p3 == 'x' and p5 == 'x' and p7 == 'x')
	):
		messagebox.showinfo("Win", 'Крестики победили')
		sys.exit()		
	elif i == 9:
		messagebox.showinfo("", 'Ничья')
		sys.exit()				
def number_ (number):
	global a, p1, p2, p3, p4, p5, p6, p7, p8, p9
	a += 1
	if number == "1":
		button_1.destroy()
		if a % 2 == 0:
			label_circle = Label(image=circle_, bg="white")
			label_circle.place(x=0, y=0)
			p1 = 'o'
			check()
		else:
			label_cross = Label(image=cross_, bg="white")
			label_cross.place(x=0, y=0)
			p1 = 'x'
			check()

	elif number == "2":
		button_2.destroy()
		if a % 2 == 0:
			label_circle = Label(image=circle_, bg="white")
			label_circle.place(x=65, y=0)
			p2 = 'o'
			check()
		else:
			label_cross = Label(image=cross_, bg="white")
			label_cross.place(x=65, y=0)
			p2 = 'x'
			check()
	elif number == "3":
		button_3.destroy()
		if a % 2 == 0:
			label_circle = Label(image=circle_, bg="white")
			label_circle.place(x=130, y=0)
			p3 = 'o'
			check()
		else:
			label_cross = Label(image=cross_, bg="white")
			label_cross.place(x=130, y=0)
			p3 = 'x'
			check()
	elif number == "4":
		button_4.destroy()
		if a % 2 == 0:
			label_circle = Label(image=circle_, bg="white")
			label_circle.place(x=0, y=60)
			p4 = 'o'
			check()
		else:
			label_cross = Label(image=cross_, bg="white")
			label_cross.place(x=0, y=60)
			p4 = 'x'
			check()
	elif number == "5":
		button_5.destroy()
		if a % 2 == 0:
			label_circle = Label(image=circle_, bg="white")
			label_circle.place(x=65, y=60)
			p5 = 'o'
			check()
		else:
			label_cross = Label(image=cross_, bg="white")
			label_cross.place(x=65, y=60)
			p5 = 'x'
			check()
	elif number == "6":
		button_6.destroy()
		if a % 2 == 0:
			label_circle = Label(image=circle_, bg="white")
			label_circle.place(x=130, y=60)			
			p6 = 'o'
			check()
		else:
			label_cross = Label(image=cross_, bg="white")
			label_cross.place(x=130, y=60)
			p6 = 'x'
			check()
	elif number == "7":
		button_7.destroy()
		if a % 2 == 0:
			label_circle = Label(image=circle_, bg="white")
			label_circle.place(x=0, y=120)
			p7 = 'o'
			check()
		else:
			label_cross = Label(image=cross_, bg="white")
			label_cross.place(x=0, y=120)
			p7 = 'x'
			check()
	elif number == "8":
		button_8.destroy()
		if a % 2 == 0:
			label_circle = Label(image=circle_, bg="white")
			label_circle.place(x=65, y=120)
			p8 = 'o'
			check()
		else:
			label_cross = Label(image=cross_, bg="white")
			label_cross.place(x=65, y=120)
			p8 = 'x'
			check()
	elif number == "9":
		button_9.destroy()
		if a % 2 == 0:
			label_circle = Label(image=circle_, bg="white")
			label_circle.place(x=130, y=120)
			p9 = 'o'
			check()
		else:
			label_cross = Label(image=cross_, bg="white")
			label_cross.place(x=130, y=120)
			p9 = 'x'
			check()


button_1 = Button(root, bg="white", width=7, height=3, command = lambda: number_("1"))
button_1.place(x=0, y=0)

button_2 = Button(root, bg="white", width=7, height=3, command = lambda: number_("2"))
button_2.place(x=65, y=0)

button_3 = Button(root, bg="white", width=7, height=3, command = lambda: number_("3"))
button_3.place(x=130, y=0)

button_4 = Button(root, bg="white", width=7, height=3, command = lambda: number_("4"))
button_4.place(x=0, y=60)

button_5 = Button(root, bg="white", width=7, height=3, command = lambda: number_("5"))
button_5.place(x=65, y=60)

button_6 = Button(root, bg="white", width=7, height=3, command = lambda: number_("6"))
button_6.place(x=130, y=60)

button_7 = Button(root, bg="white", width=7, height=3, command = lambda: number_("7"))
button_7.place(x=0, y=120)

button_8 = Button(root, bg="white", width=7, height=3, command = lambda: number_("8"))
button_8.place(x=65, y=120)

button_9 = Button(root, bg="white", width=7, height=3, command = lambda: number_("9"))
button_9.place(x=130, y=120)

root.title(string="TicTacToeGame")
root.minsize(width=190, height=177)
root.maxsize(width=190, height=177)
root['bg'] = 'white'
root.mainloop()

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
# вариации победы
var_1, var_2, var_3, var_4, var_5, var_6, var_7, var_8, var_9, var_10, var_11, var_12, var_13, var_14, var_15, var_16 = 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0

def check():
	global i
	i += 1
	if var_1 == 3 or var_2 == 3 or var_3 == 3 or var_4 == 3 or var_5 == 3 or var_6 == 3 or var_7 == 3 or var_8 == 3:
		messagebox.showinfo("Win", "Нолики победили!")
		sys.exit()
	elif var_9 == 3 or var_10 == 3 or var_11 == 3 or var_12 == 3 or var_13 == 3 or var_14 == 3 or var_15 == 3 or var_16 == 3:
		messagebox.showinfo("Win", "Крестики победили!")
		sys.exit()
	elif i == 9:
		messagebox.showinfo("standoff", "Ничья!")
		sys.exit()

def number_ (number):
	global a, my_canvas, var_1, var_2, var_3, var_4, var_5, var_6, var_7, var_8, var_9, var_10, var_11, var_12, var_13, var_14, var_15, var_16, button_1, button_2, button_3, button_4, button_5, button_6, button_7, button_8, button_9 
	a += 1
	if number == "1":
		button_1.destroy()
		button_1 = ''
		if a % 2 == 0:
			label_circle = Label(image=circle_, bg="white")
			label_circle.place(x=0, y=0)
			var_1 += 1
			var_4 += 1
			var_7 += 1
			check()
		else:
			label_cross = Label(image=cross_, bg="white")
			label_cross.place(x=0, y=0)
			var_9 += 1
			var_12 += 1
			var_15 += 1
			check()

	elif number == "2":
		button_2.destroy()
		button_2 = ''
		if a % 2 == 0:
			label_circle = Label(image=circle_, bg="white")
			label_circle.place(x=65, y=0)
			var_2 += 1
			var_4 += 1
			check()
		else:
			label_cross = Label(image=cross_, bg="white")
			label_cross.place(x=65, y=0)
			var_10 += 1
			var_12 += 1
			check()
	elif number == "3":
		button_3.destroy()
		button_3 = ''
		if a % 2 == 0:
			label_circle = Label(image=circle_, bg="white")
			label_circle.place(x=130, y=0)
			var_3 += 1
			var_4 += 1
			var_8 += 1
			check()
		else:
			label_cross = Label(image=cross_, bg="white")
			label_cross.place(x=130, y=0)
			var_11 += 1
			var_12 += 1
			var_16 += 1
			check()
	elif number == "4":
		button_4.destroy()
		button_4 = ''
		if a % 2 == 0:
			label_circle = Label(image=circle_, bg="white")
			label_circle.place(x=0, y=60)
			var_1 += 1
			var_5 += 1
			check()
		else:
			label_cross = Label(image=cross_, bg="white")
			label_cross.place(x=0, y=60)
			var_9 += 1
			var_13 += 1
			check()
	elif number == "5":
		button_5.destroy()
		button_5 = ''
		if a % 2 == 0:
			label_circle = Label(image=circle_, bg="white")
			label_circle.place(x=65, y=60)
			var_2 += 1
			var_5 += 1
			var_7 += 1
			var_8 += 1
			check()
		else:
			label_cross = Label(image=cross_, bg="white")
			label_cross.place(x=65, y=60)
			var_10 += 1
			var_13 += 1
			var_15 += 1
			var_16 += 1
			check()
	elif number == "6":
		button_6.destroy()
		button_6 = ''
		if a % 2 == 0:
			label_circle = Label(image=circle_, bg="white")
			label_circle.place(x=130, y=60)			
			var_3 += 1
			var_5 += 1
			check()
		else:
			label_cross = Label(image=cross_, bg="white")
			label_cross.place(x=130, y=60)
			var_11 += 1
			var_13 += 1
			check()
	elif number == "7":
		button_7.destroy()
		button_7 = ''
		if a % 2 == 0:
			label_circle = Label(image=circle_, bg="white")
			label_circle.place(x=0, y=120)
			var_1 += 1
			var_6 += 1
			var_8 += 1
			check()
		else:
			label_cross = Label(image=cross_, bg="white")
			label_cross.place(x=0, y=120)
			var_9 += 1
			var_14 += 1
			var_16 += 1
			check()
	elif number == "8":
		button_8.destroy()
		button_8 = ''
		if a % 2 == 0:
			label_circle = Label(image=circle_, bg="white")
			label_circle.place(x=65, y=120)
			var_2 += 1
			var_6 += 1
			check()
		else:
			label_cross = Label(image=cross_, bg="white")
			label_cross.place(x=65, y=120)
			var_10 += 1
			var_14 += 1
			check()
	elif number == "9":
		button_9.destroy()
		button_9 = ''
		if a % 2 == 0:
			label_circle = Label(image=circle_, bg="white")
			label_circle.place(x=130, y=120)
			var_3 += 1
			var_6 += 1
			var_7 += 1
			check()
		else:
			label_cross = Label(image=cross_, bg="white")
			label_cross.place(x=130, y=120)
			var_11 += 1
			var_14 += 1
			var_15 += 1
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

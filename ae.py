from tkinter import *
from tkinter.messagebox import *
from math import pi

root = Tk()
root.title("Area Calculator App")
root.geometry("1000x900+50+50")
f = ("Cambria", 17, "bold")
root.configure(bg="mediumspringgreen")

lab_title = Label(root, text="Area Calculator", font=f, bg="mediumspringgreen")
lab_title.pack(pady=5)

lab_length = Label(root, text="Length:", font=f, bg="mediumspringgreen")
ent_length = Entry(root, font=f, width=10, bg="azure2")
lab_length.pack(pady=5)
ent_length.pack(pady=5)
lab_breadth = Label(root, text="breadth:", font=f, bg="mediumspringgreen")
ent_breadth = Entry(root, font=f, width=10, bg="azure2")
lab_breadth.pack(pady=5)
ent_breadth.pack(pady=5)

lab_height = Label(root, text="Height:", font=f, bg="mediumspringgreen")
ent_height = Entry(root, font=f, width=10, bg="azure2")
lab_height.pack(pady=5)
ent_height.pack(pady=5)

lab_radius = Label(root, text="Radius:", font=f, bg="mediumspringgreen")
ent_radius = Entry(root, font=f, width=10, bg="azure2")
lab_radius.pack(pady=5)
ent_radius.pack(pady=5)


def rectangle():
	length = ent_length.get()
	breadth = ent_breadth.get()
	if length == "" or breadth == "":
		showerror("error", "input cannot be empty")
		return
	if length.isspace() or breadth.isspace():
		showerror("Error", "inputs cannot contain space")
		return

	try:
		length = float(length)
		breadth = float(breadth)
	except Exception:
		showerror("error", "inputs cannot be text")
		return
	if length <= 0 or breadth<=0:
		showerror("Error", "Inputs cannot be negative")
		return

	min_limit = 1
	max_limit = 1000
	if length < min_limit or breadth > max_limit or length > max_limit or breadth < min_limit:
		showerror("invalid Input", f"length and breadtg must be betn {min_limit} and {max_limit}")
		return
	
	area = length * breadth
	msg = "Area of reactangle = " + str(area) 
	lab_result.configure(text=msg)
	showinfo("Sucess", "success")
	ent_length.delete(0, END)
	ent_breadth.delete(0, END)
	ent_length.focus()


def triangle():
	breadth = ent_breadth.get()
	height = ent_height.get()
	if breadth == "" or height == "":
		showerror("error", "input cannot be empty")
		return
	if height.isspace():
		showerror("Error", "inputs cannot contain space")
		return
	try:
		breadth = float(breadth)
		height = float(height)
	except Exception:
		showerror("error", "inputs cannot be text")
		return
	if breadth <= 0 or height <= 0:
		showerror("Error", "inputs cannot be negative")
		return
	
	min_limit = 1
	max_limit = 1000
	if breadth < min_limit or height > max_limit or breadth > max_limit or height < min_limit:
		showerror("invalid Input", f"length and breadth must be betn {min_limit} and {max_limit}")
		return
	area = 0.5 * breadth * height
	msg = "Area of triangle = " + str(area) 
	lab_result1.configure(text=msg)
	showinfo("Sucess", "success")
	ent_breadth.delete(0, END)
	ent_height.delete(0, END)
	ent_breadth.focus()

def square():
	length = ent_length.get()
	if length == "":
		showerror("error", "length cannot be empty")
		return
	if length.isspace():
		showerror("Error", "length cannot contain space")
		return
	try:
		length = float(length)
	except Exception:
		showerror("Error", "length cannot be text")
		return
	if length <=0:
		showerror("error", "length cannot be negative")
		return

	min_limit = 1
	max_limit = 1000
	if length < min_limit or length > max_limit:
		showerror("invalid Input", f"length  must be betn {min_limit} and {max_limit}")
		return
	area = length ** 2


	msg = "Area of square = " + str(area)
	lab_result2.configure(text=msg)
	showinfo("Sucess", "success")
	ent_length.delete(0, END)
	ent_length.focus()

def circle():

	radius = ent_radius.get()
	if radius == "":
		showerror("error", "radius cannot be empty")
		return
	if radius.isspace():
		showerror("Error", "radius cannot contain space")
		return
	try:
		radius = float(radius)
	except Exception:
		showerror("Error", "radius cannot be text")
		return
	if radius <=0:
		showerror("error", "radius cannot be negative")
		return

	min_limit = 1
	max_limit = 1000
	if radius < min_limit or radius > max_limit:
		showerror("invalid Input", f"radius  must be betn {min_limit} and {max_limit}")
		return

	area = 3.14 * radius ** 2
	round_area = round(area, 4)
	msg = "Area of circle = " + str(round_area)
	lab_result3.configure(text=msg)
	showinfo("Sucess", "success")
	ent_radius.delete(0, END)
	ent_radius.focus()

def clear():
	ent_length.delete(0, END)
	ent_breadth.delete(0, END)
	ent_height.delete(0, END)
	ent_radius.delete(0, END)
	lab_result.configure(text="")
	lab_result1.configure(text="")
	lab_result2.configure(text="")
	lab_result3.configure(text="")
	ent_length.focus()

btn_rectangle = Button(root,text = "Calculate Rectangle",font = f,fg="black",bg="rosybrown1",width=17, command=rectangle)
btn_rectangle.pack(pady=3)
lab_result = Label(root, font=f, bg="mediumspringgreen")
lab_result.pack(pady=3)

btn_triangle = Button(root,text = "Calculate Triangle",font = f,fg="black",bg="rosybrown1", width=17, command=triangle)
btn_triangle.pack(pady=3)

lab_result1 = Label(root, font=f, bg="mediumspringgreen")
lab_result1.pack(pady=3)

btn_square = Button(root,text = "Calculate Square",font = f,fg="black",bg="rosybrown1", width=17, command=square)
btn_square.pack(pady=3)

lab_result2 = Label(root, font=f, bg="mediumspringgreen")
lab_result2.pack(pady=5)

btn_circle = Button(root,text = "Calculate Circle",font = f,fg="black",bg="rosybrown1", width=17, command=circle)
btn_circle.pack(pady=3)

lab_result3 = Label(root, font=f, bg="mediumspringgreen")
lab_result3.pack(pady=3)

btn_clear = Button(root,text = "Clear",font = f,fg="black",bg="rosybrown1", width=10, command=clear)
btn_clear.pack(pady=3)
root.mainloop()
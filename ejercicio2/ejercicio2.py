from tkinter import*
import time
tk = Tk()
canvas = Canvas(tk,width=400,height=400)
canvas.pack()
my_imagen = PhotoImage(file="ball.gif")
canvas.create_image(0,0,anchor=NW,image=my_imagen)

tk2 = Tk()
canvas1 = Canvas(tk2,width=400,height=200)
canvas1.pack()
canvas1.create_polygon(10,10,10,60,50,35)

for x in range(0,60):
    canvas1.move(1,5,0)
    tk2.update()
    time.sleep(0.05)
tk.mainloop()


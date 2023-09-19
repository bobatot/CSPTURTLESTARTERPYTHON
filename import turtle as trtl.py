import turtle as trtl

painter = trtl.Turtle()
painter.pensize(10)

painter.penup
painter.goto(0,0)
painter.pendown

circlesz=int(input("how big?"))

painter.circle(circlesz)

painter.penup
painter.goto(0,0)
painter.pendown()

painter.circle(circlesz)


wn = trtl.screen()
wn.mainloop()
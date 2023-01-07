from tkinter import *
from tkinter import ttk

rectOutline = 'black'

def setColor(newcolor):
    global rectOutline
    rectOutline = newcolor

class CubeSideSquare(Canvas):
    def __init__(self, parent, squareClr, sqRow, sqCol, **kwargs):
        super().__init__(parent, width=50, height=50, background='gray75', borderwidth=0, **kwargs)
        self.grid(column=sqCol, row=sqRow, sticky=(N, W, E, S))
        self.create_rectangle(2, 10, 30, 30, fill=squareClr, outline=rectOutline, width=2)
        

class CubeSide(ttk.Frame):
    def __init__(self, parent, sideClr, sideRow, sideCol, **kwargs):
        super().__init__(parent, borderwidth=0, **kwargs)
        self.grid(column=sideCol, row=sideRow, sticky=(N, S, E, W))
        self.squares = ((CubeSideSquare(self, sideClr, 0, 0),
        CubeSideSquare(self, sideClr, 0, 1),
        CubeSideSquare(self, sideClr, 0, 2)),
            (CubeSideSquare(self, sideClr, 1, 0),
        CubeSideSquare(self, sideClr, 1, 1),
        CubeSideSquare(self, sideClr, 1, 2)),
            (CubeSideSquare(self, sideClr, 2, 0),
        CubeSideSquare(self, sideClr, 2, 1),
        CubeSideSquare(self, sideClr, 2, 2))) 

        #self.columnconfigure(0, weight=1)
        #self.columnconfigure(1, weight=1)
        #self.columnconfigure(2, weight=1)

root = Tk()
content = ttk.Frame(root, padding=(5,5,5,5))

content.bind('<Configure>', lambda x: setColor("red")) # doesn't work yet somehow

#s = ttk.Style()

#s.theme_use('classic')
#print(s.theme_use())

#s.configure('TSeparator', background='red')

leftButtons = ttk.Labelframe(content, text='Left menu')
rightButtons = ttk.Labelframe(content, text='Right menu')

ok = ttk.Button(leftButtons, text="Okay")
cancel = ttk.Button(leftButtons, text="Cancel")
mayb = ttk.Button(rightButtons, text="Maybe")

#sep1 = ttk.Separator(content, orient=VERTICAL)
#sep2 = ttk.Separator(content, orient=VERTICAL)

content.grid(column=0, row=0, sticky=(N, S, E, W))
#frame.grid(column=0, row=0, columnspan=3, rowspan=2, sticky=(N, S, E, W))

leftButtons.grid(column=0, row=0, rowspan=3, sticky=(N, W))

ok.grid(column=0, row=0, sticky=(N, W))
cancel.grid(column=0, row=1, sticky=(N, W))

#sep1.grid(column=1, row=0, rowspan=3)

csW = CubeSide(content, sideClr='yellow', sideRow=1, sideCol=1)

csN = CubeSide(content, sideClr='green', sideRow=0, sideCol=2)
csC = CubeSide(content, sideClr='red', sideRow=1, sideCol=2)
csS = CubeSide(content, sideClr='blue', sideRow=2, sideCol=2)
csSS = CubeSide(content, sideClr='orange', sideRow=3, sideCol=2)

csE = CubeSide(content, sideClr='white', sideRow=1, sideCol=3)

#sep2.grid(column=5, row=0, rowspan=4)

rightButtons.grid(column=4, row=0, rowspan=2, sticky=(N, E))

mayb.grid(column=0, row=0, sticky=(N, W))

#namelbl.grid(column=3, row=0, sticky=(N, W), padx=5)
#name.grid(column=3, row=1, sticky=(N,E,W), pady=5, padx=5)


root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

content.columnconfigure(0, weight=1)
#content.columnconfigure(1, weight=1)
#content.columnconfigure(2, weight=1)
#content.columnconfigure(3, weight=1)
content.columnconfigure(4, weight=1)



root.mainloop()

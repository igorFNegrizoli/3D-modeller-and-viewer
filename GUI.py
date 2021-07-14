from tkinter import *
class CanvasMenu(Frame):

    def __init__(self):

        super().__init__()

        self.initToolbar()
        self.initSideBar()

    def initToolbar(self):

        menuBar = Menu(self.master)
        toolBar = LabelFrame(self.master, bd=1, relief=RAISED)

        optionPer = IntVar()

        labelProjection = Label(toolBar, text="Projeção:")
        labelProjection.grid(row=0, column= 1, padx=10)
    
        perspective = Radiobutton(toolBar, text="Perspectiva", variable=optionPer, value=1)
        perspective.grid(row=1, column=2, padx=5, pady=5)

        parallel = Radiobutton(toolBar, text="Paralela", variable=optionPer, value=2)
        parallel.grid(row=1, column=3, padx=5, pady=5)

        optionSom = IntVar()

        labelProjection = Label(toolBar, text="Sombreamento:")
        labelProjection.grid(row=0, column= 5, padx=10)
    
        gouraud = Radiobutton(toolBar, text="Gouraud", variable=optionSom, value=3)
        gouraud.grid(row=1, column=6, padx=5, pady=5)

        phong = Radiobutton(toolBar, text="Phong simplificado", variable=optionSom, value=4)
        phong.grid(row=1, column=7, padx=5, pady=5)

        toolBar.pack(side=TOP, fill=X)
        self.master.config(menu=menuBar)
        self.pack()

    def initSideBar(self):

        menuBar = Menu(self.master)
        sideBar = LabelFrame(self.master, bd=1, relief=RAISED)

        labelWorldLimit = Label(sideBar, text="Limite do mundo", justify=LEFT, anchor="w")
        labelWorldLimit.grid(row=0, column=0, padx=5, pady=10, sticky=W)

        WorldLimitX = Entry(sideBar, width= 10)
        WorldLimitX.grid(row=0, column=1)

        labelX = Label(sideBar, text="X")
        labelX.grid(row=0, column=2)

        WorldLimitY = Entry(sideBar, width= 10)
        WorldLimitY.grid(row=0, column=3)

        labelFocalPoint = Label(sideBar, text="Ponto focal", justify=LEFT, anchor="w")
        labelFocalPoint.grid(row=1, column=0, padx=5, pady=10, sticky=W)

        coorFocalPoint = Entry(sideBar, width= 10)
        coorFocalPoint.grid(row=1, column=1)

        labelViewUp = Label(sideBar, text="VIEW-UP", justify=LEFT, anchor="w")
        labelViewUp.grid(row=2, column=0, padx=5, pady=10, sticky=W)

        coorViewUp = Entry(sideBar, width= 10)
        coorViewUp.grid(row=2, column=1)

        labelVPR = Label(sideBar, text="VRP", justify=LEFT, anchor="w")
        labelVPR.grid(row=3, column=0, padx=5, pady=10, sticky=W)

        coorVRP = Entry(sideBar, width= 10)
        coorVRP.grid(row=3, column=1)

        labelDistance = Label(sideBar, text="Distância:", justify=LEFT, anchor="w")
        labelDistance.grid(row=4, column=0, padx=5, pady=10, sticky=W)

        labelProjectionPlane = Label(sideBar, text="Plano de projeção", justify=LEFT, anchor="w")
        labelProjectionPlane.grid(row=5, column=0, padx=5, pady=10, sticky=W)

        coorProjectionPlane = Entry(sideBar, width= 10)
        coorProjectionPlane.grid(row=5, column=1)

        labelNearPlane = Label(sideBar, text="Plano near", justify=LEFT, anchor="w")
        labelNearPlane.grid(row=6, column=0, padx=5, pady=10, sticky=W)

        coorNearPlane = Entry(sideBar, width= 10)
        coorNearPlane.grid(row=6, column=1)

        labelFarPlane = Label(sideBar, text="Plano far", justify=LEFT, anchor="w")
        labelFarPlane.grid(row=7, column=0, padx=5, pady=10, sticky=W)

        coorFarPlane = Entry(sideBar, width= 10)
        coorFarPlane.grid(row=7, column=1)

        canvas = Canvas(sideBar)
        canvas.create_line(0, 25, 380, 25)
        canvas.grid(row=8, column=0, columnspan=4)

        sideBar.pack(side=RIGHT, fill= Y)
        self.master.config(menu=menuBar)
        self.pack()

def main():

    root = Tk()
    root.title('3D-modeller-and-viewer')
    root.geometry("1300x700")
    app = CanvasMenu()
    root.mainloop()


if __name__ == '__main__':
    main()
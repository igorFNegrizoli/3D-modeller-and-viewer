from tkinter import *
class CanvasMenu(Frame):

    def __init__(self):

        super().__init__()

        self.initToolbar()
        self.initSideBar()

    def initToolbar(self):

        menuBar = Menu(self.master)
        toolBar = LabelFrame(self.master, bd=2, relief=RAISED)

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
        sideBar = LabelFrame(self.master, bd=2, relief=RAISED)

        labelWorldLimit = Label(sideBar, text="Limite do mundo")
        labelWorldLimit.grid(row=0, column=0, padx=2, pady=10)

        WorldLimitX = Entry(sideBar, width= 5)
        WorldLimitX.grid(row=0, column=1, padx=5, pady=10)

        WorldLimitY = Entry(sideBar, width= 5)
        WorldLimitY.grid(row=0, column=2,padx=5, pady=10)

        labelFocalPoint = Label(sideBar, text="Ponto focal")
        labelFocalPoint.grid(row=1, column=0, pady=10)

        coorFocalPoint = Entry(sideBar, width= 5)
        coorFocalPoint.grid(row=1, column=1, padx=5, pady=10)

        labelViewUp = Label(sideBar, text="VIEW - UP")
        labelViewUp.grid(row=2, column=0, pady=10)

        coorViewUp = Entry(sideBar, width= 5)
        coorViewUp.grid(row=2, column=1, padx=5, pady=10)

        labelVRP = Label(sideBar, text="VRP")
        labelVRP.grid(row=3, column=0, pady=10)

        coorVRP = Entry(sideBar, width= 5)
        coorVRP.grid(row=3, column=1, padx=5, pady=10)

        labelDistance = Label(sideBar, text="Distâncias:")
        labelDistance.grid(row=4, column=0, pady=10)

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
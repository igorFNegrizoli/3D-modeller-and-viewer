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
        sideBar = Frame(self.master, relief=RAISED, bd=1)
        canvas = Canvas(sideBar)
        scrollbar = Scrollbar(sideBar, orient=VERTICAL, command=canvas.yview)
        scrollableFrame = Frame(sideBar)

        scrollableFrame.bind(
            "<Configure>",
             lambda change: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=scrollableFrame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        labelWorldLimit = Label(scrollableFrame, text="Limite do mundo:", justify=LEFT, anchor="w")
        labelWorldLimit.grid(row=0, column=0, padx=15, pady=10, columnspan=3, sticky=W)

        labelWorldLimitX1 = Label(scrollableFrame, text="X1")
        labelWorldLimitX1.grid(row=1, column=0, padx=15, pady=10)

        coorWorldLimitX1 = Entry(scrollableFrame, width= 8)
        coorWorldLimitX1.grid(row=1, column=1, padx=15, pady=10)

        labelWorldLimitX2 = Label(scrollableFrame, text="X2")
        labelWorldLimitX2.grid(row=1, column=2, padx=5, pady=10)

        coorWorldLimitX2 = Entry(scrollableFrame, width= 8)
        coorWorldLimitX2.grid(row=1, column=3, padx=15, pady=10)

        labelWorldLimitY1 = Label(scrollableFrame, text="Y1")
        labelWorldLimitY1.grid(row=2, column=0, padx=15, pady=10)

        coorWorldLimitY1 = Entry(scrollableFrame, width= 8)
        coorWorldLimitY1.grid(row=2, column=1, padx=15, pady=10)

        labelWorldLimitY2 = Label(scrollableFrame, text="Y2")
        labelWorldLimitY2.grid(row=2, column=2, padx=5, pady=10)

        coorWorldLimitY2 = Entry(scrollableFrame, width= 8)
        coorWorldLimitY2.grid(row=2, column=3, padx=15, pady=10)

        labelViewUp = Label(scrollableFrame, text="VIEW-UP:", justify=LEFT, anchor="w")
        labelViewUp.grid(row=3, column=0, padx=15, pady=10, columnspan=3, sticky=W)

        labelViewUpX = Label(scrollableFrame, text="X")
        labelViewUpX.grid(row=4, column=0, padx=15, pady=10)

        coorViewUpX = Entry(scrollableFrame, width= 8)
        coorViewUpX.grid(row=4, column=1, padx=15, pady=10)

        labelViewUpY = Label(scrollableFrame, text="Y")
        labelViewUpY.grid(row=5, column=0, padx=15, pady=10)

        coorViewUpY = Entry(scrollableFrame, width= 8)
        coorViewUpY.grid(row=5, column=1, padx=15, pady=10)

        labelViewUpZ = Label(scrollableFrame, text="Z")
        labelViewUpZ.grid(row=6, column=0, padx=15, pady=10)

        coorViewUpZ = Entry(scrollableFrame, width= 8)
        coorViewUpZ.grid(row=6, column=1, padx=15, pady=10)

        labelVPR = Label(scrollableFrame, text="VRP:", justify=LEFT, anchor="w")
        labelVPR.grid(row=3, column=2, padx=15, pady=10, columnspan=3, sticky=W)

        labelVRPX = Label(scrollableFrame, text="X")
        labelVRPX.grid(row=4, column=2, padx=15, pady=10)

        coorVRPX = Entry(scrollableFrame, width=8)
        coorVRPX.grid(row=4, column=3, padx=15, pady=10)

        labelVRPY = Label(scrollableFrame, text="Y")
        labelVRPY.grid(row=5, column=2, padx=15, pady=10)

        coorVRPY = Entry(scrollableFrame, width=8)
        coorVRPY.grid(row=5, column=3, padx=15, pady=10)

        labelVRPZ = Label(scrollableFrame, text="Z")
        labelVRPZ.grid(row=6, column=2, padx=15, pady=10)

        coorVRPZ = Entry(scrollableFrame, width=8)
        coorVRPZ.grid(row=6, column=3, padx=15, pady=10)

        labelFocalPoint = Label(scrollableFrame, text="Ponto focal:", justify=LEFT, anchor="w")
        labelFocalPoint.grid(row=7, column=0, padx=15, pady=10, columnspan=3, sticky=W)

        labelFocalPointX = Label(scrollableFrame, text="X")
        labelFocalPointX.grid(row=8, column=0, padx=15, pady=10)

        coorFocalPointX = Entry(scrollableFrame, width=8)
        coorFocalPointX.grid(row=8, column=1, padx=15, pady=10)

        labelFocalPointY = Label(scrollableFrame, text="Y")
        labelFocalPointY.grid(row=9, column=0, padx=15, pady=10)

        coorFocalPointY = Entry(scrollableFrame, width=8)
        coorFocalPointY.grid(row=9, column=1, padx=15, pady=10)

        labelFocalPointZ = Label(scrollableFrame, text="Z")
        labelFocalPointZ.grid(row=10, column=0, padx=15, pady=10)

        coorFocalPointZ = Entry(scrollableFrame, width=8)
        coorFocalPointZ.grid(row=10, column=1, padx=15, pady=10)

        labelObjectCenter = Label(scrollableFrame, text="Centro do objeto:", justify=LEFT, anchor="w")
        labelObjectCenter.grid(row=7, column=2, padx=15, pady=10, columnspan=3, sticky=W)

        labelObjectCenterX = Label(scrollableFrame, text="X")
        labelObjectCenterX.grid(row=8, column=2, padx=15, pady=10)

        coorObjectCenterX = Entry(scrollableFrame, width=8)
        coorObjectCenterX.grid(row=8, column=3, padx=15, pady=10)

        labelObjectCenterY = Label(scrollableFrame, text="Y")
        labelObjectCenterY.grid(row=9, column=2, padx=15, pady=10)

        coorObjectCenterY = Entry(scrollableFrame, width=8)
        coorObjectCenterY.grid(row=9, column=3, padx=15, pady=10)

        labelObjectCenterZ = Label(scrollableFrame, text="Z")
        labelObjectCenterZ.grid(row=10, column=2, padx=15, pady=10)

        coorObjectCenterZ = Entry(scrollableFrame, width=8)
        coorObjectCenterZ.grid(row=10, column=3, padx=15, pady=10)

        labelDistance = Label(scrollableFrame, text="Distância:", justify=LEFT, anchor="w")
        labelDistance.grid(row=11, column=0, padx=15, pady=8, columnspan=3, sticky=W)

        labelProjectionPlane = Label(scrollableFrame, text="Plano de projeção", justify=LEFT, anchor="w")
        labelProjectionPlane.grid(row=12, column=0, padx=15, pady=8, columnspan=3, sticky=W)

        coorProjectionPlane = Entry(scrollableFrame, width=8)
        coorProjectionPlane.grid(row=12, column=2, padx=15, pady=8)

        labelNearPlane = Label(scrollableFrame, text="Plano near", justify=LEFT, anchor="w")
        labelNearPlane.grid(row=13, column=0, padx=15, pady=8, columnspan=3, sticky=W)

        coorNearPlane = Entry(scrollableFrame, width=8)
        coorNearPlane.grid(row=13, column=2, padx=15, pady=8)

        labelFarPlane = Label(scrollableFrame, text="Plano far", justify=LEFT, anchor="w")
        labelFarPlane.grid(row=14, column=0, padx=15, pady=8, columnspan=3, sticky=W)

        coorFarPlane = Entry(scrollableFrame, width=8)
        coorFarPlane.grid(row=14, column=2, padx=15, pady=8)  

        labelObject = Label(scrollableFrame, text="Objeto:", justify=LEFT, anchor="w")
        labelObject.grid(row=15, column=0, padx=15, pady=8, columnspan=3, sticky=W)

        labelBaseRadius = Label(scrollableFrame, text="Raio da base", justify=LEFT, anchor="w")
        labelBaseRadius.grid(row=16, column=0, padx=15, pady=8, columnspan=3, sticky=W)

        coorBaseRadius = Entry(scrollableFrame, width= 8)
        coorBaseRadius.grid(row=16, column=2, padx=15, pady=8)

        labelTopRadius = Label(scrollableFrame, text="Raio do topo", justify=LEFT, anchor="w")
        labelTopRadius.grid(row=17, column=0, padx=15, pady=8, columnspan=3, sticky=W)

        coorTopRadius = Entry(scrollableFrame, width= 8)
        coorTopRadius.grid(row=17, column=2, padx=15, pady=8)

        labelNumSides = Label(scrollableFrame, text="Número de lados", justify=LEFT, anchor="w")
        labelNumSides.grid(row=18, column=0, padx=15, pady=8, columnspan=3, sticky=W)

        coorNumLados = Entry(scrollableFrame, width= 8)
        coorNumLados.grid(row=18, column=2, padx=15, pady=8)

        labelObjHeight = Label(scrollableFrame, text="Altura do objeto", justify=LEFT, anchor="w")
        labelObjHeight.grid(row=19, column=0, padx=15, pady=8, columnspan=3, sticky=W)

        coorObjHeight = Entry(scrollableFrame, width= 8)
        coorObjHeight.grid(row=19, column=2, padx=15, pady=8)

        #novoObjeto = Button(scrollableFrame, text="Novo objeto", width=15, command = newObject)
        #novoObjeto.place(relx=0.3, rely=1, anchor=CENTER)

        #limparCena = Button(scrollableFrame, text="Limpar cena", width=15, command = newObject)
        #limparCena.place(relx=0.75, rely=0.9, anchor=CENTER)

        sideBar.pack(side=RIGHT, fill=Y)
        canvas.pack(side=LEFT, fill=Y)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.master.config(menu=menuBar)
        self.pack()

def newObject():
    print("Hello!")

def main():

    root = Tk()
    root.title('3D-modeller-and-viewer')
    root.geometry("1400x700")
    app = CanvasMenu()
    root.mainloop()


if __name__ == '__main__':
    main()
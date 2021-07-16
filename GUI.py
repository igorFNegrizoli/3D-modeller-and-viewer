from tkinter import *
from typing import Collection
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

        labelWorldLimit = Label(sideBar, text="Limite do mundo:", justify=LEFT, anchor="w")
        labelWorldLimit.grid(row=0, column=0, padx=15, pady=10, columnspan=3, sticky=W)

        labelWorldLimitX1 = Label(sideBar, text="X1")
        labelWorldLimitX1.grid(row=1, column=0, padx=15, pady=10)

        coorWorldLimitX1 = Entry(sideBar, width= 8)
        coorWorldLimitX1.grid(row=1, column=1, padx=15, pady=10)

        labelWorldLimitX2 = Label(sideBar, text="X2")
        labelWorldLimitX2.grid(row=1, column=2, padx=5, pady=10)

        coorWorldLimitX2 = Entry(sideBar, width= 8)
        coorWorldLimitX2.grid(row=1, column=3, padx=15, pady=10)

        labelWorldLimitY1 = Label(sideBar, text="Y1")
        labelWorldLimitY1.grid(row=2, column=0, padx=15, pady=10)

        coorWorldLimitY1 = Entry(sideBar, width= 8)
        coorWorldLimitY1.grid(row=2, column=1, padx=15, pady=10)

        labelWorldLimitY2 = Label(sideBar, text="Y2")
        labelWorldLimitY2.grid(row=2, column=2, padx=5, pady=10)

        coorWorldLimitY2 = Entry(sideBar, width= 8)
        coorWorldLimitY2.grid(row=2, column=3, padx=15, pady=10)


        labelViewUp = Label(sideBar, text="VIEW-UP:", justify=LEFT, anchor="w")
        labelViewUp.grid(row=3, column=0, padx=15, pady=10, columnspan=3, sticky=W)

        labelViewUpX = Label(sideBar, text="X")
        labelViewUpX.grid(row=4, column=0, padx=15, pady=10)

        coorViewUpX = Entry(sideBar, width= 8)
        coorViewUpX.grid(row=4, column=1, padx=15, pady=10)

        labelViewUpY = Label(sideBar, text="Y")
        labelViewUpY.grid(row=5, column=0, padx=15, pady=10)

        coorViewUpY = Entry(sideBar, width= 8)
        coorViewUpY.grid(row=5, column=1, padx=15, pady=10)

        labelViewUpZ = Label(sideBar, text="Z")
        labelViewUpZ.grid(row=6, column=0, padx=15, pady=10)

        coorViewUpZ = Entry(sideBar, width= 8)
        coorViewUpZ.grid(row=6, column=1, padx=15, pady=10)


        labelVPR = Label(sideBar, text="VRP:", justify=LEFT, anchor="w")
        labelVPR.grid(row=3, column=2, padx=15, pady=10, columnspan=3, sticky=W)

        labelVRPX = Label(sideBar, text="X")
        labelVRPX.grid(row=4, column=2, padx=15, pady=10)

        coorVRPX = Entry(sideBar, width=8)
        coorVRPX.grid(row=4, column=3, padx=15, pady=10)

        labelVRPY = Label(sideBar, text="Y")
        labelVRPY.grid(row=5, column=2, padx=15, pady=10)

        coorVRPY = Entry(sideBar, width=8)
        coorVRPY.grid(row=5, column=3, padx=15, pady=10)

        labelVRPZ = Label(sideBar, text="Z")
        labelVRPZ.grid(row=6, column=2, padx=15, pady=10)

        coorVRPZ = Entry(sideBar, width=8)
        coorVRPZ.grid(row=6, column=3, padx=15, pady=10)



        labelFocalPoint = Label(sideBar, text="Ponto focal:", justify=LEFT, anchor="w")
        labelFocalPoint.grid(row=7, column=0, padx=15, pady=10, columnspan=3, sticky=W)

        labelFocalPointX = Label(sideBar, text="X")
        labelFocalPointX.grid(row=8, column=0, padx=15, pady=10)

        coorFocalPointX = Entry(sideBar, width=8)
        coorFocalPointX.grid(row=8, column=1, padx=15, pady=10)

        labelFocalPointY = Label(sideBar, text="Y")
        labelFocalPointY.grid(row=9, column=0, padx=15, pady=10)

        coorFocalPointY = Entry(sideBar, width=8)
        coorFocalPointY.grid(row=9, column=1, padx=15, pady=10)

        labelFocalPointZ = Label(sideBar, text="Z")
        labelFocalPointZ.grid(row=10, column=0, padx=15, pady=10)

        coorFocalPointZ = Entry(sideBar, width=8)
        coorFocalPointZ.grid(row=10, column=1, padx=15, pady=10)



        labelObjectCenter = Label(sideBar, text="Centro do objeto:", justify=LEFT, anchor="w")
        labelObjectCenter.grid(row=7, column=2, padx=15, pady=10, columnspan=3, sticky=W)

        labelObjectCenterX = Label(sideBar, text="X")
        labelObjectCenterX.grid(row=8, column=2, padx=15, pady=10)

        coorObjectCenterX = Entry(sideBar, width=8)
        coorObjectCenterX.grid(row=8, column=3, padx=15, pady=10)

        labelObjectCenterY = Label(sideBar, text="Y")
        labelObjectCenterY.grid(row=9, column=2, padx=15, pady=10)

        coorObjectCenterY = Entry(sideBar, width=8)
        coorObjectCenterY.grid(row=9, column=3, padx=15, pady=10)

        labelObjectCenterZ = Label(sideBar, text="Z")
        labelObjectCenterZ.grid(row=10, column=2, padx=15, pady=10)

        coorObjectCenterZ = Entry(sideBar, width=8)
        coorObjectCenterZ.grid(row=10, column=3, padx=15, pady=10)


        labelDistance = Label(sideBar, text="Distância:", justify=LEFT, anchor="w")
        labelDistance.grid(row=11, column=0, padx=15, pady=8, columnspan=3, sticky=W)

        labelProjectionPlane = Label(sideBar, text="Plano de projeção", justify=LEFT, anchor="w")
        labelProjectionPlane.grid(row=12, column=0, padx=15, pady=8, columnspan=3, sticky=W)

        coorProjectionPlane = Entry(sideBar, width=8)
        coorProjectionPlane.grid(row=12, column=2, padx=15, pady=8)

        labelNearPlane = Label(sideBar, text="Plano near", justify=LEFT, anchor="w")
        labelNearPlane.grid(row=13, column=0, padx=15, pady=8, columnspan=3, sticky=W)

        coorNearPlane = Entry(sideBar, width=8)
        coorNearPlane.grid(row=13, column=2, padx=15, pady=8)

        labelFarPlane = Label(sideBar, text="Plano far", justify=LEFT, anchor="w")
        labelFarPlane.grid(row=14, column=0, padx=15, pady=8, columnspan=3, sticky=W)

        coorFarPlane = Entry(sideBar, width=8)
        coorFarPlane.grid(row=14, column=2, padx=15, pady=8)

        canvas = Canvas(sideBar)
        canvas.create_line(0, 25, 300, 25)
        canvas.place(x=0, y=590)

        #limparCena.place(relx=0.75, rely=0.9, anchor=CENTER)

        """"

        labelRaioBase = Label(sideBar, text="Raio da base", justify=LEFT, anchor="w")
        labelRaioBase.grid(row=9, column=0, padx=5, pady=10, sticky=W)

        coorRaioBase = Entry(sideBar, width= 10)
        coorRaioBase.grid(row=9, column=1, padx=10)

        labelRaioTopo = Label(sideBar, text="Raio do topo", justify=LEFT, anchor="w")
        labelRaioTopo.grid(row=10, column=0, padx=5, pady=10, sticky=W)

        coorRaioTopo = Entry(sideBar, width= 10)
        coorRaioTopo.grid(row=10, column=1, padx=10)

        labelNumLados = Label(sideBar, text="Número de lados", justify=LEFT, anchor="w")
        labelNumLados.grid(row=11, column=0, padx=5, pady=10, sticky=W)

        coorNumLados = Entry(sideBar, width= 10)
        coorNumLados.grid(row=11, column=1, padx=10)

        labelAltObj = Label(sideBar, text="Altura do objeto", justify=LEFT, anchor="w")
        labelAltObj.grid(row=12, column=0, padx=5, pady=10, sticky=W)

        coorAltobj = Entry(sideBar, width= 10)
        coorAltobj.grid(row=12, column=1, padx=10)

        novoObjeto = Button(sideBar, text="Novo objeto", width=15, command = newObject)
        novoObjeto.place(relx=0.3, rely=0.9, anchor=CENTER)

        limparCena = Button(sideBar, text="Limpar cena", width=15, command = newObject)
        limparCena.place(relx=0.75, rely=0.9, anchor=CENTER)

        """

        sideBar.pack(side=RIGHT, fill=Y)
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
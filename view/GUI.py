from tkinter import *

# Classe para criação dos Menus (Toolbar e SideBar)

class CanvasMenu(Frame):

    def __init__(self):

        super().__init__()

        self.initSideBar()
        self.initToolbar()
        self.initScreen()

    # Toolbar para a escolha da projeção e do sombreamento
    def initToolbar(self):
        
        toolBar = LabelFrame(self.master, bg='#E0E0E0', relief=FLAT)

        optionProj = IntVar()

        labelProjection = Label(toolBar, text="Projeção:", font=('Helvetica', 10, 'bold'), bg='#E0E0E0')
        labelProjection.grid(row=0, column= 1, padx=10)
    
        perspective = Radiobutton(toolBar, text="Perspectiva", variable=optionProj, value=1, font=('Helvetica', 9), bg='#E0E0E0')
        perspective.grid(row=1, column=2, padx=5, pady=5)

        parallel = Radiobutton(toolBar, text="Paralela", variable=optionProj, value=2, font=('Helvetica', 9), bg='#E0E0E0')
        parallel.grid(row=1, column=3, padx=5, pady=5)

        optionSomb = IntVar()

        labelProjection = Label(toolBar, text="Sombreamento:", font=('Helvetica', 10, 'bold'), bg='#E0E0E0')
        labelProjection.grid(row=0, column= 5, padx=10)
    
        gouraud = Radiobutton(toolBar, text="Gouraud", variable=optionSomb, value=3, font=('Helvetica', 9), bg='#E0E0E0')
        gouraud.grid(row=1, column=6, padx=5, pady=5)

        phong = Radiobutton(toolBar, text="Phong simplificado", variable=optionSomb, value=4, font=('Helvetica', 9), bg='#E0E0E0')
        phong.grid(row=1, column=7, padx=5, pady=5)

        toolBar.pack(side=TOP, fill=X)

    # SideBar para definição do mundo e do objeto
    def initSideBar(self):

        def newWorld():
            return
            
        sideBar = LabelFrame(self.master, relief=FLAT)
        squareUp = LabelFrame(sideBar, bd=1, bg='#E0E0E0', relief=RAISED)
        squareDown = LabelFrame(sideBar, sideBar, bd=1, bg='#E0E0E0', relief=RAISED)

        #  Adição dos widgets no frame 
        labelWorldLimit = Label(squareUp, text="Limite do mundo:", justify=LEFT, anchor="w", font=('Helvetica', 10, 'bold'), bg='#E0E0E0')
        labelWorldLimit.grid(row=0, column=0, padx=15, pady=10, columnspan=3, sticky=W)

        labelWarning = Label(squareUp, text="(Limite máximo: 1080x730)", justify=LEFT, anchor="w", font=('Helvetica', 8), bg='#E0E0E0')
        labelWarning.grid(row=0, column=2, padx=15, pady=10, columnspan=4, sticky=W)

        labelWorldLimitX1 = Label(squareUp, text="X1", font=('Helvetica', 9), bg='#E0E0E0')
        labelWorldLimitX1.grid(row=1, column=0, padx=15, pady=10)

        coorWorldLimitX1 = Entry(squareUp, width= 8)
        coorWorldLimitX1.grid(row=1, column=1, padx=15, pady=10)

        labelWorldLimitX2 = Label(squareUp, text="X2", font=('Helvetica', 9), bg='#E0E0E0')
        labelWorldLimitX2.grid(row=1, column=2, padx=5, pady=10)

        coorWorldLimitX2 = Entry(squareUp, width= 8)
        coorWorldLimitX2.grid(row=1, column=3, padx=15, pady=10)

        labelWorldLimitY1 = Label(squareUp, text="Y1", font=('Helvetica', 9), bg='#E0E0E0')
        labelWorldLimitY1.grid(row=2, column=0, padx=15, pady=10)

        coorWorldLimitY1 = Entry(squareUp, width= 8)
        coorWorldLimitY1.grid(row=2, column=1, padx=15, pady=10)

        labelWorldLimitY2 = Label(squareUp, text="Y2", font=('Helvetica', 9), bg='#E0E0E0')
        labelWorldLimitY2.grid(row=2, column=2, padx=5, pady=10)

        coorWorldLimitY2 = Entry(squareUp, width= 8)
        coorWorldLimitY2.grid(row=2, column=3, padx=15, pady=10)

        labelViewUp = Label(squareUp, text="VIEW-UP:", justify=LEFT, anchor="w", font=('Helvetica', 10, 'bold'), bg='#E0E0E0')
        labelViewUp.grid(row=3, column=0, padx=15, pady=10, columnspan=3, sticky=W)

        labelViewUpX = Label(squareUp, text="X", font=('Helvetica', 9), bg='#E0E0E0')
        labelViewUpX.grid(row=4, column=0, padx=15, pady=10)

        coorViewUpX = Entry(squareUp, width= 8)
        coorViewUpX.grid(row=4, column=1, padx=15, pady=10)

        labelViewUpY = Label(squareUp, text="Y", font=('Helvetica', 9), bg='#E0E0E0')
        labelViewUpY.grid(row=5, column=0, padx=15, pady=10)

        coorViewUpY = Entry(squareUp, width= 8)
        coorViewUpY.grid(row=5, column=1, padx=15, pady=10)

        labelViewUpZ = Label(squareUp, text="Z", font=('Helvetica', 9), bg='#E0E0E0')
        labelViewUpZ.grid(row=6, column=0, padx=15, pady=10)

        coorViewUpZ = Entry(squareUp, width= 8)
        coorViewUpZ.grid(row=6, column=1, padx=15, pady=10)

        labelVPR = Label(squareUp, text="VRP:", font=('Helvetica', 10, 'bold'), bg='#E0E0E0')
        labelVPR.grid(row=3, column=2, padx=15, pady=10)

        labelVRPX = Label(squareUp, text="X", font=('Helvetica', 9), bg='#E0E0E0')
        labelVRPX.grid(row=4, column=2, padx=15, pady=10)

        coorVRPX = Entry(squareUp, width=8)
        coorVRPX.grid(row=4, column=3, padx=15, pady=10)

        labelVRPY = Label(squareUp, text="Y", font=('Helvetica', 9), bg='#E0E0E0')
        labelVRPY.grid(row=5, column=2, padx=15, pady=10)

        coorVRPY = Entry(squareUp, width=8)
        coorVRPY.grid(row=5, column=3, padx=15, pady=10)

        labelVRPZ = Label(squareUp, text="Z", font=('Helvetica', 9), bg='#E0E0E0')
        labelVRPZ.grid(row=6, column=2, padx=15, pady=10)

        coorVRPZ = Entry(squareUp, width=8)
        coorVRPZ.grid(row=6, column=3, padx=15, pady=10)

        labelFocalPoint = Label(squareUp, text="Ponto focal:", justify=LEFT, anchor="w", font=('Helvetica', 10, 'bold'), bg='#E0E0E0')
        labelFocalPoint.grid(row=7, column=0, padx=15, pady=10, columnspan=3, sticky=W)

        labelFocalPointX = Label(squareUp, text="X", font=('Helvetica', 9), bg='#E0E0E0')
        labelFocalPointX.grid(row=8, column=0, padx=15, pady=10)

        coorFocalPointX = Entry(squareUp, width=8)
        coorFocalPointX.grid(row=8, column=1, padx=15, pady=10)

        labelFocalPointY = Label(squareUp, text="Y", font=('Helvetica', 9), bg='#E0E0E0')
        labelFocalPointY.grid(row=9, column=0, padx=15, pady=10)

        coorFocalPointY = Entry(squareUp, width=8)
        coorFocalPointY.grid(row=9, column=1, padx=15, pady=10)

        labelFocalPointZ = Label(squareUp, text="Z", font=('Helvetica', 9), bg='#E0E0E0')
        labelFocalPointZ.grid(row=10, column=0, padx=15, pady=10)

        coorFocalPointZ = Entry(squareUp, width=8)
        coorFocalPointZ.grid(row=10, column=1, padx=15, pady=10)

        labelDistance = Label(squareUp, text="Distância ao plano:", justify=LEFT, anchor="w", font=('Helvetica', 10, 'bold'), bg='#E0E0E0')
        labelDistance.grid(row=7, column=2, padx=15, pady=8, columnspan=3, sticky=W)

        labelProjectionPlane = Label(squareUp, text="Projeção", font=('Helvetica', 9), bg='#E0E0E0')
        labelProjectionPlane.grid(row=8, column=2, padx=15, pady=8)

        coorProjectionPlane = Entry(squareUp, width=8)
        coorProjectionPlane.grid(row=8, column=3, padx=15, pady=8)

        labelNearPlane = Label(squareUp, text="Near", font=('Helvetica', 9), bg='#E0E0E0')
        labelNearPlane.grid(row=9, column=2, padx=15, pady=8)

        coorNearPlane = Entry(squareUp, width=8)
        coorNearPlane.grid(row=9, column=3, padx=15, pady=8)

        labelFarPlane = Label(squareUp, text="Far", font=('Helvetica', 9), bg='#E0E0E0')
        labelFarPlane.grid(row=10, column=2, padx=15, pady=8)

        coorFarPlane = Entry(squareUp, width=8)
        coorFarPlane.grid(row=10, column=3, padx=15, pady=8) 

        novoMundo = Button(squareUp, text="Novo mundo", font=('Helvetica', 10), bg='#edb1ba', width=10, command = newWorld)
        novoMundo.grid(row=11, column=0, columnspan=4, pady= 20)


        labelObject = Label(squareDown, text="Dados do objeto:", justify=LEFT, anchor="w", font=('Helvetica', 10, 'bold'), bg='#E0E0E0')
        labelObject.grid(row=14, column=0, padx=4.5, pady=10, columnspan=4, sticky=W)

        labelBaseRadius = Label(squareDown, text="Raio da base", justify=LEFT, anchor="w", font=('Helvetica', 9), bg='#E0E0E0')
        labelBaseRadius.grid(row=15, column=0, padx=4.5, pady=10, sticky=W)

        coorBaseRadius = Entry(squareDown, width= 8)
        coorBaseRadius.grid(row=15, column=1,padx=4.5, pady=10)

        labelTopRadius = Label(squareDown, text="Raio do topo", justify=LEFT, anchor="w", font=('Helvetica', 9), bg='#E0E0E0')
        labelTopRadius.grid(row=15, column=2, padx=4.5, pady=10, sticky=W)

        coorTopRadius = Entry(squareDown, width= 8)
        coorTopRadius.grid(row=15, column=3, padx=4.5, pady=10)

        labelNumSides = Label(squareDown, text="Nº de lados", justify=LEFT, anchor="w", font=('Helvetica', 9), bg='#E0E0E0')
        labelNumSides.grid(row=16, column=0, padx=4.5, pady=10, sticky=W)

        coorNumLados = Entry(squareDown, width= 8)
        coorNumLados.grid(row=16, column=1, padx=4.5, pady=10)

        labelObjHeight = Label(squareDown, text="Altura", font=('Helvetica', 9), bg='#E0E0E0')
        labelObjHeight.grid(row=16, column=2, padx=4.5, pady=10)

        coorObjHeight = Entry(squareDown, width= 8)
        coorObjHeight.grid(row=16, column=3, padx=4.5, pady=10)
        
        labelObjectCenter = Label(squareDown, text="Centro Geométrico:", justify=LEFT, anchor="w", font=('Helvetica', 10, 'bold'), bg='#E0E0E0')
        labelObjectCenter.grid(row=17, column=0, padx=4.5, pady=10, columnspan=4, sticky=W)
        
        labelObjectCenterX = Label(squareDown, text="X", font=('Helvetica', 9), bg='#E0E0E0')
        labelObjectCenterX.place(relx=0.1, rely= 0.68, anchor=E)

        coorObjectCenterX = Entry(squareDown, width=8)
        coorObjectCenterX.grid(row=18, column=0, columnspan=2, pady=10)

        labelObjectCenterY = Label(squareDown, text="Y", font=('Helvetica', 9), bg='#E0E0E0')
        labelObjectCenterY.place(relx=0.42, rely= 0.68, anchor=E)

        coorObjectCenterY = Entry(squareDown, width=8)
        coorObjectCenterY.grid(row=18, column=1, columnspan=2, pady=10)

        labelObjectCenterZ = Label(squareDown, text="Z", font=('Helvetica', 9), bg='#E0E0E0')
        labelObjectCenterZ.place(relx=0.74, rely= 0.68, anchor=E)

        coorObjectCenterY = Entry(squareDown, width=8, justify=LEFT)
        coorObjectCenterY.grid(row=18, column=3, sticky=W)

        limparCena = Button(squareDown, text="Novo objeto", font=('Helvetica', 10), bg='#edb1ba', width=9, command = newObject)
        limparCena.grid(row=19, column=0, columnspan=2, pady=20)

        limparCena = Button(squareDown, text="Nova cena", font=('Helvetica', 10), bg='#edb1ba', width=9, command = newObject)
        limparCena.grid(row=19, column=2, columnspan=2, pady=20)

        sideBar.pack(side=RIGHT, fill=Y)
        squareUp.pack(side=TOP, fill=Y)
        squareDown.pack(side=BOTTOM, fill=Y)

    def initScreen(self):

            screen = Frame(self.master, highlightbackground='gray', highlightthickness=1)
            screen.rowconfigure(0, weight = 1)

            screen.columnconfigure(0, weight = 1)
            global canvas 
            canvas = Canvas(screen)

            screen.place(x=10, y= 70, width=1080, height=730)

            canvas.grid(sticky="nsew")
            canvas.bind("<Button-1>", locate_xy)
            canvas.bind("<B1-Motion>", addLine)
            canvas.create_line((60, 600, 60, 650), fill="green")
            canvas.create_line((60, 650, 110, 650), fill="blue")
            canvas.create_line((60, 650, 30, 680), fill="red")

def locate_xy(event):
    global current_x, current_y
    current_x, current_y = 0,0
    current_x, current_y = event.x, event.y
    print(current_x, current_y)   

def addLine(event):
    global current_x, current_y
    canvas.create_line((current_x, current_y, event.x, event.y), fill="black")
    current_x, current_y = event.x, event.y

def newObject():
    print("Hello!")

def main():

    root = Tk()
    root.resizable(width=False, height=False)
    root.title('3D-modeller-and-viewer')

    largura = 1405
    altura = 808

    largura_screen = root.winfo_screenwidth()
    altura_screen = root.winfo_screenheight()

    posx = largura_screen/2 - largura/2
    posy = (altura_screen/2 - altura/2) -30

    root.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))

    app = CanvasMenu()
    root.mainloop()

if __name__ == '__main__':
    main()
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

        sideBar = LabelFrame(self.master, relief=FLAT)

        # Criação do canvas com a barra de rolamento
        canvas = Canvas(sideBar, bg='#E0E0E0', relief=FLAT)
        scrollBar = Scrollbar(sideBar, command=canvas.yview)

        # Colocar o frame no canvas
        scrollableFrame = Frame(canvas, bg='#E0E0E0', relief=FLAT)

        # Atualizar a região de rolamento depois de começar o 'mainloop'
        # com todos os widgets no canvas
        scrollableFrame.bind(
            "<Configure>",
            lambda e: canvas.configure(
            scrollregion=canvas.bbox("all")
            )
        )
        canvas.create_window((0,0), window=scrollableFrame, anchor='nw')
        canvas.config(yscrollcommand= scrollBar.set)
        
        #  Adição dos widgets no frame 
        labelWorldLimit = Label(scrollableFrame, text="Limite do mundo:", justify=LEFT, anchor="w", font=('Helvetica', 10, 'bold'), bg='#E0E0E0')
        labelWorldLimit.grid(row=0, column=0, padx=15, pady=10, columnspan=3, sticky=W)

        labelWorldLimitX1 = Label(scrollableFrame, text="X1", font=('Helvetica', 9), bg='#E0E0E0')
        labelWorldLimitX1.grid(row=1, column=0, padx=15, pady=10)

        coorWorldLimitX1 = Entry(scrollableFrame, width= 8)
        coorWorldLimitX1.grid(row=1, column=1, padx=15, pady=10)

        labelWorldLimitX2 = Label(scrollableFrame, text="X2", font=('Helvetica', 9), bg='#E0E0E0')
        labelWorldLimitX2.grid(row=1, column=2, padx=5, pady=10)

        coorWorldLimitX2 = Entry(scrollableFrame, width= 8)
        coorWorldLimitX2.grid(row=1, column=3, padx=15, pady=10)

        labelWorldLimitY1 = Label(scrollableFrame, text="Y1", font=('Helvetica', 9), bg='#E0E0E0')
        labelWorldLimitY1.grid(row=2, column=0, padx=15, pady=10)

        coorWorldLimitY1 = Entry(scrollableFrame, width= 8)
        coorWorldLimitY1.grid(row=2, column=1, padx=15, pady=10)

        labelWorldLimitY2 = Label(scrollableFrame, text="Y2", font=('Helvetica', 9), bg='#E0E0E0')
        labelWorldLimitY2.grid(row=2, column=2, padx=5, pady=10)

        coorWorldLimitY2 = Entry(scrollableFrame, width= 8)
        coorWorldLimitY2.grid(row=2, column=3, padx=15, pady=10)

        labelViewUp = Label(scrollableFrame, text="VIEW-UP:", justify=LEFT, anchor="w", font=('Helvetica', 10, 'bold'), bg='#E0E0E0')
        labelViewUp.grid(row=3, column=0, padx=15, pady=10, columnspan=3, sticky=W)

        labelViewUpX = Label(scrollableFrame, text="X", font=('Helvetica', 9), bg='#E0E0E0')
        labelViewUpX.grid(row=4, column=0, padx=15, pady=10)

        coorViewUpX = Entry(scrollableFrame, width= 8)
        coorViewUpX.grid(row=4, column=1, padx=15, pady=10)

        labelViewUpY = Label(scrollableFrame, text="Y", font=('Helvetica', 9), bg='#E0E0E0')
        labelViewUpY.grid(row=5, column=0, padx=15, pady=10)

        coorViewUpY = Entry(scrollableFrame, width= 8)
        coorViewUpY.grid(row=5, column=1, padx=15, pady=10)

        labelViewUpZ = Label(scrollableFrame, text="Z", font=('Helvetica', 9), bg='#E0E0E0')
        labelViewUpZ.grid(row=6, column=0, padx=15, pady=10)

        coorViewUpZ = Entry(scrollableFrame, width= 8)
        coorViewUpZ.grid(row=6, column=1, padx=15, pady=10)

        labelVPR = Label(scrollableFrame, text="VRP:", font=('Helvetica', 10, 'bold'), bg='#E0E0E0')
        labelVPR.grid(row=3, column=2, padx=15, pady=10)

        labelVRPX = Label(scrollableFrame, text="X", font=('Helvetica', 9), bg='#E0E0E0')
        labelVRPX.grid(row=4, column=2, padx=15, pady=10)

        coorVRPX = Entry(scrollableFrame, width=8)
        coorVRPX.grid(row=4, column=3, padx=15, pady=10)

        labelVRPY = Label(scrollableFrame, text="Y", font=('Helvetica', 9), bg='#E0E0E0')
        labelVRPY.grid(row=5, column=2, padx=15, pady=10)

        coorVRPY = Entry(scrollableFrame, width=8)
        coorVRPY.grid(row=5, column=3, padx=15, pady=10)

        labelVRPZ = Label(scrollableFrame, text="Z", font=('Helvetica', 9), bg='#E0E0E0')
        labelVRPZ.grid(row=6, column=2, padx=15, pady=10)

        coorVRPZ = Entry(scrollableFrame, width=8)
        coorVRPZ.grid(row=6, column=3, padx=15, pady=10)

        labelFocalPoint = Label(scrollableFrame, text="Ponto focal:", justify=LEFT, anchor="w", font=('Helvetica', 10, 'bold'), bg='#E0E0E0')
        labelFocalPoint.grid(row=7, column=0, padx=15, pady=10, columnspan=3, sticky=W)

        labelFocalPointX = Label(scrollableFrame, text="X", font=('Helvetica', 9), bg='#E0E0E0')
        labelFocalPointX.grid(row=8, column=0, padx=15, pady=10)

        coorFocalPointX = Entry(scrollableFrame, width=8)
        coorFocalPointX.grid(row=8, column=1, padx=15, pady=10)

        labelFocalPointY = Label(scrollableFrame, text="Y", font=('Helvetica', 9), bg='#E0E0E0')
        labelFocalPointY.grid(row=9, column=0, padx=15, pady=10)

        coorFocalPointY = Entry(scrollableFrame, width=8)
        coorFocalPointY.grid(row=9, column=1, padx=15, pady=10)

        labelFocalPointZ = Label(scrollableFrame, text="Z", font=('Helvetica', 9), bg='#E0E0E0')
        labelFocalPointZ.grid(row=10, column=0, padx=15, pady=10)

        coorFocalPointZ = Entry(scrollableFrame, width=8)
        coorFocalPointZ.grid(row=10, column=1, padx=15, pady=10)

        labelObjectCenter = Label(scrollableFrame, text="Centro do objeto:", justify=LEFT, anchor="w", font=('Helvetica', 10, 'bold'), bg='#E0E0E0')
        labelObjectCenter.grid(row=7, column=2, padx=30, pady=10, columnspan=3, sticky=W)

        labelObjectCenterX = Label(scrollableFrame, text="X", font=('Helvetica', 9), bg='#E0E0E0')
        labelObjectCenterX.grid(row=8, column=2, padx=15, pady=10)

        coorObjectCenterX = Entry(scrollableFrame, width=8)
        coorObjectCenterX.grid(row=8, column=3, padx=15, pady=10)

        labelObjectCenterY = Label(scrollableFrame, text="Y", font=('Helvetica', 9), bg='#E0E0E0')
        labelObjectCenterY.grid(row=9, column=2, padx=15, pady=10)

        coorObjectCenterY = Entry(scrollableFrame, width=8)
        coorObjectCenterY.grid(row=9, column=3, padx=15, pady=10)

        labelObjectCenterZ = Label(scrollableFrame, text="Z", font=('Helvetica', 9), bg='#E0E0E0')
        labelObjectCenterZ.grid(row=10, column=2, padx=15, pady=10)

        coorObjectCenterZ = Entry(scrollableFrame, width=8)
        coorObjectCenterZ.grid(row=10, column=3, padx=15, pady=10)

        labelDistance = Label(scrollableFrame, text="Distância:", justify=LEFT, anchor="w", font=('Helvetica', 10, 'bold'), bg='#E0E0E0')
        labelDistance.grid(row=11, column=0, padx=15, pady=8, columnspan=3, sticky=W)

        labelProjectionPlane = Label(scrollableFrame, text="Plano de projeção", justify=LEFT, anchor="w", font=('Helvetica', 9), bg='#E0E0E0')
        labelProjectionPlane.grid(row=12, column=0, padx=15, pady=8, columnspan=3, sticky=W)

        coorProjectionPlane = Entry(scrollableFrame, width=8)
        coorProjectionPlane.grid(row=12, column=2, padx=15, pady=8)

        labelNearPlane = Label(scrollableFrame, text="Plano near", justify=LEFT, anchor="w", font=('Helvetica', 9), bg='#E0E0E0')
        labelNearPlane.grid(row=13, column=0, padx=15, pady=8, columnspan=3, sticky=W)

        coorNearPlane = Entry(scrollableFrame, width=8)
        coorNearPlane.grid(row=13, column=2, padx=15, pady=8)

        labelFarPlane = Label(scrollableFrame, text="Plano far", justify=LEFT, anchor="w", font=('Helvetica', 9), bg='#E0E0E0')
        labelFarPlane.grid(row=14, column=0, padx=15, pady=8, columnspan=3, sticky=W)

        coorFarPlane = Entry(scrollableFrame, width=8)
        coorFarPlane.grid(row=14, column=2, padx=15, pady=8)  

        labelObject = Label(scrollableFrame, text="Objeto:", justify=LEFT, anchor="w", font=('Helvetica', 10, 'bold'), bg='#E0E0E0')
        labelObject.grid(row=16, column=0, padx=15, pady=8, columnspan=3, sticky=W)

        labelBaseRadius = Label(scrollableFrame, text="Raio da base", justify=LEFT, anchor="w", font=('Helvetica', 9), bg='#E0E0E0')
        labelBaseRadius.grid(row=17, column=0, padx=15, pady=8, columnspan=3, sticky=W)

        coorBaseRadius = Entry(scrollableFrame, width= 8)
        coorBaseRadius.grid(row=17, column=2, padx=15, pady=8)

        labelTopRadius = Label(scrollableFrame, text="Raio do topo", justify=LEFT, anchor="w", font=('Helvetica', 9), bg='#E0E0E0')
        labelTopRadius.grid(row=18, column=0, padx=15, pady=8, columnspan=3, sticky=W)

        coorTopRadius = Entry(scrollableFrame, width= 8)
        coorTopRadius.grid(row=18, column=2, padx=15, pady=8)

        labelNumSides = Label(scrollableFrame, text="Número de lados", justify=LEFT, anchor="w", font=('Helvetica', 9), bg='#E0E0E0')
        labelNumSides.grid(row=19, column=0, padx=15, pady=8, columnspan=3, sticky=W)

        coorNumLados = Entry(scrollableFrame, width= 8)
        coorNumLados.grid(row=19, column=2, padx=15, pady=8)

        labelObjHeight = Label(scrollableFrame, text="Altura do objeto", justify=LEFT, anchor="w", font=('Helvetica', 9), bg='#E0E0E0')
        labelObjHeight.grid(row=20, column=0, padx=15, pady=8, columnspan=3, sticky=W)

        coorObjHeight = Entry(scrollableFrame, width= 8)
        coorObjHeight.grid(row=20, column=2, padx=15, pady=8)

        novoObjeto = Button(scrollableFrame, text="Novo objeto", font=('Helvetica', 10), bg='#edb1ba', width=15, command = newObject)
        novoObjeto.grid(row=21, column=0, columnspan=3, pady=50)

        limparCena = Button(scrollableFrame, text="Limpar cena", font=('Helvetica', 10), bg='#edb1ba', width=15, command = newObject)
        limparCena.grid(row=21, column=3, columnspan=3, pady=50)

        sideBar.pack(side=RIGHT, fill=Y)
        canvas.pack(side=LEFT, fill=BOTH, expand=True)
        scrollBar.pack(side=RIGHT, fill=Y)

    
    def initScreen(self):
            screen = Frame(self.master, highlightbackground='gray', highlightthickness=1)
            screen.rowconfigure(0, weight = 1)
            screen.columnconfigure(0, weight = 1)
            global canvas 
            canvas = Canvas(screen)

            screen.place(x=10, y= 70, width=980, height=640)
            canvas.grid(sticky="nsew")

            canvas.bind("<Button-1>", locate_xy)
            canvas.bind("<B1-Motion>", addLine)
            canvas.create_line((62, 528, 62, 586), fill="green")
            canvas.create_line((62, 586, 120, 586), fill="blue")
            canvas.create_line((62, 586, 20, 616), fill="red")

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

    largura = 1400
    altura = 720

    largura_screen = root.winfo_screenwidth()
    altura_screen = root.winfo_screenheight()

    posx = largura_screen/2 - largura/2
    posy = (altura_screen/2 - altura/2) -30

    root.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))

    app = CanvasMenu()
    root.mainloop()

if __name__ == '__main__':
    main()
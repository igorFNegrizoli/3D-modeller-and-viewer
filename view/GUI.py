from tkinter import *
from tkinter import messagebox


# Classe para criação dos Menus (Toolbar e SideBar)

class CanvasMenu(Frame):

    def __init__(self):

        super().__init__()

        self.initSideBar()
        self.initToolbar()
        self.initScreen()
        self.initPC()
        

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

        constant = Radiobutton(toolBar, text="Sombreamento Constante", variable=optionSomb, value=5, font=('Helvetica', 9), bg='#E0E0E0')
        constant.grid(row=1, column=8, padx=5, pady=5)

        toolBar.pack(side=TOP, fill=X)

    # SideBar para definição do mundo e do objeto
    def initSideBar(self):
            
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

        global coorWorldLimitX1
        coorWorldLimitX1 = Entry(squareUp, width= 8)
        coorWorldLimitX1.grid(row=1, column=1, padx=15, pady=10)

        labelWorldLimitX2 = Label(squareUp, text="X2", font=('Helvetica', 9), bg='#E0E0E0')
        labelWorldLimitX2.grid(row=1, column=2, padx=5, pady=10)

        global coorWorldLimitX2 
        coorWorldLimitX2 = Entry(squareUp, width= 8)
        coorWorldLimitX2.grid(row=1, column=3, padx=15, pady=10)

        labelWorldLimitY1 = Label(squareUp, text="Y1", font=('Helvetica', 9), bg='#E0E0E0')
        labelWorldLimitY1.grid(row=2, column=0, padx=15, pady=10)

        global coorWorldLimitY1
        coorWorldLimitY1 = Entry(squareUp, width= 8)
        coorWorldLimitY1.grid(row=2, column=1, padx=15, pady=10)

        labelWorldLimitY2 = Label(squareUp, text="Y2", font=('Helvetica', 9), bg='#E0E0E0')
        labelWorldLimitY2.grid(row=2, column=2, padx=5, pady=10)

        global coorWorldLimitY2
        coorWorldLimitY2 = Entry(squareUp, width= 8)
        coorWorldLimitY2.grid(row=2, column=3, padx=15, pady=10)

        labelViewUp = Label(squareUp, text="VIEW-UP:", justify=LEFT, anchor="w", font=('Helvetica', 10, 'bold'), bg='#E0E0E0')
        labelViewUp.grid(row=3, column=0, padx=15, pady=10, columnspan=3, sticky=W)

        labelViewUpX = Label(squareUp, text="X", font=('Helvetica', 9), bg='#E0E0E0')
        labelViewUpX.grid(row=4, column=0, padx=15, pady=10)

        global coorViewUpX
        coorViewUpX = Entry(squareUp, width= 8)
        coorViewUpX.grid(row=4, column=1, padx=15, pady=10)

        labelViewUpY = Label(squareUp, text="Y", font=('Helvetica', 9), bg='#E0E0E0')
        labelViewUpY.grid(row=5, column=0, padx=15, pady=10)

        global coorViewUpY 
        coorViewUpY = Entry(squareUp, width= 8)
        coorViewUpY.grid(row=5, column=1, padx=15, pady=10)

        labelViewUpZ = Label(squareUp, text="Z", font=('Helvetica', 9), bg='#E0E0E0')
        labelViewUpZ.grid(row=6, column=0, padx=15, pady=10)

        global coorViewUpZ 
        coorViewUpZ = Entry(squareUp, width= 8)
        coorViewUpZ.grid(row=6, column=1, padx=15, pady=10)

        labelVPR = Label(squareUp, text="VRP:", font=('Helvetica', 10, 'bold'), bg='#E0E0E0')
        labelVPR.grid(row=3, column=2, padx=15, pady=10)

        labelVRPX = Label(squareUp, text="X", font=('Helvetica', 9), bg='#E0E0E0')
        labelVRPX.grid(row=4, column=2, padx=15, pady=10)

        global coorVRPX
        coorVRPX = Entry(squareUp, width=8)
        coorVRPX.grid(row=4, column=3, padx=15, pady=10)

        labelVRPY = Label(squareUp, text="Y", font=('Helvetica', 9), bg='#E0E0E0')
        labelVRPY.grid(row=5, column=2, padx=15, pady=10)
        
        global coorVRPY
        coorVRPY = Entry(squareUp, width=8)
        coorVRPY.grid(row=5, column=3, padx=15, pady=10)

        labelVRPZ = Label(squareUp, text="Z", font=('Helvetica', 9), bg='#E0E0E0')
        labelVRPZ.grid(row=6, column=2, padx=15, pady=10)
       
        global coorVRPZ
        coorVRPZ = Entry(squareUp, width=8)
        coorVRPZ.grid(row=6, column=3, padx=15, pady=10)

        labelFocalPoint = Label(squareUp, text="Ponto focal:", justify=LEFT, anchor="w", font=('Helvetica', 10, 'bold'), bg='#E0E0E0')
        labelFocalPoint.grid(row=7, column=0, padx=15, pady=10, columnspan=3, sticky=W)

        labelFocalPointX = Label(squareUp, text="X", font=('Helvetica', 9), bg='#E0E0E0')
        labelFocalPointX.grid(row=8, column=0, padx=15, pady=10)

        global coorFocalPointX 
        coorFocalPointX = Entry(squareUp, width=8)
        coorFocalPointX.grid(row=8, column=1, padx=15, pady=10)

        labelFocalPointY = Label(squareUp, text="Y", font=('Helvetica', 9), bg='#E0E0E0')
        labelFocalPointY.grid(row=9, column=0, padx=15, pady=10)

        global coorFocalPointY 
        coorFocalPointY = Entry(squareUp, width=8)
        coorFocalPointY.grid(row=9, column=1, padx=15, pady=10)

        labelFocalPointZ = Label(squareUp, text="Z", font=('Helvetica', 9), bg='#E0E0E0')
        labelFocalPointZ.grid(row=10, column=0, padx=15, pady=10)

        global coorFocalPointZ 
        coorFocalPointZ = Entry(squareUp, width=8)
        coorFocalPointZ.grid(row=10, column=1, padx=15, pady=10)

        labelDistance = Label(squareUp, text="Distância ao plano:", justify=LEFT, anchor="w", font=('Helvetica', 10, 'bold'), bg='#E0E0E0')
        labelDistance.grid(row=7, column=2, padx=15, pady=8, columnspan=3, sticky=W)

        labelProjectionPlane = Label(squareUp, text="Projeção", font=('Helvetica', 9), bg='#E0E0E0')
        labelProjectionPlane.grid(row=8, column=2, padx=15, pady=8)

        global coorProjectionPlane
        coorProjectionPlane = Entry(squareUp, width=8)
        coorProjectionPlane.grid(row=8, column=3, padx=15, pady=8)

        labelNearPlane = Label(squareUp, text="Near", font=('Helvetica', 9), bg='#E0E0E0')
        labelNearPlane.grid(row=9, column=2, padx=15, pady=8)

        global coorNearPlane
        coorNearPlane = Entry(squareUp, width=8)
        coorNearPlane.grid(row=9, column=3, padx=15, pady=8)

        labelFarPlane = Label(squareUp, text="Far", font=('Helvetica', 9), bg='#E0E0E0')
        labelFarPlane.grid(row=10, column=2, padx=15, pady=8)

        global coorFarPlane
        coorFarPlane = Entry(squareUp, width=8)
        coorFarPlane.grid(row=10, column=3, padx=15, pady=8) 

        novoMundo = Button(squareUp, text="Novo mundo", font=('Helvetica', 10), bg='#edb1ba', width=10, command = newWorld)
        novoMundo.grid(row=11, column=0, columnspan=4, pady= 20)

        labelObject = Label(squareDown, text="Dados do objeto:", justify=LEFT, anchor="w", font=('Helvetica', 10, 'bold'), bg='#E0E0E0')
        labelObject.grid(row=14, column=0, padx=4.5, pady=10, columnspan=4, sticky=W)

        labelBaseRadius = Label(squareDown, text="Raio da base", justify=LEFT, anchor="w", font=('Helvetica', 9), bg='#E0E0E0')
        labelBaseRadius.grid(row=15, column=0, padx=4.5, pady=10, sticky=W)

        global coorBaseRadius
        coorBaseRadius = Entry(squareDown, width= 8)
        coorBaseRadius.grid(row=15, column=1,padx=4.5, pady=10)

        labelTopRadius = Label(squareDown, text="Raio do topo", justify=LEFT, anchor="w", font=('Helvetica', 9), bg='#E0E0E0')
        labelTopRadius.grid(row=15, column=2, padx=4.5, pady=10, sticky=W)

        global coorTopRadius
        coorTopRadius = Entry(squareDown, width= 8)
        coorTopRadius.grid(row=15, column=3, padx=4.5, pady=10)

        labelNumSides = Label(squareDown, text="Nº de lados", justify=LEFT, anchor="w", font=('Helvetica', 9), bg='#E0E0E0')
        labelNumSides.grid(row=16, column=0, padx=4.5, pady=10, sticky=W)

        global coorNumLados
        coorNumLados = Entry(squareDown, width= 8)
        coorNumLados.grid(row=16, column=1, padx=4.5, pady=10)

        labelObjHeight = Label(squareDown, text="Altura", font=('Helvetica', 9), bg='#E0E0E0')
        labelObjHeight.grid(row=16, column=2, padx=4.5, pady=10)

        global coorObjHeight
        coorObjHeight = Entry(squareDown, width= 8)
        coorObjHeight.grid(row=16, column=3, padx=4.5, pady=10)
        
        labelObjectCenter = Label(squareDown, text="Centro Geométrico:", justify=LEFT, anchor="w", font=('Helvetica', 10, 'bold'), bg='#E0E0E0')
        labelObjectCenter.grid(row=17, column=0, padx=4.5, pady=10, columnspan=4, sticky=W)
        
        labelObjectCenterX = Label(squareDown, text="X", font=('Helvetica', 9), bg='#E0E0E0')
        labelObjectCenterX.place(relx=0.1, rely= 0.68, anchor=E)

        global coorObjectCenterX 
        coorObjectCenterX = Entry(squareDown, width=8)
        coorObjectCenterX.grid(row=18, column=0, columnspan=2, pady=10)

        labelObjectCenterY = Label(squareDown, text="Y", font=('Helvetica', 9), bg='#E0E0E0')
        labelObjectCenterY.place(relx=0.42, rely= 0.68, anchor=E)

        global coorObjectCenterY
        coorObjectCenterY = Entry(squareDown, width=8)
        coorObjectCenterY.grid(row=18, column=1, columnspan=2, pady=10)

        labelObjectCenterZ = Label(squareDown, text="Z", font=('Helvetica', 9), bg='#E0E0E0')
        labelObjectCenterZ.place(relx=0.74, rely= 0.68, anchor=E)

        global coorObjectCenterZ
        coorObjectCenterZ = Entry(squareDown, width=8, justify=LEFT)
        coorObjectCenterZ.grid(row=18, column=3, sticky=W)

        novoObjeto = Button(squareDown, text="Novo objeto", font=('Helvetica', 10), bg='#edb1ba', width=9, command = newObject)
        novoObjeto.grid(row=19, column=0, columnspan=2, pady=20)

        limparCena = Button(squareDown, text="Limpar cena", font=('Helvetica', 10), bg='#edb1ba', width=9, command= clearScreen)
        limparCena.grid(row=19, column=2, columnspan=2, pady=20)

        sideBar.pack(side=RIGHT, fill=Y)
        squareUp.pack(side=TOP, fill=Y)
        squareDown.pack(side=BOTTOM, fill=Y)

    def initScreen(self):

            global screen
            screen = Frame(self.master, highlightbackground='gray', highlightthickness=1)

            screen.rowconfigure(0, weight = 1)
            screen.columnconfigure(0, weight = 1)

            global canvas 
            canvas = Canvas(screen)

            screen.place(x=10, y= 70, width=1080, height=730)

            canvas.grid(sticky="nsew")

            # Condição - objeto já estar em tela
            #canvas.bind("<Button-1>", identify)
            canvas.bind("<Button-1>", locate_xy)
            canvas.bind("<B1-Motion>", addLine)

    def initPC(self):
        planoCartesiano = Frame(self.master, highlightbackground='gray', highlightthickness=1)

        planoCartesiano.rowconfigure(0, weight = 1)
        planoCartesiano.columnconfigure(0, weight = 1)
        canvasPC = Canvas(planoCartesiano)
        planoCartesiano.place(x=20, y= 640, width=150, height=150)
        
        labelY = Label(planoCartesiano, text="Y", font=('Helvetica', 9), fg="green")
        labelY.place(relx=0.55, rely= 0.2, anchor=E)
        canvasPC.create_line((62, 25, 62, 86), fill="green")
        labelX = Label(planoCartesiano, text="X", font=('Helvetica', 9), fg="red")
        labelX.place(relx=0.85, rely= 0.5, anchor=E)
        canvasPC.create_line((62, 86, 125, 86), fill="red")
        labelZ = Label(planoCartesiano, text="Z", font=('Helvetica', 9), fg="blue")
        labelZ.place(relx=0.2, rely= 0.68, anchor=E)
        canvasPC.create_line((62, 86, 20, 120), fill="blue")
        canvasPC.grid(sticky="nsew")


def popupShowError():
    messagebox.showerror("Erro!", "Campos vazios!")

def popupShowErrorInput():
    messagebox.showerror("Erro!", "Entrada inválida!")

def popupShowLimitErrorX():
    messagebox.showerror("Erro!", "Insira valores de 0 a 1080 para X1 e X2!")

def popupShowLimitErrorY():
    messagebox.showerror("Erro!", "Insira valores de 0 a 730 para Y1 e Y2!")

def popupShowLimitError():
    messagebox.showerror("Erro!", "Limite máximo da tela atingido!")

def popupShowNumLadosError():
    messagebox.showerror("Erro!", "Número de lados deve ser entre 3 e 20")
    
def locate_xy(event):
    global current_x, current_y
    current_x, current_y = 0,0
    current_x, current_y = event.x, event.y
    print(current_x, current_y)   

def addLine(event):
    global current_x, current_y
    canvas.create_line((current_x, current_y, event.x, event.y), fill="black")
    current_x, current_y = event.x, event.y

def newWorld():
    
    if len(coorWorldLimitX1.get()) != 0 and len(coorWorldLimitY1.get()) != 0 and len(coorWorldLimitX2.get()) != 0 and len(coorWorldLimitY2.get()) != 0 \
       and len(coorViewUpX.get()) != 0 and len(coorViewUpY.get()) != 0 and len(coorViewUpZ.get()) != 0 \
       and len(coorVRPX.get()) != 0 and len(coorVRPY.get()) != 0 and len(coorVRPZ.get()) != 0 \
       and len(coorFocalPointX.get()) != 0 and len(coorFocalPointY.get()) != 0 and len(coorFocalPointZ.get()) != 0 \
       and len(coorProjectionPlane.get()) != 0 and len(coorNearPlane.get()) != 0 and len(coorFarPlane.get()) != 0:
   
        try:
            # Limite de mundo
            global coorWLX1
            coorWLX1 = int(coorWorldLimitX1.get())
            global coorWLY1
            coorWLY1 = int(coorWorldLimitY1.get())
            global coorWLX2
            coorWLX2 = int(coorWorldLimitX2.get())
            global coorWLY2
            coorWLY2 = int(coorWorldLimitY2.get())
            
            # View-up
            global coorVUX
            coorVUX = int(coorViewUpX.get())
            global coorVUY
            coorVUY = int(coorViewUpY.get())
            global coorVUZ
            coorVUZ = int(coorViewUpZ.get())
            
            #VRP
            global coorvrpx
            coorvrpx = int(coorVRPX.get())
            global coorvrpy
            coorvrpy = int(coorVRPY.get())
            global coorvrpz
            coorvrpz = int(coorVRPZ.get())

            #Ponto Focal
            global coorFPX
            coorFPX = int(coorFocalPointX.get())
            global coorFPY
            coorFPY = int(coorFocalPointY.get())
            global coorFPZ
            coorFPZ = int(coorFocalPointZ.get())

            # Distância ao plano de projeção, plano near e ao plano far
            global coorPP
            coorPP = int(coorProjectionPlane.get())
            global coorNP
            coorNP = int(coorNearPlane.get())
            global coorFP
            coorFP = int(coorFarPlane.get())
       
        except ValueError:
            popupShowErrorInput()  
        
        else:
            if ((coorWLX1 < 0) or (coorWLX1 > 1080)) or ((coorWLX2 < 0) or (coorWLX2 > 1080)):
                popupShowLimitErrorX() 
            elif ((coorWLY1 < 0) or (coorWLY1 > 730)) or ((coorWLY2 < 0) or (coorWLY2 > 730)):
                popupShowLimitErrorY() 
            elif ((coorWLX1 + coorWLX2) > 1080) or ((coorWLY1 + coorWLY2) > 730):
                popupShowLimitError() 
            else:
                placeScreen()     
    else:
        popupShowError()

def newObject():
    
    if len(coorBaseRadius.get()) != 0 and len(coorTopRadius.get()) != 0 and len(coorNumLados.get()) != 0 and len(coorObjHeight.get()) != 0 \
       and len(coorObjectCenterX.get()) != 0 and len(coorObjectCenterY.get()) != 0 and len(coorObjectCenterZ.get()) != 0:
        try:
            #Dados do Objeto

            global coorNL
            coorNL = int(coorNumLados.get())

            if(coorNL > 3 and coorNL < 20):
                #mandar para o back
                print(coorNL)

                global coorBR
                coorBR = int(coorBaseRadius.get())
                global coorTR
                coorTR = int(coorTopRadius.get())
                global coorOH
                coorOH = int(coorObjHeight.get())

                #Centro Geométrico
                global coorOCX
                coorOCX = int(coorObjectCenterX.get())
                global coorOCY
                coorOCY = int(coorObjectCenterY.get())
                global coorOCZ
                coorOCZ = int(coorObjectCenterZ.get())

                createObject()
            else:
                popupShowNumLadosError()

        except ValueError:
            popupShowErrorInput() 
    else:
        popupShowError()
    
        
def createObject():
    global obj
    obj = []
    obj1=canvas.create_polygon(10,10,70,50,200,300,10,10, fill="black", tags="clickable")
    obj2=canvas.create_polygon(50,10,70,50,400,500,10,10, fill="black", tags="clickable")
    obj3=canvas.create_polygon(30,10,70,50,700,800,10,10, fill="black", tags="clickable")
    obj.append(obj1)
    obj.append(obj2)
    obj.append(obj3)
    

def identify(event):

    item = canvas.find_closest(event.x, event.y)[0]
    id = canvas.find_withtag(tagOrId=item)
    print(id)
    objeto = obj[id[0]-1]
    for i in range(0, len(obj)):
         if i == id[0] - 1:
             canvas.itemconfig(objeto, fill='green')
         else:
             canvas.itemconfig(obj[i], fill="black")
    
    #canvas.bind("<key>", keypress)
    
# def translacao(event):
#     x,y= 0,0
#     if event.char == "q": # esquerda
#     elif event.char == "a": #direita
#     elif event.char == "w": #frente
#     elif event.char == "s": #tras
#     elif event.char == "e": #cima
#     elif event.char == "d": #baixo
#     canvas.move(id, x ,y)

# def escala(event):
#     x,y= 0,0
#     if event.char == "r": # diminui o objeto no eixo x
#     elif event.char == "f": # aumenta o objeto no eixo x
#     elif event.char == "t": # diminui o objeto no eixo z
#     elif event.char == "g": # aumenta o objeto no eixo z
#     elif event.char == "y": # diminui o objeto no eixo y
#     elif event.char == "h": # aumenta o objeto no eixo y
#     canvas.move(id, x ,y)

# def rotacao(event):
#     x,y= 0,0
#     if event.char == "u": # rotaciona para a esquerda ao redor do eixo x
#     elif event.char == "j": # rotaciona para a direita ao redor do eixo x
#     elif event.char == "i": # rotaciona para a esquerda ao redor do eixo z
#     elif event.char == "k": # rotaciona para a direita ao redor do eixo z
#     elif event.char == "o": # rotaciona para a esquerda ao redor do eixo y
#     elif event.char == "l": # rotaciona para a direita ao redor do eixo y
#     canvas.move(id, x ,y)

def placeScreen ():
    global coorWLX1, coorWLY1, coorWLX2, coorWLY2
    screen.place(x = (coorWLX1 + 10), y = (coorWLY1 + 70), width= coorWLX2, height= coorWLY2)

def clearScreen():
    canvas.delete("all")

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
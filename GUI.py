from tkinter import *
from tkinter import messagebox
from transformations import escalate, rotX, rotY, rotZ, translate
from teste_cube import return_cube
import openmesh as om
from pipeline import convertMesh2SRT
from savePoly import salvaPoligono
import numpy as np

class CanvasMenu(Frame):
    def __init__(self):

        super().__init__()

        self.initToolbar()
        self.initSideBar()
        self.initScreen()
        self.initPC()

    # Toolbar para a escolha da projeção e do sombreamento
    def initToolbar(self):

        toolBar = Frame(self.master, bg='#E0E0E0')

        global optionProj
        optionProj = BooleanVar

        labelProjection = Label(toolBar, text="Projeção:", font=('Helvetica', 10, 'bold'), bg='#E0E0E0')
        labelProjection.grid(row=0, column= 1, padx=10)
    
        perspective = Radiobutton(toolBar, text="Perspectiva", variable=optionProj, value=False, font=('Helvetica', 9), bg='#E0E0E0')
        perspective.grid(row=1, column=2, padx=5, pady=5)

        parallel = Radiobutton(toolBar, text="Paralela", variable=optionProj, value=True, font=('Helvetica', 9), bg='#E0E0E0')
        parallel.grid(row=1, column=3, padx=5, pady=5)


        optionSomb = IntVar()

        labelProjection = Label(toolBar, text="Sombreamento:", font=('Helvetica', 10, 'bold'), bg='#E0E0E0')
        labelProjection.grid(row=0, column= 5, padx=10)

        constant = Radiobutton(toolBar, text="Constante", variable=optionSomb, value=5, font=('Helvetica', 9), bg='#E0E0E0')
        constant.grid(row=1, column=6, padx=5, pady=5)
    
        gouraud = Radiobutton(toolBar, text="Gouraud", variable=optionSomb, value=3, font=('Helvetica', 9), bg='#E0E0E0')
        gouraud.grid(row=1, column=7, padx=5, pady=5)

        phong = Radiobutton(toolBar, text="Phong simplificado", variable=optionSomb, value=4, font=('Helvetica', 9), bg='#E0E0E0')
        phong.grid(row=1, column=8, padx=5, pady=5)

        toolBar.pack(side=TOP, fill=X)

    # SideBar para definição do mundo e do objeto
    def initSideBar(self):
        sideBar = Frame(self.master)

        global worldList, objectList
        worldList = []
        objectList = []

        canvasBar = Canvas(sideBar, bg='#E0E0E0')
        scrollBar = Scrollbar(sideBar, command=canvasBar.yview)
        scrollableFrame = Frame(canvasBar, bg='#E0E0E0')

        scrollableFrame.bind(
            "<Configure>",
            lambda e: canvasBar.configure(
            scrollregion=canvasBar.bbox("all")
            )
        )

        canvasBar.create_window((0,0), window=scrollableFrame, anchor='nw')
        canvasBar.config(yscrollcommand= scrollBar.set)

        #  Adição dos widgets no frame 
        labelWorldLimit = Label(scrollableFrame, text="View-port:", justify=LEFT, anchor="w", font=('Helvetica', 10, 'bold'), bg='#E0E0E0')
        labelWorldLimit.grid(row=0, column=0, padx=20, pady=10, columnspan=3, sticky=W)

        labelWarning = Label(scrollableFrame, text="(Limite máximo: 860x640)", justify=LEFT, anchor="w", font=('Helvetica', 8), bg='#E0E0E0')
        labelWarning.grid(row=0, column=2, padx=20, pady=10, columnspan=4, sticky=W)

        labelWorldLimitUMIN = Label(scrollableFrame, text="uMin", font=('Helvetica', 9), bg='#E0E0E0')
        labelWorldLimitUMIN.grid(row=1, column=0, padx=20, pady=10)

        coorWorldLimitUMIN = Entry(scrollableFrame, width= 8)
        coorWorldLimitUMIN.grid( row=1, column=1, padx=20, pady=10)
        worldList.append(coorWorldLimitUMIN)
        coorWorldLimitUMIN.insert(0, 0)

        labelWorldLimitUMAX = Label(scrollableFrame, text="uMax", font=('Helvetica', 9), bg='#E0E0E0')
        labelWorldLimitUMAX.grid(row=1, column=2, padx=15, pady=10)

        coorWorldLimitUMAX = Entry(scrollableFrame, width= 8)
        coorWorldLimitUMAX.grid(row=1, column=3, padx=20, pady=10)
        worldList.append(coorWorldLimitUMAX)
        coorWorldLimitUMAX.insert(0, 360)

        labelWorldLimitVMIN = Label(scrollableFrame, text="vMin", font=('Helvetica', 9), bg='#E0E0E0')
        labelWorldLimitVMIN.grid(row=2, column=0, padx=20, pady=10)

        coorWorldLimitY1 = Entry(scrollableFrame, width= 8)
        coorWorldLimitY1.grid(row=2, column=1, padx=20, pady=10)
        worldList.append(coorWorldLimitY1)
        coorWorldLimitY1.insert(0, 0)

        labelWorldLimitVMAX = Label(scrollableFrame, text="vMax", font=('Helvetica', 9), bg='#E0E0E0')
        labelWorldLimitVMAX.grid(row=2, column=2, padx=15, pady=10)

        coorWorldLimitVMAX = Entry(scrollableFrame, width= 8)
        coorWorldLimitVMAX.grid(row=2, column=3, padx=20, pady=10)
        worldList.append(coorWorldLimitVMAX)
        coorWorldLimitVMAX.insert(0, 360)

        labelViewUp = Label(scrollableFrame, text="VIEW-UP:", justify=LEFT, anchor="w", font=('Helvetica', 10, 'bold'), bg='#E0E0E0')
        labelViewUp.grid(row=3, column=0, padx=20, pady=10, columnspan=3, sticky=W)

        labelViewUpX = Label(scrollableFrame, text="X", font=('Helvetica', 9), bg='#E0E0E0')
        labelViewUpX.grid(row=4, column=0, pady=10)

        coorViewUpX = Entry(scrollableFrame, width= 8)
        coorViewUpX.grid(row=4, column=1, pady=10)
        worldList.append(coorViewUpX)
        coorViewUpX.insert(0, 0)

        labelViewUpY = Label(scrollableFrame, text="Y", font=('Helvetica', 9), bg='#E0E0E0')
        labelViewUpY.grid(row=5, column=0, pady=10)

        coorViewUpY = Entry(scrollableFrame, width= 8)
        coorViewUpY.grid(row=5, column=1, pady=10)
        worldList.append(coorViewUpY)
        coorViewUpY.insert(0, 1)

        labelViewUpZ = Label(scrollableFrame, text="Z", font=('Helvetica', 9), bg='#E0E0E0')
        labelViewUpZ.grid(row=6, column=0, pady=10)

        coorViewUpZ = Entry(scrollableFrame, width= 8)
        coorViewUpZ.grid(row=6, column=1, pady=10)
        worldList.append(coorViewUpZ)
        coorViewUpZ.insert(0, 0)

        labelVPR = Label(scrollableFrame, text="VRP:", font=('Helvetica', 10, 'bold'), bg='#E0E0E0')
        labelVPR.grid(row=3, column=2, pady=10)

        labelVRPX = Label(scrollableFrame, text="X", font=('Helvetica', 9), bg='#E0E0E0')
        labelVRPX.grid(row=4, column=2, pady=10)

        coorVRPX = Entry(scrollableFrame, width=8)
        coorVRPX.grid(row=4, column=3, pady=10)
        worldList.append(coorVRPX)
        coorVRPX.insert(0, 0)

        labelVRPY = Label(scrollableFrame, text="Y", font=('Helvetica', 9), bg='#E0E0E0')
        labelVRPY.grid(row=5, column=2, pady=10)
        
        coorVRPY = Entry(scrollableFrame, width=8)
        coorVRPY.grid(row=5, column=3, pady=10)
        worldList.append(coorVRPY)
        coorVRPY.insert(0, 10)

        labelVRPZ = Label(scrollableFrame, text="Z", font=('Helvetica', 9), bg='#E0E0E0')
        labelVRPZ.grid(row=6, column=2, pady=10)
       
        coorVRPZ = Entry(scrollableFrame, width=8)
        coorVRPZ.grid(row=6, column=3, pady=10)
        worldList.append(coorVRPZ)
        coorVRPZ.insert(0, 10)

        labelFocalPoint = Label(scrollableFrame, text="Ponto focal:", justify=LEFT, anchor="w", font=('Helvetica', 10, 'bold'), bg='#E0E0E0')
        labelFocalPoint.grid(row=7, column=0, padx=20, pady=10, columnspan=3, sticky=W)

        labelFocalPointX = Label(scrollableFrame, text="X", font=('Helvetica', 9), bg='#E0E0E0')
        labelFocalPointX.grid(row=8, column=0, pady=10)

        coorFocalPointX = Entry(scrollableFrame, width=8)
        coorFocalPointX.grid(row=8, column=1, pady=10)
        worldList.append(coorFocalPointX)
        coorFocalPointX.insert(0, 0)
        
        labelFocalPointY = Label(scrollableFrame, text="Y", font=('Helvetica', 9), bg='#E0E0E0')
        labelFocalPointY.grid(row=9, column=0, pady=10)

        coorFocalPointY = Entry(scrollableFrame, width=8)
        coorFocalPointY.grid(row=9, column=1, pady=10)
        worldList.append(coorFocalPointY)
        coorFocalPointY.insert(0, 0)

        labelFocalPointZ = Label(scrollableFrame, text="Z", font=('Helvetica', 9), bg='#E0E0E0')
        labelFocalPointZ.grid(row=10, column=0, pady=10)

        coorFocalPointZ = Entry(scrollableFrame, width=8)
        coorFocalPointZ.grid(row=10, column=1, pady=10)
        worldList.append(coorFocalPointZ)
        coorFocalPointZ.insert(0, 0)

        labelDistance = Label(scrollableFrame, text="Distância ao plano:", justify=LEFT, anchor="w", font=('Helvetica', 10, 'bold'), bg='#E0E0E0')
        labelDistance.grid(row=7, column=2, pady=8, columnspan=3, sticky=W)

        labelProjectionPlane = Label(scrollableFrame, text="Projeção", font=('Helvetica', 9), bg='#E0E0E0')
        labelProjectionPlane.grid(row=8, column=2, pady=8)

        distProjectionPlane = Entry(scrollableFrame, width=8)
        distProjectionPlane.grid(row=8, column=3, pady=8)
        worldList.append(distProjectionPlane)
        distProjectionPlane.insert(0, 10)

        labelNearPlane = Label(scrollableFrame, text="Near", font=('Helvetica', 9), bg='#E0E0E0')
        labelNearPlane.grid(row=9, column=2, pady=8)

        distNearPlane = Entry(scrollableFrame, width=8)
        distNearPlane.grid(row=9, column=3, pady=8)
        worldList.append(distNearPlane)
        distNearPlane.insert(0, 5)

        labelFarPlane = Label(scrollableFrame, text="Far", font=('Helvetica', 9), bg='#E0E0E0')
        labelFarPlane.grid(row=10, column=2, pady=8)

        distFarPlane = Entry(scrollableFrame, width=8)
        distFarPlane.grid(row=10, column=3, pady=8)
        worldList.append(distFarPlane)
        distFarPlane.insert(0, 15)

        labelProjectionPlane = Label(scrollableFrame, text="World window:", justify=LEFT, anchor="w", font=('Helvetica', 10, 'bold'), bg='#E0E0E0')
        labelProjectionPlane.grid(row=11, column=0, padx=20, pady=10, columnspan=3, sticky=W)

        labelProjectionPlaneXMIN = Label(scrollableFrame, text="Xmin", font=('Helvetica', 9), bg='#E0E0E0')
        labelProjectionPlaneXMIN.grid(row=12, column=0, pady=10)

        coorProjectionPlaneXMIN = Entry(scrollableFrame, width= 8)
        coorProjectionPlaneXMIN.grid(row=12, column=1, pady=10)
        worldList.append(coorProjectionPlaneXMIN)
        coorProjectionPlaneXMIN.insert(0,-10)

        labelProjectionPlaneXMAX = Label(scrollableFrame, text="Xmax", font=('Helvetica', 9), bg='#E0E0E0')
        labelProjectionPlaneXMAX.grid(row=12, column=2, pady=10)

        coorProjectionPlaneXMAX = Entry(scrollableFrame, width= 8)
        coorProjectionPlaneXMAX.grid(row=12, column=3, pady=10)
        worldList.append(coorProjectionPlaneXMAX)
        coorProjectionPlaneXMAX.insert(0,10)

        labelProjectionPlaneYMIN = Label(scrollableFrame, text="Ymin", font=('Helvetica', 9), bg='#E0E0E0')
        labelProjectionPlaneYMIN.grid(row=13, column=0, pady=10)

        coorProjectionPlaneYMIN = Entry(scrollableFrame, width= 8)
        coorProjectionPlaneYMIN.grid(row=13, column=1, pady=10)
        worldList.append(coorProjectionPlaneYMIN)
        coorProjectionPlaneYMIN.insert(0,-10)

        labelProjectionPlaneYMAX = Label(scrollableFrame, text="Ymax", font=('Helvetica', 9), bg='#E0E0E0')
        labelProjectionPlaneYMAX.grid(row=13, column=2, pady=10)

        coorProjectionPlaneYMAX = Entry(scrollableFrame, width= 8)
        coorProjectionPlaneYMAX.grid(row=13, column=3, pady=10)
        worldList.append(coorProjectionPlaneYMAX)
        coorProjectionPlaneYMAX.insert(0,10)
    
        labelObject = Label(scrollableFrame, text="Dados do objeto:", justify=LEFT, anchor="w", font=('Helvetica', 10, 'bold'), bg='#E0E0E0')
        labelObject.grid(row=15, column=0, padx=20, pady=10, columnspan=4, sticky=W)

        labelBaseRadius = Label(scrollableFrame, text="Raio da base", font=('Helvetica', 9), bg='#E0E0E0')
        labelBaseRadius.grid(row=16, column=0, padx=20, pady=10)

        BaseRadius = Entry(scrollableFrame, width= 8)
        BaseRadius.grid(row=16, column=1, pady=10)
        objectList.append(BaseRadius)
        BaseRadius.insert(0,10)

        labelTopRadius = Label(scrollableFrame, text="Raio do topo", font=('Helvetica', 9), bg='#E0E0E0')
        labelTopRadius.grid(row=16, column=2, pady=10)

        TopRadius = Entry(scrollableFrame, width= 8)
        TopRadius.grid(row=16, column=3, pady=10)
        objectList.append(TopRadius)
        TopRadius.insert(0,6)

        labelNumSides = Label(scrollableFrame, text="Nº de lados", font=('Helvetica', 9), bg='#E0E0E0')
        labelNumSides.grid(row=17, column=0, padx=20, pady=10)

        NumSides = Entry(scrollableFrame, width= 8)
        NumSides.grid(row=17, column=1, pady=10)
        objectList.append(NumSides)
        NumSides.insert(0,10)

        labelObjHeight = Label(scrollableFrame, text="Altura", font=('Helvetica', 9), bg='#E0E0E0')
        labelObjHeight.grid(row=17, column=2, pady=10)

        ObjHeight = Entry(scrollableFrame, width= 8)
        ObjHeight.grid(row=17, column=3, pady=10)
        objectList.append(ObjHeight)
        ObjHeight.insert(0,5)
        
        labelObjectCenter = Label(scrollableFrame, text="Centro Geométrico:", justify=LEFT, anchor="w", font=('Helvetica', 10, 'bold'), bg='#E0E0E0')
        labelObjectCenter.grid(row=18, column=0, padx=20, pady=10, columnspan=4, sticky=W)
        
        objectCenterX = Label(scrollableFrame, text="X", font=('Helvetica', 9), bg='#E0E0E0')
        objectCenterX.grid(row=19, column=0, pady=10)

        coorObjectCenterX = Entry(scrollableFrame, width=8)
        coorObjectCenterX.grid(row=19, column=1, pady=10)
        objectList.append(coorObjectCenterX)
        coorObjectCenterX.insert(0,0)

        objectCenterY = Label(scrollableFrame, text="Y", font=('Helvetica', 9), bg='#E0E0E0')
        objectCenterY.grid(row=20, column=0, pady=10)

        coorObjectCenterY = Entry(scrollableFrame, width=8)
        coorObjectCenterY.grid(row=20, column=1, pady=10)
        objectList.append(coorObjectCenterY)
        coorObjectCenterY.insert(0,0)

        objectCenterZ = Label(scrollableFrame, text="Z", font=('Helvetica', 9), bg='#E0E0E0')
        objectCenterZ.grid(row=21, column=0, pady=10)

        coorObjectCenterZ = Entry(scrollableFrame, width=8)
        coorObjectCenterZ.grid(row=21, column=1, pady=10)
        objectList.append(coorObjectCenterZ)
        coorObjectCenterZ.insert(0,0)

        novoMundo = Button(scrollableFrame, text="Novo mundo", font=('Helvetica', 10), bg='#edb1ba', width=9, command = newWorld)
        novoMundo.grid(row=22, column=0, pady=10)

        novoObjeto = Button(scrollableFrame, text="Novo objeto", font=('Helvetica', 10), bg='#edb1ba', width=9, command = newObject)
        novoObjeto.grid(row=22, column=1, pady=10)

        limparCena = Button(scrollableFrame, text="Limpar cena", font=('Helvetica', 10), bg='#edb1ba', width=9, command= clearScreen)
        limparCena.grid(row=22, column=3, pady=10) 

        sideBar.pack(side=RIGHT, fill=Y)
        canvasBar.pack(side=LEFT, fill=BOTH, expand=True)
        scrollBar.pack(side=RIGHT, fill=Y)

    def initPC(self):
        planoCartesiano = Frame(self.master, highlightbackground='gray', highlightthickness=1)

        planoCartesiano.rowconfigure(0, weight = 1)
        planoCartesiano.columnconfigure(0, weight = 1)

        canvasPC = Canvas(planoCartesiano)
        planoCartesiano.place(x=20, y= 550, width=150, height=150)

        labelXAxis = Label(planoCartesiano, text="X", font=('Helvetica', 9), fg="red")
        labelXAxis.place(relx=0.85, rely= 0.5, anchor=E)
        canvasPC.create_line((62, 86, 125, 86), fill="red")
        
        labelYAxis = Label(planoCartesiano, text="Y", font=('Helvetica', 9), fg="green")
        labelYAxis.place(relx=0.55, rely= 0.2, anchor=E)
        canvasPC.create_line((62, 25, 62, 86), fill="green")

        labelZAxis = Label(planoCartesiano, text="Z", font=('Helvetica', 9), fg="blue")
        labelZAxis.place(relx=0.2, rely= 0.68, anchor=E)
        canvasPC.create_line((62, 86, 20, 120), fill="blue")

        canvasPC.grid(sticky="nsew")

    def initScreen(self):
            global screen
            screen = Frame(self.master, highlightbackground='gray', highlightthickness=1)

            screen.rowconfigure(0, weight = 5)
            screen.columnconfigure(0, weight = 5)

            global canvas 
            canvas = Canvas(screen)

            screen.place(x=10, y= 70, width=860, height=640)

            canvas.grid(sticky="nsew")

            canvas.bind("<Button-1>", identifyObject)
            canvas.focus_set()
            #canvas.bind("<Button-1>", locate_xy)
            #canvas.bind("<B1-Motion>", addLine)

def popupShowErrorEmptyInput():
    messagebox.showerror("Erro!", "Campos vazios!")

def popupShowErrorInput():
    messagebox.showerror("Erro!", "Entrada inválida!")

def popupShowLimitErrorX():
    messagebox.showerror("Erro!", "Insira valores de 0 a 860 para X1 e X2!")

def popupShowLimitErrorY():
    messagebox.showerror("Erro!", "Insira valores de 0 a 640 para Y1 e Y2!")

def popupShowLimitError():
    messagebox.showerror("Erro!", "Limite máximo da tela atingido!")

def popupShowNumSidesError():
    messagebox.showerror("Erro!", "Número de lados deve ser entre 3 e 20!")

def newWorld():
    if len(worldList[0].get()) != 0 and len(worldList[1].get()) != 0 and len(worldList[2].get()) != 0 and len(worldList[3].get()) != 0 \
       and len(worldList[4].get()) != 0 and len(worldList[5].get()) != 0 and len(worldList[6].get()) != 0 \
       and len(worldList[7].get()) != 0 and len(worldList[8].get()) != 0 and len(worldList[9].get()) != 0 \
       and len(worldList[10].get()) != 0 and len(worldList[11].get()) != 0 and len(worldList[12].get()) != 0 \
       and len(worldList[13].get()) != 0 and len(worldList[14].get()) != 0 and len(worldList[15].get()) != 0 \
       and len(worldList[16].get()) != 0 and len(worldList[17].get()) != 0 and len(worldList[18].get()) != 0:
   
        try:
            #View-port
            global listViewPort
            listViewPort = []
            listViewPort.append(int(worldList[0].get()))
            listViewPort.append(int(worldList[1].get()))
            listViewPort.append(int(worldList[2].get()))
            listViewPort.append(int(worldList[3].get()))
            
            #View-up
            global listViewUp
            listViewUp = []
            listViewUp.append(int(worldList[4].get()))
            listViewUp.append(int(worldList[5].get()))
            listViewUp.append(int(worldList[6].get()))
            
            #VRP
            global listVRP
            listVRP = []
            listVRP.append(int(worldList[7].get()))
            listVRP.append(int(worldList[8].get()))
            listVRP.append(int(worldList[9].get()))

            #Ponto Focal
            global listP
            listP = []
            listP.append(int(worldList[10].get()))
            listP.append(int(worldList[11].get()))
            listP.append(int(worldList[12].get()))

            # Distância ao plano de projeção, plano near e ao plano far
            global listDist
            listDist = []
            listDist.append(int(worldList[13].get()))
            listDist.append(int(worldList[14].get()))
            listDist.append(int(worldList[15].get()))

            # Janela do mundo
            global listWW
            listWW = []
            listWW.append(int(worldList[16].get()))
            listWW.append(int(worldList[17].get()))
            listWW.append(int(worldList[18].get()))
            listWW.append(int(worldList[19].get()))
       
        except ValueError:
            popupShowErrorInput()  
        
        else:
            if ((listViewPort[0] < 0) or (listViewPort[0] > 860)) or ((listViewPort[1] < 0) or (listViewPort[1] > 860)):
                popupShowLimitErrorX() 
            elif ((listViewPort[2] < 0) or (listViewPort[2] > 640)) or ((listViewPort[3] < 0) or (listViewPort[3] > 640)):
                popupShowLimitErrorY() 
            elif ((listViewPort[0] + listViewPort[1]) > 860) or ((listViewPort[2] + listViewPort[3]) > 640):
                popupShowLimitError() 
            else:
                canvas.focus_set()
                placeScreen()  
    else:
        popupShowErrorEmptyInput()

def newObject():
    if len(objectList[0].get()) != 0 and len(objectList[1].get()) != 0 and len(objectList[2].get()) != 0 and len(objectList[3].get()) != 0 \
       and len(objectList[4].get()) != 0 and len(objectList[5].get()) != 0 and len(objectList[6].get()) != 0:
        try:

            #Número de lados
            NL = int(objectList[2].get())

            if(NL > 3 and NL < 20):

                #Raio da base
                BR = int(objectList[0].get())

                #Raio do topo
                TR = int(objectList[1].get())

                #Altura do objeto
                OH = int(objectList[3].get())

                #Centro Geométrico
                coorOCX = int(objectList[4].get())
                coorOCY = int(objectList[5].get())
                coorOCZ = int(objectList[5].get())
                canvas.focus_set()
                createObject(BR, TR, NL, OH, [coorOCX, coorOCY, coorOCZ])

            else:
                popupShowNumSidesError()

        except ValueError:
            popupShowErrorInput() 
    else:
        popupShowErrorEmptyInput()

# def locate_xy(event):
#     global current_x, current_y
#     current_x, current_y = 0,0
#     current_x, current_y = event.x, event.y
#     print(current_x, current_y)   

# def addLine(event):
#     global current_x, current_y
#     canvas.create_line((current_x, current_y, event.x, event.y), fill="black")
#     current_x, current_y = event.x, event.y

def placeScreen ():
    screen.place(x = (listViewPort[0] + 10), y = (listViewPort[2] + 70), width= listViewPort[1], height= listViewPort[3])

def clearScreen():
    canvas.delete("all")

def createObject(raioBase, raioTopo, nLados, altura, GC):
    global obj
    obj = []

    #face = []
    global mesh
    mesh = salvaPoligono(raioBase, raioTopo, nLados, altura, GC)
    #Converte para SRT
    meshSRT = convertMesh2SRT(mesh, np.array(listVRP), listDist[0], listWW[0], listWW[1], listWW[2], listWW[3], listViewPort[0], listViewPort[1], listViewPort[2], listViewPort[3], np.array(listP), np.array(listViewUp), optionProj)

    #print(meshSRT.points())

    for fh in meshSRT.faces():
        face = []
        for vh in meshSRT.fv(fh):
            point = meshSRT.point(vh)
            face.append([point[0], point[1]])
        obj.append(canvas.create_polygon(face, fill="red", tags="clickable", outline="black"))



def identifyObject(event):
    global tuple
    tuple = canvas.find_all()
    if len(tuple) == 0:
        print("Nenhum objeto no Canvas!")
    else:
        #id = int(canvas.find_closest(event.x, event.y)[0])

        for i in range(0, len(tuple)):
            canvas.itemconfig(tuple[i], fill='green')
        
        canvas.bind_all("<Key>", translacao)
        canvas.bind_all("<Key>", escala)
        canvas.bind_all("<Key>", rotacao)

        # for i in range(0, len(tuple)):
        #     if id == tuple[i]:
        #         object = obj[i]
        #         for j in range(0, len(obj)):
        #             if j == i:
        #                 canvas.itemconfig(object, fill='green')
        #             else:
        #                 canvas.itemconfig(obj[j], fill="black")



def translacao(event):
    x, y, z = 0, 0, 0
    if event.char == "q": 
        x, y, z = -1, 0, 0
        object = translate(mesh, x, y, z)
    elif event.char == "a": 
        x, y, z = 1, 0, 0
        object = translate(mesh, x, y, z)
    elif event.char == "w": 
        x, y, z = 0, 0, 1
        object = translate(mesh, x, y, z)
    elif event.char == "s":
        x, y, z = 0, 0, -1
        object = translate(mesh, x, y, z)
    elif event.char == "e":
        x, y, z = 0, 1, 0
        object = translate(mesh, x, y, z)
    elif event.char == "d": 
        x, y, z = 0, -1, 0
        object = translate(mesh, x, y, z)

    #delete object
    for i in range(0, len(obj)):
        canvas.delete(obj[i])

    #Converte para SRT
    meshSRT = convertMesh2SRT(object, np.array(listVRP), listDist[0], listWW[0], listWW[1], listWW[2], listWW[3], listViewPort[0], listViewPort[1], listViewPort[2], listViewPort[3], np.array(listP), np.array(listViewUp), optionProj)

    for fh in meshSRT.faces():
        face = []
        for vh in meshSRT.fv(fh):
            point = meshSRT.point(vh)
            face.append([point[0], point[1]])
        obj.append(canvas.create_polygon(face, fill="red", tags="clickable", outline="black"))

def escala(event):
    x,y,z= 0,0, 0
    if event.char == "r": # diminui o objeto no eixo x
        x, y, z = 0.5, 1, 1
        object = escalate(mesh, x, y, z)
    elif event.char == "f": # aumenta o objeto no eixo x
        x, y, z = 2, 1, 1
        object = escalate(mesh, x, y, z)
    elif event.char == "t": # diminui o objeto no eixo z
        x, y, z = 1, 1, 0.5
        object = escalate(mesh, x, y, z)
    elif event.char == "g": # aumenta o objeto no eixo z
        x, y, z = 1, 1, 2
        object = escalate(mesh, x, y, z)
    elif event.char == "y": # diminui o objeto no eixo y
        x, y, z = 1, 0.5, 1
        object = escalate(mesh, x, y, z)
    elif event.char == "h": # aumenta o objeto no eixo y
        x, y, z = 1, 2, 1
        object = escalate(mesh, x, y, z)
    
        #delete object
    for i in range(0, len(obj)):
        canvas.delete(obj[i])

    #Converte para SRT
    meshSRT = convertMesh2SRT(object, np.array(listVRP), listDist[0], listWW[0], listWW[1], listWW[2], listWW[3], listViewPort[0], listViewPort[1], listViewPort[2], listViewPort[3], np.array(listP), np.array(listViewUp), optionProj)

    for fh in meshSRT.faces():
        face = []
        for vh in meshSRT.fv(fh):
            point = meshSRT.point(vh)
            face.append([point[0], point[1]])
        obj.append(canvas.create_polygon(face, fill="red", tags="clickable", outline="black"))

def rotacao(event):
    angulo = 0
    if event.char == "u": # rotaciona para a esquerda ao redor do eixo xp
        angulo = 1
        object = rotX(mesh, angulo)
    elif event.char == "j": # rotaciona para a direita ao redor do eixo x
        angulo = -1
        object = rotX(mesh, angulo)
    elif event.char == "i": # rotaciona para a esquerda ao redor do eixo z
        angulo = 1
        object = rotZ(mesh, angulo)
    elif event.char == "k": # rotaciona para a direita ao redor do eixo z
        angulo = -1
        object = rotZ(mesh, angulo)
    elif event.char == "o": # rotaciona para a esquerda ao redor do eixo y
        angulo = 1
        object = rotY(mesh, angulo)
    elif event.char == "l": # rotaciona para a direita ao redor do eixo y
        angulo = -1
        object = rotY(mesh, angulo)
    
    #delete object
    for i in range(0, len(obj)):
        canvas.delete(obj[i])

    #Converte para SRT
    meshSRT = convertMesh2SRT(object, np.array(listVRP), listDist[0], listWW[0], listWW[1], listWW[2], listWW[3], listViewPort[0], listViewPort[1], listViewPort[2], listViewPort[3], np.array(listP), np.array(listViewUp), optionProj)

    for fh in meshSRT.faces():
        face = []
        for vh in meshSRT.fv(fh):
            point = meshSRT.point(vh)
            face.append([point[0], point[1]])
        obj.append(canvas.create_polygon(face, fill="red", tags="clickable", outline="black"))

def run_program():
    root = Tk()
    root.resizable(width=False, height=False)
    root.title('3D-modeller-and-viewer')

    width = 1280
    height = 720

    widthScreen = root.winfo_screenwidth()
    heightScreen = root.winfo_screenheight()

    posx = widthScreen/2 - width/2
    posy = (heightScreen/2 - height/2) - 30

    root.geometry("%dx%d+%d+%d" % (width, height, posx, posy))
    
    CanvasMenu()
   
    root.mainloop()

if __name__ == '__main__':
    run_program()
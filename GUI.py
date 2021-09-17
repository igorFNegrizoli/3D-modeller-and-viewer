from tkinter import *
from tkinter import messagebox

from numpy.core.arrayprint import BoolFormat
from transformations import escalate, rotX, rotY, rotZ, translate
from pipeline import convertMesh2SRT, perspProj, sru2src
from pipeline import isMeshVisible
from savePoly import salvaPoligono
import numpy as np
from utils import rgba2hex
from doisDCrop import cutBorder

class CanvasMenu(Frame):
    def __init__(self):

        super().__init__()

        self.initToolbar()
        self.initSideBar()
        self.initScreen()
        self.initPC()

    # Toolbar para a escolha da projeção e do sombreamento
    def initToolbar(self):
        global listProj

        toolBar = Frame(self.master, bg='#E0E0E0')

        Proj = BooleanVar()
        Proj.set("True")
        listProj.append(Proj)

        labelProjection = Label(toolBar, text="Projeção:", font=('Helvetica', 10, 'bold'), bg='#E0E0E0')
        labelProjection.grid(row=0, column= 1, padx=10)
    
        perspective = Radiobutton(toolBar, text="Perspectiva", variable=Proj, value=True, command=lambda: clicked(Proj.get()), font=('Helvetica', 9), bg='#E0E0E0')
        perspective.grid(row=1, column=2, padx=5, pady=5)

        parallel = Radiobutton(toolBar, text="Paralela", variable=Proj, value=False, command=lambda: clicked(Proj.get()), font=('Helvetica', 9), bg='#E0E0E0')
        parallel.grid(row=1, column=3, padx=5, pady=5)

        toolBar.pack(side=TOP, fill=X)

    # SideBar para definição do mundo e do objeto
    def initSideBar(self):
        sideBar = Frame(self.master)

        global worldList, objectDataList
        worldList = []
        objectDataList = []

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
        labelObject = Label(scrollableFrame, text="Dados do mundo:", justify=LEFT, anchor="w", font=('Helvetica', 10, 'bold'), bg='#E0E0E0', fg='#990303')
        labelObject.grid(row=0, column=0, padx=20, pady=10, columnspan=4, sticky=W)

        labelWorldLimit = Label(scrollableFrame, text="View-port:", justify=LEFT, anchor="w", font=('Helvetica', 10, 'bold'), bg='#E0E0E0')
        labelWorldLimit.grid(row=1, column=0, padx=20, pady=10, columnspan=3, sticky=W)

        labelWarning = Label(scrollableFrame, text="(Limite máximo: 860x640)", justify=LEFT, anchor="w", font=('Helvetica', 8), bg='#E0E0E0')
        labelWarning.grid(row=1, column=1, padx=20, pady=10, columnspan=4, sticky=W)

        labelWorldLimitUMIN = Label(scrollableFrame, text="uMin", font=('Helvetica', 9), bg='#E0E0E0')
        labelWorldLimitUMIN.grid(row=2, column=0, padx=20, pady=10)

        coorWorldLimitUMIN = Entry(scrollableFrame, width= 8)
        coorWorldLimitUMIN.grid(row=2, column=1, padx=20, pady=10)
        coorWorldLimitUMIN.insert(0, 0)
        worldList.append(coorWorldLimitUMIN)

        labelWorldLimitUMAX = Label(scrollableFrame, text="uMax", font=('Helvetica', 9), bg='#E0E0E0')
        labelWorldLimitUMAX.grid(row=2, column=2, padx=15, pady=10)

        coorWorldLimitUMAX = Entry(scrollableFrame, width= 8)
        coorWorldLimitUMAX.grid(row=2, column=3, padx=20, pady=10)
        coorWorldLimitUMAX.insert(0, 860)
        worldList.append(coorWorldLimitUMAX)

        labelWorldLimitVMIN = Label(scrollableFrame, text="vMin", font=('Helvetica', 9), bg='#E0E0E0')
        labelWorldLimitVMIN.grid(row=3, column=0, padx=20, pady=10)

        coorWorldLimitY1 = Entry(scrollableFrame, width= 8)
        coorWorldLimitY1.grid(row=3, column=1, padx=20, pady=10)
        coorWorldLimitY1.insert(0, 0)
        worldList.append(coorWorldLimitY1)

        labelWorldLimitVMAX = Label(scrollableFrame, text="vMax", font=('Helvetica', 9), bg='#E0E0E0')
        labelWorldLimitVMAX.grid(row=3, column=2, padx=15, pady=10)

        coorWorldLimitVMAX = Entry(scrollableFrame, width= 8)
        coorWorldLimitVMAX.grid(row=3, column=3, padx=20, pady=10)
        coorWorldLimitVMAX.insert(0, 640)
        worldList.append(coorWorldLimitVMAX)
        
        labelViewUp = Label(scrollableFrame, text="View-up:", justify=LEFT, anchor="w", font=('Helvetica', 10, 'bold'), bg='#E0E0E0')
        labelViewUp.grid(row=4, column=0, padx=20, pady=10, columnspan=3, sticky=W)

        labelViewUpX = Label(scrollableFrame, text="X", font=('Helvetica', 9), bg='#E0E0E0')
        labelViewUpX.grid(row=5, column=0, pady=10)

        coorViewUpX = Entry(scrollableFrame, width= 8)
        coorViewUpX.grid(row=5, column=1, pady=10)
        coorViewUpX.insert(0, 0)
        worldList.append(coorViewUpX)
        
        labelViewUpY = Label(scrollableFrame, text="Y", font=('Helvetica', 9), bg='#E0E0E0')
        labelViewUpY.grid(row=6, column=0, pady=10)

        coorViewUpY = Entry(scrollableFrame, width= 8)
        coorViewUpY.grid(row=6, column=1, pady=10)
        coorViewUpY.insert(0, 1)
        worldList.append(coorViewUpY)

        labelViewUpZ = Label(scrollableFrame, text="Z", font=('Helvetica', 9), bg='#E0E0E0')
        labelViewUpZ.grid(row=7, column=0, pady=10)

        coorViewUpZ = Entry(scrollableFrame, width= 8)
        coorViewUpZ.grid(row=7, column=1, pady=10)
        coorViewUpZ.insert(0, 0)
        worldList.append(coorViewUpZ)

        labelVPR = Label(scrollableFrame, text="VRP:", font=('Helvetica', 10, 'bold'), bg='#E0E0E0')
        labelVPR.grid(row=4, column=2, pady=10)

        labelVRPX = Label(scrollableFrame, text="X", font=('Helvetica', 9), bg='#E0E0E0')
        labelVRPX.grid(row=5, column=2, pady=10)

        coorVRPX = Entry(scrollableFrame, width=8)
        coorVRPX.grid(row=5, column=3, pady=10)
        coorVRPX.insert(0, 0)
        worldList.append(coorVRPX)

        labelVRPY = Label(scrollableFrame, text="Y", font=('Helvetica', 9), bg='#E0E0E0')
        labelVRPY.grid(row=6, column=2, pady=10)
        
        coorVRPY = Entry(scrollableFrame, width=8)
        coorVRPY.grid(row=6, column=3, pady=10)
        coorVRPY.insert(0, 10)
        worldList.append(coorVRPY)

        labelVRPZ = Label(scrollableFrame, text="Z", font=('Helvetica', 9), bg='#E0E0E0')
        labelVRPZ.grid(row=7, column=2, pady=10)
       
        coorVRPZ = Entry(scrollableFrame, width=8)
        coorVRPZ.grid(row=7, column=3, pady=10)
        coorVRPZ.insert(0, 10)
        worldList.append(coorVRPZ)
        
        labelFocalPoint = Label(scrollableFrame, text="Ponto focal:", justify=LEFT, anchor="w", font=('Helvetica', 10, 'bold'), bg='#E0E0E0')
        labelFocalPoint.grid(row=8, column=0, padx=20, pady=10, columnspan=3, sticky=W)

        labelFocalPointX = Label(scrollableFrame, text="X", font=('Helvetica', 9), bg='#E0E0E0')
        labelFocalPointX.grid(row=9, column=0, pady=10)

        coorFocalPointX = Entry(scrollableFrame, width=8)
        coorFocalPointX.grid(row=9, column=1, pady=10)
        coorFocalPointX.insert(0, 0)
        worldList.append(coorFocalPointX)
        
        labelFocalPointY = Label(scrollableFrame, text="Y", font=('Helvetica', 9), bg='#E0E0E0')
        labelFocalPointY.grid(row=10, column=0, pady=10)

        coorFocalPointY = Entry(scrollableFrame, width=8)
        coorFocalPointY.grid(row=10, column=1, pady=10)
        coorFocalPointY.insert(0, 0)
        worldList.append(coorFocalPointY)

        labelFocalPointZ = Label(scrollableFrame, text="Z", font=('Helvetica', 9), bg='#E0E0E0')
        labelFocalPointZ.grid(row=11, column=0, pady=10)

        coorFocalPointZ = Entry(scrollableFrame, width=8)
        coorFocalPointZ.grid(row=11, column=1, pady=10)
        coorFocalPointZ.insert(0, 0)
        worldList.append(coorFocalPointZ)

        labelDistance = Label(scrollableFrame, text="Distância ao plano:", justify=LEFT, anchor="w", font=('Helvetica', 10, 'bold'), bg='#E0E0E0')
        labelDistance.grid(row=8, column=2, pady=8, columnspan=3, sticky=W)

        labelProjectionPlane = Label(scrollableFrame, text="Projeção", font=('Helvetica', 9), bg='#E0E0E0')
        labelProjectionPlane.grid(row=9, column=2, pady=8)

        distProjectionPlane = Entry(scrollableFrame, width=8)
        distProjectionPlane.grid(row=9, column=3, pady=8)
        distProjectionPlane.insert(0, 10)
        worldList.append(distProjectionPlane)
        
        labelNearPlane = Label(scrollableFrame, text="Near", font=('Helvetica', 9), bg='#E0E0E0')
        labelNearPlane.grid(row=10, column=2, pady=8)

        distNearPlane = Entry(scrollableFrame, width=8)
        distNearPlane.grid(row=10, column=3, pady=8)
        distNearPlane.insert(0, 5)
        worldList.append(distNearPlane)
        
        labelFarPlane = Label(scrollableFrame, text="Far", font=('Helvetica', 9), bg='#E0E0E0')
        labelFarPlane.grid(row=11, column=2, pady=8)

        distFarPlane = Entry(scrollableFrame, width=8)
        distFarPlane.grid(row=11, column=3, pady=8)
        distFarPlane.insert(0, 15)
        worldList.append(distFarPlane)
        
        labelProjectionPlane = Label(scrollableFrame, text="World window:", justify=LEFT, anchor="w", font=('Helvetica', 10, 'bold'), bg='#E0E0E0')
        labelProjectionPlane.grid(row=12, column=0, padx=20, pady=10, columnspan=3, sticky=W)

        labelProjectionPlaneXMIN = Label(scrollableFrame, text="XMin", font=('Helvetica', 9), bg='#E0E0E0')
        labelProjectionPlaneXMIN.grid(row=13, column=0, pady=10)

        coorProjectionPlaneXMIN = Entry(scrollableFrame, width= 8)
        coorProjectionPlaneXMIN.grid(row=13, column=1, pady=10)
        coorProjectionPlaneXMIN.insert(0, -10)
        worldList.append(coorProjectionPlaneXMIN)
    
        labelProjectionPlaneXMAX = Label(scrollableFrame, text="XMax", font=('Helvetica', 9), bg='#E0E0E0')
        labelProjectionPlaneXMAX.grid(row=13, column=2, pady=10)

        coorProjectionPlaneXMAX = Entry(scrollableFrame, width= 8)
        coorProjectionPlaneXMAX.grid(row=13, column=3, pady=10)
        coorProjectionPlaneXMAX.insert(0,10)
        worldList.append(coorProjectionPlaneXMAX)

        labelProjectionPlaneYMIN = Label(scrollableFrame, text="YMin", font=('Helvetica', 9), bg='#E0E0E0')
        labelProjectionPlaneYMIN.grid(row=14, column=0, pady=10)

        coorProjectionPlaneYMIN = Entry(scrollableFrame, width= 8)
        coorProjectionPlaneYMIN.grid(row=14, column=1, pady=10)
        coorProjectionPlaneYMIN.insert(0,-10)
        worldList.append(coorProjectionPlaneYMIN)
        
        labelProjectionPlaneYMAX = Label(scrollableFrame, text="YMax", font=('Helvetica', 9), bg='#E0E0E0')
        labelProjectionPlaneYMAX.grid(row=14, column=2, pady=10)

        coorProjectionPlaneYMAX = Entry(scrollableFrame, width= 8)
        coorProjectionPlaneYMAX.grid(row=14, column=3, pady=10)
        coorProjectionPlaneYMAX.insert(0,10)
        worldList.append(coorProjectionPlaneYMAX)
    
        labelObject = Label(scrollableFrame, text="Dados do objeto:", justify=LEFT, anchor="w", font=('Helvetica', 10, 'bold'), bg='#E0E0E0', fg='#990303')
        labelObject.grid(row=15, column=0, padx=20, pady=10, columnspan=4, sticky=W)

        labelBaseRadius = Label(scrollableFrame, text="Raio da base", font=('Helvetica', 9), bg='#E0E0E0')
        labelBaseRadius.grid(row=16, column=0, padx=20, pady=10)

        BaseRadius = Entry(scrollableFrame, width= 8)
        BaseRadius.grid(row=16, column=1, pady=10)
        BaseRadius.insert(0,5)
        objectDataList.append(BaseRadius)
        
        labelTopRadius = Label(scrollableFrame, text="Raio do topo", font=('Helvetica', 9), bg='#E0E0E0')
        labelTopRadius.grid(row=16, column=2, pady=10)

        TopRadius = Entry(scrollableFrame, width= 8)
        TopRadius.grid(row=16, column=3, pady=10)
        TopRadius.insert(0,6)
        objectDataList.append(TopRadius)
        
        labelNumSides = Label(scrollableFrame, text="Nº de lados", font=('Helvetica', 9), bg='#E0E0E0')
        labelNumSides.grid(row=17, column=0, padx=20, pady=10)

        NumSides = Entry(scrollableFrame, width= 8)
        NumSides.grid(row=17, column=1, pady=10)
        NumSides.insert(0,10)
        objectDataList.append(NumSides)

        labelObjHeight = Label(scrollableFrame, text="Altura", font=('Helvetica', 9), bg='#E0E0E0')
        labelObjHeight.grid(row=17, column=2, pady=10)

        ObjHeight = Entry(scrollableFrame, width= 8)
        ObjHeight.grid(row=17, column=3, pady=10)
        ObjHeight.insert(0,5)
        objectDataList.append(ObjHeight)
        
        labelObjectCenter = Label(scrollableFrame, text="Centro geométrico:", justify=LEFT, anchor="w", font=('Helvetica', 10, 'bold'), bg='#E0E0E0')
        labelObjectCenter.grid(row=18, column=0, padx=20, pady=10, columnspan=4, sticky=W)

        objectCenterX = Label(scrollableFrame, text="X", font=('Helvetica', 9), bg='#E0E0E0')
        objectCenterX.grid(row=19, column=0, pady=10)

        coorObjectCenterX = Entry(scrollableFrame, width=8)
        coorObjectCenterX.grid(row=19, column=1, pady=10)
        coorObjectCenterX.insert(0,10)
        objectDataList.append(coorObjectCenterX)

        objectCenterY = Label(scrollableFrame, text="Y", font=('Helvetica', 9), bg='#E0E0E0')
        objectCenterY.grid(row=20, column=0, pady=10)

        coorObjectCenterY = Entry(scrollableFrame, width=8)
        coorObjectCenterY.grid(row=20, column=1, pady=10)
        coorObjectCenterY.insert(0,0)
        objectDataList.append(coorObjectCenterY)

        objectCenterZ = Label(scrollableFrame, text="Z", font=('Helvetica', 9), bg='#E0E0E0')
        objectCenterZ.grid(row=21, column=0, pady=10)

        coorObjectCenterZ = Entry(scrollableFrame, width=8)
        coorObjectCenterZ.grid(row=21, column=1, pady=10)
        coorObjectCenterZ.insert(0,0)
        objectDataList.append(coorObjectCenterZ)

        
        labelSomb = Label(scrollableFrame, text="Sombreamento:", justify=LEFT, anchor="w", font=('Helvetica', 10, 'bold'), bg='#E0E0E0', fg='#990303')
        labelSomb.grid(row=22, column=0, padx=20, pady=10, columnspan=4, sticky=W)

        labelRGBKa = Label(scrollableFrame, text="Ka", justify=LEFT, anchor="w", font=('Helvetica', 9, 'bold'), bg='#E0E0E0')
        labelRGBKa.grid(row=23, column=0,padx=20, pady=10, sticky=W)

        RKa = Label(scrollableFrame, text="R", font=('Helvetica', 9), bg='#E0E0E0')
        RKa.grid(row=24, column=0, pady=10)

        entryRKa = Entry(scrollableFrame, width=8)
        entryRKa.grid(row=24, column=1, pady=10)
        entryRKa.insert(0,0.4)
        objectDataList.append(entryRKa)

        GKa = Label(scrollableFrame, text="G", font=('Helvetica', 9), bg='#E0E0E0')
        GKa.grid(row=25, column=0, pady=10)

        entryGKa = Entry(scrollableFrame, width=8)
        entryGKa.grid(row=25, column=1, pady=10)
        entryGKa.insert(0, 0.5)
        objectDataList.append(entryGKa)

        BKa = Label(scrollableFrame, text="B", font=('Helvetica', 9), bg='#E0E0E0')
        BKa.grid(row=26, column=0, pady=10)

        entryBKa = Entry(scrollableFrame, width=8)
        entryBKa.grid(row=26, column=1, pady=10)
        entryBKa.insert(0, 0.6)
        objectDataList.append(entryBKa)

        labelRGBKd = Label(scrollableFrame, text="Kd", justify=LEFT, anchor="w", font=('Helvetica', 9, 'bold'), bg='#E0E0E0')
        labelRGBKd.grid(row=23, column=2, pady=10, sticky=W)
        
        RKd = Label(scrollableFrame, text="R", font=('Helvetica', 9), bg='#E0E0E0')
        RKd.grid(row=24, column=2, pady=10)

        EntryRKd = Entry(scrollableFrame, width=8)
        EntryRKd.grid(row=24, column=3, pady=10)
        EntryRKd.insert(0, 0.7)
        objectDataList.append(EntryRKd)

        GKd = Label(scrollableFrame, text="G", font=('Helvetica', 9), bg='#E0E0E0')
        GKd.grid(row=25, column=2, pady=10)

        EntryGKd = Entry(scrollableFrame, width=8)
        EntryGKd.grid(row=25, column=3, pady=10)
        EntryGKd.insert(0,0.8)
        objectDataList.append(EntryGKd)

        BKd = Label(scrollableFrame, text="B", font=('Helvetica', 9), bg='#E0E0E0')
        BKd.grid(row=26, column=2, pady=10)

        EntryBKd = Entry(scrollableFrame, width=8)
        EntryBKd.grid(row=26, column=3, pady=10)
        EntryBKd.insert(0,0.9)
        objectDataList.append(EntryBKd)
        
        labelRGBKs = Label(scrollableFrame, text="Ks", justify=LEFT, anchor="w", font=('Helvetica', 9, 'bold'), bg='#E0E0E0')
        labelRGBKs.grid(row=27, column=0, padx=20, pady=10, sticky=W)

        RKs = Label(scrollableFrame, text="R", font=('Helvetica', 9), bg='#E0E0E0')
        RKs.grid(row=28, column=0, pady=10)

        EntryRKs = Entry(scrollableFrame, width=8)
        EntryRKs.grid(row=28, column=1, pady=10)
        EntryRKs.insert(0, 0.5)
        objectDataList.append(EntryRKs)

        GKs = Label(scrollableFrame, text="G", font=('Helvetica', 9), bg='#E0E0E0')
        GKs.grid(row=29, column=0, pady=10)
        
        EntryGKs = Entry(scrollableFrame, width=8)
        EntryGKs.grid(row=29, column=1, pady=10)
        EntryGKs.insert(0, 0.3)
        objectDataList.append(EntryGKs)

        BKs = Label(scrollableFrame, text="B", font=('Helvetica', 9), bg='#E0E0E0')
        BKs.grid(row=30, column=0, pady=10)
        
        EntryBKs = Entry(scrollableFrame, width=8)
        EntryBKs.grid(row=30, column=1, pady=10)
        EntryBKs.insert(0, 0.2)
        objectDataList.append(EntryBKs)
        
        labelN = Label(scrollableFrame, text="n", font=('Helvetica', 9), bg='#E0E0E0')
        labelN.grid(row=28, column=2, pady=10)

        EntryN = Entry(scrollableFrame, width=8)
        EntryN.grid(row=28, column=3, pady=10)
        EntryN.insert(0,2.15)
        objectDataList.append(EntryN)

        labelRGBIla = Label(scrollableFrame, text="Luz ambiente", justify=LEFT, anchor="w", font=('Helvetica', 9, 'bold'), bg='#E0E0E0')
        labelRGBIla.grid(row=31, column=0, padx=20, pady=10, columnspan=4, sticky=W)

        IlaR = Label(scrollableFrame, text="R", font=('Helvetica', 9), bg='#E0E0E0')
        IlaR.grid(row=32, column=0, pady=10)

        EntryIlaR = Entry(scrollableFrame, width=8)
        EntryIlaR.grid(row=32, column=1, pady=10)
        EntryIlaR.insert(0,120)
        objectDataList.append(EntryIlaR)

        IlaG = Label(scrollableFrame, text="G", font=('Helvetica', 9), bg='#E0E0E0')
        IlaG.grid(row=33, column=0, pady=10)
        
        EntryIlaG = Entry(scrollableFrame, width=8)
        EntryIlaG.grid(row=33, column=1, pady=10)
        EntryIlaG.insert(0,120)
        objectDataList.append(EntryIlaG)

        IlaB = Label(scrollableFrame, text="B", font=('Helvetica', 9), bg='#E0E0E0')
        IlaB.grid(row=34, column=0, pady=10)
        
        EntryIlaB = Entry(scrollableFrame, width=8)
        EntryIlaB.grid(row=34, column=1, pady=10)
        EntryIlaB.insert(0,120)
        objectDataList.append(EntryIlaB)
        
        labelRGBfla = Label(scrollableFrame, text="Fonte luminosa", justify=LEFT, anchor="w", font=('Helvetica', 9, 'bold'), bg='#E0E0E0')
        labelRGBfla.grid(row=31, column=2, padx=20, pady=10, columnspan=4, sticky=W)

        IflR = Label(scrollableFrame, text="R", font=('Helvetica', 9), bg='#E0E0E0')
        IflR.grid(row=32, column=2, pady=10)

        EntryIflR = Entry(scrollableFrame, width=8)
        EntryIflR.grid(row=32, column=3, pady=10)
        EntryIflR.insert(0,150)
        objectDataList.append(EntryIflR)

        IflG = Label(scrollableFrame, text="G", font=('Helvetica', 9), bg='#E0E0E0')
        IflG.grid(row=33, column=2, pady=10)
        
        EntryIflG = Entry(scrollableFrame, width=8)
        EntryIflG.grid(row=33, column=3, pady=10)
        EntryIflG.insert(0,150)
        objectDataList.append(EntryIflG)

        IflB = Label(scrollableFrame, text="B", font=('Helvetica', 9), bg='#E0E0E0')
        IflB.grid(row=34, column=2, pady=10)
        
        EntryIflB = Entry(scrollableFrame, width=8)
        EntryIflB.grid(row=34, column=3, pady=10)
        EntryIflB.insert(0,150)
        objectDataList.append(EntryIflB)

        labelCoorFontLum = Label(scrollableFrame, text="Coord. fonte luminosa:", justify=LEFT, anchor="w", font=('Helvetica', 10, 'bold'), bg='#E0E0E0')
        labelCoorFontLum.grid(row=35, column=0, padx=20, pady=10, columnspan=4, sticky=W)

        labelCoorFontLumX = Label(scrollableFrame, text="X", font=('Helvetica', 9), bg='#E0E0E0')
        labelCoorFontLumX.grid(row=36, column=0, pady=10)

        coorFontLumX = Entry(scrollableFrame, width=8)
        coorFontLumX.grid(row=36, column=1, pady=10)
        coorFontLumX.insert(0, 70)
        objectDataList.append(coorFontLumX)

        labelCoorFontLumY = Label(scrollableFrame, text="Y", font=('Helvetica', 9), bg='#E0E0E0')
        labelCoorFontLumY.grid(row=37, column=0, pady=10)

        coorFontLumY = Entry(scrollableFrame, width=8)
        coorFontLumY.grid(row=37, column=1, pady=10)
        coorFontLumY.insert(0, 20)
        objectDataList.append(coorFontLumY)

        labelCoorFontLumZ = Label(scrollableFrame, text="Z", font=('Helvetica', 9), bg='#E0E0E0')
        labelCoorFontLumZ.grid(row=38, column=0, pady=10)

        coorFontLumZ = Entry(scrollableFrame, width=8)
        coorFontLumZ.grid(row=38, column=1, pady=10)
        coorFontLumZ.insert(0, 35)
        objectDataList.append(coorFontLumZ)

        novoMundo = Button(scrollableFrame, text="Novo mundo", font=('Helvetica', 10), bg='#edb1ba', width=9, command = newWorld)
        novoMundo.grid(row=39, column=0, pady=10)

        novoObjeto = Button(scrollableFrame, text="Novo objeto", font=('Helvetica', 10), bg='#edb1ba', width=9, command = newObject)
        novoObjeto.grid(row=39, column=1, pady=10)

        atualizarObjeto = Button(scrollableFrame, text="Atualizar objeto", font=('Helvetica', 10), bg='#edb1ba', width=9, command = updateObject)
        atualizarObjeto.grid(row=39, column=2, pady=10)

        limparCena = Button(scrollableFrame, text="Limpar cena", font=('Helvetica', 10), bg='#edb1ba', width=9, command= clearScreen)
        limparCena.grid(row=39, column=3, pady=10) 

        sideBar.pack(side=RIGHT, fill=Y)
        canvasBar.pack(side=LEFT, fill=BOTH, expand=True)
        scrollBar.pack(side=RIGHT, fill=Y)

    def initPC(self):
        global canvasPC
        planoCartesiano = Frame(self.master, highlightbackground='gray', highlightthickness=1)
        canvasPC = Canvas(planoCartesiano)
        planoCartesiano.place(x=20, y= 530, width=170, height=170)
        planoCartesiano.rowconfigure(0, weight = 1)
        planoCartesiano.columnconfigure(0, weight = 1)
        canvasPC.grid(sticky="nsew")

    def initScreen(self):
        global screen, canvas 
        screen = Frame(self.master, highlightbackground='gray', highlightthickness=1)

        screen.rowconfigure(0, weight = 5)
        screen.columnconfigure(0, weight = 5)

        canvas = Canvas(screen)

        screen.place(x=10, y= 70, width=860, height=640)

        canvas.grid(sticky="nsew")



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
            listViewUp.append(float(worldList[4].get()))
            listViewUp.append(float(worldList[5].get()))
            listViewUp.append(float(worldList[6].get()))
            
            #VRP
            global listVRP
            listVRP = []
            listVRP.append(float(worldList[7].get()))
            listVRP.append(float(worldList[8].get()))
            listVRP.append(float(worldList[9].get()))

            #Ponto Focal
            global listP
            listP = []
            listP.append(float(worldList[10].get()))
            listP.append(float(worldList[11].get()))
            listP.append(float(worldList[12].get()))

            # Distância ao plano de projeção, plano near e ao plano far
            global listDist
            listDist = []
            listDist.append(float(worldList[13].get()))
            listDist.append(float(worldList[14].get()))
            listDist.append(float(worldList[15].get()))

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
                redefineObject()
                deleteLabel()
                EixosSinalizadores()
                
    else:
        popupShowErrorEmptyInput()

def newObject():
    if len(objectDataList[0].get()) != 0 and len(objectDataList[1].get()) != 0 and len(objectDataList[2].get()) != 0 and len(objectDataList[3].get()) != 0 \
       and len(objectDataList[4].get()) != 0 and len(objectDataList[5].get()) != 0 and len(objectDataList[6].get()) != 0 and len(objectDataList[7].get()) != 0 \
       and len(objectDataList[8].get()) != 0 and len(objectDataList[9].get()) != 0 and len(objectDataList[10].get()) != 0 and len(objectDataList[11].get()) != 0 \
       and len(objectDataList[12].get()) != 0 and len(objectDataList[13].get()) != 0 and len(objectDataList[14].get()) != 0 and len(objectDataList[15].get()) != 0 \
       and len(objectDataList[16].get()) != 0 and len(objectDataList[17].get()) != 0 and len(objectDataList[18].get()) != 0 and len(objectDataList[19].get()) != 0 \
       and len(objectDataList[20].get()) != 0 and len(objectDataList[21].get()) != 0 and len(objectDataList[22].get()) != 0 and len(objectDataList[23].get()) != 0 \
       and len(objectDataList[24].get()) != 0 and len(objectDataList[25].get()) != 0:
        try:

            #Número de lados
            NL = int(objectDataList[2].get())

            if(NL > 3 and NL < 20):

                #Raio da base
                BR = float(objectDataList[0].get())

                #Raio do topo
                TR = float(objectDataList[1].get())

                #Altura do objeto
                OH = float(objectDataList[3].get())

                #Centro Geométrico
                coorOCX = float(objectDataList[4].get())
                coorOCY = float(objectDataList[5].get())
                coorOCZ = float(objectDataList[5].get())

                #Ka
                global listK
                listK = []
                listK.append(float(objectDataList[7].get()))
                listK.append(float(objectDataList[8].get()))
                listK.append(float(objectDataList[9].get()))

                #Kd
                listK.append(float(objectDataList[10].get()))
                listK.append(float(objectDataList[11].get()))
                listK.append(float(objectDataList[12].get()))

                #Ks
                listK.append(float(objectDataList[13].get()))
                listK.append(float(objectDataList[14].get()))
                listK.append(float(objectDataList[15].get()))
                
                #n
                listK.append(float(objectDataList[16].get()))

                #luz ambiente
                global listLuz
                listLuz = []
                listLuz.append(int(objectDataList[17].get()))
                listLuz.append(int(objectDataList[18].get()))
                listLuz.append(int(objectDataList[19].get()))

                #fonte luminosa
                listLuz.append(int(objectDataList[20].get()))
                listLuz.append(int(objectDataList[21].get()))
                listLuz.append(int(objectDataList[22].get()))

                #coord. fonte luminosa
                listLuz.append(int(objectDataList[23].get()))
                listLuz.append(int(objectDataList[24].get()))
                listLuz.append(int(objectDataList[25].get()))

                canvas.focus_set()
                createObject(BR, TR, NL, OH, [coorOCX, coorOCY, coorOCZ])

            else:
                popupShowNumSidesError()

        except ValueError:
            popupShowErrorInput() 
    else:
        popupShowErrorEmptyInput()

def deleteLabel():
    global labelXAxis, labelYAxis, labelZAxis
    if(labelXAxis != None and labelYAxis != None and labelZAxis != None):
        labelXAxis.place_forget()
        labelYAxis.place_forget()
        labelZAxis.place_forget()

def EixosSinalizadores():
    global listViewUp, listDist, listVRP, listP
    global labelXAxis, labelYAxis, labelZAxis

    if ((len(listVRP) != 0) and (len(listP) != 0) and (len(listDist) != 0) and (len(listViewUp) != 0)):

        canvasPC.delete("all")
        tamanhoLinha = 60
        matrizPCsrt = None

        matrizPontos = np.array([[0, tamanhoLinha, 0, 0],[0, 0, tamanhoLinha, 0], [0, 0, 0, tamanhoLinha], [1, 1, 1, 1]])

        print(listDist)
        print(listP)
        print(listViewUp)
        print(listVRP)

        PCsrc = sru2src(np.array(listVRP),np.array(listP) ,np.array(listViewUp))
        
        matrizPCsrt = np.dot(PCsrc, matrizPontos)

        if listProj[0]:
            matrizPerpec = perspProj(listDist[0])
            matrizPCsrt = np.dot(matrizPerpec, matrizPCsrt)

        matrizPCsrt[1:]*=-1

        x = (matrizPCsrt[0][0] - 80)
        y = (matrizPCsrt[1][0] - 77)

        EndLineX = [matrizPCsrt[0][1] - x, matrizPCsrt[1][1] - y]
        EndLineY = [matrizPCsrt[0][2] - x, matrizPCsrt[1][2] - y]
        EndLineZ = [matrizPCsrt[0][3] - x, matrizPCsrt[1][3] - y]

        
        labelXAxis = Label(canvasPC, text="X", font=('Helvetica', 9), fg="red")
        labelXAxis.place(x= EndLineX[0], y= EndLineX[1]-10, anchor=E)
        canvasPC.create_line((matrizPCsrt[0][0] - x, matrizPCsrt[1][0] - y, EndLineX[0], EndLineX[1]), fill="red", width=2)
        
        labelYAxis = Label(canvasPC, text="Y", font=('Helvetica', 9), fg="green")
        labelYAxis.place(x=EndLineY[0], y= EndLineY[1]-10, anchor=E)
        canvasPC.create_line((matrizPCsrt[0][0] - x, matrizPCsrt[1][0] - y, EndLineY[0], EndLineY[1]), fill="green", width=2)

        labelZAxis = Label(canvasPC, text="Z", font=('Helvetica', 9), fg="blue")
        labelZAxis.place(x=EndLineZ[0], y= EndLineZ[1]+10, anchor=E)
        canvasPC.create_line((matrizPCsrt[0][0] - x, matrizPCsrt[1][0] - y, EndLineZ[0], EndLineZ[1]), fill="blue", width=2)

        
def placeScreen ():
    screen.place(x = (listViewPort[0] + 10), y = (listViewPort[2] + 70), width= listViewPort[1], height= listViewPort[3])

def clearScreen():
    global meshAtual, polygon, kAtual
    canvas.delete("all")
    meshAtual = None
    polygon = None
    kAtual = None
    listMesh.clear()
    listObject.clear()
    listIlum.clear()

def redefineObject():
    global polygon, meshAtual
    if((canvas.find_all) != 0):
        canvas.delete("all")
        listObject.clear()
        polygon = None
        meshAtual = None
        for i in range(0, len(listMesh)):
            obj = []
            listKs = listIlum[i]
            
            meshSRT = convertMesh2SRT(listMesh[i], np.array(listVRP), listDist[0], listWW[0], listWW[1], listWW[2], listWW[3], listViewPort[0], listViewPort[1], listViewPort[2], listViewPort[3], np.array(listP), np.array(listViewUp), listProj[0], np.array([listLuz[0], listLuz[1], listLuz[2]]), np.array([listLuz[3], listLuz[4], listLuz[5]]), np.array([listLuz[6], listLuz[7], listLuz[8]]), [listKs[0], listKs[1], listKs[2]], [listKs[3], listKs[4], listKs[5]], [listKs[6], listKs[7], listKs[8]], listKs[9])
            if(isMeshVisible(meshSRT, listDist[1], listDist[2])):
                for fh in meshSRT.faces():
                    face = []
                    for vh in meshSRT.fv(fh):
                        point = meshSRT.point(vh)
                        face.append([point[0], point[1]])
                    obj.append(canvas.create_polygon(face, fill=rgba2hex(meshSRT.color(fh)), tags="clickable", outline="black"))

                listObject.append(obj)


def createObject(raioBase, raioTopo, nLados, altura, GC):
    global listMesh, listObject, listIlum
    obj = []

    mesh = salvaPoligono(raioBase, raioTopo, nLados, altura, GC)
    listMesh.append(mesh)

    #Converte para SRT

    meshSRT = convertMesh2SRT(mesh, np.array(listVRP), listDist[0], listWW[0], listWW[1], listWW[2], listWW[3], listViewPort[0], listViewPort[1], listViewPort[2], listViewPort[3], np.array(listP), np.array(listViewUp), listProj[0], np.array([listLuz[0], listLuz[1], listLuz[2]]), np.array([listLuz[3], listLuz[4], listLuz[5]]), np.array([listLuz[6], listLuz[7], listLuz[8]]), [listK[0], listK[1], listK[2]], [listK[3], listK[4], listK[5]], [listK[6], listK[7], listK[8]], listK[9])
    if isMeshVisible(meshSRT, listDist[1], listDist[2]):
        listIlum.append(listK)
        for fh in meshSRT.faces():
            face = []
            for vh in meshSRT.fv(fh):
                point = meshSRT.point(vh)
                face.append([point[0], point[1]])
            obj.append(canvas.create_polygon(face, fill=rgba2hex(meshSRT.color(fh)), tags="clickable", outline="black"))

        listObject.append(obj)

def identifyObject(event):
    canvas.focus_set()
    global meshAtual, polygon, listMesh, kAtual
    meshAtual = None
    polygon = None
    kAtual = None
    if not event.widget.find_withtag("current"):
        print("Nenhum objeto no Canvas!")
        for i in range(0, len(listObject)):
            for j in range(0, len(listObject[i])):
                canvas.itemconfig(listObject[i][j], outline="black")
        polygon = None
    else:
        id = event.widget.find_withtag("current")[0]
        #pintar poligono clicado
        for i in range(0, len(listObject)):
            for j in range(0, len(listObject[i])):
                if listObject[i][j] == id:
                    polygon = listObject[i]
                    aux = i
                    for k in range(0, len(polygon)):
                        canvas.itemconfig(polygon[k], outline="red")
                        
        #pintar poligonos extras
        for i in range(0, len(listObject)):
            if i != aux:
                for j in range(0, len(listObject[i])):
                    canvas.itemconfig(listObject[i][j], outline="black")

        meshAtual = listMesh[aux]
        kAtual = listIlum[aux]

def interfaceTeclas(event):
    if meshAtual is not None:
        translacao(event)
        escala(event)
        rotacao(event)

def opCreate(object):
    #deleta object
    global polygon, kAtual
    for i in range(0, len(polygon)):
        canvas.delete(polygon[i])
    polygon.clear()

    #Lista de faces que vai ser ordenada
    faces = []

    #Converte para SRT
    meshSRT = convertMesh2SRT(object, np.array(listVRP), listDist[0], listWW[0], listWW[1], listWW[2], listWW[3], listViewPort[0], listViewPort[1], listViewPort[2], listViewPort[3], np.array(listP), np.array(listViewUp), listProj[0], np.array([listLuz[0], listLuz[1], listLuz[2]]), np.array([listLuz[3], listLuz[4], listLuz[5]]), np.array([listLuz[6], listLuz[7], listLuz[8]]), [kAtual[0], kAtual[1], kAtual[2]], [kAtual[3], kAtual[4], kAtual[5]], [kAtual[6], kAtual[7], kAtual[8]], kAtual[9])
    if(isMeshVisible(meshSRT, listDist[1], listDist[2])):
        for fh in meshSRT.faces():
            face = []
            faceProfundidade = 0
            for vh in meshSRT.fv(fh):
                point = meshSRT.point(vh)
                faceProfundidade += point[2]
                face.append([point[0], point[1]])
            newFace = cutBorder(face, listViewPort[0], listViewPort[1], listViewPort[2], listViewPort[3])
            if newFace != []:
                #polygon.append(canvas.create_polygon(newFace, fill=rgba2hex(meshSRT.color(fh)), tags="clickable", outline="red"))
                #Em vez de já desenhar na tela, adicionar a newFace, profundidade e a cor na faces
                #IMPORTANTE: Aqui a gente tá fazendo o algoritmo do pintor só pro objeto que a gente ta passando no opCreate, mas isso deve ser feito para TODOS os objetos todas as vezes que fazemos qualquer operação
                faces.append([newFace,faceProfundidade/3,rgba2hex(meshSRT.color(fh))])

    #Ordenamos todas as faces pelo item [1] que é a profundidade
    #Reforçand: aqui na faces a gente tem todas as faces do poligono mas temos que fazer com que faces tenha as faces de TODOS os poligonos. Não implementei essa parte ṕois nem sei onde eles estao sendo armazenados kkkk. Não esqueçam que estou livre se precisarem de ajuda :)
    faces = sorted(faces , key=lambda k: k[1])
    #Agora desenhamos todas em ordem de profundidade
    for currFace in faces:
        polygon.append(canvas.create_polygon(currFace[0], fill=currFace[2], tags="clickable", outline="red"))

def translacao(event):
    x, y, z = 0, 0, 0
    if event.char == "q": 
        x, y, z = -0.1, 0, 0
        objectTrans = translate(meshAtual, x, y, z)
        opCreate(objectTrans)
    elif event.char == "a": 
        x, y, z = 0.1, 0, 0
        objectTrans = translate(meshAtual, x, y, z)
        opCreate(objectTrans)
    elif event.char == "w": 
        x, y, z = 0, 0, 0.1
        objectTrans = translate(meshAtual, x, y, z)
        opCreate(objectTrans)
    elif event.char == "s":
        x, y, z = 0, 0, -0.1
        objectTrans = translate(meshAtual, x, y, z)
        opCreate(objectTrans)
    elif event.char == "e":
        x, y, z = 0, 0.1, 0
        objectTrans = translate(meshAtual, x, y, z)
        opCreate(objectTrans)
    elif event.char == "d": 
        x, y, z = 0, -0.1, 0
        objectTrans = translate(meshAtual, x, y, z)
        opCreate(objectTrans)

def escala(event):
    x, y, z = 0, 0, 0
    if event.char == "r": # diminui o objeto no eixo x
        x, y, z = 0.95, 1, 1
        objectEsc = escalate(meshAtual, x, y, z)
        opCreate(objectEsc)
    elif event.char == "f": # aumenta o objeto no eixo x
        x, y, z = 1.05, 1, 1
        objectEsc = escalate(meshAtual, x, y, z)
        opCreate(objectEsc)
    elif event.char == "t": # diminui o objeto no eixo z
        x, y, z = 1, 1, 0.95
        objectEsc = escalate(meshAtual, x, y, z)
        opCreate(objectEsc)
    elif event.char == "g": # aumenta o objeto no eixo z
        x, y, z = 1, 1, 1.05
        objectEsc = escalate(meshAtual, x, y, z)
        opCreate(objectEsc)
    elif event.char == "y": # diminui o objeto no eixo y
        x, y, z = 1, 0.95, 1
        objectEsc = escalate(meshAtual, x, y, z)
        opCreate(objectEsc)
    elif event.char == "h": # aumenta o objeto no eixo y
        x, y, z = 1, 1.05, 1
        objectEsc = escalate(meshAtual, x, y, z)
        opCreate(objectEsc)

def rotacao(event):
    angulo = 0
    if event.char == "u": # rotaciona para a esquerda ao redor do eixo xp
        angulo = 0.1
        objectRot = rotX(meshAtual, angulo)
        opCreate(objectRot)
    elif event.char == "j": # rotaciona para a direita ao redor do eixo x
        angulo = -0.1
        objectRot = rotX(meshAtual, angulo)
        opCreate(objectRot)
    elif event.char == "i": # rotaciona para a esquerda ao redor do eixo z
        angulo = 0.1
        objectRot = rotZ(meshAtual, angulo)
        opCreate(objectRot)
    elif event.char == "k": # rotaciona para a direita ao redor do eixo z
        angulo = -0.1
        objectRot = rotZ(meshAtual, angulo)
        opCreate(objectRot)
    elif event.char == "o": # rotaciona para a esquerda ao redor do eixo y
        angulo = 0.1
        objectRot = rotY(meshAtual, angulo)
        opCreate(objectRot)
    elif event.char == "l": # rotaciona para a direita ao redor do eixo y
        angulo = -0.1
        objectRot = rotY(meshAtual, angulo)
        opCreate(objectRot)

def clicked(value):
    global listProj, polygon, meshAtual
    listProj[0] = value
    if(canvas.find_all != 0):
        canvas.delete("all")
        listObject.clear()
        polygon = None
        meshAtual = None

        for i in range(0, len(listMesh)):
            obj = []
            listaKs = listIlum[i]
            meshSRT = convertMesh2SRT(listMesh[i], np.array(listVRP), listDist[0], listWW[0], listWW[1], listWW[2], listWW[3], listViewPort[0], listViewPort[1], listViewPort[2], listViewPort[3], np.array(listP), np.array(listViewUp), listProj[0], np.array([listLuz[0], listLuz[1], listLuz[2]]), np.array([listLuz[3], listLuz[4], listLuz[5]]), np.array([listLuz[6], listLuz[7], listLuz[8]]), [listaKs[0], listaKs[1], listaKs[2]], [listaKs[3], listaKs[4], listaKs[5]], [listaKs[6], listaKs[7], listaKs[8]], listaKs[9])
            if(isMeshVisible(meshSRT, listDist[1], listDist[2])):
                for fh in meshSRT.faces():
                    face = []
                    for vh in meshSRT.fv(fh):
                        point = meshSRT.point(vh)
                        face.append([point[0], point[1]])
                    obj.append(canvas.create_polygon(face, fill=rgba2hex(meshSRT.color(fh)), tags="clickable", outline="black"))

                listObject.append(obj)

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
 
    global polygon, meshAtual, listObject, listMesh, listProj, listIlum, listVRP, listP, listViewUp, listDist, labelXAxis, labelYAxis, labelZAxis
    
    meshAtual = None
    polygon = None
    labelXAxis = None
    labelYAxis = None
    labelZAxis = None
    listMesh = []
    listObject = []
    listProj = []
    listIlum = []
    listViewUp = []
    listP = []
    listViewUp = []
    listDist = []

    CanvasMenu()
    newWorld()
    canvas.bind("<Button-1>", identifyObject)
    canvas.bind_all("<Key>", interfaceTeclas)
   
    root.mainloop()

if __name__ == '__main__':
    run_program()
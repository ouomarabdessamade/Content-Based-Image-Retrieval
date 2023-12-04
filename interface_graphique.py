from ClassDescriptor.colordescriptor import ColorDescriptor
from ClassDescriptor.colordescripMoyenne import ColorDesMoyenne   
from ClassDescriptor.colordescRGB import RGBHistogram

from ClassDescriptor.TexturedesCriptor import texturedescriptor

from ClassDescriptor.zernikeDescriptor import ZernikeMoments
from ClassDescriptor.ShapeDetector22 import ShapeDetector

from ClassDescriptor.searcher import Searcher
from ClassDescriptor.SearchIbride import SearcherIbride  
from tkinter import*
from tkinter import ttk
import tkinter.messagebox as MessageBox
from PIL import Image, ImageTk
from tkinter import filedialog
import numpy as np 
import os
import cv2


im = ''
vagglo = []
listeglob = []
listeporsentages = []
file_path = ''
phot =''
class InterfaceGraphique :
    def __init__(self,feneter):
        self.imag_path = ''
        self.pathe ='queries/101801.jpg'
        self.feneter=feneter 
        self.feneter.title("image search engine ")
        self.feneter.geometry("1400x700+100+50")
        self.feneter.config(bg="#D1D7F0")   
        #-----------bloquer le redimentionnement de la fenetre----------------# 
        #self.feneter.resizable(width=False, height=False)
        #--------------logo de l'application----------------------------------#
        self.feneter.iconbitmap("imagInterface/logo.ico")

        #================ bg Image ===========================================#
        self.bg=ImageTk.PhotoImage(file="imagInterface/bg_image.png")
        bg=Label(self.feneter,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)
        #===========img left==================================================#
        #self.left=ImageTk.PhotoImage(file="imagInterface/bgf.png")
        #left=Label(self.feneter,image=self.left).place(x=120,y=100,width=390,height=500)
        #==============frame ================================================#
        frame = Frame(self.feneter ,relief=RAISED, bg="white",  highlightbackground="lightgray",highlightthickness=2)
        frame.place(x=20,y=50,width=1370,height=600)
        #========================Canvas=======================================#
        self.canvas = Canvas(self.feneter, bg='lightgray', width=650,height=597)
        self.canvas.place(x=735,y=50)
        #==================bouten file========================================#
        textpath = Label(frame, text=" Image Search Engine ",font=("Comic Sans MS", 20), bg="white").place(x=10 ,y=5)

        self.folder=ImageTk.PhotoImage(file="imagInterface/RRR.png")
        foldere=Label(frame,image=self.folder, bg="white").place(x=5,y=50,width=60,height=60)
        self.variable_path = StringVar()
        
        self.txt_val_path = Entry(frame , font=("Ariel", 18) , relief=RIDGE , highlightbackground="gray",highlightthickness=2, bg="#E0E2E7", fg="#1D5590", textvariable=self.variable_path)
        self.txt_val_path.place(x=70,y=60 ,width=637, height=40)
        self.variable_path.set("Paste or enter image Path")
        
        self.openImage=ImageTk.PhotoImage(file="imagInterface/77.png")
        openImage=Label(frame,image=self.openImage, bg="white").place(x=5,y=120,width=60,height=60)
        #self.openImage =ImageTk.PhotoImage(file="imagInterface/77.png")             # image=self.openImage, compound='left' ,
        file_boutton = Button(frame, font=("times new romman", 16,"bold"),text=" Upload ",bd=0,cursor="hand2", activebackground ="#CAE5E4",activeforeground="#0F5A7D", borderwidth = 3, bg="#CFD6DE",fg="#1D5590", command=self.UploadAction).place(x=70 ,y=125,width=300)
        #---------------------frame 2-----------------------------------------#
        self.frame2 = Frame(frame, bg="lightgray",relief=RAISED, highlightbackground="gray",highlightthickness=3)
        self.frame2.place(x=5,y=200,height=390,width=700)
        
        text_search = Label(self.frame2, text=" Type of Search    ",font=("Comic Sans MS", 16, "bold"), bg="lightgray").place(x=42,y=4)
        self.search=ImageTk.PhotoImage(file="imagInterface/logoSearch.png")
        searche=Label(self.frame2,image=self.search, bg="lightgray").place(x=0,y=3,width=50,height=50)
        #===========================================================Bouton de Recherche par couleur ========================================================================================================================================================#
        couleur_boutton = Button(self.frame2,font=("times new romman",15,"bold"),text="Search by Color",bg="#266F7F",fg="#EEF3F4", bd=0, cursor="hand2", activebackground ="#CAE5E4",activeforeground="#0F5A7D",borderwidth = 2, command=self.SearchColor).place(x=20 ,y=60,width=200)
        #---------------------------------------------------------------------#
        self.typediscripcolor = StringVar()
        self.cmb_Color = ttk.Combobox(self.frame2,font=("times new romman",15,"bold"),state='readonly',justify=CENTER, textvariable=self.typediscripcolor)
        self.cmb_Color['values']=(" HSV "," RGB "," Moyenne ")
        self.cmb_Color.place(x=250,y=65,width=160)
        self.cmb_Color.current(2)
        
        #----------------------Radio button ----------------------------------#
        self.radioValColor = DoubleVar()
        self.radioColor0 = ttk.Radiobutton(self.frame2, text= " 0 % ", variable=self.radioValColor, value=0)# background="lightgray", 
        self.radioColor0.place(x=420,y=70)
        self.radioColor1 = ttk.Radiobutton(self.frame2, text= " 25 % ", variable=self.radioValColor, value=0.25)# background="lightgray", 
        self.radioColor1.place(x=480,y=70)
        
        self.radioColor2 = ttk.Radiobutton(self.frame2, text= " 50 % ", variable=self.radioValColor, value=0.50)
        self.radioColor2.place(x=540,y=70)
        self.radioColor2.invoke()
        
        self.radioColor3 = ttk.Radiobutton(self.frame2, text= " 75 % ", variable=self.radioValColor, value=0.75)
        self.radioColor3.place(x=600,y=70)
     
        #============================================================ Bouton de Recherche par form =========================================================================================================================================================#
        form_boutton = Button(self.frame2,font=("times new romman",15,"bold"),text=" Search by Shape",bd=0,cursor="hand2",bg="#DBFC7C",fg="#0B3A6B",activebackground ="#CDD3C8",activeforeground="#0F5A7D",borderwidth = 2, command=self.SearchForm).place(x=20 ,y=140,width=200)
        #---------------------------------------------------------------------
        self.valdeShape = StringVar() 
        self.cmb_form = ttk.Combobox(self.frame2,font=("times new romman",15,"bold"),state='readonly',justify=CENTER, textvariable=self.valdeShape )
        self.cmb_form['values']=("Zernike","HuMoment")
        self.cmb_form.place(x=250,y=145,width=160)
        self.cmb_form.current(0)
        #----------------------Radio button ----------------------------------#
        self.radioValForm = DoubleVar()
        self.radioForm0 = ttk.Radiobutton(self.frame2, text= " 0 % ", variable=self.radioValForm, value=0)# background="lightgray", 
        self.radioForm0.place(x=420,y=150)
        
        self.radioForm1 = ttk.Radiobutton(self.frame2, text= " 25 % ", variable=self.radioValForm, value=0.25)# background="lightgray", 
        self.radioForm1.place(x=480,y=150)
        self.radioForm1.invoke()
        
        self.radioForm2 = ttk.Radiobutton(self.frame2, text= " 50 % ", variable=self.radioValForm, value=0.50)
        self.radioForm2.place(x=540,y=150)
        
        
        self.radioForm3 = ttk.Radiobutton(self.frame2, text= " 75 % ", variable=self.radioValForm, value=0.75)
        self.radioForm3.place(x=600,y=150)
        
        #============================================================ Bouton de Recherche par texture ======================================================================================================================================================#
        textur_boutton= Button(self.frame2,font=("times new romman",15,"bold"),text="Search by Texture ",bd=0,cursor="hand2",bg="#FFCA81",fg="#0B3A6B",activebackground ="#CAE5E4",activeforeground="#0F5A7D",borderwidth = 2, command=self.SerchTexture).place(x=20 ,y=220,width=200)
        #---------------------------------------------------------------------
        self.typediscritexture = StringVar()
        self.cmb_textur = ttk.Combobox(self.frame2,font=("times new romman",15,"bold"),state='readonly',justify=CENTER, textvariable= self.typediscritexture)
        self.cmb_textur['values']=(" LBP "," Haralick ")
        self.cmb_textur.place(x=250,y=225,width=160)
        self.cmb_textur.current(0)
        #----------------------Radio button ----------------------------------#
        self.radioValTextur = DoubleVar()
        self.raddtextur0 = ttk.Radiobutton(self.frame2, text= " 0 % ", variable=self.radioValTextur, value=0)# background="lightgray", 
        self.raddtextur0.place(x=420,y=230)
        
        self.raddtextur1 = ttk.Radiobutton(self.frame2, text= " 25 % ", variable=self.radioValTextur, value=0.25)# background="lightgray", 
        self.raddtextur1.place(x=480,y=230)
        self.raddtextur1.invoke()
        
        self.raddtextur2 = ttk.Radiobutton(self.frame2, text= " 50 % ", variable=self.radioValTextur, value=0.50)
        self.raddtextur2.place(x=540,y=230)
        
        self.raddtextur3 = ttk.Radiobutton(self.frame2, text= " 75 % ", variable=self.radioValTextur, value=0.75)
        self.raddtextur3.place(x=600,y=230)
       
        #==========================================================Boutton ibred=======================================================================#
        text_serchibrid = Label(self.frame2, text=" Hybrid search :    ",font=("Comic Sans MS", 16, "bold"), bg="lightgray").place(x=20,y=300)
        Ibrid_boutton= Button(self.frame2,font=("times new romman",15,"bold"),text=" Hybrid Search ",bd=0,cursor="hand2",bg="#6F9197",fg="#EEF3F4",activebackground ="#CAE5E4",activeforeground="#0F5A7D",borderwidth = 2, command=self.ibridSerch).place(x=420 ,y=295,width=250)
        
     
        
    def createcanva(self, listpath, lisdistance, listporcentage ):
        self.path1 = listpath[0]
        self.path2 = listpath[1]
        self.path3 = listpath[2]
        self.path4 = listpath[3]
        self.path5 = listpath[4]
        self.path6 = listpath[5]
        self.path7 = listpath[6]
        self.path8 = listpath[7]
        self.path9 = listpath[8]
        self.path10 = listpath[9]
        
        self.dist0 = lisdistance[0]
        self.dist1 = lisdistance[1]
        self.dist2 = lisdistance[2]
        self.dist3 = lisdistance[3]
        self.dist4 = lisdistance[4]
        self.dist5 = lisdistance[5]
        self.dist6 = lisdistance[6]
        self.dist7 = lisdistance[7]
        self.dist8 = lisdistance[8]
        self.dist9 = lisdistance[9]
        
        self.porcetage1 = listporcentage[0]
        self.porcetage2 = listporcentage[1]
        self.porcetage3 = listporcentage[2]
        self.porcetage4 = listporcentage[3]
        self.porcetage5 = listporcentage[4]
        self.porcetage6 = listporcentage[5]
        self.porcetage7 = listporcentage[6]
        self.porcetage8 = listporcentage[7]
        self.porcetage9 = listporcentage[8]
        self.porcetage10 = listporcentage[9]
        
        self.root = Toplevel()
        self.root.wm_title(" Type of Search ")
        self.root.geometry("1525x755+30+20")
       
        #============les canvaces=============================================#
        self.label1 = Label(self.root, text="dist 1:", font=("Comic Sans MS", 12) ).place(x=1,y=5)
        self.vardist1 = DoubleVar()
        self.txt_varDist1 = Entry(self.root, font=("Comic Sans MS",12,"bold"), bg="lightgray",fg="green", textvariable=self.vardist1)
        self.txt_varDist1.place(x=70,y=5,width=233)
        self.vardist1.set(self.dist0)
        #--------------procentage---------------------------------------------#
        self.lbporcen1 = Label(self.root, text="Simularité :", font=("Comic Sans MS", 12) ).place(x=1,y=40)
        self.varporcent1 = StringVar()
        self.txt_varporcebn1 = Entry(self.root, font=("Comic Sans MS",12,"bold"), bg="lightgray",fg="#1C1F39", textvariable=self.varporcent1)
        self.txt_varporcebn1.place(x=100,y=40,width=203)
        self.varporcent1.set(str(self.porcetage1)+ " % ")
        self.canvas1 = Canvas(self.root, bg="lightgray", width=300, height=300)
        img1 = Image.open(self.path1)
        img1 = img1.resize((300,300), Image.ANTIALIAS)
        self.canvas1.image = ImageTk.PhotoImage(img1)
        self.canvas1.create_image(0, 0, image = self.canvas1.image  , anchor='nw')
        self.canvas1.place(x=0, y=70)
        
        # --------------------------------------------------------------------#
        self.label2 = Label(self.root, text="dist 2:", font=("Comic Sans MS", 12) ).place(x=306,y=5)
        self.vardist2 = DoubleVar()
        self.txt_varDist2 = Entry(self.root, font=("Comic Sans MS",12,"bold"), bg="lightgray",fg="green", textvariable=self.vardist2)
        self.txt_varDist2.place(x=375,y=5,width=233)
        self.vardist2.set(self.dist0)
        #--------------procentage---------------------------------------------#
        self.lbporcen2 = Label(self.root, text="Simularité :", font=("Comic Sans MS", 12) ).place(x=306,y=40)
        self.varporcent2 = StringVar()
        self.txt_varporcebn2 = Entry(self.root, font=("Comic Sans MS",12,"bold"), bg="lightgray",fg="#1C1F39", textvariable=self.varporcent2)
        self.txt_varporcebn2.place(x=405,y=40,width=203)
        self.varporcent2.set(str(self.porcetage2)+ " % ")
        self.canvas2 = Canvas(self.root, bg="lightgray", width=300, height=300)
        img2 = Image.open(self.path2)
        img2 = img2.resize((300,300), Image.ANTIALIAS)
        self.canvas2.image = ImageTk.PhotoImage(img2)
        self.canvas2.create_image(0, 0, image = self.canvas2.image  , anchor='nw')
        self.canvas2.place(x=305, y=70)
         
        #---------------------------------------------------------------------#
        self.label3 = Label(self.root, text="dist 3:", font=("Comic Sans MS", 12) ).place(x=609,y=5)
        self.vardist3 = DoubleVar()
        self.txt_varDist3 = Entry(self.root, font=("Comic Sans MS",12,"bold"), bg="lightgray",fg="green", textvariable=self.vardist3)
        self.txt_varDist3.place(x=680,y=5,width=233)
        self.vardist3.set(self.dist1)
        #--------------procentage----------------------------------------------#
        self.lbporcen3 = Label(self.root, text="Simularité :", font=("Comic Sans MS", 12) ).place(x=609,y=40)
        self.varporcent3 = StringVar()
        self.txt_varporcebn3 = Entry(self.root, font=("Comic Sans MS",12,"bold"), bg="lightgray",fg="#1C1F39", textvariable=self.varporcent3)
        self.txt_varporcebn3.place(x=710,y=40,width=203)
        self.varporcent3.set(str(self.porcetage2)+ " % ")
         
        self.canvas3 = Canvas(self.root, bg="lightgray", width=300, height=300)
        img3 = Image.open(self.path3)
        img3 = img3.resize((300,300), Image.ANTIALIAS)
        self.canvas3.image = ImageTk.PhotoImage(img3)
        self.canvas3.create_image(0, 0, image = self.canvas3.image  , anchor='nw')
        self.canvas3.place(x=610, y=70)
        #---------------------------------------------------------------------#
        self.label4 = Label(self.root, text="dist 4:", font=("Comic Sans MS", 12) ).place(x=912,y=5)
        self.vardist4 = DoubleVar()
        self.txt_varDist4 = Entry(self.root, font=("Comic Sans MS",12,"bold"), bg="lightgray",fg="green", textvariable=self.vardist4)
        self.txt_varDist4.place(x=985,y=5,width=233)
        self.vardist4.set(self.dist2)
        #--------------procentage----------------------------------------------#
        self.lbporcen4 = Label(self.root, text="Simularité :", font=("Comic Sans MS", 12) ).place(x=912,y=40)
        self.varporcent4 = StringVar()
        self.txt_varporcebn4 = Entry(self.root, font=("Comic Sans MS",12,"bold"), bg="lightgray",fg="#1C1F39", textvariable=self.varporcent4)
        self.txt_varporcebn4.place(x=1015,y=40,width=203)
        self.varporcent4.set(str(self.porcetage3)+ " % ")
         
        
        self.canvas4 = Canvas(self.root, bg="lightgray", width=300, height=300)
        img4 = Image.open(self.path4)
        img4 = img4.resize((300,300), Image.ANTIALIAS)
        self.canvas4.image = ImageTk.PhotoImage(img4)
        self.canvas4.create_image(0, 0, image = self.canvas4.image  , anchor='nw')
        self.canvas4.place(x=915, y=70)
        #---------------------------------------------------------------------#
        self.label5 = Label(self.root, text="dist 5:", font=("Comic Sans MS", 12) ).place(x=1215,y=5)
        self.vardist5 = DoubleVar()
        self.txt_varDist5 = Entry(self.root, font=("Comic Sans MS",12,"bold"), bg="lightgray",fg="green", textvariable=self.vardist5)
        self.txt_varDist5.place(x=1290,y=5,width=233)
        self.vardist5.set(self.dist3)
        #--------------procentage----------------------------------------------#
        self.lbporcen5 = Label(self.root, text="Simularité :", font=("Comic Sans MS", 12) ).place(x=1215,y=40)
        self.varporcent5 = StringVar()
        self.txt_varporcebn5 = Entry(self.root, font=("Comic Sans MS",12,"bold"), bg="lightgray",fg="#1C1F39", textvariable=self.varporcent5)
        self.txt_varporcebn5.place(x=1320,y=40,width=203)
        self.varporcent5.set(str(self.porcetage4)+ " % ")
        
        self.canvas5 = Canvas(self.root, bg="lightgray", width=300, height=300)
        img5 = Image.open(self.path5)
        img5 = img5.resize((300,300), Image.ANTIALIAS)
        self.canvas5.image = ImageTk.PhotoImage(img5)
        self.canvas5.create_image(0, 0, image = self.canvas5.image  , anchor='nw')
        self.canvas5.place(x=1220, y=70)
        
        #==============================================================================#
        self.label6 = Label(self.root, text="dist 6:", font=("Comic Sans MS", 12) ).place(x=1,y=385)
        self.vardist6 = DoubleVar()
        self.txt_varDist6 = Entry(self.root, font=("Comic Sans MS",12,"bold"), bg="lightgray",fg="green", textvariable=self.vardist6)
        self.txt_varDist6.place(x=70,y=385,width=233)
        self.vardist6.set(self.dist4)
        #--------------procentage---------------------------------------------#
        self.lbporcen6 = Label(self.root, text="Simularité :", font=("Comic Sans MS", 12) ).place(x=1,y=420)
        self.varporcent6 = StringVar()
        self.txt_varporcebn6 = Entry(self.root, font=("Comic Sans MS",12,"bold"), bg="lightgray",fg="#1C1F39", textvariable=self.varporcent6)
        self.txt_varporcebn6.place(x=100,y=420,width=203)
        self.varporcent6.set(str(self.porcetage4)+ " % ")
        
        self.canvas6 = Canvas(self.root, bg="lightgray", width=300, height=300)
        img6 = Image.open(self.path6)
        img6 = img6.resize((300,300), Image.ANTIALIAS)
        self.canvas6.image = ImageTk.PhotoImage(img6)
        self.canvas6.create_image(0, 0, image = self.canvas6.image  , anchor='nw')
        self.canvas6.place(x=0, y=450)
         
        #--------------------------------------------------
        self.label7 = Label(self.root, text="dist 7:", font=("Comic Sans MS", 12) ).place(x=306,y=385)
        self.vardist7 = DoubleVar()
        self.txt_varDist7 = Entry(self.root, font=("Comic Sans MS",12,"bold"), bg="lightgray",fg="green", textvariable=self.vardist7)
        self.txt_varDist7.place(x=375,y=385,width=233)
        self.vardist7.set(self.dist5)
        #--------------procentage----------------------------------------------#
        self.lbporcen7 = Label(self.root, text="Simularité :", font=("Comic Sans MS", 12) ).place(x=306,y=415)
        self.varporcent7 = StringVar()
        self.txt_varporcebn7 = Entry(self.root, font=("Comic Sans MS",12,"bold"), bg="lightgray",fg="#1C1F39", textvariable=self.varporcent7)
        self.txt_varporcebn7.place(x=405,y=415,width=203)
        self.varporcent7.set(str(self.porcetage6)+ " % ")
        
        self.canvas7 = Canvas(self.root, bg="lightgray", width=300, height=300)
        img7 = Image.open(self.path7)
        img7 = img7.resize((300,300), Image.ANTIALIAS)
        self.canvas7.image = ImageTk.PhotoImage(img7)
        self.canvas7.create_image(0, 0, image = self.canvas7.image  , anchor='nw')
        self.canvas7.place(x=305, y=450)
         
        #---------------------------------------------------------------------#
        self.label8 = Label(self.root, text="dist 8:", font=("Comic Sans MS", 12) ).place(x=609,y=385)
        self.vardist8 = DoubleVar()
        self.txt_varDist8 = Entry(self.root, font=("Comic Sans MS",12,"bold"), bg="lightgray",fg="green", textvariable=self.vardist8)
        self.txt_varDist8.place(x=680,y=385,width=233)
        self.vardist8.set(self.dist6)
        #--------------procentage----------------------------------------------#
        self.lbporcen8 = Label(self.root, text="Simularité :", font=("Comic Sans MS", 12) ).place(x=609,y=415)
        self.varporcent8 = StringVar()
        self.txt_varporcebn8 = Entry(self.root, font=("Comic Sans MS",12,"bold"), bg="lightgray",fg="#1C1F39", textvariable=self.varporcent8)
        self.txt_varporcebn8.place(x=710,y=415,width=203)
        self.varporcent8.set(str(self.porcetage7)+ " % ")
        
        self.canvas8 = Canvas(self.root, bg="lightgray", width=300, height=300)
        img8 = Image.open(self.path8)
        img8 = img8.resize((300,300), Image.ANTIALIAS)
        self.canvas8.image = ImageTk.PhotoImage(img8)
        self.canvas8.create_image(0, 0, image = self.canvas8.image  , anchor='nw')
        self.canvas8.place(x=610, y=450)
        #---------------------------------------------------------------------#
        self.label9 = Label(self.root, text="dist 9:", font=("Comic Sans MS", 12) ).place(x=912,y=385)
        self.vardist9 = DoubleVar()
        self.txt_varDist9 = Entry(self.root, font=("Comic Sans MS",12,"bold"), bg="lightgray",fg="green", textvariable=self.vardist9)
        self.txt_varDist9.place(x=985,y=385,width=233)
        self.vardist9.set(self.dist7)
        #--------------procentage----------------------------------------------#
        self.lbporcen9 = Label(self.root, text="Simularité :", font=("Comic Sans MS", 12) ).place(x=912,y=415)
        self.varporcent9 = StringVar()
        self.txt_varporcebn9 = Entry(self.root, font=("Comic Sans MS",12,"bold"), bg="lightgray",fg="#1C1F39", textvariable=self.varporcent9)
        self.txt_varporcebn9.place(x=1010,y=415,width=203)
        self.varporcent9.set(str(self.porcetage8)+ " % ")
        
        self.canvas9 = Canvas(self.root, bg="lightgray", width=300, height=300)
        img9 = Image.open(self.path9)
        img9 = img9.resize((300,300), Image.ANTIALIAS)
        self.canvas9.image = ImageTk.PhotoImage(img9)
        self.canvas9.create_image(0, 0, image = self.canvas9.image  , anchor='nw')
        self.canvas9.place(x=915, y=450)
        #---------------------------------------------------------------------#
        self.label10 = Label(self.root, text="dist 10:", font=("Comic Sans MS", 12) ).place(x=1213, y=385)
        self.vardist10 = DoubleVar()
        self.txt_varDist10 = Entry(self.root, font=("Comic Sans MS",12,"bold"), bg="lightgray",fg="green", textvariable=self.vardist10)
        self.txt_varDist10.place(x=1290,y=385,width=233)
        self.vardist10.set(self.dist8)
        #--------------procentage---------------------------------------------#
        self.lbporcen10 = Label(self.root, text="Simularité :", font=("Comic Sans MS", 12) ).place(x=1213,y=415)
        self.varporcent10 = StringVar()
        self.txt_varporcebn10 = Entry(self.root, font=("Comic Sans MS",12,"bold"), bg="lightgray",fg="#1C1F39", textvariable=self.varporcent10)
        self.txt_varporcebn10.place(x=1317,y=415,width=203)
        self.varporcent10.set(str(self.porcetage9)+ " % ")
        
        self.canvas10 = Canvas(self.root, bg="lightgray", width=300, height=300)
        img10 = Image.open(self.path10)
        img10 = img10.resize((300,300), Image.ANTIALIAS)
        self.canvas10.image = ImageTk.PhotoImage(img10)
        self.canvas10.create_image(0, 0, image = self.canvas10.image  , anchor='nw')
        self.canvas10.place(x=1220, y=450)
       
        self.root.mainloop() 
        
        
        
    def set_file_path(self, path):
        global   file_path
        file_path = path    
        
  
         
    def getfilename():
        return file_path
    
    
    def UploadAction(self, event=None):
        self.txt_val_path.delete(0, END)
        #tmp_directory="C:/Mini projet TDM/queries"    , initialdir=tmp_directory
        self.filename = filedialog.askopenfilename(filetypes=[("All Files ", "*.jpg *.png *.jpeg *.JPEG *.PNG")])
        if(self.filename ==''):
            self.variable_path.set('Paste or enter image Path')
            return
        print('Query Image Selected : \n', self.filename)
        img = Image.open(self.filename)
        img = img.resize((650,597), Image.ANTIALIAS)
        self.canvas.image = ImageTk.PhotoImage(img)
        self.canvas.create_image(0, 0, image=self.canvas.image, anchor='nw')
        
        self.set_file_path(self.filename)
        self.variable_path.set(self.filename)
       
        
       
        
    def ibridSerch(self):
        filn=self.variable_path.get()
        self.filename = str(self.variable_path.get())
        if(filn == 'Paste or enter image Path' or filn=='' ):
             MessageBox.showinfo("Error"," Paste or enter image Path Please !!", parent=self.feneter) 
        else:
            try:   
                a = self.radioValColor.get()
                b = self.radioValTextur.get()
                c = self.radioValForm.get()
                if(a + b + c != 1):
                    MessageBox.showinfo("Impossible","il faut que la somme des poids = 100 %  !!", parent=self.feneter) 
                else:
                    joinpath = os.path.join("queries", self.filename)    
                    pathquery= joinpath
                    #print(pathquery)
                    pathindexcolor = 'IndexImages/indexdataHybridColorMoyenne.csv'
                    pathindexForm ='IndexImages/indexdataHybrideZirnek.csv'
                    pathindexTexture = 'IndexImages/indexTextureHybride.csv'
                    pathdataset = 'datasetHybride/' 
                    # initialize the image descriptor
                    ojcl = ColorDesMoyenne()
                    objText = texturedescriptor()
                    objShape = ZernikeMoments(21)
                    # load the query image and describe it
                    query = cv2.imread(pathquery)
                    #print("query :  ", pathquery)
                    featurColeur = ojcl.describe(query)
                    featurTextur = objText.lbp_features(query) 
                    featurShape = objShape.detectZernik(query)
                    # perform the search
                    searcheribride = SearcherIbride(pathindexcolor, pathindexForm, pathindexTexture)
                    resulofsearch, listeporsentages = searcheribride.ibridesearch(featurColeur, a, featurTextur, b, featurShape, c)
                    i=0
                    listepath = []
                    listscore = []
                   # loop over the dists
                    for (score, distID) in resulofsearch:
                       #load the dist image and display it
                       res = pathdataset +  distID
                       listepath.insert(i, res)
                       listscore.insert(i , score)
                       i+=1
                       
                    self.createcanva(listepath, listscore, listeporsentages)
   
                
            except Exception as es:                  
                 MessageBox.showinfo("Error",f" Error Due to : {str(es)} ", parent=self.feneter)  
        
    
        
    def SearchColor(self):
        filn=self.variable_path.get()
        typeserch = self.typediscripcolor.get()
        self.filename = str(self.variable_path.get())
        if(filn == 'Paste or enter image Path' or filn=='' ):
              MessageBox.showinfo("Error"," Paste or enter image Path Please !!", parent=self.feneter) 
        else:
             try:   
                 if(typeserch == ' HSV '):  
                        joinpath = os.path.join("queries", self.filename)    
                        pathquery= joinpath
                        #print(pathquery)
                        pathindex = 'IndexImages/indexColor.csv'
                        pathdataset = 'datasetColor/' 
                        # initialize the image descriptor
                        cd = ColorDescriptor((8, 12, 3))
                       
                        # load the query image and describe it
                        query = cv2.imread(pathquery)
                        #print("query :  ", pathquery)
                        features = cd.describe(query)
                       
                        # perform the search
                        searcher = Searcher(pathindex)
                        #print("index :   ", pathindex)
                        dists, listeporsentages = searcher.search(features)
                      
                        i=0
                        listepath = []
                        listscore = []
                        # loop over the dists
                        for (score, distID) in dists:
                            #load the dist image and display it
                            res = pathdataset +  distID
                            listepath.insert(i, res)
                            listscore.insert(i , score)
                            #print(res)
                            #print(score)
                            i+=1
                           
                        self.createcanva(listepath, listscore, listeporsentages)
                 elif(typeserch == ' RGB '):
                        joinpath = os.path.join("queries", self.filename)    
                        pathquery= joinpath
                        #print(pathquery)
                        pathindex = 'IndexImages/indexColorRGB.csv'
                        pathdataset = 'datasetColor/' 
                        # initialize the image descriptor
                        cd = RGBHistogram((8, 12, 3))
                       
                        # load the query image and describe it
                        query = cv2.imread(pathquery)
                        #print("query :  ", pathquery)
                        features = cd.describe(query)
                       
                        # perform the search
                        searcher = Searcher(pathindex)
                        #print("index :   ", pathindex)
                        dists, listeporsentages = searcher.search(features)
                      
                        i=0
                        listepath = []
                        listscore = []
                        # loop over the dists
                        for (score, distID) in dists:
                            #load the dist image and display it
                            res = pathdataset +  distID
                            listepath.insert(i, res)
                            listscore.insert(i , score)
                            #print(res)
                            #print(score)
                            i+=1
                           
                        self.createcanva(listepath, listscore, listeporsentages)
                 elif(typeserch == ' Moyenne '):
                        joinpath = os.path.join("queries", self.filename)    
                        pathquery= joinpath
                        #print(pathquery)
                        pathindex = 'IndexImages/indexColorMoyenne.csv'
                        pathdataset = 'datasetColor/' 
                        # initialize the image descriptor
                        cdmoyenne = ColorDesMoyenne()
                       
                        # load the query image and describe it
                        query = cv2.imread(pathquery)
                        #print("query :  ", pathquery)
                        features = cdmoyenne.describe(query)
                       
                        # perform the search
                        searcher = Searcher(pathindex)
                        #print("index :   ", pathindex)
                        dists, listeporsentages = searcher.searchcolorMoyenne(features)
                      
                        i=0
                        listepath = []
                        listscore = []
                        # loop over the dists
                        for (score, distID) in dists:
                            #load the dist image and display it
                            res = pathdataset +  distID
                            listepath.insert(i, res)
                            listscore.insert(i , score)
                            i+=1
                           
                        self.createcanva(listepath, listscore, listeporsentages)
                    
             except Exception as ese:                  
                  MessageBox.showinfo("Error",f" Error Due to : {str(ese)} ", parent=self.feneter)  
                 
                 
  

       
    def SerchTexture(self):
        filn=self.variable_path.get()
        typeserchtexture = self.typediscritexture.get()
        self.filename = str(self.variable_path.get())
        if(filn == 'Paste or enter image Path' or filn==''):
             MessageBox.showinfo("Error"," Paste or enter image Path Please !!", parent=self.feneter) 
        else:
            try: 
                if(typeserchtexture == ' LBP '):
                   joinpath = os.path.join("queries", self.filename)
                   pathquery= joinpath
                   pathindex = 'IndexImages/indexTexture.csv'
                   pathdataset = 'dasetTexture/' 
                   # initialize the image descriptor
                   cd = texturedescriptor()
                   
                   # load the query image and describe it
                   query = cv2.imread(pathquery)
                   #print("query :  ", pathquery)
                   features = cd.lbp_features(query)
                   
                   # perform the search
                   searcher = Searcher(pathindex)
                   dists, listeporsentages = searcher.searchTexture(features)
                   
                   i=0
                   listepath = []
                   listscore = []
                   # loop over the dists
                   for (score, distID) in dists:
                       #load the dist image and display it
                       res = pathdataset +  distID
                       listepath.insert(i, res)
                       listscore.insert(i , score)
                       i+=1
                       
                   self.createcanva(listepath, listscore, listeporsentages)
                elif(typeserchtexture == ' Haralick '):
                     joinpath = os.path.join("queries", self.filename)
                     pathquery= joinpath
                     pathindex = 'IndexImages/indexTextureHaralick.csv'
                     pathdataset = 'dasetTexture/' 
                     # initialize the image descriptor
                     cde = texturedescriptor()
                     # load the query image and describe it
                     query = cv2.imread(pathquery)
                     #print("query :  ", pathquery)
                     features = cde.MatCooccurenceHaralick(query)
                     # perform the search
                     searcher = Searcher(pathindex)
                     #print("index :   ", pathindex)
                     dists, listeporsentages = searcher.searchTexture(features)
                     listepath = []
                     listscore = []
                     i=0
                     # loop over the dists
                     for (score, distID) in dists:
                         #load the dist image and display it
                         res = pathdataset +  distID
                         listepath.insert(i, res)
                         listscore.insert(i , score)
                         #print(res)
                         #print(score)
                         i+=1
                       
                     self.createcanva(listepath, listscore, listeporsentages)
                    
            except Exception as esi:                  
                 MessageBox.showinfo("Error",f" Error Due to : {str(esi)} ", parent=self.feneter)      


  

#=========================la recherche par form===============================#
    def SearchForm(self):
        self.filename = str(self.variable_path.get())
        filn=self.variable_path.get()
        if(filn == 'Paste or enter image Path' or filn==''):
             MessageBox.showinfo("Error"," Paste or enter image Path Please !!", parent=self.feneter) 
        else:
            try:   
                if(self.valdeShape.get()=='Zernike'):
                       joinpath = os.path.join("queries", self.filename)    
                       pathquery= joinpath
                       #print(pathquery)
                       pathindex = 'IndexImages/indexFormZsernik.csv'
                       pathdataset = 'datasetForme/' 
                       # initialize the image descriptor
                       cd = ZernikeMoments(21)
                       # load the query image and describe it
                       query = cv2.imread(pathquery)
                       #print("query :  ", pathquery)
                       features = cd.detectZernik(query)
                       # perform the search
                       searcher = Searcher(pathindex)
                       dists , listeporsentages= searcher.searchShape(features)
                       
                       i=0
                       listepath = []
                       listscore = []
                       # loop over the dists
                       for (score, distID) in dists:
                           #load the dist image and display it
                           res = pathdataset +  distID
                           listepath.insert(i, res)
                           listscore.insert(i , score)
                           #print(res)
                           #print(score)
                           i+=1
                       
                       self.createcanva(listepath, listscore, listeporsentages)
                            #listdist3.insert(i, dist)
                elif(self.valdeShape.get()=='HuMoment'):
                       joinpath = os.path.join("queries", self.filename)    
                       pathquery= joinpath
                       #print(pathquery)
                       pathindex = 'IndexImages/indexShape2.csv'
                       pathdataset = 'datasetForme/' 
                       # initialize the image descriptor
                       cd = ShapeDetector()
                       # load the query image and describe it
                       query = cv2.imread(pathquery)
                       #print("query :  ", pathquery)
                       features = cd.detect(query)
                       # perform the search
                       searcher = Searcher(pathindex)
                       dists, listeporsentages = searcher.searchShape(features)
                       # display the query
                       #cv2.imshow("Image Query", query)
                       i=0
                       listepath = []
                       listscore = []
                       # loop over the dists
                       for (score, distID) in dists:
                           #load the dist image and display it
                           res = pathdataset +  distID
                           listepath.insert(i, res)
                           listscore.insert(i , score)
                           #print(res)
                           #print(score)
                           i+=1
                           
                       self.createcanva(listepath, listscore, listeporsentages)
         
            except Exception as es:                  
                 MessageBox.showinfo("Error",f" Error Due to : {str(es)} ", parent=self.feneter)       


   

    
        
feneter=Tk()
obj=InterfaceGraphique(feneter)
feneter.mainloop()  
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk  #pip install pillow
import random

class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.title("Billing Software")

        ##########Variable
        self.c_name=StringVar()
        self.c_phon = StringVar()
        self.c_bill_no = StringVar()
        self.c_email = StringVar()
        z=random.randint(1000,9999)
        self.c_search = StringVar()
        self.c_product = StringVar()
        self.c_prices = IntVar()
        self.c_qty = IntVar()
        self.c_sub_total = StringVar()
        self.c_tax_input= StringVar()
        self.c_total = StringVar()



        ######### Product Categories List
        self.category=["Select Option","Clothing","LifeStyle","Mobiles"]

########## Sub Clothing
        self.SubCatClothing = ["Pant", "T-shirt", "Shirt"]
        self.pant=["Levis","Mufit","Spykar"]
        self.price_levis=5000
        self.price_mufit = 700
        self.price_spyka= 8000

        self.T_shirt=["Polo", "Roadster", "Jack&Jones"]
        self.price_polo = 1500
        self.price_roadster = 1800
        self.price_jackJones = 1700

        self.Shirt = ["Peter England", "Louis Phillipe", "Park Avenue"]
        self.price_peter = 2100
        self.price_louis = 2700
        self.price_park = 1740

###########SubLifeStyle
        self.SubCatClothing = ["Birth Soap", "Face Cream", "Hair Oil"]
        self.Bath_soap = ["LifeBuy", "Lux", "Santoor","Pear1"]
        self.price_life=float(20)
        self.price_lux = 20
        self.price_santoor =20

        self.T_shirt = ["Fair&Lovely", "Ponds", "Olay","Garnier"]
        self.price_fair = 20
        self.price_ponds = 20
        self.price_olay =20
        self.price_garnier=30

        self.Hair_oil = ["Parachute", "Jashmin", "Bajaj"]
        self.price_parachute = 25
        self.price_jashmin = 22
        self.price_bajaj = 30

        self.category = ["Iphone", "Samsung", "Xiome"]
        self.Iphone=["Iphone_X","Iphone_11","Iphone_12"]
        self.price_ix = 40000
        self.price_i11 =60000
        self.price_i12= 85000

        self.Samsung = ["Samsung M16", "Samsung M12", "Samsung M21"]
        self.price_sm16 = 16000
        self.price_sm12 = 12000
        self.price_m21 = 18000

        self.Xiome = ["Rad11", "Redme-12", "RedmePro"]
        self.price_r11 = 11000
        self.price_12 = 12000
        self.price_rpro = 9000

        ######### Image1
        img = Image.open("Images/banner.png")
        img = img.resize((500, 130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        lbl=Label(self.root,image=self.photoimg)
        lbl.place(x=0,y=0,width=500,height=130)

        ######### Image2
        img_1 = Image.open("Images/banner.png")
        img_1 = img_1.resize((500, 130), Image.ANTIALIAS)
        self.photoimg_1 = ImageTk.PhotoImage(img_1)

        lbl_1 = Label(self.root, image=self.photoimg_1)
        lbl_1.place(x=500, y=0, width=500, height=130)

        ######### Image3
        img_2 = Image.open("Images/banner.png")
        img_2 = img_2.resize((520, 130), Image.ANTIALIAS)
        self.photoimg_2 = ImageTk.PhotoImage(img_2)

        lbl_2 = Label(self.root, image=self.photoimg_2)
        lbl_2.place(x=1000, y=0, width=520, height=130)


        ######## Heading
        lbl_title=Label(self.root,text="BILLING SOFTWARE USING PYTHON",font=('times new roman',35,'bold'),fg='red')
        lbl_title.place(x=0,y=130,width=1530,height=45)

        Main_Frame=Frame(self.root,bd=5,relief=GROOVE,bg='white')
        Main_Frame.place(x=0,y=175,width=1530,height=620)

        ######### Search
        Search_Frame = Frame(Main_Frame, bd=2, bg='white')
        Search_Frame.place(x=1020,y=15,width=500,height=40)


        self.lblBill=Label(Search_Frame,font=('times new roman',12,'bold'),fg='white',bg='red',text='Bill Number')
        self.lblBill.grid(row=0,column=0,sticky=W,padx=1)
        self.txt_Entry_Search=ttk.Entry(Search_Frame,font=('arial',10,'bold'),width=24)
        ########## Customer Label Frame
        Cust_Frame = LabelFrame(Main_Frame, text='Customer',font=('times new roman',12,'bold'), bg='white')
        self.txt_Entry_Search.grid(row=0,column=1,sticky=W,padx=2)
        Cust_Frame.place(x=10, y=5, width=350, height=140)

        self.BtnSearch=Button(Search_Frame,text="Search",font=('times new roman',12,'bold'), bg='white')
        self.BtnSearch.grid(row=0,column=2)



        ###########Mobile Label Frame
        self.lblmobile_no=Label(Cust_Frame,font=('times new roman',12,'bold'),bg='white',text='Mobile No.',bd=4)
        self.lblmobile_no.grid(row=1,column=0,sticky=W,padx=5,pady=2)

        self.txtmobile_no=ttk.Entry(Cust_Frame,font=('times new roman',10,'bold'),width=24)
        self.txtmobile_no.grid(row=1,column=1,sticky=W,padx=5,pady=2)

        ############Customer Label Frame
        self.lblcustname = Label(Cust_Frame, font=('times new roman', 12, 'bold'), bg='white', text='Customer Name',
                                 bd=4)
        self.lblcustname .grid(row=2, column=0, sticky=W, padx=5, pady=2)

        self.txtcustname  = ttk.Entry(Cust_Frame, font=('times new roman', 10, 'bold'), width=24)
        self.txtcustname .grid(row=2, column=1, sticky=W, padx=5, pady=2)

        ############Email Label Frame
        self.lblemail = Label(Cust_Frame, font=('times new roman', 12, 'bold'), bg='white', text='Email',
                              bd=4)
        self.lblemail.grid(row=3, column=0, sticky=W, padx=5, pady=2)

        self.txtemail = ttk.Entry(Cust_Frame, font=('times new roman', 10, 'bold'), width=24)
        self.txtemail.grid(row=3, column=1, sticky=W, padx=5, pady=2)

        ########## ProductLabel Frame
        Prodt_Frame = LabelFrame(Main_Frame, text='Product', font=('times new roman', 12, 'bold'), bg='white')
        Prodt_Frame.place(x=370, y=5, width=620, height=140)

        ###########Product Label Frame
        self.lblcategory = Label(Prodt_Frame, font=('times new roman', 12, 'bold'), bg='white', text='Sub Category', bd=4)
        self.lblcategory.grid(row=0, column=0, sticky=W, padx=5, pady=2)

        self.cmbcategory = ttk.Combobox(Prodt_Frame, font=('times new roman', 10, 'bold'), width=24)

        self.cmbcategory.grid(row=0, column=1, sticky=W, padx=5, pady=2)

        ###########Sub Category Label Frame
        self.lblproductname = Label(Prodt_Frame, font=('times new roman', 12, 'bold'), bg='white', text='Product Name',
                                 bd=4)
        self.lblproductname.grid(row=1, column=0, sticky=W, padx=5, pady=2)

        self.cmbsubcategory = ttk.Combobox(Prodt_Frame, font=('times new roman', 10, 'bold'), width=24)
        self.cmbsubcategory.grid(row=1, column=1, sticky=W, padx=5, pady=2)

        ###########Category Label Frame
        self.lblcategory = Label(Prodt_Frame, font=('times new roman', 12, 'bold'), bg='white', text='Select Category',
                                 bd=4)
        self.lblcategory.grid(row=2, column=0, sticky=W, padx=5, pady=2)

        self.cmbcategory = ttk.Combobox(Prodt_Frame, font=('times new roman', 10, 'bold'), width=24)
        self.cmbcategory.grid(row=2, column=1, sticky=W, padx=5, pady=2)

        ###########Price Label Frame
        self.lblprice = Label(Prodt_Frame, font=('times new roman', 12, 'bold'), bg='white', text='Price',
                                 bd=4)
        self.lblprice.grid(row=0, column=2, sticky=W, padx=5, pady=2)

        self.cmbprice = ttk.Combobox(Prodt_Frame, font=('times new roman', 10, 'bold'), width=24)

        self.cmbprice.grid(row=0, column=3, sticky=W, padx=5, pady=2)
 ############Qty Label Frame
        self.lblqty = Label(Prodt_Frame, font=('times new roman', 12, 'bold'), bg='white', text='Qty',
                              bd=4)
        self.lblqty.grid(row=1, column=2, sticky=W, padx=5, pady=2)

        self.txtqty = ttk.Entry(Prodt_Frame, font=('times new roman', 10, 'bold'), width=24)
        self.txtqty.grid(row=1, column=3, sticky=W, padx=5, pady=2)
########################################################################################################
        ###########Rigth Frame Bill Aria
        RightlabelFrame=LabelFrame(Main_Frame,text="Bill Aria",font=("times new roman",12,"bold"),)
        RightlabelFrame.place(x=1000,y=45,width=480,height=440)
        scroll_y = Scrollbar(RightlabelFrame, orient=VERTICAL)
        self.textarea = Text(RightlabelFrame,yscrollcommand=scroll_y.set,bg="white",fg="blue",font=('arial', 15, 'bold'))
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.textarea.yview)
########################################################################################################
        Bottom_Frame=LabelFrame(Main_Frame,text="Bill Counter",font=('arial',15,'bold'),bg='orangered',fg='white')
        Bottom_Frame.place(x=0,y=485,width=1520,height=125)

        self.lblSubTotal=Label(Bottom_Frame,font=('arial',15,'bold'),bg='orangered',fg='white',text='Sub Total')
        self.lblSubTotal.grid(row=0,column=0,sticky=W,padx=5,pady=2)

        self.EntrySubTotal=ttk.Entry(Bottom_Frame,font=('arial',15,'bold'))
        self.EntrySubTotal.grid(row=0,column=1,sticky=W,padx=5,pady=2)

        self.lblSubTotal = Label(Bottom_Frame, font=('arial', 15, 'bold'), bg='orangered', fg='white', text='Gov Tax')
        self.lblSubTotal.grid(row=1, column=0, sticky=W, padx=5, pady=2)

        self.EntrySubTotal = ttk.Entry(Bottom_Frame, font=('arial', 15, 'bold'))
        self.EntrySubTotal.grid(row=0, column=2, sticky=W, padx=5, pady=2)


########################################################################################################
        Btn_Frame=Frame(Bottom_Frame,bd=2,bg='white')
        Btn_Frame.place(x=320,y=0)

        self.BtnAddToCart=Button(Btn_Frame,height=2,text="Add To Cart",font=('arial',15,'bold'),bg='orangered',fg='white')
        self.BtnAddToCart.grid(row=0,column=0)

        self.BtnGenerate = Button(Btn_Frame, height=2, text="Generate Receipt", font=('arial', 15, 'bold'), bg='orangered',fg = 'white')
        self.BtnGenerate.grid(row=0, column=1)

        self.BtnSave= Button(Btn_Frame, height=2, text="Save", font=('arial', 15, 'bold'), bg='orangered',fg = 'white')
        self.BtnSave.grid(row=0, column=2)
        self.BtnPrint = Button(Btn_Frame, height=2, text="Print", font=('arial', 15, 'bold'), bg='orangered',fg = 'white')
        self.BtnPrint.grid(row=0, column=3)
        self.BtnClear = Button(Btn_Frame, height=2, text="Clear", font=('arial', 15, 'bold'), bg='orangered',fg = 'white')
        self.BtnClear.grid(row=0, column=4)
        self.BtnExit = Button(Btn_Frame, height=2, text="Exit", font=('arial', 15, 'bold'), bg='orangered',fg = 'white')
        self.BtnExit.grid(row=0, column=0)







root=Tk()
ob=Bill_App(root)
root.mainloop()




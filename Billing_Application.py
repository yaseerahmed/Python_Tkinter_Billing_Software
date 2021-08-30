from tkinter import *
import math,random,os
from tkinter import messagebox
class Application:
    def __init__(self,window):
        self.window=window
        #window = Tk()
        self.window.title("BILLING SOFTWARE") #title of application
        self.window.geometry('1280x650+0+0')
        l1 = Label(window,text="My First Software",bd=10,relief=GROOVE,font=("Arail", 30,"bold"),bg = "black",fg = "white",pady=2)
        l1.pack(fill=X)
        #Variables
        self.customername=StringVar()
        self.customernumber=StringVar()
        self.customerbill=StringVar()
        x=random.randint   (1000,9999)
        self.customerbill.set(str(x))
        self.rice=IntVar()
        self.oil=IntVar()
        self.soaps=IntVar()
        self.tissue=IntVar()
        self.chillipowder=IntVar()
        self.sugar=IntVar()
        self.coke=IntVar()
        self.mazza=IntVar()
        self.waterbottle=IntVar()
        self.thumpsup=IntVar()
        self.sprite=IntVar()
        self.realdrink=IntVar()
        self.plates=IntVar()
        self.spoon=IntVar()
        self.tablecloth=IntVar()
        self.cups=IntVar()
        self.cups=IntVar()
        self.dishes=IntVar()
        self.broom=IntVar()
        self.totalitemsprice=StringVar()
        self.totalcooldrinkprice=StringVar()
        self.totalgrocceryprice=StringVar()
        self.totalitemstax=StringVar()
        self.totalcooldrinktax=StringVar()
        self.totalgroccerytax=StringVar()
        self.searchbill=StringVar()
        #Frame of applcation for customer details
        f1 = LabelFrame(window,bd=10,relief=GROOVE,text="Details",font=("times new roman",18),fg="violet",bg="black")
        f1.place(x=0,y=72,relwidth=1)
        c_name = Label(f1,text="Customer name",fg="white",bg="black",font=("Times new roman",16),padx=5,pady=8).grid(row=0,column=0)
        c_name_text = Entry(f1,bd=4,width=18,textvariable=self.customername, font=("times new roman",13),relief=SUNKEN).grid(row=0,column=1,padx=5,pady=20)
        C_number = Label(f1,text="Phone number",fg="white",bg="black",font=("Times new roman",16),padx=5,pady=8).grid(row=0,column=2)
        C_number_text = Entry(f1,bd=4,width=18,textvariable=self.customernumber,font=("times new roman",13),relief=SUNKEN).grid(row=0,column=3,padx=5,pady=20)
        billno = Label(f1,text="Bill No.",fg="white",bg="black",font=("Times new roman",16),padx=5,pady=8).grid(row=0,column=4)
        billno_text = Entry(f1,bd=4,width=18,textvariable=self.customerbill,font=("times new roman",13),relief=SUNKEN).grid(row=0,column=5,padx=5,pady=20)
        #seaarch button
        b1 = Button(f1,command=self.find_bill,text="Search",bd=4,font=("Arail",10),width=10).grid(row=0,column=6,padx=10,pady=10)
        #label as company name
        Company = Label(f1,text="  FASTSERVICES",fg="white",bg="black",font=("Times new roman",16,"bold"),padx=5,pady=8).grid(row=0,column=7)
        #frame 2
        f2 = LabelFrame(window,bd=10,text="Items",bg="black",fg="violet",font=("Times new roman",20))
        f2.place(x=0,y = 180,width=325,height=350)
        #entities in frame 2
        Rice = Label(f2,text="Rice    ",fg="white",bg="black",font=("times new roman",20)).grid(row=1,column=0)
        Rice_text = Entry(f2,bd=4,width=10,textvariable=self.rice,font=("times new roman",13),relief=SUNKEN).grid(row=1,column=1,padx=5,pady=10)
        Oil = Label(f2,text="Oil    ",fg="white",bg="black",font=("times new roman",20)).grid(row=2,column=0)
        Oil_text = Entry(f2,bd=4,width=10,textvariable=self.oil,font=("times new roman",13),relief=SUNKEN).grid(row=2,column=1,padx=5,pady=10)
        soaps = Label(f2,text="Soaps    ",fg="white",bg="black",font=("times new roman",20)).grid(row=3,column=0)
        soaps_text = Entry(f2,bd=4,width=10,textvariable=self.soaps,font=("times new roman",13),relief=SUNKEN).grid(row=3,column=1,padx=5,pady=10)
        Tissues = Label(f2,text="Tissues    ",fg="white",bg="black",font=("times new roman",20)).grid(row=4,column=0)
        Tissues_text = Entry(f2,bd=4,width=10,textvariable=self.tissue,font=("times new roman",13),relief=SUNKEN).grid(row=4,column=1,padx=5,pady=10)
        ChiiliPowder = Label(f2,text="Chilli Powder",fg="white",bg="black",font=("times new roman",20)).grid(row=5,column=0)
        ChilliPowder_text = Entry(f2,bd=4,width=10,textvariable=self.chillipowder,font=("times new roman",13),relief=SUNKEN).grid(row=5,column=1,padx=5,pady=10)
        Sugar = Label(f2,text="Sugar",fg="white",bg="black",font=("times new roman",20)).grid(row=6,column=0)
        Sugar_text = Entry(f2,bd=4,width=10,textvariable=self.sugar,font=("times new roman",13),relief=SUNKEN).grid(row=6,column=1,padx=5,pady=10)
        #frame 3
        f3 = LabelFrame(window,bd=10,text="Cool drinks",bg="black",fg="violet",font=("Times new roman",20))
        f3.place(x=325,y = 180,width=325,height=350)
        #entities in frame 3
        Coke = Label(f3,text="Coke    ",fg="white",bg="black",font=("times new roman",20)).grid(row=1,column=0)
        coke_text = Entry(f3,bd=4,width=10,textvariable=self.coke,font=("times new roman",13),relief=SUNKEN).grid(row=1,column=1,padx=5,pady=10)
        Mazaa = Label(f3,text="Mazaa    ",fg="white",bg="black",font=("times new roman",20)).grid(row=2,column=0)
        Mazaa_text = Entry(f3,bd=4,width=10,textvariable=self.mazza,font=("times new roman",13),relief=SUNKEN).grid(row=2,column=1,padx=5,pady=10)
        WaterBottle = Label(f3,bd=4,text="WaterBottle    ",fg="white",bg="black",font=("times new roman",20)).grid(row=3,column=0)
        WaterBottle_text = Entry(f3,bd=4,width=10,textvariable=self.waterbottle,font=("times new roman",13),relief=SUNKEN).grid(row=3,column=1,padx=5,pady=10)
        ThumpsUp = Label(f3,text="ThumpsUp    ",fg="white",bg="black",font=("times new roman",20)).grid(row=4,column=0)
        ThumpsUp_text = Entry(f3,bd=4,width=10,textvariable=self.thumpsup,font=("times new roman",13),relief=SUNKEN).grid(row=4,column=1,padx=5,pady=10)
        Sprite = Label(f3,text="Sprite",fg="white",bg="black",font=("times new roman",20)).grid(row=5,column=0)
        Spriter_text = Entry(f3,bd=4,width=10,textvariable=self.sprite,font=("times new roman",13),relief=SUNKEN).grid(row=5,column=1,padx=5,pady=10)
        RealDrink = Label(f3,text="Real Drink",fg="white",bg="black",font=("times new roman",20)).grid(row=6,column=0)
        RealDrink_text = Entry(f3,bd=4,width=10,textvariable=self.realdrink,font=("times new roman",13),relief=SUNKEN).grid(row=6,column=1,padx=5,pady=10)
        #frame 4
        f4 = LabelFrame(window,bd=10,text="Grossery",bg="black",fg="violet",font=("Times new roman",20))
        f4.place(x=650,y = 180,width=325,height=350)
        #entities in frame 4
        Plates = Label(f4,text="Plates    ",fg="white",bg="black",font=("times new roman",20)).grid(row=1,column=0)
        Plates_text = Entry(f4,width=10,textvariable=self.plates,bd=4,font=("times new roman",13),relief=SUNKEN).grid(row=1,column=1,padx=5,pady=10)
        spoons = Label(f4,text="spoons    ",fg="white",bg="black",font=("times new roman",20)).grid(row=2,column=0)
        spoons_text = Entry(f4,width=10,textvariable=self.spoon,bd=4,font=("times new roman",13),relief=SUNKEN).grid(row=2,column=1,padx=5,pady=10)
        TableCloth = Label(f4,text="Table Cloth    ",fg="white",bg="black",font=("times new roman",20)).grid(row=3,column=0)
        TableCloth_text = Entry(f4,bd=4,width=10,textvariable=self.tablecloth,font=("times new roman",13),relief=SUNKEN).grid(row=3,column=1,padx=5,pady=10)
        Cups = Label(f4,text="Cups    ",fg="white",bg="black",font=("times new roman",20)).grid(row=4,column=0)
        Cups_text = Entry(f4,bd=4,width=10,textvariable=self.cups,font=("times new roman",13),relief=SUNKEN).grid(row=4,column=1,padx=5,pady=10)
        dishes = Label(f4,text="Dish Plates",fg="white",bg="black",font=("times new roman",20)).grid(row=5,column=0)
        dishes_text = Entry(f4,bd=4,width=10,textvariable=self.dishes,font=("times new roman",13),relief=SUNKEN).grid(row=5,column=1,padx=5,pady=10)
        broom = Label(f4,text="Broom",fg="white",bg="black",font=("times new roman",20)).grid(row=6,column=0)
        broom_text = Entry(f4,width=10,textvariable=self.broom,bd=4,font=("times new roman",13),relief=SUNKEN).grid(row=6,column=1,padx=5,pady=10)
        #Bill Atea
        f5 = LabelFrame(window,bd=12,bg="White",relief=SUNKEN)
        f5.place(x=975,y=180,width=300,height=350)
        l51 = Label(f5,text="Billing Area",font=("Arail",15,"bold"),bg="lightgrey",relief=SUNKEN).pack(fill=X)
        #scroll bar
        scroll_y = Scrollbar(f5,orient=VERTICAL)
        self.textarea=Text(f5,yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)
        #frame 6 Bill menu
        f6 = LabelFrame(window,bd=3,text="bill Menu",bg="black",fg="violet",relief=GROOVE)
        f6.place(x=0,y = 530,relwidth=1,height=130)
        #l61 = Label(f6,text="j1",bg="black").pack()
        #entities in frame 6
        TotalItemsPrice = Label(f6,text="Total Items Price",fg="white",bg="black",font=("times new roman",20)).grid(row=1,column=0)
        TotalItemsPrice_text = Entry(f6,width=10,textvariable=self.totalitemsprice,bd=4,font=("times new roman",8),relief=SUNKEN).grid(row=1,column=1,padx=5,pady=1)
        TotalCoolDrinksPrice = Label(f6,text="Total CoolDrinks Price",fg="white",bg="black",font=("times new roman",20)).grid(row=2,column=0)
        TotalCoolDrinksPrice_text = Entry(f6,width=10,textvariable=self.totalcooldrinkprice,bd=4,font=("times new roman",8),relief=SUNKEN).grid(row=2,column=1,padx=5,pady=1)
        TotalGrocceryPrice = Label(f6,text="Total Groccery Price",fg="white",bg="black",font=("times new roman",20)).grid(row=3,column=0)
        TotalGrocceryPrice_text = Entry(f6,width=10,textvariable=self.totalgrocceryprice,bd=4,font=("times new roman",8),relief=SUNKEN).grid(row=3,column=1,padx=5,pady=1)
        TotalItemstax = Label(f6,text="Total Items tax",fg="white",bg="black",font=("times new roman",20)).grid(row=1,column=2)
        TotalItemstax_text = Entry(f6,width=10,textvariable=self.totalitemstax,bd=4,font=("times new roman",8),relief=SUNKEN).grid(row=1,column=3,padx=5,pady=1)
        TotalCoolDrinkstax = Label(f6,text="Total CoolDrinks tax",fg="white",bg="black",font=("times new roman",20)).grid(row=2,column=2)
        TotalCoolDrinkstax_text = Entry(f6,width=10,textvariable=self.totalcooldrinktax,bd=4,font=("times new roman",8),relief=SUNKEN).grid(row=2,column=3,padx=5,pady=1)
        TotalGroccerytax = Label(f6,text="Total Groccery tax",fg="white",bg="black",font=("times new roman",20)).grid(row=3,column=2)
        TotalGroccerytax_text = Entry(f6,width=10,textvariable=self.totalgroccerytax,bd=4,font=("times new roman",8),relief=SUNKEN).grid(row=3,column=3,padx=5,pady=1)
        #Buttons
        f7 = LabelFrame(window,bg="black",relief=SUNKEN)
        f7.place(x=670,y=540,relwidth=1,height=120)
        l71=Label(f7,width=1,height=1,bg="black").grid(row=1,column=1)
        total = Button(f7,command=self.total,text="Total",height=3,width=12,relief=RAISED,bg="white",fg="black",font=("times new roman",15)).grid(row=2,column=5)
        Bill = Button(f7,command=self.bill_area,text="Bill",height=3,width=12,relief=RAISED,bg="white",fg="black",font=("times new roman",15)).grid(row=2,column=6)
        Print = Button(f7,command=self.save_bill,text="Print",height=3,width=12,relief=RAISED,bg="white",fg="black",font=("times new roman",15)).grid(row=2,column=7)
        Clear = Button(f7,command=self.clear_data,text="Clear",height=3,width=12,relief=RAISED,bg="white",fg="black",font=("times new roman",15)).grid(row=2,column=8)
        
    def total(self):
        self.total_items_price=float((self.rice.get()*45)+
                                    (self.oil.get()*170)+
                                    (self.soaps.get()*20)+
                                    (self.tissue.get()*30)+
                                    (self.chillipowder.get()*70)+
                                    (self.sugar.get()*41)
                                    )
        self.totalitemsprice.set("Rs. "+str(self.total_items_price))
        self.totalitemstax.set("Rs. "+str(round(self.total_items_price*0.02,2)))
       
        self.total_cooldrink_price=float((self.coke.get()*30)+
                                    (self.mazza.get()*80)+
                                    (self.waterbottle.get()*20)+
                                    (self.thumpsup.get()*80)+
                                    (self.sprite.get()*75)+
                                    (self.realdrink.get()*60)
                                    )
        self.totalcooldrinkprice.set("Rs. "+str(self.total_cooldrink_price))
        self.totalcooldrinktax.set("Rs. "+str(round(self.total_cooldrink_price*0.02,2)))
        
        self.total_groccery_price=float((self.plates.get()*40)+
                                    (self.spoon.get()*10)+
                                    (self.tablecloth.get()*90)+
                                    (self.cups.get()*25)+
                                    (self.dishes.get()*70)+
                                    (self.broom.get()*40)
                                    )
        self.totalgrocceryprice.set("Rs. "+str(self.total_groccery_price))
        self.totalgroccerytax.set("Rs. "+str(round(self.total_groccery_price*0.02,2)))
    
    def welcome_text(self):
        self.textarea.delete('1.0',END)
        self.textarea.insert(END,"Welcome to Fast Services Retail")
        self.textarea.insert(END,f"\n Bill Number    : {self.customerbill.get()}")
        self.textarea.insert(END,f"\n Customer Name  : {self.customername.get()}")
        self.textarea.insert(END,f"\n Mobile Numbner : {self.customernumber.get()}")
        self.textarea.insert(END,"\n===============================\n")
        self.textarea.insert(END,"Product     Quantity     Price")
        self.textarea.insert(END,"\n===============================\n")
    def bill_area(self):
        if self.customername.get() =="" or self.customernumber.get()=="":
            messagebox.showerror("Error","Please enter the customer details")
        elif self.totalitemsprice.get()=="Rs. 0.0" and self.totalcooldrinkprice.get()=="Rs. 0.0" and self.totalgrocceryprice.get()=="Rs. 0.0":
            messagebox.showerror("Error","Please enter the products purchased")
        else:
            self.welcome_text()
            if self.rice.get()!=0:
                self.textarea.insert(END,f"\n Rice          {self.rice.get()}          {self.rice.get()*45}")
            if self.oil.get()!=0:
                self.textarea.insert(END,f"\n Oil           {self.oil.get()}          {self.oil.get()*170}")
            if self.soaps.get()!=0:
                self.textarea.insert(END,f"\n Soaps         {self.soaps.get()}          {self.soaps.get()*20}")
            if self.tissue.get()!=0:
                self.textarea.insert(END,f"\n Tissue        {self.tissue.get()}          {self.tissue.get()*30}")
            if self.chillipowder.get()!=0:
                self.textarea.insert(END,f"\n Chilli powder {self.chillipowder.get()}          {self.chillipowder.get()*70}")
            if self.sugar.get()!=0:
                self.textarea.insert(END,f"\n Sugar         {self.sugar.get()}          {self.sugar.get()*41}")
            #cooldrinks
            if self.coke.get()!=0:
                self.textarea.insert(END,f"\n Coke          {self.coke.get()}          {self.coke.get()*30}")
            if self.mazza.get()!=0:
                self.textarea.insert(END,f"\n Mazza         {self.mazza.get()}          {self.mazza.get()*80}")
            if self.waterbottle.get()!=0:
                self.textarea.insert(END,f"\n Water bottle  {self.waterbottle.get()}          {self.waterbottle.get()*20}")
            if self.thumpsup.get()!=0:
                self.textarea.insert(END,f"\n Thumps Up     {self.sprite.get()}          {self.thumpsup.get()*80}")
            if self.sprite.get()!=0:
                self.textarea.insert(END,f"\n Sprite        {self.sprite.get()}          {self.sprite.get()*75}")
            if self.realdrink.get()!=0:
                self.textarea.insert(END,f"\n Real drink    {self.realdrink.get()}          {self.realdrink.get()*60}")
            #Groccery
            if self.plates.get()!=0:
                self.textarea.insert(END,f"\n Plates        {self.plates.get()}          {self.plates.get()*40}")
            if self.spoon.get()!=0:
                self.textarea.insert(END,f"\n spoon         {self.spoon.get()}          {self.spoon.get()*10}")
            if self.tablecloth.get()!=0:
                self.textarea.insert(END,f"\n Table cloth   {self.tablecloth.get()}          {self.tablecloth.get()*90}")
            if self.cups.get()!=0:
                self.textarea.insert(END,f"\n Cup           {self.cups.get()}          {self.cups.get()*25}")
            if self.dishes.get()!=0:
                self.textarea.insert(END,f"\n Dishes        {self.dishes.get()}          {self.dishes.get()*70}")
            if self.broom.get()!=0:
                self.textarea.insert(END,f"\n Broom         {self.broom.get()}          {self.broom.get()*40}")
            self.textarea.insert(END,"\n----------------------------")
            if self.totalitemstax.get()!="Rs. 0:0":
                self.textarea.insert(END,f"\nTotal Items Tax      {self.totalitemstax.get()}")
            if self.totalcooldrinktax.get()!="0:0":
                self.textarea.insert(END,f"\nTotal Cool drink Tax {self.totalcooldrinktax.get()}")
            if self.totalgroccerytax.get()!="0:0":
                self.textarea.insert(END,f"\nTotal Groccery Tax   {self.totalgroccerytax.get()}")
            if self.totalitemsprice.get()!="Rs. 0:0":
                self.textarea.insert(END,f"\nTotal Items Price    {self.totalitemsprice.get()}")
            if self.totalcooldrinkprice.get()!="0:0":
                self.textarea.insert(END,f"\nTotal Cooldrink Price{self.totalcooldrinkprice.get()}")
            if self.totalgrocceryprice.get()!="0:0":
                self.textarea.insert(END,f"\nTotal Groccery Price {self.totalgrocceryprice.get()}")
            self.textarea.insert(END,"\n----------------------------")
            self.totalbill = self.total_items_price*1.02 + self.total_cooldrink_price*1.02 + self.total_groccery_price*1.02
            self.textarea.insert(END,f"\nTotal Bill :          Rs. {self.totalbill}")
            
    def save_bill(self):
        op = messagebox.askyesno("Save bill","Do you want to save the bill")
        if op>0:
            self.bill_data = self.textarea.get('1.0',END)
            f1=open("billno "+str(self.customerbill.get())+".txt","w") #file will get saved to same locaation where the code is saved.
            f1.write(self.bill_data)
            f1.close()
            messagebox.showinfo("Saved","Bill has been saved successfully")
        else:
            return
    def find_bill(self):
        for i in os.listdir("/"):
            print(i)
    def clear_data(self):
        self.customername.set("")
        self.customernumber.set("")
        self.customerbill.set("")
        self.rice.set(0)
        self.oil.set(0)
        self.soaps.set(0)
        self.tissue.set(0)
        self.chillipowder.set(0)
        self.sugar.set(0)
        self.coke.set(0)
        self.mazza.set(0)
        self.waterbottle.set(0)
        self.thumpsup.set(0)
        self.sprite.set(0)
        self.realdrink.set(0)
        self.plates.set(0)
        self.spoon.set(0)
        self.tablecloth.set(0)
        self.cups.set(0)
        self.cups.set(0)
        self.dishes.set(0)
        self.broom.set(0)
        self.totalitemsprice.set(0)
        self.totalcooldrinkprice.set(0)
        self.totalgrocceryprice.set(0)
        self.totalitemstax.set(0)
        self.totalcooldrinktax.set(0)
        self.totalgroccerytax.set(0)
        self.searchbill.set(0)
root = Tk()
obj = Application(root)
root.mainloop()
print(os.getcwd())
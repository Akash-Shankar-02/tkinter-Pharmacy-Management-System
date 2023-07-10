from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from Products import *
import random,os
from tkinter import messagebox
import tempfile

class Bill:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x800+0+0")
        self.root.title("Billing Software")

#=====================================variables==========================================#

        self.var_prodname=StringVar()
        self.var_price=IntVar()
        self.var_ptype=StringVar()
        self.billno=StringVar()
        x=random.randint(1000,9999)
        self.billno.set(x)
        self.cname=StringVar()
        self.cphone=StringVar()
        self.email=StringVar()       
        self.var_subtotal=StringVar()
        self.var_total=StringVar()
        self.var_tax=StringVar()
        self.var_qty=IntVar()

##################### title ###############################################
        lbl_title=Label(self.root,text="Billing Software",font=("times new roman",35,"bold"),fg="white",bg="black")
        lbl_title.place(x=0,y=10,width=1530,height=45)

        mainframe=Frame(self.root,bd=5,relief=GROOVE,bg="white")
        mainframe.place(x=0,y=55,width=1360,height=640)

######################## customer label frame ##############################
        custframe=LabelFrame(mainframe,text="Customer details",font=("arial",12,"bold"),fg="black",bg="white")
        custframe.place(x=10,y=5,width=350,height=200)

        self.lbl_name=Label(custframe,text="Customer Name",font=("arial",12,"bold"),bg="white",fg="black")
        self.lbl_name.grid(row=0,column=0,stick=W,padx=5,pady=2)
        self.entry_name=ttk.Entry(custframe,textvariable=self.cname,font=("arial",12,"bold"),width=20)
        self.entry_name.grid(row=0,column=1)

        self.lbl_mob=Label(custframe,text="Mobile No.",font=("arial",12,"bold"),bg="white",fg="black")
        self.lbl_mob.grid(row=1,column=0,stick=W,padx=5,pady=2)
        self.entry_mob=ttk.Entry(custframe,textvariable=self.cphone,font=("arial",12,"bold"),width=20)
        self.entry_mob.grid(row=1,column=1)

        self.lbl_email=Label(custframe,text="Email ID",font=("arial",12,"bold"),bg="white",fg="black")
        self.lbl_email.grid(row=2,column=0,stick=W,padx=5,pady=2)
        self.entry_email=ttk.Entry(custframe,textvariable=self.email,font=("arial",12,"bold"),width=20)
        self.entry_email.grid(row=2,column=1)

######################## Product label frame ##############################
        prodframe=LabelFrame(mainframe,text="Product",font=("arial",12,"bold"),bg="white",fg="black")
        prodframe.place(x=370,y=5,width=500,height=170)

        #Product type
        ptype=Label(prodframe,text="Product Type",font=("times new roman",12,"bold"),padx=2,pady=6)
        ptype.grid(row=0,column=0,sticky=W)
        combo_ptype=ttk.Combobox(prodframe,textvariable=self.var_ptype,font=("arial",12,"bold"),width=34,state="readonly")
        combo_ptype['values']=("Select Type","Tablet","Tonic","Baby Product","Essential")
        combo_ptype.current(0)
        combo_ptype.grid(row=0,column=1,sticky=W)

        #Product name
        prodname=Label(prodframe,text="Product Name",font=("times new roman",12,"bold"),padx=2,pady=6)
        prodname.grid(row=1,column=0,sticky=W)
        txtname=ttk.Entry(prodframe,textvariable=self.var_prodname,font=("arial",12,"bold"),width=34)
        txtname.grid(row=1,column=1)

        #price
        price=Label(prodframe,text="Price",font=("times new roman",12,"bold"),padx=2,pady=6)
        price.grid(row=2,column=0,sticky=W)
        txtprice=ttk.Entry(prodframe,textvariable=self.var_price,font=("arial",12,"bold"),width=34)
        txtprice.grid(row=2,column=1)   


######################## Product label frame 2 ##############################
        prodframe2=LabelFrame(mainframe,text="",font=("arial",12,"bold"),bg="white",fg="black")
        prodframe2.place(x=370,y=180,width=500,height=50)

        #quantity
        qty=Label(prodframe2,text="Quantity",font=("times new roman",12,"bold"),padx=2,pady=6)
        qty.grid(row=0,column=0,sticky=W)
        txtqty=ttk.Entry(prodframe2,textvariable=self.var_qty,font=("arial",12,"bold"),width=29)
        txtqty.grid(row=0,column=1)   

        ############ fetch data function ###############
        def fetch_data():
            conn=pymysql.connect(host="localhost",user="root",password="akash",database="pms")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from bill")
            rows=my_cursor.fetchall()
            if len(rows)!=0:
                self.products_table.delete(*self.products_table.get_children())
                for i in rows:
                    self.products_table.insert("",END,values=i)
                conn.commit()
            conn.close()
        
        ##################################################################################

        showall=Button(prodframe2,text="Show All",command=fetch_data,font=("arial",11,"bold"),width=10,bg="gold",fg="black")
        showall.grid(row=0,column=2,padx=1)

#====================== Bill Frame ==============================#

        billframe=LabelFrame(mainframe,text="Bill",font=("arial",12,"bold"),bg="white",fg="black")
        billframe.place(x=880,y=65,width=465,height=440)

        scroll_y=Scrollbar(billframe,orien=VERTICAL)
        self.textarea=Text(billframe,yscrollcommand=scroll_y.set,bg="white",fg="blue",font=("times new roman",12,"bold"))
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.textarea.yview)
        self.textarea.pack(fill=BOTH,expand=1)
 
        self.cart=[]

        def additem():
                self.n=self.var_price.get()
                self.m=self.var_qty.get()*self.n
                self.cart.append(self.m)
                if self.var_prodname.get()=="":
                        messagebox.showerror("Error","Please Select the Product Name")
                else:
                        self.textarea.insert(END,f"\n {self.var_prodname.get()}\t\t\t{self.var_qty.get()}\t\t{self.m}") 
                        self.var_subtotal.set(str('Rs.%.2f'%(sum(self.cart))))
                        self.var_tax.set(str('Rs.%.2f'%((12/100)*sum(self.cart))))
                        self.var_total.set(str('Rs.%.2f'%(sum(self.cart)+(12/100)*sum(self.cart))))               



        def bill():
                self.textarea.delete(1.0,END)
                self.textarea.insert(END,"\t\t Apollo Pharmacy")
                self.textarea.insert(END,f"\n Bill Number:{self.billno.get()}")
                self.textarea.insert(END,f"\n Customer Name:{self.cname.get()}")
                self.textarea.insert(END,f"\n Phone Number:{self.cphone.get()}")
                self.textarea.insert(END,f"\n Customer Email:{self.email.get()}")

                self.textarea.insert(END,"\n================================================")
                self.textarea.insert(END,f"\n Products\t\t\tQTY\t\tprice")
                self.textarea.insert(END,"\n================================================")
        
        
        self.addtocart=Button(prodframe,text="Add To Cart",command=additem,font=("arial",12,'bold'),bg="red4",fg="white")
        self.addtocart.grid(row=3,column=1)
        bill()                

#=======================Bill Counter Label Frame=============================#

        billcounterframe=LabelFrame(self.root,bd=2,relief=RIDGE,text="Bill Counter",font=("times new roman",12,"bold"),bg="white",fg="black")
        billcounterframe.place(x=10,y=400,width=365,height=185)

        self.subtotal=Label(billcounterframe,font=("arial",12,'bold'),bg="white",text="Sub Total",bd=4)
        self.subtotal.grid(row=0,column=0,sticky=W,padx=5,pady=2)
        self.entrysubtotal=ttk.Entry(billcounterframe,textvariable=self.var_subtotal,font=("arial",12,'bold'),width=24)
        self.entrysubtotal.grid(row=0,column=1,sticky=W,padx=5,pady=2)

        self.tax=Label(billcounterframe,font=("arial",12,'bold'),bg="white",text="Tax",bd=4)
        self.tax.grid(row=1,column=0,sticky=W,padx=5,pady=2)
        self.entrytax=ttk.Entry(billcounterframe,textvariable=self.var_tax,font=("arial",12,'bold'),width=24)
        self.entrytax.grid(row=1,column=1,sticky=W,padx=5,pady=2)

        self.total=Label(billcounterframe,font=("arial",12,'bold'),bg="white",text="Total",bd=4)
        self.total.grid(row=2,column=0,sticky=W,padx=5,pady=2)
        self.entrytotal=ttk.Entry(billcounterframe,textvariable=self.var_total,font=("arial",12,'bold'),width=24)
        self.entrytotal.grid(row=2,column=1,sticky=W,padx=5,pady=2)

#=======================Button Frame=========================================# 
        
        buttonframe=LabelFrame(self.root,bd=2,bg="white")
        buttonframe.place(x=880,y=580,width=1340,height=50)

        def gen_bill():
                if self.var_prodname.get()=="":
                        messagebox.showerror("Error","Please Add to Cart")

                else:
                        text=self.textarea.get(9.0,(9.0+float(len(self.cart))))
                        bill()
                        self.textarea.insert(END,text)
                        self.textarea.insert(END,"\n================================================")
                        self.textarea.insert(END,f"\n Sub Total:\t\t\t{self.var_subtotal.get()}")
                        self.textarea.insert(END,f"\n GST:\t\t\t{self.var_tax.get()}")
                        self.textarea.insert(END,f"\n Total:\t\t\t{self.var_total.get()}")

        def save_bill():
                op=messagebox.askyesno("Save Bill","Do you want to save the Bill")
                if op>0:
                        self.bill_data=self.textarea.get(1.0,END)
                        f1=open('bills/'+str(self.billno.get())+".txt","w")
                        f1.write(self.bill_data)
                        op=messagebox.showinfo("Saved",f"Bill No:{self.billno.get()} is saved successfully")
                        f1.close()

        def printf():
                q=self.textarea.get(1.0,"end-1c")
                filename=tempfile.mktemp('.txt')
                open(filename,'w').write(q)
                os.startfile(filename,"print")

        def clear():
                self.textarea.delete(1.0,END)
                self.cname.set("")
                self.cphone.set("")
                self.email.set("")
                x=random.randint(1000,9999)
                self.billno.set(str(x))
                self.var_prodname.set("")
                self.var_price.set("")
                self.var_ptype.set("")     
                self.var_subtotal.set("")
                self.var_total.set("")
                self.var_tax.set("")
                self.var_qty.set("")


      
        self.generatebill=Button(buttonframe,height=1,command=gen_bill,text="Generate Bill",font=("arial",19,'bold'),bg="red4",fg="white")
        self.generatebill.grid(row=1,column=0)

        self.savebill=Button(buttonframe,height=1,command=save_bill,text="Save Bill",font=("arial",19,'bold'),bg="red4",fg="white")
        self.savebill.grid(row=1,column=2)

        self.print=Button(buttonframe,height=1,command=printf,text="Print",font=("arial",19,'bold'),bg="red4",fg="white")
        self.print.grid(row=1,column=4)

        self.clear=Button(buttonframe,height=1,command=clear,text="Clear",font=("arial",19,'bold'),bg="red4",fg="white")
        self.clear.grid(row=1,column=6)

#=====================================table frame================================================#

        tableframe=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and Search System",font=("times new roman",12,"bold"),bg="white",fg="black")
        tableframe.place(x=375,y=290,width=500,height=300)

        lblsearchby=Label(tableframe,font=("arial",12,"bold"),text="Search by",bg="black",fg="white")
        lblsearchby.grid(row=0,column=0,sticky=W)
        
        self.search_var=StringVar()
        combo_search=ttk.Combobox(tableframe,textvariable=self.search_var,font=("arial",12,"bold"),width=15,state="readonly")
        combo_search['value']=("prodname","ptype")
        combo_search.current(0)
        combo_search.grid(row=0,column=1)
        
        self.txtsearch=StringVar()
        searchtxt=ttk.Entry(tableframe,textvariable=self.txtsearch,width=15,font=("arial",11,"bold"))
        searchtxt.grid(row=0,column=2,padx=5)


        ############# search function #################

        def search():
            conn=pymysql.connect(host="localhost",user="root",password="akash",database="pms")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from bill where "+str(self.search_var.get())+" = "+"\""+str(self.txtsearch.get())+"\"")
            rows=my_cursor.fetchall()
            if len(rows)!=0:
                self.products_table.delete(*self.products_table.get_children())
                for i in rows:
                    self.products_table.insert("",END,values=i)
                conn.commit()
            conn.close()


        ################################################################################
        search=Button(tableframe,text="Search",command=search,font=("arial",11,"bold"),width=10,bg="gold",fg="black")
        search.grid(row=0,column=3,padx=1)

#====================================show data table============================================#

        details_table=Frame(tableframe,bd=2,relief=RIDGE)
        details_table.place(x=0,y=30,width=500,height=250)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)
        self.products_table=ttk.Treeview(details_table,column=("ptype","prodname","price"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)        

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.products_table.xview)
        scroll_y.config(command=self.products_table.yview)
        
        self.products_table.heading("ptype",text="Product Type")        
        self.products_table.heading("prodname",text="Name")
        self.products_table.heading("price",text="Price")


        self.products_table["show"]="headings"
        self.products_table.column("ptype",width=150)       
        self.products_table.column("prodname",width=150)
        self.products_table.column("price",width=150)
        

#=============================get cursor function====================================================================#
        def get_cursor(events=""):
            cursor_row=self.products_table.focus()
            content=self.products_table.item(cursor_row)
            row=content["values"]
            
            self.var_ptype.set(row[0]),
            self.var_prodname.set(row[1]),
            self.var_price.set(row[2]),
 


        self.products_table.pack(fill=BOTH,expand=1)
        self.products_table.bind("<ButtonRelease-1>",get_cursor)
        fetch_data()
        

      


if __name__ == '__main__':
    root=Tk()
    obj=Bill(root)
    root.mainloop()


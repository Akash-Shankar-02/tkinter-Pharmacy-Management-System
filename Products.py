from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import pymysql
import random
from tkinter import messagebox

class products:
    def __init__(self,root):
        self.root=root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1530x800+0+0")

#=====================================variables==========================================#

        self.var_prodno=StringVar()
        x=random.randint(1000,9999)
        self.var_prodno.set(str(x))

        self.var_prodname=StringVar()
        self.var_mfgdate=StringVar()
        self.var_expdate=StringVar()
        self.var_price=StringVar()
        self.var_ptype=StringVar()
        self.var_qty=StringVar()

#======================================title=============================================#

        lbl_title=Label(self.root,text="ADD PRODUCT DETAILS",font=("times new roman",24,"bold"),bg="dark olive green",fg="white",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1370,height=100)

#=======================================logo==============================================#

        # img=Image.open(r"C:\Users\desksiruseri\Downloads/plogo2.jpg")
        img=Image.open(r"plogo.png")
        img=img.resize((150,150),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        lblimg=Label(self.root,image=self.photoimg,bd=4,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=100)

#==============================label frame================================================#

        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Product Information",font=("times new roman",18,"bold"),fg="white",bg="dark slate gray")
        labelframeleft.place(x=5,y=110,width=475,height=560)

#=============================Label and Entry=============================================#

    #Product number
        prodno=Label(labelframeleft,text="Product Number",font=("times new roman",15,"bold"),fg="white",bg="dark slate gray",padx=2,pady=6)
        prodno.grid(row=0,column=0,sticky=W)
        entry_no=ttk.Entry(labelframeleft,textvariable=self.var_prodno,font=("arial",15,"bold"),width=25)
        entry_no.grid(row=0,column=1)

    #Product name
        prodname=Label(labelframeleft,text="Product Name",font=("times new roman",15,"bold"),fg="white",bg="dark slate gray",padx=2,pady=6)
        prodname.grid(row=1,column=0,sticky=W)
        txtname=ttk.Entry(labelframeleft,textvariable=self.var_prodname,font=("arial",15,"bold"),width=25)
        txtname.grid(row=1,column=1)

    #manufacture date
        mfgdate=Label(labelframeleft,text="MFG Date",font=("times new roman",15,"bold"),fg="white",bg="dark slate gray",padx=2,pady=6)
        mfgdate.grid(row=2,column=0,sticky=W)
        txtmfgdate=ttk.Entry(labelframeleft,textvariable=self.var_mfgdate,font=("arial",15,"bold"),width=25)
        txtmfgdate.grid(row=2,column=1)

    #Expiry Date
        expdate=Label(labelframeleft,text="Expiry",font=("times new roman",15,"bold"),fg="white",bg="dark slate gray",padx=2,pady=6)
        expdate.grid(row=3,column=0,sticky=W)
        txtexpdate=ttk.Entry(labelframeleft,textvariable=self.var_expdate,font=("arial",15,"bold"),width=25)
        txtexpdate.grid(row=3,column=1)

    #price
        price=Label(labelframeleft,text="Price",font=("times new roman",15,"bold"),fg="white",bg="dark slate gray",padx=2,pady=6)
        price.grid(row=4,column=0,sticky=W)
        txtprice=ttk.Entry(labelframeleft,textvariable=self.var_price,font=("arial",15,"bold"),width=25)
        txtprice.grid(row=4,column=1)    

    #product type
        ptype=Label(labelframeleft,text="Product Type",font=("times new roman",15,"bold"),fg="white",bg="dark slate gray",padx=2,pady=6)
        ptype.grid(row=5,column=0,sticky=W)
        combo_ptype=ttk.Combobox(labelframeleft,textvariable=self.var_ptype,font=("arial",15,"bold"),width=25,state="readonly")
        combo_ptype['values']=("Select Type","Tablet","Tonic","Baby Product","Essential")
        combo_ptype.current(0)
        combo_ptype.grid(row=5,column=1,sticky=W)


#==========================================buttons======================================================#

        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        ####### add data function #######
        def add_data():
            if self.var_expdate.get()=="" or self.var_mfgdate.get()=="":
                messagebox.showerror("Error","All fields are required")
            else:
                try:
                    conn=pymysql.connect(host="localhost",user="root",password="akash",database="pms")
                    my_cursor=conn.cursor()
                    my_cursor.execute("insert into product values(%s,%s,%s,%s,%s,%s)",(
                                                                               self.var_prodno.get(),
                                                                               self.var_prodname.get(),
                                                                               self.var_mfgdate.get(),
                                                                               self.var_expdate.get(),
                                                                               self.var_price.get(),
                                                                               self.var_ptype.get(),

                                                                            ))
                    conn.commit()
                    fetch_data()
                    conn.close()
                    messagebox.showinfo("Success","product has been added",parent=self.root)
                except Exception as es:
                    messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)

        ####### add data function 2 #######
        def add_data2():
            if self.var_price.get()=="" or self.var_ptype.get()=="":
                messagebox.showerror("Error","All fields are required")
            else:
                conn=pymysql.connect(host="localhost",user="root",password="akash",database="pms")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into bill values(%s,%s,%s)",(
                                                                        self.var_ptype.get(),
                                                                        self.var_prodname.get(),
                                                                        self.var_price.get(),

                                                                ))
            conn.commit()
            fetch_data()
            conn.close()
            messagebox.showinfo("Success","product has been added to bill",parent=self.root)


        ############ fetch data function ################  
        def fetch_data():
            conn=pymysql.connect(host="localhost",user="root",password="akash",database="pms")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from product")
            rows=my_cursor.fetchall()
            if len(rows)!=0:
                self.products_table.delete(*self.products_table.get_children())
                for i in rows:
                    self.products_table.insert("",END,values=i)
                conn.commit()
            conn.close()

        ################# update function #################            
        def update():
            if self.var_price.get()=="":
                messagebox.showerror("Error","Please enter mobile number",parent=self.root)
            else:
                conn=pymysql.connect(host="localhost",user="root",password="akash",database="pms")
                my_cursor=conn.cursor()
                my_cursor.execute("update product set productname=%s,mfgdate=%s,expdate=%s,price=%s,ptype=%s where productno=%s",(
                                                                                                                                                                                                                                                                                
                                                                                                                                        self.var_prodname.get(),
                                                                                                                                        self.var_mfgdate.get(),
                                                                                                                                        self.var_expdate.get(),
                                                                                                                                        self.var_price.get(),
                                                                                                                                        self.var_ptype.get(),
                                                                                                                                        self.var_prodno.get()
                                                                                                                                              
                                                                                                                                    ))
            conn.commit()
            fetch_data()
            conn.close()
            messagebox.showinfo("Update","product details has been updated successfully")

        ################# update function 2 #################            
        def update2():
            if self.var_price.get()=="":
                messagebox.showerror("Error","Please enter mobile number",parent=self.root)
            else:
                conn=pymysql.connect(host="localhost",user="root",password="akash",database="pms")
                my_cursor=conn.cursor()
                my_cursor.execute("update bill set ptype=%s,price=%s where prodname=%s",(
                                                                                                                                                                                                                                                                                
                                                                                            self.var_ptype.get(),
                                                                                            self.var_price.get(),
                                                                                            self.var_prodname.get()
                                                                                                                                              
                                                                                        ))
            conn.commit()
            fetch_data()
            conn.close()
        
        ########### delete function ##########
        def mdelete():
            mdelete=messagebox.askyesno("Pharmacy Management System","Do you want to delete this product",parent=self.root)
            if mdelete>0:
                conn=pymysql.connect(host="localhost",user="root",password="akash",database="pms")
                my_cursor=conn.cursor()
                query="delete from product where productno=%s"
                value=(self.var_prodno.get(),)
                my_cursor.execute(query,value)
                
                messagebox.showinfo("deleted","product details has been deleted successfully")
            else:
                if not mdelete:
                    return
            conn.commit()
            fetch_data()
            conn.close()

        ########### delete function 2 ##########
        def mdelete2():
            mdelete2=messagebox.askyesno("Pharmacy Management System","Do you want to delete this product",parent=self.root)
            if mdelete2>0:
                conn=pymysql.connect(host="localhost",user="root",password="akash",database="pms")
                my_cursor=conn.cursor()
                query="delete from bill where prodname=%s"
                value=(self.var_prodname.get(),)
                my_cursor.execute(query,value)
                
                messagebox.showinfo("deleted","product details has been deleted from bill successfully")
            else:
                if not mdelete2:
                    return
            conn.commit()
            fetch_data()
            conn.close()

        ################# reset function #################
        def reset():
            #self.var_ref.set(""),
            self.var_prodname.set(""),
            self.var_mfgdate.set(""),
            self.var_expdate.set(""),
            self.var_price.set(""),
            self.var_ptype.set(""),

        
            x=random.randint(1000,9999)
            self.var_prodno.set(str(x))
           

        btn_add=Button(btn_frame,text="Add",command=lambda:[add_data(),add_data2()],font=("arial",11,"bold"),width=10,bg="green",fg="white")
        btn_add.grid(row=0,column=0,padx=1)

        btn_update=Button(btn_frame,text="Update",command=lambda:[update(),update2()],font=("arial",11,"bold"),width=10,bg="navy blue",fg="white")
        btn_update.grid(row=0,column=1,padx=1)

        btn_delete=Button(btn_frame,text="Delete",command=lambda:[mdelete(),mdelete2()],font=("arial",11,"bold"),width=10,bg="red",fg="white")
        btn_delete.grid(row=0,column=2,padx=1)

        btn_reset=Button(btn_frame,text="Reset",command=reset,font=("arial",11,"bold"),width=10,bg="black",fg="gold")
        btn_reset.grid(row=0,column=3,padx=1)

#=====================================table frame================================================#

        tableframe=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and Search System",font=("times new roman",18,"bold"),fg="white",bg="red4")
        tableframe.place(x=465,y=110,width=890,height=560)

        lblsearchby=Label(tableframe,font=("arial",12,"bold"),text="Search by",bg="black",fg="white")
        lblsearchby.grid(row=0,column=0,sticky=W)
        
        self.search_var=StringVar()
        combo_search=ttk.Combobox(tableframe,textvariable=self.search_var,font=("arial",12,"bold"),width=27,state="readonly")
        combo_search['value']=("productno","productname","type")
        combo_search.current(0)
        combo_search.grid(row=0,column=1)
        
        self.txtsearch=StringVar()
        searchtxt=ttk.Entry(tableframe,textvariable=self.txtsearch,width=29,font=("arial",11,"bold"))
        searchtxt.grid(row=0,column=2,padx=5)

        ############# search function #################

        def search():
            conn=pymysql.connect(host="localhost",user="root",password="akash",database="pms")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from product where "+str(self.search_var.get())+" = "+'"'+str(self.txtsearch.get())+'"')
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

        showall=Button(tableframe,text="Show All",command=fetch_data,font=("arial",11,"bold"),width=10,bg="gold",fg="black")
        showall.grid(row=0,column=4,padx=1)

#====================================show data table============================================#

        details_table=Frame(tableframe,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=880,height=470)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)
        self.products_table=ttk.Treeview(details_table,column=("prodno","prodname","mfgdate","expdate","price","ptype"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)        

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.products_table.xview)
        scroll_y.config(command=self.products_table.yview)

        self.products_table.heading("prodno",text="productno")
        self.products_table.heading("prodname",text="Name")
        self.products_table.heading("mfgdate",text="MFG Date")
        self.products_table.heading("expdate",text="Expiry Date")
        self.products_table.heading("price",text="Price")
        self.products_table.heading("ptype",text="Product Type")


        self.products_table["show"]="headings"

        self.products_table.column("prodno",width=150)
        self.products_table.column("prodname",width=150)
        self.products_table.column("mfgdate",width=150)
        self.products_table.column("expdate",width=150)
        self.products_table.column("price",width=150)
        self.products_table.column("ptype",width=150)


        

#=============================get cursor function====================================================================#
        def get_cursor(events=""):
            cursor_row=self.products_table.focus()
            content=self.products_table.item(cursor_row)
            row=content["values"]

            self.var_prodno.set(row[0]),
            self.var_prodname.set(row[1]),
            self.var_mfgdate.set(row[2]),
            self.var_expdate.set(row[3]),
            self.var_price.set(row[4]),
            self.var_ptype.set(row[5]),


        self.products_table.pack(fill=BOTH,expand=1)
        self.products_table.bind("<ButtonRelease-1>",get_cursor)
        fetch_data()
        



####################p##########################################################################################################################################################

if __name__ == "__main__":
    root=Tk()
    obj=products(root)
    root.mainloop()
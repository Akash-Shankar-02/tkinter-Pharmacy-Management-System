from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import pymysql
import random
from tkinter import messagebox

class Staff_win:
    def __init__(self,root):
        self.root=root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1530x800+0+0")

#=====================================variables==========================================#

        self.var_ref=StringVar()
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

        self.var_name=StringVar()
        self.var_mother=StringVar()
        self.var_gender=StringVar()
        self.var_postcode=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()

#======================================title=============================================#

        lbl_title=Label(self.root,text="ADD STAFF DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1400,height=120)

#=======================================logo==============================================#

        # img=Image.open(r"C:\Users\desksiruseri\Downloads/plogo2.jpg")
        img=Image.open(r"plogo.png")
        img=img.resize((175,175),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        lblimg=Label(self.root,image=self.photoimg,bd=4,relief=RIDGE)
        lblimg.place(x=5,y=2,width=120,height=120)

#==============================label frame================================================#

        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Staff Information",font=("times new roman",12,"bold"),fg="black",bg="light blue")
        labelframeleft.place(x=5,y=140,width=425,height=490)

#=============================Label and Entry=============================================#

    #staff ref
        ref=Label(labelframeleft,text="staff Ref",font=("times new roman",12,"bold"),fg="black",bg="light blue",padx=2,pady=6)
        ref.grid(row=0,column=0,sticky=W)
        entry_ref=ttk.Entry(labelframeleft,textvariable=self.var_ref,font=("arial",12,"bold"),width=29)
        entry_ref.grid(row=0,column=1)

    #staff name
        name=Label(labelframeleft,text="staff Name",font=("times new roman",12,"bold"),fg="black",bg="light blue",padx=2,pady=6)
        name.grid(row=1,column=0,sticky=W)
        txtname=ttk.Entry(labelframeleft,textvariable=self.var_name,font=("arial",12,"bold"),width=29)
        txtname.grid(row=1,column=1)

    #mother name
        mother=Label(labelframeleft,text="staff's Mother Name",font=("times new roman",12,"bold"),fg="black",bg="light blue",padx=2,pady=6)
        mother.grid(row=2,column=0,sticky=W)
        txtmname=ttk.Entry(labelframeleft,textvariable=self.var_mother,font=("arial",12,"bold"),width=29)
        txtmname.grid(row=2,column=1)

    #gender
        gender=Label(labelframeleft,text="Gender",font=("times new roman",12,"bold"),fg="black",bg="light blue",padx=2,pady=6)
        gender.grid(row=3,column=0,sticky=W)
        combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gender,font=("arial",12,"bold"),width=27,state="readonly")
        combo_gender['values']=("Select Gender","male","female")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1,sticky=W)

    #postcode
        postcode=Label(labelframeleft,text="Postcode",font=("times new roman",12,"bold"),fg="black",bg="light blue",padx=2,pady=6)
        postcode.grid(row=4,column=0,sticky=W)
        txtpcode=ttk.Entry(labelframeleft,textvariable=self.var_postcode,font=("arial",12,"bold"),width=29)
        txtpcode.grid(row=4,column=1)    

    #mobile
        mobile=Label(labelframeleft,text="Mobile No",font=("times new roman",12,"bold"),fg="black",bg="light blue",padx=2,pady=6)
        mobile.grid(row=5,column=0,sticky=W)
        txtmobile=ttk.Entry(labelframeleft,textvariable=self.var_mobile,font=("arial",12,"bold"),width=29)
        txtmobile.grid(row=5,column=1)

    #email
        email=Label(labelframeleft,text="Email",font=("times new roman",12,"bold"),fg="black",bg="light blue",padx=2,pady=6)
        email.grid(row=6,column=0,sticky=W)
        txtemail=ttk.Entry(labelframeleft,textvariable=self.var_email,font=("arial",12,"bold"),width=29)
        txtemail.grid(row=6,column=1)

    #Nationality
        nation=Label(labelframeleft,text="Nationality",font=("times new roman",12,"bold"),fg="black",bg="light blue",padx=2,pady=6)
        nation.grid(row=7,column=0,sticky=W)
        combo_nation=ttk.Combobox(labelframeleft,textvariable=self.var_nationality,font=("arial",12,"bold"),width=27,state="readonly")
        combo_nation['values']=("Select Nationality","Indian","Others")
        combo_nation.current(0)
        combo_nation.grid(row=7,column=1,sticky=W)

#==========================================buttons======================================================#

        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=400,width=412,height=40)

        ####### add data function #######
        def add_data():
            if self.var_mobile.get()=="" or self.var_mother.get()=="":
                messagebox.showerror("Error","All fields are required")
            else:
                try:
                    conn=pymysql.connect(host="localhost",user="root",password="akash",database="pms")
                    my_cursor=conn.cursor()
                    my_cursor.execute("insert into staff values(%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                               self.var_ref.get(),
                                                                               self.var_name.get(),
                                                                               self.var_mother.get(),
                                                                               self.var_gender.get(),
                                                                               self.var_postcode.get(),
                                                                               self.var_mobile.get(),
                                                                               self.var_email.get(),
                                                                               self.var_nationality.get()
                                                                            ))
                    conn.commit()
                    fetch_data()
                    conn.close()
                    messagebox.showinfo("Success","staff has been added",parent=self.root)
                except Exception as es:
                    messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)

        ############ fetch data function ###############
        def fetch_data():
            conn=pymysql.connect(host="localhost",user="root",password="akash",database="pms")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from staff")
            rows=my_cursor.fetchall()
            if len(rows)!=0:
                self.staff_details_table.delete(*self.staff_details_table.get_children())
                for i in rows:
                    self.staff_details_table.insert("",END,values=i)
                conn.commit()
            conn.close()

        ################# update function #################            
        def update():
            if self.var_mobile.get()=="":
                messagebox.showerror("Error","Please enter mobile number",parent=self.root)
            else:
                conn=pymysql.connect(host="localhost",user="root",password="akash",database="pms")
                my_cursor=conn.cursor()
                my_cursor.execute("update staff set Name=%s,Mother=%s,Gender=%s,Postcode=%s,Mobile=%s,Email=%s,Nationality=%s where Ref=%s",(
                                                                                                                                                                                                                                                                                
                                                                                                                                        self.var_name.get(),
                                                                                                                                        self.var_mother.get(),
                                                                                                                                        self.var_gender.get(),
                                                                                                                                        self.var_postcode.get(),
                                                                                                                                        self.var_mobile.get(),
                                                                                                                                        self.var_email.get(),
                                                                                                                                        self.var_nationality.get(),
                                                                                                                                        self.var_ref.get()
                                                                                                                                              
                                                                                                                                    ))
            conn.commit()
            fetch_data()
            conn.close()
            messagebox.showinfo("Update","Staff details has been updated successfully")


        ########### delete function ##########
        def mdelete():
            mdelete=messagebox.askyesno("Pharmacy Management System","Do you want to delete this customer",parent=self.root)
            if mdelete>0:
                conn=pymysql.connect(host="localhost",user="root",password="akash",database="pms")
                my_cursor=conn.cursor()
                query="delete from staff where ref=%s"
                value=(self.var_ref.get(),)
                my_cursor.execute(query,value)
            else:
                if not mdelete:
                    return
            conn.commit()
            fetch_data()
            conn.close()

        ################# reset function #################
        def reset():
            #self.var_ref.set(""),
            self.var_name.set(""),
            self.var_mother.set(""),
            #self.var_gender.set(""),
            self.var_postcode.set(""),
            self.var_mobile.set(""),
            self.var_email.set(""),
            #self.var_nationality.set("")
        
            x=random.randint(1000,9999)
            self.var_ref.set(str(x))
           

        btn_add=Button(btn_frame,text="Add",command=add_data,font=("arial",11,"bold"),width=10,bg="black",fg="gold")
        btn_add.grid(row=0,column=0,padx=1)

        btn_update=Button(btn_frame,text="Update",command=update,font=("arial",11,"bold"),width=10,bg="black",fg="gold")
        btn_update.grid(row=0,column=1,padx=1)

        btn_delete=Button(btn_frame,text="Delete",command=mdelete,font=("arial",11,"bold"),width=10,bg="black",fg="gold")
        btn_delete.grid(row=0,column=2,padx=1)

        btn_reset=Button(btn_frame,text="Reset",command=reset,font=("arial",11,"bold"),width=10,bg="black",fg="gold")
        btn_reset.grid(row=0,column=3,padx=1)

#=====================================table frame================================================#

        tableframe=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and Search System",font=("times new roman",12,"bold"),fg="black",bg="light green")
        tableframe.place(x=435,y=140,width=900,height=490)

        lblsearchby=Label(tableframe,font=("arial",12,"bold"),text="Search by",bg="red",fg="white")
        lblsearchby.grid(row=0,column=0,sticky=W)
        
        self.search_var=StringVar()
        combo_search=ttk.Combobox(tableframe,textvariable=self.search_var,font=("arial",12,"bold"),width=27,state="readonly")
        combo_search['value']=("ref","mobile")
        combo_search.current(0)
        combo_search.grid(row=0,column=1)
        
        self.txtsearch=StringVar()
        searchtxt=ttk.Entry(tableframe,textvariable=self.txtsearch,width=29,font=("arial",11,"bold"))
        searchtxt.grid(row=0,column=2,padx=5)

        ############# search function #################

        def search():
            conn=pymysql.connect(host="localhost",user="root",password="akash",database="pms")
            my_cursor=conn.cursor()
            my_cursor.execute("select * from staff where "+str(self.search_var.get())+" LIKE "+str(self.txtsearch.get()))
            rows=my_cursor.fetchall()
            if len(rows)!=0:
                self.staff_details_table.delete(*self.staff_details_table.get_children())
                for i in rows:
                    self.staff_details_table.insert("",END,values=i)
                conn.commit()
            conn.close()

        ################################################################################
        search=Button(tableframe,text="Search",command=search,font=("arial",11,"bold"),width=10,bg="black",fg="gold")
        search.grid(row=0,column=3,padx=1)

        showall=Button(tableframe,text="Show All",command=fetch_data,font=("arial",11,"bold"),width=10,bg="black",fg="gold")
        showall.grid(row=0,column=4,padx=1)

#====================================show data table============================================#

        details_table=Frame(tableframe,bd=2,relief=RIDGE)
        details_table.place(x=0,y=50,width=890,height=415)

        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)
        self.staff_details_table=ttk.Treeview(details_table,column=("ref","name","mother","gender","postcode","mobile","email","nationality"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)        

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.staff_details_table.xview)
        scroll_y.config(command=self.staff_details_table.yview)

        self.staff_details_table.heading("ref",text="Reference No")
        self.staff_details_table.heading("name",text="Name")
        self.staff_details_table.heading("mother",text="Mother Name")
        self.staff_details_table.heading("gender",text="Gender")
        self.staff_details_table.heading("postcode",text="Postcode")
        self.staff_details_table.heading("mobile",text="Mobile No")
        self.staff_details_table.heading("email",text="email")
        self.staff_details_table.heading("nationality",text="Nationality")

        self.staff_details_table["show"]="headings"

        self.staff_details_table.column("ref",width=100)
        self.staff_details_table.column("name",width=100)
        self.staff_details_table.column("mother",width=100)
        self.staff_details_table.column("gender",width=100)
        self.staff_details_table.column("postcode",width=100)
        self.staff_details_table.column("mobile",width=100)
        self.staff_details_table.column("email",width=100)
        self.staff_details_table.column("nationality",width=100)

        

#=============================get cursor function====================================================================#
        def get_cursor(events=""):
            cursor_row=self.staff_details_table.focus()
            content=self.staff_details_table.item(cursor_row)
            row=content["values"]

            self.var_ref.set(row[0]),
            self.var_name.set(row[1]),
            self.var_mother.set(row[2]),
            self.var_gender.set(row[3]),
            self.var_postcode.set(row[4]),
            self.var_mobile.set(row[5]),
            self.var_email.set(row[6]),
            self.var_nationality.set(row[7])


        self.staff_details_table.pack(fill=BOTH,expand=1)
        self.staff_details_table.bind("<ButtonRelease-1>",get_cursor)
        fetch_data()



###############################################################################################################################################################################

if __name__ == "__main__":
    root=Tk()
    obj=Staff_win(root)
    root.mainloop()
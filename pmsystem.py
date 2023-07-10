from tkinter import*
from PIL import Image,ImageTk
from Staff import Staff_win
from Products import products
from Bill import Bill

class PharmacyManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Pharmacy Management System")
        self.root.geometry("1550x800+0+0")

#============================logo=========================================================#

        # img=Image.open(r"C:\Users\desksiruseri\Downloads/plogo2.jpg")
        img=Image.open(r"plogo.png")
        img=img.resize((280,350),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        lblimg=Label(self.root,image=self.photoimg,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=300,height=300)

#==============================title=====================================================#

        lbl_title=Label(self.root,text="Pharmacy Management System",font=("times new roman",40,"bold"),fg="black",bg="white",bd=4,relief=RIDGE)
        lbl_title.place(x=301,y=10,width=1225,height=80)

#=============================main frame=================================================#
            
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=301,width=1520,height=500)

#=============================main frame2=================================================#
            
        main_frame2=Frame(self.root,bd=4,relief=RIDGE)
        main_frame2.place(x=301,y=120,width=1200,height=120)

#==============================button frame==============================================#

        btn_frame=Frame(main_frame2,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=10,width=1180,height=90)

        def staff_details():
               self.newWindow = Toplevel(self.root)
               self.app=Staff_win(self.newWindow)

        def productswin():
                self.newWindow = Toplevel(self.root)
                self.app=products(self.newWindow)

        def billwin():
                self.newWindow = Toplevel(self.root)
                self.app=Bill(self.newWindow)       

        staff_btn=Button(btn_frame,command=staff_details,text="STAFF",width=20,font=("times new roman",14,"bold"),fg="black",bg="gold",bd=4,cursor="hand1")
        staff_btn.place(x=10,y=10,width=200,height=50)

        bill_btn=Button(btn_frame,command=billwin,text="BILL",width=20,font=("times new roman",14,"bold"),fg="black",bg="gold",bd=4,cursor="hand1")
        bill_btn.place(x=270,y=10,width=200,height=50)

        products_btn=Button(btn_frame,command=productswin,text="PRODUCTS",width=20,font=("times new roman",14,"bold"),fg="black",bg="gold",bd=4,cursor="hand1")
        products_btn.place(x=540,y=10,width=200,height=50)        

        report_btn=Button(btn_frame,text="REPORT",width=20,font=("times new roman",14,"bold"),fg="black",bg="gold",bd=4,cursor="hand1")
        report_btn.place(x=810,y=10,width=200,height=50)

#==============================right image========================================================#

        # img2=Image.open(r"C:\Users\desksiruseri\Downloads/pharm.jpg")
        img2=Image.open(r"main.png")
        img2=img2.resize((1500,480),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg2=Label(main_frame,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg2.place(x=0,y=0,width=1500,height=480)

#==================================================================================================#



if __name__=="__main__":
    root=Tk()
    obj=PharmacyManagementSystem(root)
    root.mainloop()
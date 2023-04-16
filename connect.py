from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox 
import mysql.connector
from PIL import Image, ImageTk,ImageSequence

con=mysql.connector.connect(host="localhost",user="root",passwd="0000",database="python")
rootp=Tk()
rootp.title("AIRPORT MANGEMENT SYSTEM")
rootp.geometry("1300x800")
Label(rootp,text="Welcome To Airline Booking System",font="jokerman 33 bold",fg="red",bg="black",relief=SUNKEN).pack()
f0=Frame(rootp,width=900,height=200)
image=Image.open(r"C:\\Users\\rosha\\Desktop\\Projects\\Airline Mangement System\\5.jpg")
image=image.resize((600,220),Image.ANTIALIAS)
photo=ImageTk.PhotoImage(image)
photo_label=Label(f0,image=photo).pack()
f0.pack(padx=22,pady=22)



def fun8():
    root2=Toplevel()
    root2.title("CANCELLATION SYSTEM")
    root2.geometry("1300x800")
    Label(root2,text="Welcome To our Cancellation System",font="jokerman 33 bold",fg="red").pack()
    f2=Frame(root2,width=100,height=15)
    image=Image.open(r"C:\\Users\\rosha\\Desktop\\Projects\\Airline Mangement System\\3.jpg")
    image=image.resize((400,200),Image.ANTIALIAS)
    photo=ImageTk.PhotoImage(image)
    photo_label=Label(root2,image=photo).pack()
    f2.pack()
    
    Label(root2,text="Enter last 4 digit of your Citizenship Number",font="lucida 20 bold").pack()
    e1=Entry(root2)
    e1.pack()
    Label(root2,text="Choose your class",font="lucida 20 bold").pack()
    w2=Combobox(root2,height=5,width=17,values=["BusinessClass","Economic"])
    w2.pack()
    Label(root2,text="select boarding",font="lucida 20 bold").pack()
    w3=Combobox(root2,height=5,width=17,values=["LUCKNOW","DELHI","MUMBAI","CHENNAI"])
    w3.pack()
    def fun2():
        d=e1.get()
        b=w2.get()
        c=w3.get()
        cur=con.cursor()
        x=str(d)
        y=str(c)
        con.commit()
        if d=='' or b=='' or c=='':
             messagebox.showerror("Oops","You can't Enter the leave any field empty")
        else:     
             if b=="Economic":
                 cur.execute("select * from Economic2")
                 messagebox.showinfo("your reservation is cancelled",cur.fetchall())
                 cur.execute("delete from Economic2 where adno='%s' and boarding='%s'"%(d,c))
                 con.commit()
             else:
                 cur.execute("select * from Business2")
                 messagebox.showinfo("your reservation is cancelled",cur.fetchall())
                 cur.execute("delete from Business2 where adno='%s' and boarding='%s'"%(d,c))
                 con.commit()
                
        
                    
            
    Bc=Button(root2,text="Cancel Reservation",font="lucida 15",command=fun2).pack()
    root2.mainloop()
def fun9():
    
    root4=Toplevel()
    root4.title("SEARCH FLIGHT")
    root4.geometry("1300x800")
    Label(root4,text="Welcome To Searching System",font="jokerman 33 bold",fg="red").pack()
    f1=Frame(root4,width=100,height=15)
    image=Image.open(r"C:\\Users\\rosha\\Desktop\\Projects\\Airline Mangement System\\2.jpg")
    image=image.resize((500,250),Image.ANTIALIAS)
    photo=ImageTk.PhotoImage(image)
    photo_label=Label(root4,image=photo).pack()
    f1.pack()
    Label(root4,text="Enter Boarding",font="lucida 15 bold").pack()
    w1=Combobox(root4,height=5,width=15,values=["LUCKNOW","DELHI","MUMBAI","CHENNAI"])
    w1.pack()
    Label(root4,text="select destination",font="lucida 15 bold").pack()
    w2=Combobox(root4,height=5,width=15,values=["LUCKNOW","DELHI","MUMBAI","CHENNAI"])
    w2.pack()
    # Label(root4,text="Choose day of travel",font="lucida 15 bold").pack()
    # w3=Combobox(root4,height=5,width=15,values=["sunday","monday","tuesday","wednesday","thursday","friday","saturday"])
    # w3.pack()
    #Label(root4,text="choose time of your flight",font="lucida 15 bold").pack()
    #w4=Combobox(root4,height=5,width=15,values=["1:00","7:00","13:00","16:00","21:00"])
    #w4.pack()
    #Label(root4,text='Choose Class',font="lucida 15 bold").pack()
    #w5=Combobox(root4,height=5,width=15,values=["BusinessClass","Economic"])
    #w5.pack()
    #Label(root4,text='Set fair range',font="lucida 15 bold").pack()
    #w6=Combobox(root4,height=5,width=15,values=["2500","3500","4000","5500"])
    #w6.pack()
    
    def fun10():
        a=w1.get()
        b=w2.get()
        # c=w3.get()
        #d=w4.get()
        #e=w5.get()
        #f=w6.get()
        cur=con.cursor()
        if a=='' or b=='':
            messagebox.showerror("Error","Cant leave any field empty")
           
                
        else:
             if a!=b:
                 con.commit()
                 cur.execute("select * from eco where boarding='%s' and destination='%s' " %(a,b))
                 e1=cur.fetchall()
                 if e1==[]:
                     messagebox.showerror("flights are not availble")
                 else:
                     messagebox.showinfo("flights availble are ",e1)

             else:
                messagebox.showerror("Oops","boarding and destination can't me same")
        
    Bs=Button(root4,text="search",font="lucida 12",command=fun10).pack()
    root4.mainloop()
def fun5():
    root5=Toplevel()
    root5.title('FLIGHT BOOKING')
    root5.geometry("1300x800")

    Label(root5,text="Welcome To Our Flight Search And Booking System",font="jokerman 33 bold",fg="red").pack()
    f3=Frame(root5,width=100,height=15)
    image=Image.open(r"C:\\Users\\rosha\\Desktop\\Projects\\Airline Mangement System\\4.jpg")
    image=image.resize((400,200),Image.ANTIALIAS)
    photo=ImageTk.PhotoImage(image)
    photo_label=Label(root5,image=photo).pack()
    f3.pack()
    
    Label(root5,text="Enter Boarding",font="lucida 15 bold").pack()
    w=Combobox(root5,height=5,width=15,values=["MUMBAI","DELHI","LUCKNOW","CHENNAI"])
    w.pack()
    Label(root5,text='Enter Destination',font="lucida 15 bold").pack()
    w1=Combobox(root5,height=5,width=15,values=["MUMBAI","DELHI","LUCKNOW","CHENNAI"])
    w1.pack()
    Label(root5,text='Enter last 4 digit of your Citizenship Number',font="lucida 15 bold").pack()
    e=Entry(root5)
    e.pack()
    Label(root5,text='Choose Class',font="lucida 15 bold").pack()
    w2=Combobox(root5,text='Class',height=5,width=15,values=["BusinessClass","Economic"])
    w2.pack()
    Label(root5,text="Choose day of travel",font="lucida 15 bold").pack()
    w3=Combobox(root5,text="choose day",height=5,width=15,values=["sunday","monday","tuesday","wednesday","thursday","friday","saturday"])
    w3.pack()
    Label(root5,text="choose time of your flight",font="lucida 15 bold").pack()
    w4=Combobox(root5,height=5,width=15,values=["1:00","7:00","13:00","16:00","21:00"])
    w4.pack()
    Label(root5,text="Set fair range",font="lucida 15 bold").pack()
    w5=Combobox(root5,height=5,width=15,values=["2500","3500","4000","5500"])
    w5.pack()
    
    def fun():
        a=w.get()
        b=w1.get()
        c=e.get()
        d=w2.get()
        e4=w3.get()
        f=w4.get()
        g=w5.get()
        f1=str(f)
        x=(a,b,c,e4,f1,g)
        cur=con.cursor()
        
        if a=='' or b=='' or c=='' or d=='' or e4=='' or f1=='' or g=='':
            messagebox.showerror("OOPS","you can't leave any field empty")
        else :
            if d=='Economic':
                
                if a!=b:
                    #cur.execute("create table Economic2(boarding char(20),destination char(20),adno integer,day char(20),time char(30),fare integer)")
                    cur.execute("insert into Economic2 values(%s,%s,%s,%s,%s,%s)",x)
                    con.commit()
                    messagebox.showinfo("congrats","your seat has been reserved")
                    
                    cur.execute("select * from Economic2 where adno='%s'" %(c))
                    messagebox.showinfo("records",cur.fetchall())
                else:
                    messagebox.showerror("Error","you can't choose same city")
            if d=='BusinessClass':
                #cur.execute("create table Business2(boarding char(20),destination char(20),adno integer,day char(20),time char(30),fare integer)")
                if a!=b:
                    
                    cur.execute("insert into Business2 values(%s,%s,%s,%s,%s,%s)",x)
                    messagebox.showinfo("congrats","your seat has been reserved")
                    con.commit()
                    cur.execute("select * from Business2 where adno='%s'" %(c))
                    messagebox.showinfo("records",cur.fetchall())
                else :
                    messagebox.showerror("Error","you can't choose same city")
    #slider_1=Scale(root,orient=HORIZONTAL,length=300,sliderlength=20,from_=1000,to=6000).pack()
    Bi=Button(root5,text="Insert",command=fun,font="lucida 15").pack()
    #Bo=Button(root,text="See Flights",command=dis).pack()
    #Bf=Button(root,text='Set fair range',command=fun1).pack()
    root5.mainloop()
    

B1=Button(rootp,text="Search Flight",height=4,width=35,font="lucida 15 bold",bg="gray",command=fun9).pack()
B2=Button(rootp,text="Book Flight",height=4,width=35,font="lucida 15 bold",bg="gray",command=fun5).pack()
B3=Button(rootp,text="Cancel Booking",height=4,width=35,font="lucida 15 bold",bg="gray",command=fun8).pack()


rootp.mainloop()
    

from tkinter import *
import time
import csv
import socket
from email.message import EmailMessage
import smtplib
import os
from os import path
import random
import math
from tkinter import *
import tkinter.font as font
from PIL import ImageTk,Image

f='u.csv'
k=0
tempu=''
cl=1
def opyy():
    if cinternet()==1:
        import mailreader as re
        e=re.e()
        m=e
        c=[]
        p=[]
        for i in e:
            if len(i)!=4:
                e.remove(i)
            l=[]
            for j in m:
                if i[0]==j[0] and i[2]==j[2]:
                    l.append(j)
            c.append(l[-1])
        c.sort()
        for x in range(0,len(c)-1):
            if c[x]!=c[x+1]:
                p.append(c[x])
                if c[-1] not in p:
                    p.append(c[-1])
        fil=open(f,'r')
        r=csv.reader(fil)
        fil.close()
        updates(p)
        
def loggedin(u):
    def lkk():
        ggg(u)
    def rkk():
        opyy()
        m.destroy()
        scoreboard(u)
    def scobd():
        m.destroy()
        controls(u)
    def sd():
        m.destroy()
        login()
    
        
    m=Tk()
    m.geometry('800x400')
    m.resizable(False, False)
    m.title('the hungry snake')
    canvas = Canvas(m, width = 800, height = 400)
    canvas.pack()
    img = ImageTk.PhotoImage(Image.open("mainmenu.png"))
    canvas.create_image(0, 0, anchor=NW, image=img)
    Button(text="play",bg='violet',activebackground='pink'
           ,activeforeground='black',height="3", width="30"
           ,command=lkk).place(x=170,y=100)
    Button(text="scoreboard",bg='violet',activebackground='pink'
           ,activeforeground='black', height="3",width="30"
           ,command=rkk).place(x=170,y=170)
    Button(text="controls",bg='violet',activebackground='pink'
           ,activeforeground='black', height="3",width="30"
           ,command=scobd).place(x=170,y=240)
    Button(text="back", bg='violet',activebackground='pink'
           ,activeforeground='black',height="3",width="30"
           ,command=sd).place(x=170,y=310)
    m.mainloop()
    






def ggg(u):
    global cl
    def score(s):
        global cl
        us=[]
        k=0
        content=[]
        file=open(f,'r')
        c=csv.reader(file)
        for i in c:
            if s[1]==i[0]:
                if s[0]>int(i[3]):
                    k=1
                    i[3]=str(s[0])
                    us=i
            content.append(i)
        file.close()
        if k==1:
            updates(content)
            if len(us)==4:
                if send("mr.mistakie@gmail.com",str(us),0) == 0:
                    print('connect to internet')
    global tempu
    import thedothuntergame as sgt
    score(sgt.themaingame(u,cl))

if path.exists(f)==False:
    zzz=open(f,'w',newline='')
    zzz.close()
def chcsvw(c,r,ll,p):
    if ll==0:
        fil=open(f,'w',newline='')
        w=csv.writer(fil)
        for ii in c:
            w.writerow(ii)
        fil.close()
        
        
    
def chcsv(u,p,e,s):
    global f
    fil=open(f,'r')
    r=csv.reader(fil)
    temp=0
    temp2=''
    temp4=0
    sco=[]
    c=[]
    if s==0:
        
        for i in r:
            if len(i)>0 and i[2]==u:
                temp4=1
        return temp4
    
    if s==1:
        for i in r:
            if len(i)>0 and i[0]==u:                
                if i[1]==p:
                    return (0)
                else:
                    return (1)
    if s==2: 
        c=[]
        e=u
        us=[]
        for i in r:
            if len(i)>0 and i[0]==e:
                i[1]=p
                us=i
            c.append(i)
        fil.close()
        sendmail('mr.mistakie@gmail.com',str(us))
        updates(c)
    if s==3:
        for i in r:
            if i[0]==u:
                temp2= i[2]
        return temp2
    if s==4:
        for i in r:
            if len(i)>0:
                if i[0]==u:
                    temp4=1
        return temp4
    if s==5:
        for i in r:
            c.append(i)
        return(c)
            
    
def genotp():
    d='0123456789'
    k=''
    for i in range(4):
        l=d[math.floor(random.random()*10)]
        k=k+l
    return k


def sendmail(k,o):
    m = EmailMessage()
    m["From"] = "mr.mistakie@gmail.com"
    m["Subject"] = "DOTHUNTER REGISTRATION OTP"
    m["To"] = k
    m.set_content(o)
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()
    s.login('mr.mistakie', 'simplepass')
    s.send_message(m)
def updates(c):
    file=open(f,'w',newline='')
    w=csv.writer(file)
    for i in c:
        w.writerow(i)
    file.close()

def cinternet():
    n=0
    ipa=socket.gethostbyname(socket.gethostname())
    if ipa=='127.0.0.1':
        n=0
    else:
        n=1
    return n

def send(k,o,l):
    if l==1:
        if cinternet()==1:
            sendmail(k,f'Your OTP is:\n{o}\n\nTHANKYOU FOR CHOOSING OUR GAME,\nhope you enjoy it!!!')
            return 1
        else:
            return 0
    else:
        if cinternet()==1:
            sendmail(k,o)
            return 1
        else:
            return 0
        
k=0
def regup(upe):
    def regupback():
        global k
        m.destroy()
        k=0
        reg()
    def regupok():
        global k
        u= tu.get()
        p= tp.get()
        if chcsv(u,0,0,4)==1 :
            if k==0:
                Label(text="username already taken", bg="white"
                      ,fg='red', width="30", height="2"
                      , font=("Calibri", 10)).place(x=180,y=190)
                k+=1
        if chcsv(u,0,0,4)!=1 and len(u)!=0 and len(p)!=0:
            upe[0],upe[1]=u,p
            u=str(upe)
            sendmail('dothunter.inc@gmail.com',u)
            regcsv(upe,m)
            k=0
            
    
    m=Tk()
    m.geometry('800x400')
    m.resizable(False, False)
    canvas = Canvas(m, width = 800, height = 400)
    canvas.place(x=0,y=0)
    img = ImageTk.PhotoImage(Image.open("regn.png"))
    canvas.create_image(0, 0, anchor=NW, image=img)
    m.title('registering site page 2')
    tu=Entry(width =40)
    tu.place(x=170,y=114)
    tp = Entry( width = 40,show='*')
    tp.place(x=170,y=162)
    
    Button(text="ok", height="2",width="10",bg='violet'
           ,activebackground='pink',activeforeground='black'
           ,command=regupok).place(x=200,y=230)
    Button(text="Back", height="2", width="10",bg='violet'
           ,activebackground='pink',activeforeground='black'
           ,command=regupback).place(x=200,y=290)
    m.mainloop()
    

        

        

k=0
def opt(mm,o,k,mot):
    
    def otpcheck():
        if o==top.get():
            m.destroy()
            regup(k)
    def t():
        o=genotp()
        opt(mm,o,k,m)
    def ore ():
        t()
    tm=send(mm,o,1)   
    mot.destroy()
    def BCK():
        m.destroy()
        reg()

    if tm==1:
        m=Tk()
        cc="Enter OTP\n Sent to\n "+k[2]
        m.geometry('400x400')
        m.title('otP')
        canvas = Canvas(m, width = 500, height = 400)
        canvas.place(x=-1,y=0)
        img = ImageTk.PhotoImage(Image.open("sml.png"))
        canvas.create_image(0, 0, anchor=NW, image=img)
        m.resizable(False, False)
        Label(text=cc, bg="violet", width="300", height="3", font=("Calibri", 15)).pack() 
        top = Entry(width = 20)
        top.place(x=140,y=100)
        b12op=Button(text="Done", height="3", width="30",bg='violet'
                     ,activebackground='pink',activeforeground='white'
                     ,command=otpcheck)
        b12op.place(x=90,y=150)
        b12dop=Button(text="Resend", height="3", width="30",bg='violet'
                      ,activebackground='pink',activeforeground='white'
                      ,command=ore)
        b12dop.place(x=90,y=220)
        b12bop=Button(text="Back", height="3", width="30",bg='violet'
                      ,activebackground='pink',activeforeground='white'
                      ,command=BCK)
        b12bop.place(x=90,y=290)
        m.mainloop()
    if tm==0:
        def bk():
            m.destroy()
            reg()
        m=Tk()
        m.geometry('400x400')
        m.resizable(False, False)
        m.title('connect to inter net')
        Label(text="your are offline", bg="green", width="300", height="2"
              , font=("Calibri", 13)).pack() 
        Label(text="").pack()
        fu=Frame(m)
        fu.pack(pady=8)
        Label(fu,text="connect to internet and then click 'back' button"
              , height="5", width="300",font=("Calibri", 13)).pack()
        Button(text="back", height="2",width="10",command=bk).pack(pady=8)
    

def reg():
    k=0
    def regback():
        global k
        m.destroy()
        k=0
        main()
    def gop(mn,o,upe):
        opt(mn,o,upe,m)
    
    def itcr():
        global k
        e = te.get()
        if chcsv(e,0,0,0)!=0:
            k+=1
        return k
    def op():
        if len(te.get())>6:
            opyy()
            regotp()
                            
    def regotp():
        e= te.get()
        
        if chcsv(e,0,0,0)==1:
            if itcr()==1:
                Label(text="email already used", bg="white",fg='red'
                      , width="30", height="2", font=("Calibri", 10)).place(x=220,y=165)
        else:
            if '@' in e and (".com" in e or '.in' in e) :
                if len(e)>5 :
                    o=genotp()
                    upe=[0,0,e,0]
                    gop(e,o,upe)
    t=0
    m=Tk()
    m.geometry('800x400')
    m.resizable(False, False)
    m.title('registering site page')
    canvas = Canvas(m, width = 800, height = 400)
    canvas.pack()
    img = ImageTk.PhotoImage(Image.open("rege.png"))
    canvas.create_image(0, 0, anchor=NW, image=img)
    te = Entry(width = 50)
    te.place(x=200,y=134)
    Button(text="Get otp",bg='violet',activebackground='pink'
           ,activeforeground='black', height="2",width="16"
           ,command=op).place(x=240,y=215)
    Button(text="Back",bg='violet',activebackground='pink'
           ,activeforeground='black', height="2", width="16"
           ,command=regback).place(x=70,y=215)
    m.mainloop()

def regcsv(k,m):
    def mo(m):
        opyy()
        m.destroy()
        main()
    with open(f,'a',newline='') as c:
        w=csv.writer(c)
        w.writerow(k)
        c.close()
        mo(m)
def passc(u):
    def gg():
        m.destroy()
        loggedin(u)
    def kk():
        z=t.get()
        chcsv(u,z,0,2)
        
        gg()
    m=Tk()
    m.geometry('800x400')
    m.resizable(False, False)
    m.title('change password site')
    Label(text="change password", bg="violet", width="300"
          , height="2", font=("Calibri", 18)).pack()     
    canvas = Canvas(m, width = 800, height = 400)
    canvas.pack()
    img = ImageTk.PhotoImage(Image.open("chnp.png"))
    canvas.create_image(0, 0, anchor=NW, image=img)

    
    t = Entry(width = 40,show='*')
    t.place(x=340,y=120)
    t1 = Entry(width = 40,show='*')
    t1.place(x=340,y=170)
    Button(text="change password", height="2",width="15",bg='violet'
           ,activebackground='pink',activeforeground='white'
           ,command=kk).place(x=310,y=240)
    Button(text="skip", height="2", width="15",bg='violet'
           ,activebackground='pink',activeforeground='white'
           ,command=gg).place(x=310,y=300)
    m.mainloop()
    
def otpfp(O,u):
    def ll():
        m.destroy()
        passc(u)
    def otpchf():
        if O==top.get():
            ll()
    def kk():
        m.destroy()
        forgotpass()

    m=Tk()
    m.geometry('400x400')
    m.resizable(False, False)
    m.title('otp')
    canvas = Canvas(m, width = 500, height = 400)
    canvas.place(x=-1,y=0)
    img = ImageTk.PhotoImage(Image.open("sml.png"))
    canvas.create_image(0, 0, anchor=NW, image=img)
    Label(text="Enter OTP", bg="purple", width="300", height="2", font=("Calibri", 18)).pack() 
    top = Entry(width = 20)
    top.place(x=140,y=100)
    b12op=Button(text="Done", height="3", width="30",bg='violet'
                 ,activebackground='pink',activeforeground='white'
                 ,command=otpchf)
    b12op.place(x=90,y=150)    
    b13op=Button(text="Back", height="3", width="30",bg='violet'
                 ,activebackground='pink',activeforeground='white'
                 ,command=kk)
    b13op.place(x=90,y=220)
    m.mainloop()
    

def forgotpass():
    def blog():
        m.destroy()
        login()
    def goo(n,u):
        m.destroy()
        otpfp(n,u)
    def nin():
        def bk():
            m.destroy()
            forgotpass()
        m=Tk()
        m.geometry('400x400')
        m.resizable(False, False)
        m.title('connect to inter net')
        Label(text="your are offline", bg="green", width="300"
              , height="2", font=("Calibri", 13)).pack() 
        Label(text="").pack()
        fu=Frame(m)
        fu.pack(pady=8)
        Label(fu,text="connect to internet and then click 'back' button",
              height="5", width="300",font=("Calibri", 13)).pack()
        Button(text="back", height="2",width="10",
               command=bk).pack(pady=8)
    
    def fpfemail():
        u=t.get()
        if len(u)>0:
            if chcsv(u,0,0,3)!='':
                fpo=genotp()
                if send(chcsv(u,0,0,3),fpo,1)==1:
                    goo(fpo,u)
                else:
                    m.destroy()
                    nin()
            else:
                Label(text="no username found", bg="white"
                      ,fg='red', width="30", height="2",
                      font=("Calibri", 10)).place(x=100,y=140)
            
        
        
    m=Tk()
    m.geometry('400x400')
    m.resizable(False, False)
    m.title('FORGOT PASSWORD')
    canvas = Canvas(m, width = 400, height = 400)
    canvas.place(x=-1,y=0)
    img = ImageTk.PhotoImage(Image.open("sml.png"))
    canvas.create_image(0, 0, anchor=NW, image=img)
    Label(text="ENTER YOUR USERNAME", fg='black',bg="purple",
          width="300", height="2", font=("Calibri", 18)).pack()
    t = Entry( width = 40)
    t.place(x=80,y=100)
    Button(text="send otp to mail", height="2",width="15",bg='violet'
           ,fg='black',activebackground='pink',activeforeground='white'
           ,command=fpfemail).place(x=150,y=190)
    Button(text="Back", height="2", width="15",bg='violet',fg='black',
           activebackground='pink',activeforeground='white',
           command=blog).place(x=150,y=250)    
    m.mainloop()    

def login():
    global K
    def fpotp():
        m.destroy()
        forgotpass()
        
    
    def lmk():
        global k
        m.destroy()
        main()
    def oii():
        m.destroy()
        loggedin()
    

    def itc():
        global k
        p = t1.get()
        u=t.get()
        if chcsv(u,p,0,1)!=0:
            k+=1
        return k
    def it():
        p= t1.get()
        u=t.get()
        if len(p)>0 and len(u)>0:
            opyy()            
            if chcsv(u,p,0,1)==0:
                m.destroy()
                loggedin(u)
            else:
                Label(text="wrong username or password", bg="white"
                      ,fg='red', width="30", height="2",
                      font=("Calibri", 10)).place(x=155,y=220)
    
    m=Tk()
    m.resizable(False, False)
    m.geometry('800x400')
    m.title('login page')
    canvas = Canvas(m, width = 800, height = 400)
    canvas.pack()
    img = ImageTk.PhotoImage(Image.open("loginn.png"))
    canvas.create_image(0, 0, anchor=NW, image=img)
    t = Entry(width = 40)
    t.place(x=175,y=107)
    
    t1 = Entry(width = 40,show='*')
    t1.place(x=175,y=154)
    Button(text="Forgot password", height="1",width="15",bg='violet'
           ,fg='red',activebackground='pink',activeforeground='white'
           ,command=fpotp).place(x=175,y=184) 
    Button(text="login", height="2",width="15",bg='violet',
           activebackground='pink',activeforeground='white',
           command=it).place(x=155,y=270)
    Button(text="Back", height="2", width="15",bg='violet',
           activebackground='pink',activeforeground='white'
           ,command=lmk).place(x=155,y=330)
    m.mainloop()
def scoreboard(u):
    def sbbck():
        m.destroy()
        loggedin(u)
    def order(n):
        h=len(n)
        for j in range(0,20):
            for i in range(0,h-1):
                if int(n[i][1])<int(n[i+1][1]):
                    n[i],n[i+1]=n[i+1],n[i]
        return n
    s=chcsv(0,0,0,5)
    for i in s:
        i.remove(i[1])
        i.remove(i[1])
    v=order(s)
    m=Tk()
    m.geometry('800x400')
    m.resizable(False, False)
    canvas = Canvas(m, width = 800, height = 400)
    canvas.pack()
    img = ImageTk.PhotoImage(Image.open("1.png"))
    canvas.create_image(0, 0, anchor=NW, image=img)
    m.title('scoreboard')
    p=0
    pp=1
    for i in v:
        Label(text=str(pp) ,bg='violet',font=20).place(x=50,y=130+p)
        Label(text=i[0] ,bg='violet',font=20).place(x=320,y=130+p)
        Label(text=i[1],bg='violet',font=20).place(x=650,y=130+p)
        if pp>=4:
            break

        pp+=1
        p+=40
    Button(text="back", height="3", width="30",bg='purple',
           activebackground='pink',activeforeground='black'
           ,command=sbbck).place(x=300,y=300)
    m.mainloop()

def controls(u):
    global cl
    def no():
        global cl
        if cl==1:
            cl=0
        else:
            cl=1
        m.destroy()
        controls(u)
    def ccck():
        global cl
        m.destroy()
        loggedin(u)
    
    m = Tk()
    m.geometry('800x400')
    m.resizable(False, False)
    m.title('login page')
    canvas = Canvas(m, width = 820, height = 440)
    canvas.place(x=-20,y=-20)
    if cl==0:
        img = ImageTk.PhotoImage(Image.open("wasd.png"))
        canvas.create_image(20, 20, anchor=NW, image=img)
        b1=Button(text="ARROY", height="3", width="30",bg='violet',
                  activebackground='pink',activeforeground='black',
                  command=no)
        b1.place(x=370,y=320)
        Button(text="back", height="3", width="30",bg='violet',
               activebackground='pink',activeforeground='black',
               command=ccck).place(x=130,y=320)
        m.mainloop()
    else:
        img = ImageTk.PhotoImage(Image.open("arrow.png"))
        canvas.create_image(20, 20, anchor=NW, image=img)
        b1=Button(text="WASD", height="3", width="30",bg='violet',
                  activebackground='pink',activeforeground='black',
                  command=no)
        b1.place(x=370,y=320)
        Button(text="back", height="3", width="30",bg='violet',
               activebackground='pink',activeforeground='black',
               command=ccck).place(x=130,y=320)
        m.mainloop()
        

    
    
def main():
    def l():
        m.destroy()
        login()
    def r():
        m.destroy()
        reg()
    m=Tk()
    m.resizable(False, False)
    m.geometry('800x400')
    m.title('login page')
    canvas = Canvas(m, width = 800, height = 400)
    canvas.pack()
    img = ImageTk.PhotoImage(Image.open("main.png"))
    canvas.create_image(0, 0, anchor=NW, image=img)
    Button(text="Login", height="3", width="30",bg='violet',
           activebackground='pink',activeforeground='black',
           command=l).place( x=60, y=130)
    Button(text="Register", height="3",width="30",bg='violet',
           activebackground='pink',activeforeground='black',
           command=r).place( x=60, y=200)
    m.mainloop()

main()
    






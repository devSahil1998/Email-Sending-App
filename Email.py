from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from smtplib import SMTP,SMTPAuthenticationError
from tkinter import *
from tkinter import ttk,messagebox

def bindmethod(num):
    if num==1:
        Gui.entry2.config(show='')
    elif num==2:
        Gui.entry2.config(show='*')
    elif num==3:
        if Gui.entry4.instate(['!disabled']):
            Gui.entry4.state(['disabled'])
        else:
            Gui.entry4.state(['!disabled'])
            Gui.entry5.state(['disabled'])
    elif num==4:
        if Gui.entry5.instate(['!disabled']):
            Gui.entry5.state(['disabled'])
        else:
            Gui.entry5.state(['!disabled'])
            Gui.entry4.state(['disabled'])

def send():
    if Gui.entry4.instate(['!disabled']):
        try:
            email_conn.sendmail(Gui.entry3.get(),Gui.entry4.get(),Gui.textbox.get('1.0','end'))
        except:
            messagebox.showerror(title='ERROR',message='An Error Occurred Please Try Again Later Sometime.')
            return None
    elif Gui.entry5.instate(['!disabled']):
        temp_text=Gui.entry5.get(); alist=temp_text.split(' ')
        for mail in alist:
            try:
                email_conn.sendmail(Gui.entry3.get(),mail,Gui.textbox.get('1.0','end'))
            except:
                messagebox.showerror(title='ERROR',message='An Error Occurred Please Try Again Later Sometime.')
                return None
    else:
        messagebox.showwarning(title='Warning',message='No Recipent Address Written')
    messagebox.showinfo(title='SUCCESS',message='MESSAGE SENT')
    Gui.entry4.delete(0,END); Gui.entry5.delete(0,END); Gui.textbox.delete('1.0','end')
    Gui.entry4.state(['disabled']); Gui.entry5.state(['disabled'])

def callback():
    Gui.frame1.pack_forget()
    global email_conn
    try:
        email_conn = SMTP('smtp.gmail.com', 587)
        email_conn.ehlo()
        email_conn.starttls()
    except:
        messagebox.showerror(title='An Error Occurred', message='Check Your Internet Connection')
        return None
    try:
        email_conn.login(Gui.entry1.get(), Gui.entry2.get())
        Gui.sender()
    except SMTPAuthenticationError:
        messagebox.showerror(title='An Error Occurred', message='Wrong Email or Password')
        return None
    except :
        messagebox.showerror(title='An Error Occurred', message='Error Occurred Is Unknown')
        return None

def logout():
    Gui.frame2.pack_forget()
    Gui.frame1.pack()
    Gui.entry1.delete(0,END); Gui.entry2.delete(0,END)
    email_conn.quit()

class gui:
    def __init__(self,master):
        self.style=ttk.Style()
        self.style.configure('TFrame',background='#CCCCFF')
        self.style.configure('TLabel',background='#CCCCFF')
        self.style.configure('TEntry',background='#CCCCFF')
        self.style.configure('TButton',background='#CCCCFF')
        self.style.configure('TRadiobutton',background='#CCCCFF')
        self.frame1=ttk.Frame(master)
        self.frame2=ttk.Frame(master)
        self.frame1.pack()
        self.label1 = ttk.Label(self.frame1, text='Email :',font=('arial',12,'bold'))
        self.label2 = ttk.Label(self.frame1, text='Password :', font=('arial', 12, 'bold'))
        self.entry1 = ttk.Entry(self.frame1, width='40')
        self.entry2 = ttk.Entry(self.frame1, width='40', show='*')
        self.button1 = ttk.Button(self.frame1, text='LOGIN', command=callback)
        self.eye=PhotoImage(file='eye.png').subsample(18,18)
        self.eye_label=ttk.Label(self.frame1, image=self.eye)
        self.eye_label.bind('<ButtonPress-1>',lambda e: bindmethod(1))
        self.eye_label.bind('<ButtonRelease-1>', lambda e: bindmethod(2))
        self.label1.grid(row=0, column=0, padx=20, pady=20)
        self.label2.grid(row=1, column=0, padx=20, pady=20)
        self.entry1.grid(row=0, column=1, padx=20, pady=20)
        self.entry2.grid(row=1, column=1, padx=20, pady=20)
        self.button1.grid(row=2, column=1, padx=20, pady=20)
        self.eye_label.grid(row=1, column=2, sticky='w')

    def sender(self):
        self.frame2.pack()
        self.label3 = ttk.Label(self.frame2, text="Sender's Email :")
        self.label4 = ttk.Label(self.frame2, text="Message :")
        self.entry3 = ttk.Entry(self.frame2, width=40)
        self.entry3.insert(0,self.entry1.get())
        self.entry3.state(['readonly'])
        self.radiobutton1=ttk.Radiobutton(self.frame2, text="Reciever's Email")
        self.radiobutton1.bind('<ButtonPress-1>',lambda e :bindmethod(3))
        self.radiobutton2=ttk.Radiobutton(self.frame2, text="Send To Many")
        self.radiobutton2.bind('<ButtonPress-1>',lambda e: bindmethod(4))
        self.entry4 = ttk.Entry(self.frame2, width=40)
        self.entry5 = ttk.Entry(self.frame2, width=40)
        self.entry5.insert(0,"Enter Email's Seperated By Space")
        self.entry4.state(['disabled']); self.entry5.state(['disabled']);
        self.textbox = Text(self.frame2, width=40, height=20, wrap='word')
        self.button2 = ttk.Button(self.frame2, text='SEND', command=send)
        self.button3 = ttk.Button(self.frame2, text='LOGOUT', command=logout)
        self.label3.grid(row=0, column=0, padx=20, pady=20)
        self.entry3.grid(row=0, column=1, padx=20, pady=20)
        self.radiobutton1.grid(row=1, column=0, padx=20, pady=20)
        self.entry4.grid(row=1, column=1, padx=20, pady=20)
        self.radiobutton2.grid(row=2, column=0, padx=20, pady=20)
        self.entry5.grid(row=2, column=1, padx=20, pady=20)
        self.label4.grid(row=3, column=0, padx=20, pady=20)
        self.textbox.grid(row=4, column=0, padx=20, pady=20)
        self.button2.grid(row=5, column=0, padx=20, pady=20)
        self.button3.grid(row=5, column=0, padx=20, pady=20,sticky='w')
root=Tk()
root.title("Email Sender")
root.resizable(False, False)
Gui=gui(root)
root.mainloop()

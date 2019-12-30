import tkinter as tk
import random
from tkinter import messagebox,W ,FLAT, NW
import time
from gamble import account
import threading

class mainGame():
    def __init__(self,hexkey, addr):
        random.seed(time.time())
        self.priv_key = bytes.fromhex(hexkey)
        self.address = addr
        self.user = account(self.priv_key,self.address)
        self.game()
    
    def game(self, waitPull=False):
        total = self.user.getBalance()
        window = tk.Tk()
        canvas = tk.Canvas(window, bg='white', height=900, width=900)
        canvas.pack()

        image_file = tk.PhotoImage(file='slot.png')
        image = canvas.create_image(10,10 , anchor='nw', image=image_file)
        title = tk.Label(window, bg='powderblue',text='拉 霸 機', font =('標楷體', 20,"bold"),fg = 'green',width=15, height=1)
        title.pack()
        canvas.create_window(400,90,window=title)
        self.num1 = tk.StringVar()
        self.num2 = tk.StringVar()
        self.num3 = tk.StringVar()
        self.num1.set(0)
        self.num2.set(0)
        self.num3.set(0)

        label1 = tk.Label(window, textvariable=self.num1,font =('Rubik', 14,"bold"), padx=10,width=5, height=1,bg= 'turquoise')
        label1.pack()
        label2 = tk.Label(window, textvariable=self.num2,font =('Rubik', 14,"bold"), padx=10,width=5, height=1,bg= 'goldenrod')
        label2.pack()
        label3 = tk.Label(window, textvariable=self.num3,font =('Rubik', 14,"bold"), padx=10,width=5, height=1,bg= 'lime')
        label3.pack()
        self.acc_bal = tk.StringVar() #顯示餘額
        self.acc_bal.set('餘額: '+str(total))
        label4 = tk.Label(window, textvariable=self.acc_bal,font =('Rubik', 14,"bold"), padx=10,width=8, height=1,bg= 'white')
        label4.pack()
        
        canvas.create_window(185,340,window=label1)
        canvas.create_window(355,340,window=label2)
        canvas.create_window(520,340,window=label3)
        canvas.create_window(680,270,window=label4)
        button1 = tk.Button(window, text = "拉\n蕊", command = self.play, anchor = W, font =('STXinwei', 20 ,"bold"),bg= 'black',fg='red')
        button1.configure(width = 2, activebackground = "#33B5E5", relief = FLAT)
        button1_window = canvas.create_window(653, 320, anchor=NW, window=button1)

        window.mainloop()
    
    def play(self):
        
        
        self.num1.set("?")
        self.num2.set("?")
        self.num3.set("?")
        total = self.user.getBalance()
        self.acc_bal.set("餘額: "+str(total-200))
        messagebox.showinfo('Info', '祝你中獎')
        number = self.user.pull(100)
        self.number = self.user.pull(100)
        self.num1.set(self.number//100)
        self.num2.set((self.number//10)%10)
        self.num3.set(self.number%10)
        total = self.user.getBalance()
        self.acc_bal.set("餘額: "+str(total))
        if self.num1.get()== self.num2.get() == self.num3.get():
            total = self.user.getBalance()
            self.acc_bal.set("餘額: "+str(total))
            messagebox.showinfo('Info', '恭喜中獎')
        else:
            messagebox.showinfo('Info', '沒中')
            #exit()
            
        

mainGame('1f967cdb8950a2eb987488bed2d0fcd0a1ea3abb9cd3acbd780f722b3c7ed8e6','0xE37793f19BE9a5Aa809c5C2eA0957a780D184164')
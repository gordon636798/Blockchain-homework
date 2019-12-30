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
        self.image_files = []
        total = self.user.getBalance()
        window = tk.Tk()
        self.canvas = tk.Canvas(window, bg='white', height=900, width=900)
        self.canvas.pack()
        
        image_file = tk.PhotoImage(file='element.gif')
        image = self.canvas.create_image(15,30 , anchor='nw', image=image_file)
        
        #self.randomNum()
        
        
        title = tk.Label(window, bg='Lavender',text='嘉大首家線上賭場上線啦', font =('正黑體', 20,"bold"),fg = 'DeepSkyBlue',width=20, height=1)
        title.pack()
        self.canvas.create_window(170,17,window=title)
        self.input = tk.Entry(window)
        self.input.pack()
        self.input.config({"background": 'gainsboro'})
        self.canvas.create_window(120,315,window=self.input)
        self.num1 = tk.StringVar()
        self.num1.set("輸入注數")

        label1 = tk.Label(window, textvariable=self.num1,font =('Rubik', 12,"bold"), padx=10,width=9, height=1,bg= 'turquoise')
        label1.pack()
        """label2 = tk.Label(window, textvariable=self.num2,font =('Rubik', 14,"bold"), padx=10,width=5, height=1,bg= 'goldenrod')
        label2.pack()
        label3 = tk.Label(window, textvariable=self.num3,font =('Rubik', 14,"bold"), padx=10,width=5, height=1,bg= 'lime')
        label3.pack()"""
        self.acc_bal = tk.StringVar() #顯示餘額
        self.acc_bal.set('餘額: '+str(total))
        label4 = tk.Label(window, textvariable=self.acc_bal,font =('Rubik', 14,"bold"), padx=10,width=9, height=1,bg= 'white')
        label4.pack()
        
        self.canvas.create_window(120,290,window=label1)
        """self.canvas.create_window(355,340,window=label2)
        self.canvas.create_window(520,340,window=label3)"""
        self.canvas.create_window(300,255,window=label4)
        button1 = tk.Button(window, text = "   下 注  ", command = self.play, anchor = W, font =('STXinwei', 20 ,"bold"),bg= 'black',fg='red')
        button1.configure(width = 7, activebackground = "#33B5E5", relief = FLAT)
        button1_window = self.canvas.create_window(240, 280, anchor=NW, window=button1)

        window.mainloop()
    
    def play(self):
        var = self.input.get()
        oldTotal = self.user.getBalance()
        if int(var)<=0 or int(var)>=100:
            messagebox.showinfo('Info', '請輸入有效的注數(1~99)')
            return
        else:
            self.num1.set("等待中獎結果")
            self.acc_bal.set('餘額: '+str(oldTotal-int(var)*10))
            messagebox.showinfo('Info', '下注成功!')
            self.user.bet(int(var))
            
        #person = self.user.getWinner()
        #print(person)
        self.num1.set("輸入注數")
        total = self.user.getBalance()
        if oldTotal>=total:
            str1="恭喜獲得 煙霧彈 (1日)"
        else:
            str1="恭喜獲得 黃金AK47 (永久)"
        self.acc_bal.set('餘額: '+str(total))
        messagebox.showinfo('Info', str1)

mainGame('1f967cdb8950a2eb987488bed2d0fcd0a1ea3abb9cd3acbd780f722b3c7ed8e6','0xE37793f19BE9a5Aa809c5C2eA0957a780D184164')
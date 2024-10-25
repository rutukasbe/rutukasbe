#!/usr/bin/env python
# coding: utf-8

# In[1]:


class RMS:
        
    def __init__(self,restaurant_name,restaurant_menu):
        self.user_bill=0
        self.user_order=''
        self.user_pay=0
        self.menu=restaurant_menu
        self.rest_name=restaurant_name
    
    def welcome_user(self):
        #welcome user
        print('welcome to',self.rest_name)
    
    def display_menu(self):
        #display menu
        for i in self.menu:
            print(i.title(),self.menu[i])
    
    def take_order(self):
        #take order
        self.user_order=input("please place your order")
    
    def prepare_order(self):
        #preparing order
        import time
        print("preparing your",self.user_order.title())
        time.sleep(0.5)
        self.user_bill=self.user_bill+self.menu[self.user_order.lower()]
    
    def serve_order(self):
        #order serve
        print("your order is ready")
        print("please enjoy your",self.user_order.title())
    
    def display_bill(self):
        #display bill
        #user_bill=menu[user_order.lower()]
        print("total bill:",self.user_bill)
    
    def verify_payment(self):
        #take payment
        self.user_pay=int(input("please pay your bill is here:"))
        
        while self.user_pay<self.user_bill:
                print(" Invalid payment")
                self.user_bill=self.user_bill-self.user_pay
                print("please pay remaining",self.user_bill)
                self.user_pay=int(input("please pay your bill is here:"))
                    
            
        if self.user_pay>self.user_bill:
            print("payment successfull")
            print("here is your change:",self.user_pay-self.user_bill)
        else:
            pass
            
    def thank_user(self):
        print("thank you for visiting",self.rest_name)
        
    def order_process(self):
        self.display_menu()
        self.take_order()
        if self.user_order.lower() in self.menu:
           self.prepare_order()
           self.serve_order()
           self.user_rep=input("do you want to order anything else ?")
           while self.user_rep.lower()=='yes':
                self.repeat_order()
                self.user_rep=input("do you want to order anything else ?")
            
           self.display_bill()
           self.verify_payment()
           self.thank_user()
        else:
            print("invalid order")
            self.order_process()
    def repeat_order(self):
        self.display_menu()
        self.take_order()
        if self.user_order.lower() in self.menu:
            self.prepare_order()
            self.serve_order()
        else:
            print("invalid order")
            self.repeat_order()
            
            
                


# In[2]:


rn="Moonlight cafe"
rm={'pizza':200,'sandwitch':150,'cold-drinks':100,'cold coffee':80,'burger':180,'drip coffee':250,'cheese pizza':300,'hot coffee':100}
Moonlight_cafe=RMS(rn,rm)

Moonlight_cafe.welcome_user()
Moonlight_cafe.order_process()


# In[ ]:


#import library
import tkinter as tk

#create window
window=tk.Tk()

#change title of window
window.title('RMS OOPs')

#window size
window.geometry('300x300')

tk.Label(window,text=' Moonlight cafe ',font=('helvetica',25)).place(x=50,y=40)
tk.Button(window,text='START',width=25,command=Moonlight_cafe.order_process).place(x=60,y=150)


window.mainloop()


# In[ ]:


Moonlight_cafe.welcome_user()
Moonlight_cafe.order_process()


# In[ ]:





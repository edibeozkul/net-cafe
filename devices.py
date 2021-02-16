# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 14:13:03 2021

@author: edibe
"""

import datetime

class UseDevice:
    def __init__(self,stock):
        self.stock = stock
        self.now = 0
    
    def displayDeviceNumber(self):
        print("{} device is available to rent".format(self.stock))
        return self.stock
    
    def ForHours(self, n):
        if n < 0:
            print("It's invalid input. Please try again.")
            return None
        elif n > self.stock:
            print("Sorry! There is just {} device is available right now.".format.self(stock))
            return None
        else:
            self.now = datetime.datetime.now()
            print("Well Done! It's yours for {} hours.".format(n,self.now.hour))
            self.stock -= n
            return self.now
            
    
    def ForMinutes(self, n):
        if n < 0:
            print("It's invalid input. Please try again.")
            return None
        elif n > self.stock:
            print("Sorry! There is just {} device is available right now.".format.self(stock))
            return None
        else:
            self.now = datetime.datetime.now()
            print("Well Done! It's yours for {} minutes.".format(n,self.now.minute))
            self.stock -= n
            return self.now
        
    
    def quitDevice(self, request, brand):
        computerHPrice = 30
        computerMPrice = 3
        phoneHPrice = 20
        phoneMPrice = 2
        
        usingTime, usingBasis, numOfDevice = request
        bill = 0
        
        if brand == "phone":
            if usingTime and usingBasis and numOfDevice:
                self.stock += numOfDevice
                now = datetime.datetime.now()
                usingPeriod = now - usingTime
                
                if usingBasis == 1:
                    bill = usingPeriod.second / 3600 * phoneHPrice * numOfDevice
                elif usingBasis == 2:
                    bill = usingPeriod.second / 60 * phoneMPrice * numOfDevice
                    
            print("Total Cost: {} $ ".format(bill))
            print("Hope you enjoyed. See you soon!")
            
            return bill
        
        elif brand == "computer":
            if usingTime and usingBasis and numOfDevice:
                self.stock += numOfDevice
                now = datetime.datetime.now()
                usingPeriod = now - usingTime
                
                if usingBasis == 1:
                    bill = usingPeriod.second / 3600 * computerHPrice * numOfDevice
                elif usingBasis == 2:
                    bill = usingPeriod.second / 60 * computerMPrice * numOfDevice
                    
                    print("Total Cost: {} $ ".format(bill))
                    print("Hope you enjoyed. See you soon!")
            
                    return bill
    
                else:
                    print("YOU DO NOT CHOOSE ANY DEVİCE")
                    return None
        
class UseComputer(UseDevice):
    
    global a
    a = 12
    
    def __init__(self, stock):
        super().__init__(stock)
        
    def discount(self, b):
        bill = b - (b * a) / 100
        return bill
    
class UsePhone(UseDevice):
    def __init__(self, stock):
        super().__init__(stock)
        
   
    
class Customer:
    def __init__(self):
        self.computers = 0
        self.usingBasisComputer = 0
        self.usingTimeComputer = 0
        
        self.phones = 0
        self.usingBasisPhone = 0
        self.usingTimePhone = 0
            
    def requestDevice(self, choice):
        
        if choice == "phone":
            phones = input("How many phone do you need?")
            try:
                phones = int(phones)
            except ValueError:
                print("You entered an invalid value. Type something like, hmm, a number?")
                return -1
            
            if phones < 1:
                print("Um, something went wrong!")
                return -1
            else:
                self.phones = phones
            return self.phones
        
        elif choice == "computer":
            computers = input("How many computer do you need?")
            try:
                computers = int(computers)
            except ValueError:
                print("You entered an invalid value. Type something like, hmm, a number?")
                return -1
            
            if computers < 1:
                print("Um, something went wrong!")
                return -1
            else:
                self.computers = computers
            return self.computers 
        else:
            print("Something went wrong. Sorry!")
    
    def quitDevice(self, choice):
        
        if choice == "phone":
            if self.usingTimePhone and self.usingBasisPhone and self.phones:
                return self.usingTimePhone, self.usingBasisPhone, self.phones
            else: return 0,0,0
            
        elif choice == "computer":
            if self.usingTimeComputer and self.usingBasisComputer and self.computers:
                return self.usingTimeComputer, self.usingBasisComputer, self.computers
            else: return 0,0,0
            
        else:
            print("Something went wrong. Sorry!")

            
        
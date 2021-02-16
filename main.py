# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 14:12:49 2021

@author: edibe
""" 
from devices import UsePhone, UseComputer, Customer

 phone = UsePhone(10)
 computer = UseComputer(50)
 customer = Customer()
 
 mainMenu = True
 
 while True:
     if mainMenu:
         print("""
      _______________
      
               COMPUTERS&PHONES
               ________________________
                    You choose the phone or computer you want 
                    and use it as much as you 
                    want.
                    
                    P. Phone Menu
                    C. Computer Menu
                    
                    Q. EXIT
                    
                    """)
            mainMenu = False
            
            userChoice = input("Enter: ")
            
                if userChoice == "A" or userChoice == "a":
                print("""
                      _________________
                      
                      Phone Menu
                      ___________
                      
                      1. Show Available Phones
                      
                      Request Phone 
                          2. for hour (20$x)
                          3. for minutes (2$x)
                     
                      4. Return Device
                      5. Main Menu
                      6. Exit
                      """
                      )
                
                userChoice = input("Enter: ")
                
                try:
                    userChoice = int(userChoice)
                except ValueError:
                    print("You entered an invalid value. Type something like, hmm, a number?")
                    continue
            
                        if userChoice == 1:
                            phone.displayDeviceNumber()
                            userChoice = "A"
                        elif userChoice == 2:
                            customer.usingTimePhone = phone.ForHours(customer.requestDevice("phone"))
                            customer.usingBasisPhone = 1
                        mainMenu = True
                        print("__________________")
                        elif userChoice == 3:
                            customer.usingTimePhone = phone.ForMinutes(customer.requestDevice("phone"))
                            customer.usingBasisPhone = 2
                            mainMenu = True
                            print("__________________")
                        elif userChoice == 4:
                            customer.bill = phone.quitDevice(customer.quitDevice("phone"), "phone")
                            customer.usingBasisPhone, customer.usingTimePhone, customer.phones = 0,0,0
                            mainMenu = True
                        elif userChoice == 5:
                            mainMenu = True
                        elif userChoice = 6:
                            break 
                        else:
                            print("Invalid Input. Try a Number Between 1-6 ")
                
                elif userChoice == "B" or userChoice == "b":
                print("""
                      _________________
                      
                      Computer Menu
                      ___________
                      
                      1. Show Available Computers
                      
                      Request Computer 
                          2. for hour (30$x)
                          3. for minutes (3$x)
                     
                      4. Return Device
                      5. Main Menu
                      6. Exit
                      """
                      )
                
                userChoice = input("Enter: ")
                
                try:
                    userChoice = int(userChoice)
                except ValueError:
                    print("You entered an invalid value. Type something like, hmm, a number?")
                    continue
                    
                        userChoice = input("Enter: ")
                
                try:
                    userChoice = int(userChoice)
                except ValueError:
                    print("You entered an invalid value. Type something like, hmm, a number?")
                    continue
            
            if userChoice == 1:
                computer.displayDeviceNumber()
                userChoice = "B"
            elif userChoice == 2:
                customer.usingTimeComputer = computer.ForHours(customer.requestDevice("computer"))
                customer.usingBasisComputer = 1
                mainMenu = True
                print("__________________")
            elif userChoice == 3:
                customer.usingTimeComputer = computer.ForMinutes(customer.requestDevice("computer"))
                customer.usingBasisComputer = 2
                mainMenu = True
                print("__________________")
            elif userChoice == 4:
                customer.bill = computer.quitDevice(customer.quitDevice("computer"), "computer")
                customer.usingBasisComputer, customer.usingTimeComputer, customer.computers = 0,0,0
                mainMenu = True
            elif userChoice == 5:
                mainMenu = True
            elif userChoice = 6:
                break 
            else:
                print("Invalid Input. Try a Number Between 1-6 ")
                mainMenu = True
         
                
             elif userChoice == "Q" or userChoice == "q":
                 break
             
             else: print("Invalid Input. Try A/B or Q. ")
             mainMenu = True
             
        print("_____ THANK YOU ! _____")

                 
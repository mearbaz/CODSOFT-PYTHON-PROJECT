#!/usr/bin/env python
# coding: utf-8

# # My Calculator

# In[4]:


n = 4
for i in range(n+1):
    for j in range(i):
        print("*",end ='')
        
    for j in range(i,n):
        print(' ', end = '')
        
    for k in range(i,n):
        print(' ', end='')
        
    for l in range(i):
        print('*', end='')
        
    for j in range(i):
        print("*",end ='')
     
    for j in range(i,n):
        print(' ', end = '')
        
    for k in range(i,n):
        print(' ', end='')
        
    for l in range(i):
        print('*', end='')
        
    print('')
    
   
print(' MY CALCULATOR')      
  
num1 =float(input("Enter the first Num: "))
num2 = float(input("Enter the second Num: "))

print("\nEnter 1 for Addition")
print("Enter 2 for Subtraction")
print ("Enter 3 for Multiplication")
print('Enter 4 for Division')

choise= int(input('\nChoose between 1 to 4: '))

if choise == 1:
    print(num1+num2)
elif choise ==2:
    print(num1-num2)
elif choise == 3:
    print(num1*num2)
elif choise == 4:
    print(num1/num2)
else:
    print("INVALIED VALUE")


# # My Contact Book

# In[ ]:


contact ={}

def dis_contact():
    print("NAME \t\t CONTACT NUMBER")
    for key in contact:
        print("{} \t\t {}".format(key,contact.get(key)))

        
while True:
    
    choose = int(input(" 1. Add new Contact \n 2. View Contact List \n 3. Search Contact \n 4. Update Contact \n 5. Delete Contact \n 6. Exit \n\n Enter the Choise: "))
    
    if choose == 1:
        name = input("Enter the Name: ")
        phone = input("Enter the Numbe: ")
        contact[name] = phone
        
    elif choose == 2:
        if not contact:
            print("Empty Contact Book")
        else:
            dis_contact()
            
    elif choose == 3:
        search = input("Enter the contact name: ")
        if search in contact:
            print(search,"'s number is ",contact[search])
        else:
            print("Name is Not found in Contact Book")
            
    elif choose == 4:
        edit = input("Enter the Name: ")
        if edit in contact:
            phone = input("Enter the Number: ")
            contact[edit]=phone
            dis_contact()
        else:
            print("Name is Not found in Contact Book")
            
    elif choose == 5:
        del_contact = input("Enter the Name: ")
        if del_contact in contact:
            confirm = input("Do you want to Delete enter 'y' or 'Y': ")
            if confirm == 'y' or confirm == 'Y':
                contact.pop(del_contact)
            dis_contact()
        else:
            print("Name is Not found in Contact Book")
            
    else:
        break
        
    


# ## Random Password Generator

# In[3]:


import random

uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase = uppercase.lower()
digits = "0123456789"

upper, lower, nums = True, True, True

pas = ""

if upper:
    pas += uppercase
if lower:
    pas += lowercase
if nums:
    pas += digits
    
length = int(input("Enter length: "))

password ="".join(random.sample(pas,length))
print(password)


# ## (Rock, Paper, Scissors) Game

# In[3]:


import random 

options = ('rock', 'paper','scissors')


running =True

while running:
    
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter choice (rock, paper, scissors): ")


    print(f"player : {player}")
    print(f"computer : {computer}")

    if player == computer:
        print("It's Tie!")
    elif player == "rock" and computer == "scissors":
        print("You Win!")
    elif player == "paper" and computer == "rock":
        print("You Win!")
    elif player == "scissors" and computer =="paper":
        print("You Win!")
    else:
        print("You Lose!")
        
    if not input("Play Again? (y/n)").lower() == "y":
        running = False
print("Thank you!")       


# In[ ]:





# In[ ]:





import mysql.connector as myconn
import BACK_END as pack
mycon=myconn.connect(host='localhost',user='root',passwd='vvvvvvvp14',database='project')

print('___________________________________________________________________________________________')
print()
print('WELCOME TO GADA ELECTRONICS')
print('___________________________________________________________________________________________')

def admin(b):
    
        if b==1:
               print('in table Products')
               pack.add_p()
        elif b==2:
                print('in table Customer')
                pack.add_cust()
        elif b==3:
                print('in table Invoice')
                pack.add_invoice()
        elif b==4:
                print('in table Warranty')
                pack.add_warranty()
        elif b==5:
                print('in table offers')
                pack.add_offer()
        elif b==6:
                pack.update_tables()
        elif b==0:
                loop()


        
def employee(b):
        if b==1:
                print('in table Customer')
                pack.add_cust()
        elif b==2:
                print('in table Invoice')
                pack.add_invoice()
        elif b==3:
                print('Products')   
                pack.show_p()
        elif b==4:
                print('Customers')
                pack.show_cust()
        elif b==5:
                print('Invoices')
                pack.show_invoice()
        elif b==6:
                print('Warranty')
                pack.show_warranty()
        elif b==7:
                print('Offers')
                pack.show_offer()
        elif b==0:
                loop()
        
def cust(b):
    if b==1:
        pack.show_cust_invoice()
    elif b==2:
        pack.show_offer()
    elif b==0:
        loop()
        
#show_invoice can only be operated by employee
#show_cust_invoice shows only one user record


        

#using loop
def loop():
    flag=False 
    a=int(input('''Enter as 
    1.Admin
    2.Employee
    3.Customer
    \nenter 0 to close\t:'''))

    while a!=0:
        if a==1:
            if flag==False:
                passwd=int(input('enter Admin password'))
                if passwd==706968:
                    print('''
    Welcome back Admin''')
                    flag=True

                else:
                    print('WRONG PASSWORD')
                    continue
        
                
            b=int(input('''
    enter 1 to add product
    enter 2 to add customer
    enter 3 to add invoice
    enter 4 to add warranty
    enter 5 to add offer
    enter 6 to update tables
    enter 0 to return\t'''))


            admin(b)
            #loop(a)
                
           
            

        elif a==2:
            if flag==False:
                passwd=int(input('enter employee password'))
                if passwd==345600:
                    print('''
    Welcome back employee''')
                    flag=True

                else:
                    print('WRONG PASSWORD')
                    continue
                
                #using loop in employee
            b=int(input('''
    enter 1 to add customer
    enter 2 to add invoice
    enter 3 to show products
    enter 4 to show customer
    enter 5 to show invoice
    enter 6 to show warranty
    enter 7 to show offers
    enter 0 to return\t:'''))
            employee(b)
            
                
        elif a==3:
            b=int(input('''
    enter 1 to see your invoice
    enter 2 to see all offers
    or enter 0 to return'''))
            cust(b)
            
                

        
loop()          
import mysql.connector as myconn    
mycon=myconn.connect(host='localhost',user='root',passwd='vvvvvvvp14',database='project')


def auto_s_no():
#to auto generate s number when used
  cursor=mycon.cursor()
  cursor.execute('select MAX(s_no) from products')
  data=cursor.fetchall()

  s_no=0
  for a in data:
     s_no=a[0]+1

  return s_no

def auto_cust_ID():
#to auto fill the customer ID column when used
  cursor=mycon.cursor()
  cursor.execute('select MAX(customer_ID) from customer')

  data=cursor.fetchall()

  for a in data:
     cust_ID=''

     for b in range(2,len(a[0])):
      cust_ID+=a[0][b]
     cust_ID=int(cust_ID)+1
     cust_ID=str(cust_ID)

     if len(cust_ID)==1:  
      cust_ID='GE000'+cust_ID
     elif len(cust_ID)==2:
      cust_ID='GE00'+cust_ID
     elif len(cust_ID)==3:
      cust_ID='GE0'+cust_ID
     elif len(cust_ID)==4:
      cust_ID='GE'+cust_ID
     else:
      cust_ID='ERROR(customer ID too long)'

  return cust_ID

def auto_invoice_no():
#to auto generate invoice number when used
  cursor=mycon.cursor()
  cursor.execute('select MAX(invoice_no) from invoice')
  data=cursor.fetchall()

  for a in data:
     return (a[0]+1)

def auto_bill_amt(a,b,c):
#to automatically fill the bill amount when used 
  amt=0

  for q in [a,b,c]:

    cursor=mycon.cursor()
    price=('select price from products where model_no IN (%s)')
    data_price=(q,)
    cursor.execute(price,data_price)
    data=cursor.fetchall()
    amt+=data[0][0]

  return amt

def update_tables():

     cursor=mycon.cursor()
     print('''\n******************Update********************
Currently entered data in tables of database''')
     table=int(input('''enter 1 for products
enter 2 for customer
enter 3 for invoice
enter 4 for offers    \t:'''))
     if table==1:
          print('''\nIn PRODUCTS you can only update the following column(s)
************************price**************************''')
          a=int(input('''\nDo you want to a specific row or whole column(s) to be updated
enter 1 for row
enter 0 for whole column(s)\t :'''))
          if a==1:
              update_products=('UPDATE PRODUCTS SET price=%s WHERE model_no=%s')
              model_no=input('\nenter the model no. of the product\t:') 
              new_price=int(input('enter new price\t     :'))
              data_products=(new_price,model_no)
              cursor.execute(update_products,data_products)
              mycon.commit()
          elif a!=1:
              update_products=("UPDATE PRODUCTS SET price=%s * price")
              new_price_percent=input('\nenter new price increase inpercent:')
              new_price_percent=int(new_price_percent)
              new_price_percent=(new_price_percent+100)/100
              new_price_percent=str(new_price_percent)
              print(new_price_percent,type(new_price_percent))
              update_products=('update PRODUCTS SET price='+new_price_percent+'*price')

              cursor.execute(update_products,new_price_percent)
              mycon.commit()
            
     elif table==2:
          print('''\nIn CUSTOMER you can only update the following column(s)
*******************name,mobile number******************
And the update can only be made to a row at once''')
          a=int(input('''\nDo you want to update both or one of those column(s)
enter 1 for name only
enter 2 for mobile number only
enter 0 for both\t:'''))
          if a==1:
              update_customer=('UPDATE CUSTOMER SET name=%s WHERE customer_ID=%s')
              customer_ID=input('\nenter the customer_ID\t:') 
              new_name=input('enter new name\t:')
              data_customer=(new_name,customer_ID)
              cursor.execute(update_customer,data_customer)
              mycon.commit()
          elif a==2:
              update_product=('UPDATE CUSTOMER SET mobile_num=%s WHERE customer_ID=%s')
              customer_ID=input('\nenter the customer_ID\t:') 
              new_mobile_num=int(input('enter new mobile no\t:'))
              data_customer=(new_mobile_num,customer_ID)
              cursor.execute(update_customer,data_customer)
              mycon.commit()
          elif a==0:
              update_product=('UPDATE CUSTOMER SET name=%s,mobile_num=%s WHERE customer_ID=%s')
              customer_ID=input('\nenter the customer_ID\t:') 
              new_name=input('enter new name\t:')
              new_mobile_num=int(input('enter new mobile no\t:'))
              data_customer=(new_name,new_mobile_num,customer_ID)
              cursor.execute(update_customer,data_customer)
              mycon.commit()
            
     elif table==3:
         print('''\nIn INVOICE you can only update the following column(s)
**************************DOP*************************
And the update can only be made to a row at once''')
         update_invoice=('UPDATE INVOICE SET DOP=%s WHERE invoice_no=%s')
         invoice_no=input('\nenter the invoice_no\t:') 
         new_DOP=input('enter new DOP\t:')
         data_invoice=(new_DOP,invoice_no)
         cursor.execute(update_invoice,data_invoice)
         mycon.commit()
        
     elif table==4:
         print('''\nIn OFFERS you can only update the following column(s)
*********************Discount_per********************
And the update can be to a row only at once''')
         update_offers=('UPDATE offers SET Discount_per=%s WHERE off_code=%s')
         off_code=input('\nenter off_code\t:') 
         new_Discount_per=int(input('enter the Discount_per\t:')) 
         data_offers=(new_Discount_per,off_code)
         cursor.execute(update_offers,data_offers)
         mycon.commit()
     else:
          print('\n******NOT*A*TABLE*YOU*CAN*UPDATE********')
def add_p():
                        #s_no to be auto generated
    cursor=mycon.cursor()
    add_product=('INSERT INTO PRODUCTS'
             '(s_no, name,model_no,price)'
             'values(%s,%s,%s,%s)')
    s_no=auto_s_no()
    print('Serial number\t:',s_no)
    name=input('enter name of product')
    model_no=input('enter model number of product')
    price=int(input('enter price of product'))
    data_product=(s_no,name ,model_no,price)
   
    #insertion into table

    cursor.execute(add_product,data_product)
    mycon.commit()

    print('executed')

#insertion of a customer
invoice_no=0
   
def add_cust():
   
    global invoice_no
    add_customer=('INSERT INTO CUSTOMER'
                  '(invoice_no,name,mobile_num,customer_id)'
                  'values(%s,%s,%s,%s)')
    invoice_no=int(input('enter invoice number :'))
    name=input('enter customer name  :')
    mobile_num=input('enter mobile number  :')
    cust_id=auto_cust_ID()
    print('Customer ID\t     :',cust_id)
    data_customer=(invoice_no,name,mobile_num,cust_id)

    #insertion into table
    cursor=mycon.cursor()
    cursor.execute(add_customer,data_customer)
    mycon.commit()


    print("executed")
   
def add_invoice():
    #global invoice_no
                           
    #bill amount and invoice number auto generated 
    num=int(input('enter number of product(1-3)'))
   
    invoice_no=auto_invoice_no()
    print('Invoice number\t:',invoice_no)
    product1=input('enter model number of product 1:')
   
    #arranging invoice according to product purchased
    if num==3:
        add_in=('INSERT INTO INVOICE'
                '(invoice_no,product1,product2,product3,bill_amt,dop)'
                ' values(%s,%s,%s,%s,%s,%s)')
        product2=input('enter model number of product 2:')
        product3=input('enter model number of product 3:')
        bill_amt=auto_bill_amt(product1,product2,product3)
        dop=input('enter date of purchase         :')
        data_in=(invoice_no,product1,product2,product3,bill_amt,dop)
        print('Amount to be paid\t:',bill_amt)
       
    elif num==2:
        add_in=('INSERT INTO INVOICE'
                '(invoice_no,product1,product2,bill_amt,dop)'
                ' values(%s,%s,%s,%s,%s)')
        product2=input('enter model number of product 2:')
        bill_amt=auto_bill_amt(product1,product2,'00000000000000000000')
        dop=input('enter date of purchase         :')
        data_in=(invoice_no,product1,product2,bill_amt,dop)
        print('Amount to be paid\t:',bill_amt)

    elif num==1:
        add_in=('INSERT INTO INVOICE'
                '(invoice_no,product1,bill_amt,dop)'
                ' values(%s,%s,%s,%s)')
        bill_amt=auto_bill_amt(product1,'00000000000000000000','00000000000000000000')
        dop=input('enter date of purchase         :')
        data_in=(invoice_no,product1,bill_amt,dop)
        print('Amount to be paid\t:',bill_amt)
   
    else:
        print('enter number between 1-3')
        add_invoice()

    #insertion into table
   
    cursor=mycon.cursor()
    cursor.execute(add_in,data_in)
    mycon.commit()
    print("executed")


def add_warranty():
    cursor=mycon.cursor()
    year=int(input('''enter number of years of warranty
    or press enter 0 for current date'''))

    p_name=input('enter name of product')
    model_no=input('enter model number of product')

    if year==0:
        add_warranty=('INSERT INTO warranty'
                 '(product_name,model_no)'
                 'values(%s,%s)')
        data_warranty=(p_name,model_no)
    elif year!=0:
        end_date=input('enter the end date')
        add_warranty=('INSERT INTO warranty'
                 '(product_name,model_no,end_date)'
                 'values(%s,%s,%s)')
        data_warranty=(p_name,model_no,end_date)
    cursor.execute(add_warranty,data_warranty)
    mycon.commit()
    print("executed")

def add_offer():
    add_offer=('INSERT INTO offers VALUES(%s,%s,%s,%s)')
    off_code=input('enter offer code    :')
    off_name=input('enter offer name    :')
    model_no=input('enter model number  :')
    Discount_per=int(input('enter Discount percentage:'))
    data_offers=(off_code,Discount_per,model_no,off_name)
    cursor=mycon.cursor()
    cursor.execute(add_offer,data_offers)
    mycon.commit()


    print("executed")



def show_p():
    cursor=mycon.cursor()
    cursor.execute('select * from products order by s_no')
    data=cursor.fetchall()
       
    for row in data:
        print(row)


def show_cust():
    cursor=mycon.cursor()
    cursor.execute('select * from customer order by customer_id')
    data=cursor.fetchall()
       
    for row in data:
        print(row)


def show_invoice():
    cursor=mycon.cursor()
    cursor.execute('select * from invoice')
    data=cursor.fetchall()
       
    for row in data:
        print(row)

        
def show_offer():
    cursor=mycon.cursor()
    cursor.execute('select * from offers order by off_code')
    data=cursor.fetchall()

    for row in data:
        print(row)
def show_warranty():
  cursor=mycon.cursor()
  cursor.execute('select * from warranty')
  data=cursor.fetchall()

  for row in data:
      print(row)


def show_cust_invoice():
                                        #in progress
                                        #
    mob_no=input('Confirm your mobile_no')
    cursor=mycon.cursor()
    cursor.execute("select * from customer where mobile_num="+mob_no)
    fake_data=cursor.fetchone()
    invoice_no_ex=fake_data[0]
   

    #showing invoice from invoice number extracted
    invoice_no_ex=str(invoice_no_ex)
    cursor=mycon.cursor()
    cursor.execute("select * from invoice where invoice_no="+invoice_no_ex)
    data=cursor.fetchone()
    print(data)
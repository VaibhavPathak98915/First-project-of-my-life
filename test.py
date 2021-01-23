import mysql.connector as myconn
myconn=myconn.connect(host='localhost',user='root',passwd='vvvvvvvp14',database='project')

'''def drop_data():
    cursor=mycon.cursor()
    print(''The data of whole column can not be deleted
BUT only the data of a whole row can be deleted at once\n\n')
    
    table=int(input(''enter 1 for products
enter 2 for customer
enter 3 for invoice
enter 4 for warranty
enter 5 for offers    \t:'))
    
    if table==1:
    
    elif table==2:
    
    elif table==3
	
	elif table==4:
	
	elif tabe==5:
	
	else:'''
def auto_bill_amt(a,b,c):
#to automatically fill the bill amount when used 
  amt=0
  for q in [a,b,c]:
  	cursor=mycon.cursor()
  	price=('select price from products where model_no IN (%s)')
  	data_price=(q,)
  	cursor.execute(price,data_price)
  	data=cursor.fetchall()
  	print(data)
  	amt+=data[0][0]
  print(amt)            
a=input()
b=input()
c=input()
auto_bill_amt(a,b,c)
'''n=0
  for row in data:
    n+=1
    amt.append(row[0])
    #calc price of two or more same products 
    if (a==b) and (n==1):
      amt.append(row[0])
    if (b==c) and (n==2):
      amt.append(row[0])
    if (a==c) and (n==1):
      amt.append(row[0])

  n=0
  for a in range(0,len(amt)):
    n+=amt[a]

  print(n)'''
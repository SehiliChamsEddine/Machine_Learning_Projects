def Pass(password="helo999"):
    p=''
    i=0
    while True:
        if (p != password) and (i < 3): 
             p=input("enter the password :")   
             i+=1
             if p==password :
                a =  True 
             else :
                 a=False
             if i==3 and p!=password  :
               print("your are not wellcome")
               break
        else:
            break
    if a :
         print("the password is correct")
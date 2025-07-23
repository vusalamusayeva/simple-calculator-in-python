def addition():
    total=0
    count=0
    while True:
        num = float(input('Enter num:'))
        if num == 0:
            break
        total+=num
        count+=1 
    return [total,count]
    

def subtraction():
    num1=float(input('Enter num1:'))
    subtract=num1
    count=1
    while True:
        num = float(input('Enter num:'))
        if num==0:
            break
        subtract -= num
        count += 1
    return [subtract, count]

def multiplication():
    num1= float(input('Enter num:'))
    multiply = num1
    count =1
    while True:
        num=float(input('Enter num:'))
        if num == 0:
            break
        multiply*=num
        count+=1
    return [multiply,count]

def average():
    total=0
    count=0
    num=1
    while num!=0:
        num=float(input('Enter num:'))
        if num!=0:
            total+=num
            count+=1
    if count==0:
        return 0
    avg = total / count
    return avg


    
your_choice=input('Choose operation: ')

if your_choice == '1':
    result=addition()
    print(result)
elif your_choice == '2':
    result=subtraction()
    print(result)
elif your_choice== '3':
    result=multiplication()
    print(result)
elif your_choice== '4':
    result=average()
    print(result)
elif your_choice== '0':
    print('See you soon!') 
else:
    print('Invalid choice.')

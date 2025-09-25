#10 5 1
print('enter the returning amount')
num=input()
try:
    n = (int(num)/10)
    print('there are ',int(n),' ten dirham bills')
    r=(int(num)%10)
    s5 = (r/5)
    print('there are ',int(s5),' five dirham bills')
    rem = (r%5)
    m1 = (rem/1)
    print('there are ',int(m1),' one coins')
except ValueError:
    print("Error: you did not enter a num")
        

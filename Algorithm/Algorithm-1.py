n = 0
result = 0
while n <= 5:
    result= result+n
    n=n+1
    print(f', the factorial of{n} = {result}')

    # max number

a=124
b=21
c=32
if a>b:
    if a>c:
        print('a is max')
        if b>c:
            if b>a:
                print('b is max')
            else:
                print('c is max')


# even and odd numbers from list

list= [3,4,5,6,0]
even_num= 0
odd_num= 0
for num in list:
    if num % 2== 0:
        even_num += 1

    else:
        odd_num += 1

    print("even number in the list", even_num)
    print("odd number in list", odd_num)





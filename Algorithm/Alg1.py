def is_palindrome(x):
    return x == (x[::-1])
print(is_palindrome("radar"))
print(is_palindrome("raddr"))

# find missing number
def missing_number( x,y):
    x.sort()
    y.sort()
    for i in range(len(x)):
       if x[i] != y[i]:
         return x[-1]
my_list1=[1,2,3,4,5]
my_list2=[1,2,6,3,4,5]
mis_num=(missing_number(my_list1, my_list2))
print(mis_num)


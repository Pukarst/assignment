#   Prime Number in a Range

def is_prime(num):
    if num<2:
        return False
    for n in range(2,num):
        if num%n==0:
            return False
    return True

start_num=int(input('Enter the number you want to select as a start number--->'))
end_num=int(input('Enter the number you want to select as a end number--->'))

for num in range(start_num,end_num+1):
    if is_prime(num):
        print('The prime numbers between the starting and ending range are as follows-->',num)
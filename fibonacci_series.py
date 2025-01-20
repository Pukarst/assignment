#   recursive Fibonacci Series

def fibo(n):
    if n<2:
        return n
    else:
        return fibo(n-1)+fibo(n-2)
    
n=int(input('Enter the number of terms you want to know-->'))

for m in range(n):
    print(f'The fibonacci sequence for the {n} terms are as-->',fibo(m))

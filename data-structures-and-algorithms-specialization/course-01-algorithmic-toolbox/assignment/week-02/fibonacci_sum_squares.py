# Uses python3
from sys import stdin

def multiply(F, M, m): 
      
    x = (F[0][0] * M[0][0] + 
         F[0][1] * M[1][0]) 
    y = (F[0][0] * M[0][1] + 
         F[0][1] * M[1][1]) 
    z = (F[1][0] * M[0][0] + 
         F[1][1] * M[1][0]) 
    w = (F[1][0] * M[0][1] + 
         F[1][1] * M[1][1]) 
      
    F[0][0] = x % m
    F[0][1] = y % m
    F[1][0] = z % m
    F[1][1] = w % m

def power(F, n, m): 
  
    if( n == 0 or n == 1): 
        return
    M = [[1, 1], 
         [1, 0]]
          
    power(F, n // 2, m) 
    multiply(F, F, m) 
          
    if (n % 2 != 0): 
        multiply(F, M, m) 

def fibonacci_sum_squares_naive(n):
    bigsum = 0
    smallsum = 0

    F = [[1, 1], 
         [1, 0]] 
    
    if n == 0:
        bigsum = 1
    else:
        power(F, n, 10)
        bigsum = F[0][0] % 10
    
    F = [[1, 1], 
         [1, 0]] 
    
    if n == 0:
        smallsum = 0
    else:
        power(F, n - 1, 10)
        smallsum = F[0][0] % 10

    return ((bigsum * smallsum) + 10) % 10

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_squares_naive(n))

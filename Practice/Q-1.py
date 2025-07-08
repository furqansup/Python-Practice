# Q1. Check if a number is prime

# def is_prime(n):
    
#  count = 0

#  for i in range(1, n+1):
#     if n % i == 0:
#         count +=1

#  if count == 2:
#     print(f'{n} is a prime number')
#  else:
#     print(f'{n} is not a prime number')

# is_prime(120000000)


# More efficient way

def prime_no(n):

   if n <= 1:
   # if n is less than 1 which are 0 and negative values, 
   # then it can never be a prime number because prime number is only postive natural numbers
      print (f"{n} is not a prime number")
      return
   
   for i in range(2, int(n**0.5)+1):
      # Check every number from 2 up to square root of n. If any of them divides n, then n is not prime.
      # If no number divides n, then it’s prime.
      if n % i == 0:
         # if dividing any number in between gives 0 as remainder then its not a prime number
         print (f'{n} is not a prime number')
         return
   
   print (f"{n} is a prime number")

prime_no(11)
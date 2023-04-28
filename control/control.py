#Write a function that uses while, 
#if and continue statements to print all the even numbers between 0 and 50. 
def even_numbers():
    v=0
    while v<50:
        v+=1
        if v%2!=0:
            continue
        print(v)
        
#Write a function that takes an integer argument and prints "Prime" if the number is prime, and "Not prime" if the number is not prime.
def prime_or_not(nums):
    if nums <=1:
        print("Not prime")
        return
    for i in range(2, int(nums/2)+1):
        if (nums%i) ==0:
            print("Not prime")
            break
    else:
        print("prime")


#Write a function that takes a list of integers as input and prints the sum of all the even numbers in the list.
def sum_even_numbers(numbers):
    p=0
    for i in numbers:
        if i%2==0:
            p+=i
    print(p)

#Write a function that takes any two integers as input, 
#and prints the sum of all the numbers between the two integers (inclusive) that are divisible by 3.
def sum_all_numbers(b,c):
    k=0
    for n in range(min(b,c),max(b,c)+1):
        if n%3 ==0:
            k+=n
    print(k)


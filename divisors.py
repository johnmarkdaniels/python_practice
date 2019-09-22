num = int(input('Please input a number: '))
x = range(1,num+1)
divisors = [i for i in x if num % i == 0]
# for i in x:
#     if num % i == 0:
#         divisors.append(i)
#     else:
#         pass

print(divisors)

if len(divisors) == 2:
    print(f'Your number ({str(num)}) is also a prime number!')

num = int(input('Please input a number: '))
if num % 2 == 0:
    print(f'Your number ({str(num)}) is an even number.')
    if num % 4 == 0:
        print('Incidentally, your number is evenly divisible by 4.')
else:
    print(f'Your number ({str(num)}) is an odd number.')

def find_primes(target):
    nums = [x for x in range(2,target)]
    # print(nums)
    # num = 11
    primes = []
    for num in nums:
        for x in range(2,num):
            # print(num,x)
            if num % x == 0:
                # print('Is not a prime')
                break
            else:
                if x == num-1:
                    primes.append(num)
    return(primes)

print(find_primes(37))



a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
less_than_5 = [x for x in a if x < 5]
print(less_than_5)

query = int(input('Give me a number to query: '))
less_than_query = [x for x in a if x < query]
print(less_than_query)

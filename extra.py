data = [1,2,3,4,5]

print(', '.join(map(str, map(lambda x: x**2,data))))
print([x*x for x in data])

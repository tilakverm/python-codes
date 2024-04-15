age = [43,67,21,98,52]

print(age)
print(age[0])
print(len(age))

print(age[1:4]) 
age.append(2)
print(age)

age.sort()
print(age)

age.sort(reverse=True)
print(age)

age.reverse()
print(age)

age.insert(1,5)
print(age)

age.remove(43)
print(age)

age.pop(2)
print(age)



set={1,2,3,4,5,1,2,3,4,5}
set1={1,1,5,6,2,3,5,2,1,6}
set2={1,"PROSINGHVI", 3,4,5.8,7.9, False}
print(set2)
print(set1)
print(set)
set1.pop()
print(set1)
set1={"red", "Blue", "orange"}
set2={"Blue", "green"}
setz = set1.intersection(set2)
print(setz)
setx=set1.union(set2)
print(setx)
my_array = [1, 3, 5, 3, 7, 9, 3]
occurrences_of_three = my_array.count(3)
print(f"Number of occurrences of 3: {occurrences_of_three}")
reversed_array = my_array[::-1]
print(f"Reversed array: {reversed_array}")
a = {1, 2, 3, 4, 5, 6, 7, 8, 9}
b={9,8,7,3,5,1,2,6}
print(a.difference(b))
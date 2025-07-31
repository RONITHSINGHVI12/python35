s1 = {1, 5, 6}
s2={"a", "b", "c"}
s3=list(zip(s1,s2))
print(s3)
new_dict={s1: s2 for s1, s2 in zip(s1,s2)}
print(new_dict)
list1=[1,5,8,7,6]
list2=[300,500, 700, 800,200]
for x, y in zip (list1, list2[::-1]):
 print(x,y)
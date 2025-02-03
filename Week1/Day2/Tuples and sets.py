# Tuples
numbers=(10,20,30,40,20,50,20)
print(type(numbers))


#methods
print(numbers.count(20))
print(numbers.index(30))

#Concatenate tuples
numbers2=(2,3,5,7)
mixed_tuples=numbers+numbers2
print(mixed_tuples)

a,b,c,d=5,10,15,20
print(a,b,c,d)

name,age,mail="Juliana",28,"danieljaoui82"

a_tuple=(10,20,30,40)
a,b,c,d=a_tuple
print(a,b,c,d)

# Sets= unordered data structure
my_set={1,4,8,9}
#my_set=set()
my_set.add(12)
print(my_set)

favorite_numbers={1,3,2,8,9}
favorite_numbers.add(12)
print(favorite_numbers)
prime_number={1,3,5,11,13}
intersect=favorite_numbers.intersection(prime_number)
print(intersect)
favorite_numbers.clear()
print(favorite_numbers)
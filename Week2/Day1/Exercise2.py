class Dog():
    def __init__(self,name,height):
         self.name=name
         self.height=height

    def bark(self):
         print(f" {self.name} goes woof!")

    def jump(self):
         print(f"{self.name} jumps {self.height*2} cm high")

dog=Dog("Mickey",55)
dog.bark()
dog.jump()

davids_dog=Dog("Rex",50)
print(f" The dog of david is {davids_dog.name} and its height is {davids_dog.height}")
davids_dog.bark()
davids_dog.jump()

sarahs_dog=Dog("Teacup",20)
print(f" The dog of david is {sarahs_dog.name} and its height is {sarahs_dog.height}")
sarahs_dog.bark()
sarahs_dog.jump()

if davids_dog.height > sarahs_dog.height:
    bigger_dog = davids_dog.name
elif davids_dog.height < sarahs_dog.height:
    bigger_dog = sarahs_dog.name
else:
    bigger_dog = "Both dogs are the same size."

print(bigger_dog)

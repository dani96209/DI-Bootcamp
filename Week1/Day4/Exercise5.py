def make_shirt(size,text):
    print(f"The size of the shirt is {size} and the text is {text}")

make_shirt("small","I love Chicago")

#Modify the make_shirt() function:
def make_shirt(size="large",text="I love Python"):
    print(f"The size of shirt is {size} and the text is {text}")

make_shirt()
def make_shirt(size,text="I love SQL"):
    print(f"The size of shirt is {size} and the text is {text}")
make_shirt("medium")

# Make a shirt of any size withe a different message
make_shirt("Extra large","I love Manhattan")
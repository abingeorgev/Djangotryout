print('Hello, Abin George Varghese')

def hi(name):
    if name == "Ola":
        print("Hi Ola!")
    elif name == "Sonja":
        print("Hi Sonja!")
    else:
        print("Hi anonymous!")
    print("Hi " + name + "!")

if 3 > 4:
    print('It works!')
else:
    hi("Ola")

names = ['Rachel', 'Jeena', 'Ansar', 'Abin']
for name in names:
    hi(name)


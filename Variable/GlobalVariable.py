# this is global variable
# name = "Ismail"


# def printName():
#     # this is function scope variable
#     reName = "Ismail"
#     print(name)


# printName()
# print(reName)


# we can my function scope variable to global variable in python using global keyword

def printName(inputName):
    # this is function scope variable
    global outputName
    outputName = inputName
    # print(name)


printName("Ismail assign as a argument")
print(outputName)

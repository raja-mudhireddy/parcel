class employ:
    small="kid"
    big="elder"
    def __init__(abc,color,height):
        abc.c=color
        abc.h=height
    def myfunction(smart):
        print("user information" +smart.c,smart.h)
person=employ("black", 3.7)
person.myfunction()
print(person.c)
print(person.small)
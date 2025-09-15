def sq():
    a=30
    print("the area is",a*a)
def rect(a,b):
    print("the area of rect is",l*b)
def circle(r):
    return 3.14*r*r
def tri(a,b):
    return 0.5*a*b
while(1):
    print("__MENU__")
    print("1.sq")
    print("2.rect")
    print("3.circle")
    print("4.tri")
    print("5.exit")
    a=int(input("enter the choice "))
    if(a==1):
        sq()
    elif(a==2):
        l=int(input("enter length"))
        b=int(input("enter breadth"))
        rect(a,b)
    elif(a==3):
        r=int(input("enter radius"))
        x=circle(r)
        print("area is",x)
    elif(a==4):
        h=12
        b=10
        
        
        

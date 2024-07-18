
print("we are here to do a little maths.we are converting your values to either radians or degrees as per your choice")
print("is your value in radians or in degrees")
#def gty():tr
try:
    n=int(input("type in your value  "))
    x=int(input("type 1 for radian and 2 for degrees "))
    #    return (n,x)
    if x==1 :
        m=n*180
        print(m)
    elif x==2 :
        m=n/180                                                
        print(m)
    else:
        print("wrong choice")
except ValueError:
    print("please type in integers only")
        
import random

def min3 ( x,y,z):
    if x<y:
        if x<z:
            return x
        else:
            return z
    else:
        if y<z:
            return y
        else:
            return z

def box ( height,width):
    for h in range (height):
        for w in range (width):
            print ("*",end="")
        print()

def find(mylist,key):
    for pos in range(len(mylist)):
        if key == mylist[pos]:
            print (f'found {key} at pos {pos}')

def average_list(my_list):
    sum=0
    for num in my_list:
        sum += num

    avg=sum/len(my_list)
    return avg

def main ():
    print(min3(4, 7, 5))
    print(min3(4, 5, 5))
    print(min3(4, 4, 4))
    print(min3(-2, -6, -100))
    print(min3("Z", "B", "A"))
    print()

    box(7,5)  # Print a box 7 high, 5 across
    print()   # Blank line
    box(3,2)  # Print a box 3 high, 2 across
    print()   # Blank line
    box(3,10) # Print a box 3 high, 10 across

    my_list = [36, 31, 79, 96, 36, 91, 77, 33, 19, 3, 34, 12, 70, 12, 54, 98, 86, 11, 17, 17]
 
    find(my_list, 12)
    find(my_list, 91)
    find(my_list, 80)
    avg = average_list([1,2,3])
    print(avg)

    my_list=[]
    for num in range(10000):
        my_list.append(random.randrange(1,6))
    
    avg = average_list(my_list)
    print(avg)

if __name__ == "__main__":
    main()


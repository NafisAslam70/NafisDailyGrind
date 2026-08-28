def abc(x,y):
    #write your code logic here !!
    try:
        d=x//y
        print(d)
        print("Program Exit")
    except Exception as e:
        print("Division not possible")
        print("Program Exit")
x = int(input())
y = int(input())
abc(x,y)

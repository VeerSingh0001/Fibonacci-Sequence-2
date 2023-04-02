def fib(value):
    firstnum = 0
    secondnum = 1
    if value <= 0:
        print("Please enter a value greater than 0!")
    elif value == 1:
        print(firstnum)
    else:
        print(firstnum, secondnum, end=" ")
        for i in range(2, value):
            result = firstnum + secondnum
            firstnum,secondnum = secondnum,result
            if result <= value:
                print(result, end=" ")
            else:
                break
            
values = int(input("Enter the number till you want to print Fibonacci Sequence: "))
fib(values)
        
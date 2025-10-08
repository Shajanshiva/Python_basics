mark = int(input("Enter a mark"))
print(mark)

match mark:
    case _ if mark <= 100 and mark >= 80 :
        print("A Grade")
    case _ if mark<=79 and mark >= 69:
        Print("B Grade")
    




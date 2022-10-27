for row in range(7):
    for col in range(7):
        if ((col == 0 or col == 5) and row != 0 and row != 3) or (row == 0 and (col > 1 and col < 4)) or (row == 3 and (col >= 0 and col < 4)):
            print(f"*", end=" ")
        else:
            print(end=" ")
    print();

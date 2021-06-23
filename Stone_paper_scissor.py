import random
c_no=random.randint(0,2)
a = 5

while 5>a:

 """
0 = stone
1 = paper
2 = scissor
"""
in_no=int(input("Press 0 for Stone\nPress 1 for Paper\nPress 2 for scissor\n"))
if c_no == in_no:
    print("Match tie")
    a = a-1

elif c_no == 0 and  in_no == 1:
    print("Congrats!!You Win")
    a= a-1

elif c_no == 0 and in_no == 2:
    print("Oops!You Lost")
    a = a - 1

elif c_no == 1 and in_no == 0:
    print("Oops!You Lost")
    a = a - 1

elif c_no == 1 and in_no == 2:
    print("Congrats!!You Win")
    a = a - 1

elif c_no == 2 and in_no == 0:
    print("Congrats!!You Win")
    a = a - 1

elif c_no == 2 and in_no == 1:
    print("Oops!You Lost")
    a = a - 1


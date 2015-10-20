from arithmetics import *

adder = 0

if add(1, 2) == 3:
    print("addition is working fine!")
    adder += 1

if subtract(5, 3) == 2:
    print("subtraction is working fine!")
    adder += 1

if multiply(3, 3) == 9:
    print("multiplication is working fine!")
    adder += 1

if devide(18, 6) == 3:
    print("division is working fine!")
    adder += 1

if adder == 0:
    print("everything's fucked.")

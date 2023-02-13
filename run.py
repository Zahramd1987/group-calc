def calculate():
    operation = input(
        """
please type in the operation:
+ add
- sub
* multi
/ divide
! factorial
"""
    )

    num1 = float(input("enter your num:"))
    num2 = float(input("enter your num:"))
    if operation == "/":
        print("{} / {} =".format(num1, num2))
        print(num1 / num2)

    else:
        print("you have not typed a valid operation")
        # add again() function to calculate()  function again()


def again():
    calculate_again = input(
        """
Do you want calculate again?
please type YES or NO
"""
    )

    if calculate_again.upper() == "YES":
        calculate()
    elif calculate_again.upper() == "NO":
        print("see you later")

    else:
        again()


calculate()

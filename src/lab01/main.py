#! /usr/bin/env python

def main():
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    num4 = int(input())
    num5 = int(input())
    if num1 >= num2 and num1 >= num3 and num1 >= num4 and num1 >= num5:
        print(num1)
    elif num2 >= num1 and num2 >= num3 and num2 >= num4 and num2 >= num5:
        print(num2)
    elif num3 >= num1 and num3 >= num2 and num3 >= num4 and num3 >= num5:
        print(num3)
    elif num4 >= num1 and num4 >= num2 and num4 >= num3 and num4 >= num5:
        print(num4)
    elif num5 >= num1 and num5 >= num2 and num5 >= num4 and num5 >= num4:
        print(num5)
    if num1 <= num2 and num1 <= num3 and num1 <= num4 and num1 <= num5:
        print(num1)
    elif num2 <= num1 and num2 <= num3 and num2 <= num4 and num2 <= num5:
        print(num2)
    elif num3 <= num1 and num3 <= num2 and num3 <= num4 and num3 <= num5:
        print(num3)
    elif num4 <= num1 and num4 <= num2 and num4 <= num3 and num4 <= num5:
        print(num4)
    elif num5 <= num1 and num5 <= num2 and num5 <= num4 and num5 <= num4:
        print(num5)
    # add your code here

if __name__ == "__main__":
    main()


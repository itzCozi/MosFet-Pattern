# Packages
import os
import math
import time

# Vars
W = "Dubskies"
P = "Platypus"

# Functions
def add(num1, num2, num3):
  ans = num1 + num2 + num3
  return ans
def sub(num1, num2, num3):
  ans = num1 - num2 - num3
  return ans
def mul(num1, num2, num3):
  ans = num1 * num2 * num3
  return ans
def div(num1, num2, num3):
  ans = num1 / num2 / num3
  return ans

# Start
num1 = int(input("Enter INT number: "))
num2 = int(input("Enter INT number: "))
num3 = int(input("Enter INT number: "))
X = float(input("Enter FLOAT number: "))
Y = float(input("Enter FLOAT number: "))

# Main
def main():
  global num1, num2, num3, X, Y
  print("____ADD____")
  print("A: " + str(num1))
  print("B: " + str(num2))
  print("C: " + str(num3))
  print("------------")
  print("= " + str(add(num1, num2, num3)))
  time.sleep(3)
  print("____SUB____")
  print("A: " + str(num1))
  print("B: " + str(num2))
  print("C: " + str(num3))
  print("------------")
  print("= " + str(sub(num1, num2, num3)))
  time.sleep(3)
  print("____MUL____")
  print("A: " + str(num1))
  print("B: " + str(num2))
  print("C: " + str(num3))
  print("------------")
  print("= " + str(mul(num1, num2, num3)))
  time.sleep(3)
  print("____DIV____")
  print("A: " + str(num1))
  print("B: " + str(num2))
  print("C: " + str(num3))
  print("------------")
  print("= " + str(div(num1, num2, num3)))
  time.sleep(3)
  print("____END____")
  print("X: " + str(X))
  print("Y: " + str(Y))
  print("------------")
  print(X + Y)
  
# End/Loop
main()
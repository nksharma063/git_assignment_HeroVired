# git_assignment_HeroVired
## All topics covered below are prvided by Hero Vired Faculty and to pratice and document all steps fr solution after the problem statement. 

#### Q.1: You are part of a development team working on a Python application called "CalculatorPlus." The application provides basic arithmetic operations, such as addition, subtraction, multiplication, and division. Your task is to implement a new feature that adds support for calculating the square root of a number. 

a.Create a repository name: git_assignment_HeroVired
b.Create a ‘dev’ branch and add this code.

import math class Calculator:
def add(self, a, b): return a + b
def subtract(self, a, b): return a - b
def multiply(self, a, b):
return a * b
def divide(self, a, b): return a / b

#### TODO: Implement the following function to calculate the square root of a number.
def square_root(self, x):
return math.sqrt(x)
You need to uncomment the above function and complete its implementation to add the square root feature.

if name  == " main":
calculator = Calculator()
num1 = 16
num2 = 4
print(f"{num1} + {num2} = {calculator.add(num1, num2)}") print(f"{num1} - {num2} = {calculator.subtract(num1, num2)}") print(f"{num1} * {num2} = {calculator.multiply(num1, num2)}") print(f"{num1} / {num2} = {calculator.divide(num1, num2)}")

####T ODO: Uncomment and test the square root feature. # num3 = 25
#### print(f"The square root of {num3} = {calculator.square_root(num3)}")

c.Merge this branch with the main branch and make a release of version 1 of the ‘calculator plus app’.
d.Add any of your classmates as collaborators.
e.Implement a feature by creating a new branch called ‘feature/sqrt’.
f.Add the ‘sqrt’ code into it.
g.While you are working on this feature, imagine that one critical bug is reported in the main branch, and you need to switch back to the ‘dev’ branch, create fixes, and apply them while keeping your ‘feature/sqrt’ branch up-to-date. For this, you need to create

The bug fixation is in the divide function and the new function should be: def divide(self, a, b):
if b == 0:
raise ValueError("Cannot divide by zero.") return a / b

h.After completing the feature implementation and ensuring that the application works correctly, create a pull request targeting the main branch.
i.Request a code review from a team member and make any necessary improvements based on the review feedback.
j.Once the code reviewer approves your pull request, merge the "feature/sqrt" branch into the ‘dev’ branch.
k.Finally, do the testing in the ‘dev’ branch itself and merge it into the ‘main’ branch and create a ‘version 2’ release.

Solution:

### Edited the file and created one class calculator with just one init methods to initiate the class.
#### Added Dev branch worked and added logical fucntions and then created on object and called them by passing parameters.
##### Added feature/sqrt and started adding the sqrt fucntion.
####### Got some feature update in Dev branch, updated the value error and started working on feature qsqrt, invited one collaboartor, will asked for feedback and merge the feature sqrt to Dev and then to Main to release verson 2.


### Question 3
#### Q.3: In this same GitHub repository, create a new branch ‘geometry-calculator’, we'll work on a simple Python program that calculates the area of a circle and the area of a rectangle. We'll use Git stash to switch between working on multiple features (calculating circle area and calculating rectangle area) without committing incomplete changes.

 

import math
class GeometryCalculator:
def calculate_circle_area(self, radius): return math.pi * radius ** 2
def calculate_rectangle_area(self, length, width): return length * width
if      name      == "     main     ": calculator = GeometryCalculator()
# TODO: Implement the feature to calculate the area of a circle # radius = 5
# print(f"The area of the circle with radius {radius} =
{calculator.calculate_circle_area(radius)}")
# TODO: Implement the feature to calculate the area of a rectangle # length = 10
# width = 6
# print(f"The area of the rectangle with length {length} and width {width} =
{calculator.calculate_rectangle_area(length, width)}")

SOlutions.
Created one main branch geometry-calculator. Edited basic main code with just class name.
Created one branch circle area and impemneted the __init__ method called the math fucntion and implmeneted the area of circle logic.
Stashed the changed for a while.
Created one more branch rectangle area, implemented the logic again with __init__ method [this ste i created to create merge problem when binding everything into main], stashed teh changes,.
Swicthed back and tried bring back the stash but accidentl used the --index swicth and Calculator.py impleneted in all new brach and wanted to merge.
Deleted the change, again made some changes in both bran ch, swicthed in one and another.
git stash apply stash@{} index to apply the stash from WIP list through git stash list.
now will push both geometry calculator, and then to dev , will review ad push to main and create one more version.

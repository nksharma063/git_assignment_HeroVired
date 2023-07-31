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

### Q.2: For a project that deals with large binary files, integrate Git LFS (Large File Storage) to handle these files efficiently. Demonstrate how to add, commit, and push binary files to the repository, ensuring they are tracked by Git LFS correctly. Clone the repository on another machine to verify that the binary files are downloaded correctly. 

Git lfs will list all the details about lfs.
This works in multiple way basically it hold the pointer in repo and upoad teh large file to git server and later you can download them for use.

git lfs install
git lfs track "*.iso", "*.pdf", "*.gzip", "*.zip"
git add .gitattributes  --> it will add above extesion so in future when you will do some activity in branch , it will perform some oeratopn.
git checkout to branch
git commit , add and push to branch normally


# Steps i followed, are in "main" branch, later space was not available to work on another branch becasue the quota is full.

### git lfs install
### git lfs track "*.iso", "*.pdf", "*.gzip", "*.zip"
### git add .gitattributes  --> it will add above extesion so in future when you will do some activity in branch , it will perform some oeratopn.
### i added the files and when cloned teh same repo in different machine only pointers are copied but some git lfs was broken in ubuntu so further not able to work.
### i created  lfs branch but further was not abel to complete.

Complete Documentation
In the repository ‘git_assignment_HeroVired’, create a branch ‘lfs’. Upload any large file whose size is over ‘200mb’ and try to push this file into the repository. 
Like Git, Git LFS commands are separated into high level ("porcelain")
commands and low level ("plumbing") commands.




=== High level porcelain commands

git lfs checkout:
  Populate working copy with real content from Git LFS files.
git lfs dedup:
  De-duplicate Git LFS files.
git lfs env:
  Display the Git LFS environment.
git lfs ext:
  Display Git LFS extension details.
git lfs fetch:
  Download Git LFS files from a remote.
git lfs fsck:
  Check Git LFS files for consistency.
git lfs install:
  Install Git LFS configuration.
git lfs lock:
  Set a file as "locked" on the Git LFS server.
git lfs locks:
  List currently "locked" files from the Git LFS server.
git lfs logs:
  Show errors from the Git LFS command.
git lfs ls-files:
  Show information about Git LFS files in the index
  and working tree.
git lfs migrate:
  Migrate history to or from Git LFS
git lfs prune:
  Delete old Git LFS files from local storage
git lfs pull:
  Fetch Git LFS changes from the remote & checkout any required working tree
  files.
git lfs push:
  Push queued large files to the Git LFS endpoint.
git lfs status:
  Show the status of Git LFS files in the working
  tree.
git lfs track:
  View or add Git LFS paths to Git attributes.
git lfs uninstall:
  Uninstall Git LFS by removing hooks and smudge/clean filter configuration.
git lfs unlock:
  Remove "locked" setting for a file on the Git LFS server.
git lfs untrack:
  Remove Git LFS paths from Git Attributes.
git lfs update:
  Update Git hooks for the current Git repository.
git lfs version:
  Report the version number.

=== Low level plumbing commands

git lfs clean:
  Git clean filter that converts large files to pointers.
git lfs filter-process:
  Git process filter that converts between large files and pointers.
git lfs merge-driver:
  Merge text-based LFS files
git lfs pointer:
  Build and compare pointers.
git lfs post-checkout:
  Git post-checkout hook implementation.
git lfs post-commit:
  Git post-commit hook implementation.
git lfs post-merge:
  Git post-merge hook implementation.
git lfs pre-push:
  Git pre-push hook implementation.
git lfs smudge:
  Git smudge filter that converts pointer in blobs to the actual content.
git lfs standalone-file:
  Git LFS standalone transfer adapter for file URLs (local paths).

Examples
--------

To get started with Git LFS, the following commands can be used.

. Setup Git LFS on your system. You only have to do this once per user
account:
+

git lfs install

. Choose the type of files you want to track, for examples all ISO
images, with git lfs track:
+

git lfs track "*.iso"

. The above stores this information in gitattributes(5) files, so that
file needs to be added to the repository:
+


. Commit, push and work with the files normally:
+

git add file.iso
git commit -m "Add disk image"
git push

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




# Will merge dev to main as it does have calculator and geometry to make the final release. Thank you. Review done by Tilak , thank you.

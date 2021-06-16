    3  git clone https://github.com/insighttechworld/local-devops-project.git
    4  ls -la
    5  ls -l
    6  cd local-devops-project/
    7  ls -l
    8  cat README.md
    9  vi README.md
   10  touch appserver.py
   11  vi appserver.py
   12  history
[remote@dev-server local-devops-project]$ cat appserver.py
# Solve the quadratic equation ax**2 + bx + c = 0

# import complex math module
import cmath

a = 1
b = 5
c = 6

# calculate the discriminant
d = (b**2) - (4*a*c)

# find two solutions
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)


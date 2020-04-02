import sys
import re

#import the test needed doing and the file
test_name = sys.argv[1]
filename = sys.argv[2]

#open the file
file = open(filename, "r")

#from the file import in the start state, end state and restricted values
start_value = file.readline()
goal = file.readline()
restricted_raw = file.readline()
#make it so that the restricted values are in a list instead of a string
restricted = list(restricted_raw.split(","))

#troubleshooting area

#####################################

count = 0
expanded_nodes = []
results = []

#returns the child nodes of n given the previously changed number y [index] ensuring we dont reduce from 0 and increase from 9
def return_children(n, y):
    if y == 0:
        if re.findall("0\d\d",n) or re.findall("9\d\d",n):
            if re.findall("\d0\d",n) or re.findall("\d9\d",n):
                if re.findall("\d\d0",n) or re.findall("\d\d9",n):
                    #We have 1, 2, 3 values invalid
                    pass
                else:
                    #we 1, 2 values invalid
                    pass
            else:
                #we have invalid changed values for first 1 value, need to continue for 3rd value
                if re.findall("\d\d0",n) or re.findall("\d\d9",n):
                    pass
                else:
                    #we have 1st value invalid
                    pass
        else:
            pass
        values = [n - 100, n + 100, n - 10, n + 10, n - 1, n + 1]
    elif y == 1:
        #do not increase or decrease the first number
        values = [n - 10, n + 10, n - 1, n + 10]
    elif y == 2:
        #do not increase or decrease the second number
        values = [n - 100, n + 100, n - 1, n + 1]
    elif y == 3:
        #do not increase or decrease the third number
        values = [n - 100, n + 100, n - 10, n + 10]
    node_comparison = values.insert(0,n)
    expanded_nodes.append(node_comparison)
    return values

if test_name == "BFS":
    #code for BFS
    current_node_expanded = return_children(start_value, 0)
    count += 1
    while count <= 1000:


        count += 1
    pass
elif test_name == "DFS":
    #code for DFS - left most and continue down until you find a repeated node

    pass
elif test_name == "IDS":
    #code for IDS

    pass
elif test_name == "Greedy":
    #code for Greedy

    pass
elif test_name == "A*":
    #code for A*

    pass
elif test_name == "Hill-climbing":
    #code for Hill-climbing

    pass
else:
    print("error: the test defined is not found within this program.")

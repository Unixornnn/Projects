import sys

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

def return_children(n, y):
    if y == 0:
        return [n - 100, n + 100, n - 10, n + 10, n - 1, n + 1]
    elif y == 1:
        #do not increase or decrease the first number
        return [n - 10, n + 10, n - 1, n + 10]
    elif y == 2:
        #do not increase or decrease the second number
        return [n - 100, n + 100, n - 1, n + 1]
    elif y == 3:
        #do not increase or decrease the third number
        return [n - 100, n + 100, n - 10, n + 10]

if test_name == "BFS":
    #code for BFS
    return_children(start_value, 0)
    pass
elif test_name == "DFS":
    #code for DFS

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

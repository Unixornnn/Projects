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
expanded_nodes = [(start_value.rstrip("\n"),0)]
results = [start_value.strip("\n")]

#returns the child nodes of n given the previously changed number y [index] ensuring we dont reduce from 0 and increase from 9
def return_children(n, y):
    values = []
    n = n.zfill(3)
    if y == 0:
        #able to change all 3 values
        if re.findall("0\d\d",n):
            pass
        else:
            node = str(int(n) - 100)
            values.append(node.zfill(3))
        if re.findall("9\d\d",n):
            pass
        else:
            node = str(int(n) + 100)
            values.append(node.zfill(3))
        if re.findall("\d0\d",n):
            pass
        else:
            node = str(int(n) - 10)
            values.append(node.zfill(3))
        if re.findall("\d9\d",n):
            pass
        else:
            node = str(int(n) + 10)
            values.append(node.zfill(3))
        if re.findall("\d\d0",n):
            pass
        else:
            node = str(int(n) - 1)
            values.append(node.zfill(3))
        if re.findall("\d\d9",n):
            pass
        else:
            node = str(int(n) + 1)
            values.append(node.zfill(3))

    elif y == 1:
        #do not increase or decrease the first number
        if re.findall("\d0\d",n):
            pass
        else:
            node = str(int(n)-10)
            values.append(node.zfill(3))
        if re.findall("\d9\d",n):
            pass
        else:
            node = str(int(n)+10)
            values.append(node.zfill(3))
        if re.findall("\d\d0",n):
            pass
        else:
            node = str(int(n)-1)
            values.append(node.zfill(3))
        if re.findall("\d\d9",n):
            pass
        else:
            node = str(int(n)+1)
            values.append(node.zfill(3))

    elif y == 2:
        #do not increase or decrease the second number
        if re.findall("0\d\d",n):
            pass
        else:
            node = str(int(n)-100)
            values.append(node.zfill(3))
        if re.findall("9\d\d",n):
            pass
        else:
            node = str(int(n)+100)
            values.append(node.zfill(3))
        if re.findall("\d\d0",n):
            pass
        else:
            node = str(int(n)-1)
            values.append(node.zfill(3))
        if re.findall("\d\d9",n):
            pass
        else:
            node = str(int(n)+1)
            values.append(node.zfill(3))
    elif y == 3:
        #do not increase or decrease the third number
        if re.findall("0\d\d",n):
            pass
        else:
            node = str(int(n)-100)
            values.append(node.zfill(3))
        if re.findall("9\d\d",n):
            pass
        else:
            node = str(int(n)+100)
            values.append(node.zfill(3))
        if re.findall("\d0\d",n):
            pass
        else:
            node = str(int(n)-10)
            values.append(node.zfill(3))
        if re.findall("\d9\d",n):
            pass
        else:
            node = str(int(n)+10)
            values.append(node.zfill(3))
    expanded_nodes.append((values[0],y))
    return values

def lowest_heuristic_index(x, y):
    #retuns the index of the highest heuristic for a given set of child nodes
    lowest_index = 0
    lowest_value = 1000
    i = 0
    value = []
    while i < len(x):
        if x[i] in restricted:
            value.append(1000)
        elif (x[i],y) in expanded_nodes:
            value.append(1000)
        else:
            #calculate the manhattan distance for each child node of an expanded node
            number = str(x[i])
            value1 = abs(int(number[0]) - int(goal[0]))
            value2 = abs(int(number[1]) - int(goal[1]))
            value3 = abs(int(number[2]) - int(goal[2]))
            value.append(value1 + value2 + value3)
        i+= 1
    i = 0
    while i < len(value):
        if value[i] < lowest_value:
            lowest_index = i
            lowest_value = value[i]
        elif value[i] == lowest_value:
            lowest_index = i
            lowest_value = value[i]
        else:
            pass
        i+= 1
    return lowest_index

def check_expanded(x,y):
    #may be broke, need to check further before further implementation
    #check whether this node has already been expanded, x is the value, and y is the previously changed value
    for i in expanded_nodes:
        if i == (x,y):
            return True
        else:
            return False

if test_name == "BFS":
    #code for BFS
    #dont generate the children everytime and keep track of the length of the original children creation - only iterate down once thats done
    prev_change= 0
    index = 0
    while count <= 1000:
        while index < len(results):
            if (results[i],prev_change) in expanded_nodes:
                x = return_children(results,[i],prev_change)
                for i in x:
                    results.insert(index,i)
                index += len(x)
            else:
                expanded_nodes.append(i,prev_change)
                count += 1
            if index + 1 = len(results):
                index = 0

elif test_name == "DFS":
    #code for DFS - left most and continue down until you find a repeated node
    count = 0
    prev_change = 0
    index = 1
    while count <= 1000:
        x = return_children(results[count], prev_change)
        if x[index] in expanded_nodes:
            index += 1
            continue
        elif x[index] in restricted:
            index += 1
            continue
        changed_value = abs(int(x[index]) - int(x[0]))
        if changed_value == 100:
            prev_change = 1
        elif changed_value == 10:
            prev_change = 2
        elif changed_value == 1:
            prev_change = 3
        results.append(x[index])
        if int(x[index]) == int(goal):
            break
        expanded_nodes.append((x[index],prev_change))
        count += 1
        index = 1

elif test_name == "IDS":
    #code for IDS

    pass
elif test_name == "Greedy":
    count = 0
    prev_change = 0
    while count <= 1000:
        x = return_children(results[count], prev_change)
        y = lowest_heuristic_index(x,prev_change)
        changed_value = abs(int(x[y]) - int(x[0]))
        if changed_value == 100:
            prev_change = 1
        elif changed_value == 10:
            prev_change = 2
        elif changed_value == 1:
            prev_change = 3
        results.append(x[y])
        if int(x[y]) == int(goal):
            break
        expanded_nodes.append((x[y],prev_change))
        count += 1

    #code for Greedy

    pass
elif test_name == "A*":
    #code for A*

    pass
elif test_name == "Hill-climbing":
    #code for Hill-climbing
    #implement a value which gives the number of digits that are in the correct position, seeking to increase this number with each move, or at least not decrease

    pass
else:
    print("error: the test defined is not found within this program.")

print(results)

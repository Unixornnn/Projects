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
restricted_raw = file.read()
#make it so that the restricted values are in a list instead of a string
restricted_split = list(restricted_raw.split(", "))
restricted = []
for i in restricted_split:
    restricted.append(i.strip())

#troubleshooting area

#####################################

count = 0
#expanded_nodes = [(start_value.rstrip("\n"),0)]
expanded_nodes = [start_value.rstrip("\n") + "0"]
bfs_expanded = [start_value.strip()]
results = [start_value.strip("\n")]
success = False

#returns the child nodes of n given the previously changed number y [index] ensuring we dont reduce from 0 and increase from 9
def return_children(n, y):
    values = []
    n = n.zfill(3)
    if y == 0:
        #able to change all 3 values
        values.append(n.zfill(3).rstrip("\n"))
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
        values.append(n.zfill(3).rstrip("\n"))
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
        values.append(n.zfill(3).rstrip("\n"))
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
        values.append(n.zfill(3).rstrip("\n"))
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
    return values

def lowest_heuristic_index(x, y):
    #retuns the index of the highest heuristic for a given set of child nodes
    lowest_index = 0
    lowest_value = 1000
    i = 0
    value = []
    while i < len(x):
        if str(x[i]) in restricted:
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

def get_heuristic(n,m):
    first_value = abs(n[0] - m[0])
    second_value = abs(n[1] - m[1])
    third_value = abs(n[2] - m[2])
    final_value = first_value + second_value + third_value
    return final_value

if test_name == "BFS":
    count = 1
    prev_change = 0
    second = []
    results = [start_value.strip()]
    index = 0
    x = return_children(start_value,0)
    while count <= 1000:
        if count == 1:
            for i in x[1:]:
                results.append(i)
                changed_value = abs(int(i) - int(x[0]))
                if changed_value == 100:
                    prev_change = 1
                elif changed_value == 10:
                    prev_change = 2
                elif changed_value == 1:
                    prev_change = 3
                if i in restricted:
                    continue
                elif (str(i) + str(prev_change)) in expanded_nodes:
                    continue
                elif int(i) == int(goal):
                    success = True
                    break
                    break
                second.append(return_children(i,prev_change))
                count += 1
        else:
            for i in x:
                if success == True:
                    break
                for a in i[1:]:
                    if success == True:
                        break
                    changed_value = abs(int(a) - int(i[0]))
                    if changed_value == 100:
                        prev_change = 1
                    elif changed_value == 10:
                        prev_change = 2
                    elif changed_value == 1:
                        prev_change = 3
                    if a in restricted:
                        continue
                    elif (str(a) + str(prev_change)) in expanded_nodes:
                        continue
                    results.append(a)
                    if int(a) == int(goal):
                        success = True
                        break
                    expanded_nodes.append(str(a) + str(prev_change))
                    second.append(return_children(a,prev_change))
                    count += 1
        x = second
        if success == True:
            break

elif test_name == "DFS":
    #code for DFS - left most and continue down until you find a repeated node
    count = 0
    prev_change = 0
    index = 0
    nodes = []
    x = return_children(start_value, prev_change)
    for i in x:
        nodes.append(i)
    while count <= 1000:
        changed_value = abs(int(nodes[index]) - int(nodes[0]))
        if changed_value == 100:
            prev_change = 1
        elif changed_value == 10:
            prev_change = 2
        elif changed_value == 1:
            prev_change = 3
        node = nodes[index] + str(prev_change)
        if node in expanded_nodes:
            index += 1
            continue
        elif node[0:3] in restricted:
            index += 1
            continue
        else:
            expanded_nodes.append(node)
            count += 1
            if int(nodes[index]) == int(goal):
                success = True
                break
            x = return_children(node[0:3],node[3])
            nodes = (nodes[0:index + 1] + x[0:] + nodes[index + 2:])
            index = 0
            continue

elif test_name == "IDS":
    #code for IDS

    pass

elif test_name == "Greedy":
    #FINISHED
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
        if x[y] == results[count]:
            success = False
            break
        results.append(x[y])
        #expanded_nodes.append((x[y],prev_change))
        expanded_nodes.append(x[y] + str(prev_change))
        if int(x[y]) == int(goal):
            success = True
            break
        count += 1

elif test_name == "A*":
    values = []
    heuristic_values = []
    node = start_value
    current = 0
    count = 0
    prev_change
    minimum = 1000
    depth = 0
    while count <= 1000:
        x = return_children(node[0:3],node[4])
        for i in x[1:]:
            changed_value = abs(int(x[y]) - int(x[0]))
            if changed_value == 100:
                prev_change = 1
            elif changed_value == 10:
                prev_change = 2
            elif changed_value == 1:
                prev_change = 3
            values.append((str(node) + str(depth) + str(prev_change))
        for i in values:
            heuristic = get_heuristic(i) + i[3]
            heuristic_values.append(heuristic)
        for i in heuristic_values:
            if i < minimum:
                current = i
            else:
                continue
        index = heuristic_values.index(current)
        node = values[index]
        if node in expanded_nodes:
            
    #code for A*

elif test_name == "Hill-climbing":
    #FINISHED
    #code for Hill-climbing
    #implement a value which gives the number of digits that are in the correct position, seeking to increase this number with each move, or at least not decrease
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
        original_value = x[0]
        new_value = x[y]
        original_heuristic = ((abs(int(original_value[0]) - int(goal[0]))) + (abs(int(original_value[1]) - int(goal[1]))) + (abs(int(original_value[2]) - int(goal[2]))))
        new_heuristic = ((abs(int(new_value[0]) - int(goal[0]))) + (abs(int(new_value[1]) - int(goal[1]))) + (abs(int(new_value[2]) - int(goal[2]))))
        if new_heuristic < original_heuristic:
            expanded_nodes.append(x[y] + str(prev_change))
            results.append(x[y])
            count += 1
            if int(x[y]) == int(goal):
                success = True
                break
        else:
            success == False
            break

else:
    print("error: the test defined is not found within this program.")

if success == True:
    #insert the direct path print here
    for i in results:
        if results.index(i) == len(results) - 1:
            print(i)
        else:
            print(i,end = ', ')
else:
    print("No solution found.")
    print(results)

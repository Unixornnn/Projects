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
expanded_nodes = [start_value.rstrip("\n") + "0" + "0"]
greedy_expanded = [start_value.rstrip("\n") + "0"]
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
        elif (str(x) + str(y)) in greedy_expanded:
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

if test_name == "BFS":
    count = 1
    prev_change = 0
    second = []
    results = [start_value.strip()]
    index = 0
    posneg = 0
    x = return_children(start_value,0)
    while count <= 1000:
        if count == 1:
            for i in x[1:]:
                results.append(i)
                changed_value = (int(i) - int(x[0]))
                if changed_value == 100:
                    prev_change = 1
                    posneg = 1
                elif changed_value == -100:
                    prev_change = 1
                    posneg = 0
                elif changed_value == 10:
                    prev_change = 2
                    posneg = 1
                elif changed_value == -10:
                    prev_change = 2
                    posneg = 0
                elif changed_value == 1:
                    prev_change = 3
                    posneg = 1
                elif changed_value == -1:
                    prev_change = 3
                    posneg = 0
                if i in restricted:
                    continue
                elif (str(i) + str(prev_change) + str(posneg)) in expanded_nodes:
                    continue
                elif int(i) == int(goal):
                    success = True
                    break
                expanded_nodes.append(str(i) + str(prev_change) + str(posneg))
                second.append(return_children(i,prev_change))
                count += 1
        else:
            for i in x:
                if success == True:
                    break
                for a in i[1:]:
                    if success == True:
                        break
                    changed_value = int(a) - int(i[0])
                    if changed_value == 100:
                        prev_change = 1
                        posneg = 1
                    elif changed_value == -100:
                        prev_change = 1
                        posneg = 0
                    elif changed_value == 10:
                        prev_change = 2
                        posneg = 1
                    elif changed_value == -10:
                        prev_change = 2
                        posneg = 0
                    elif changed_value == 1:
                        prev_change = 3
                        posneg = 1
                    elif changed_value == -1:
                        prev_change = 3
                        posneg = 0
                    if a in restricted:
                        continue
                    elif (str(a) + str(prev_change) + str(posneg)) in expanded_nodes:
                        continue
                    results.append(a)
                    if int(a) == int(goal):
                        expanded_nodes.append(str(a) + str(prev_change) + str(posneg))
                        success = True
                        break
                    expanded_nodes.append(str(a) + str(prev_change) + str(posneg))
                    second.append(return_children(a,prev_change))
                    count += 1
        x = second
        if success == True:
            break

elif test_name == "DFS":
    #code for DFS - left most and continue down until you find a repeated node
    pass

elif test_name == "IDS":
    #code for IDS

    pass

elif test_name == "Greedy":
    #FINISHED
    count = 0
    prev_change = 0
    posneg = 0
    node = start_value.strip()
    while count <= 1000:
        x = return_children(node, prev_change)
        original = x[0]
        x.remove(x[0])
        y = lowest_heuristic_index(x, prev_change)
        changed_value = int(x[y]) - int(original)
        if changed_value == 100:
            prev_change = 1
            posneg = 1
        elif changed_value == -100:
            prev_change = 1
            posneg = 0
        elif changed_value == 10:
            prev_change = 2
            posneg = 1
        elif changed_value == -10:
            prev_change = 2
            posneg = 0
        elif changed_value == 1:
            prev_change = 3
            posneg = 1
        elif changed_value == -1:
            prev_change = 3
            posneg = 0
        if x[y] == results[count]:
            success = False
            break
        results.append(x[y])
        node = x[y]
        greedy_expanded.append(x[y] + str(prev_change))
        if int(x[y]) == int(goal):
            success = True
            break
        count += 1

elif test_name == "A*":
    pass
    #code for A*

elif test_name == "Hill-Climbing":
    count = 0
    prev_change = 0
    posneg = 0
    while count <= 1000:
        x = return_children(results[count], prev_change)
        original = x[0]
        x.remove(x[0])
        y = lowest_heuristic_index(x, prev_change)
        changed_value = int(x[y]) - int(original)
        if changed_value == 100:
            prev_change = 1
            posneg = 1
        elif changed_value == -100:
            prev_change = 1
            posneg = 0
        elif changed_value == 10:
            prev_change = 2
            posneg = 1
        elif changed_value == -10:
            prev_change = 2
            posneg = 0
        elif changed_value == 1:
            prev_change = 3
            posneg = 1
        elif changed_value == -1:
            prev_change = 3
            posneg = 0
        new_value = x[y]
        original_heuristic = ((abs(int(original[0]) - int(goal[0]))) + (abs(int(original[1]) - int(goal[1]))) + (abs(int(original[2]) - int(goal[2]))))
        new_heuristic = ((abs(int(new_value[0]) - int(goal[0]))) + (abs(int(new_value[1]) - int(goal[1]))) + (abs(int(new_value[2]) - int(goal[2]))))
        if new_heuristic < original_heuristic:
            greedy_expanded.append(x[y] + str(prev_change))
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

#below is how my code handles the values generated in the tests above


if success == True:
    #insert the direct path print here
    if test_name == "Greedy" or test_name == "Hill-Climbing":
        for i in results:
            if results.index(i) == len(results) - 1:
                print(i)
            else:
                print(i,end = ', ')
    else:
        current = int(goal)
        final = []
        finished = False
        posneg = 0
        while True:
            for i in expanded_nodes:
                value = int(i[0:3])
                posneg = int(i[4])
                changed_value = int(i[3])
                if value == current:
                    if len(final) >= 2:
                        if final[0] == final[1]:
                            finished = True
                            break
                    final.insert(0,str(value).zfill(3))
                    if posneg == 1:
                        #means we added 1 to get to this number, therefore we need to subtract to get new goal
                        if changed_value == 1:
                            current = value - 100
                        elif changed_value == 2:
                            current = value - 10
                        elif changed_value == 3:
                            current = value - 1
                    elif posneg == 0:
                        #need to add 1
                        if changed_value == 1:
                            current = value + 100
                        elif changed_value == 2:
                            current = value + 10
                        elif changed_value == 3:
                            current = value + 1
                else:
                    pass
            if finished == True:
                break
    #correct formatting for printing the above values (final)
        for i in final[1:]:
            if final.index(i) == len(final) - 1:
                print(i)
            else:
                print(i, end = ', ')

    #
    for i in results:
        if results.index(i) == len(results) - 1:
            print(i)
        else:
            print(i,end = ', ')
else:
    print("No solution found.")
    for i in results:
        if results.index(i) == len(results) - 1:
            print(i)
        else:
            print(i,end = ', ')

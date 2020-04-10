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
restricted_split = list(restricted_raw.split(","))
restricted = []
for i in restricted_split:
    restricted.append(i.strip())

class What:
    def __init__(self,v,c,p):
        self.value = v
        self.children = c
        self.parent = p

    def get_parent(self):
        return self.parent

#troubleshooting area

#####################################

count = 0
expanded_nodes = []
greedy_expanded = []
results = []
success = False

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

def lowest_heuristic_index_tuple(x):
    lowest_index = 0
    lowest_value = 1000
    i = 0
    values = []
    while i < len(x):
        value = ((x[i])[0])
        parent = ((x[i])[1])
        changed_value = int(value) - int(parent)
        if changed_value == 0:
            prev_change = 0
            posneg = 0
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
        if str(value) in restricted:
            values.append(1000)
        elif (str(value) + str(prev_change)) in greedy_expanded:
            values.append(1000)
        else:
            #calculate the manhattan distance for each child node of an expanded node
            number = value
            value1 = abs(int(number[0]) - int(goal[0]))
            value2 = abs(int(number[1]) - int(goal[1]))
            value3 = abs(int(number[2]) - int(goal[2]))
            values.append(value1 + value2 + value3)
        i+= 1
    i = 0
    while i < len(values):
        if values[i] < lowest_value:
            lowest_index = i
            lowest_value = values[i]
        elif values[i] == lowest_value:
            lowest_index = i
            lowest_value = values[i]
        else:
            pass
        i+= 1
    return lowest_index

def get_heuristic_a(x):
    lowest_index = 0
    lowest_value = 1000
    i = 0
    values = []
    while i < len(x):
        value = ((x[i])[0])
        parent = ((x[i])[1])
        changed_value = int(value) - int(parent)
        if changed_value == 0:
            prev_change = 0
            posneg = 0
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
        if str(value) in restricted:
            values.append(1000)
        elif (str(value) + str(prev_change)) in greedy_expanded:
            values.append(1000)
        else:
            #calculate the manhattan distance for each child node of an expanded node
            number = value
            value1 = abs(int(number[0]) - int(goal[0]))
            value2 = abs(int(number[1]) - int(goal[1]))
            value3 = abs(int(number[2]) - int(goal[2]))
            distance = get_level(value) - 1
            values.append(value1 + value2 + value3 + distance)
        i+= 1
    i = 0
    while i < len(values):
        if values[i] < lowest_value:
            lowest_index = i
            lowest_value = values[i]
        elif values[i] == lowest_value:
            lowest_index = i
            lowest_value = values[i]
        else:
            pass
        i+= 1
    return lowest_index

def get_level(y):
    final = []
    current = y
    prev_changed_val = 0
    success = False
    while True:
        for i in expanded_nodes:
            value = int(i[0:3])
            posneg = int(i[4])
            changed_value = int(i[3])
            if value == current:
                if changed_value == prev_changed_val:
                    continue
                if str(i) == (str(start_value.strip()) + "00"):
                    success = True
                    final.insert(0,str(value).zfill(3))
                    break
                if len(final) >= 2:
                    if final[0] == final[1]:
                        success = True
                        final.insert(0,str(value).zfill(3))
                        break
                final.insert(0,str(value).zfill(3))
                if posneg == 1:
                    #means we added 1 to get to this number, therefore we need to subtract to get new goal
                    if changed_value == 1:
                        current = value - 100
                        prev_changed_val = 1
                    elif changed_value == 2:
                        current = value - 10
                        prev_changed_val = 2
                    elif changed_value == 3:
                        current = value - 1
                        prev_changed_val = 3
                elif posneg == 0:
                    #need to add 1
                    if changed_value == 1:
                        current = value + 100
                        prev_changed_val = 1
                    elif changed_value == 2:
                        current = value + 10
                        prev_changed_val = 2
                    elif changed_value == 3:
                        current = value + 1
                        prev_changed_val = 3
            else:
                continue
        if success == True:
            break
    return len(final)


if test_name == "B":
    count = 0
    prev_change = 0
    add_parent = []
    index = 0
    node = start_value.strip()
    values = []
    expanded_nodes = [str(node) + "0" + "0"]
    results = [node]
    while count <= 1000:
        x = return_children(node,prev_change)
        for i in x:
            add_parent.append((i,node))
        values = values + add_parent
        value = ((values[index])[0])
        parent = ((values[index])[1])
        changed_value = int(value) - int(parent)
        if changed_value == 0:
            prev_change = 0
            posneg = 0
        elif changed_value == 100:
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
        if ((values[index])[0]) in restricted:
            index += 1
            continue
        elif (str((values[index])[0]) + str(prev_change) + str(posneg)) in expanded_nodes:
            index += 1
            continue
        results.append((values[index])[0])
        node = ((values[index])[0])
        values.remove(values[index])
        count += 1
        if int(node) == int(goal):
            expanded_nodes.append(str(node) + str(prev_change) + str(posneg))
            success = True
            break
        expanded_nodes.append(str(node) + str(prev_change) + str(posneg))

elif test_name == "D":
    count = 0
    prev_change = 0
    index = 0
    node = start_value.strip()
    values = [node]
    results = [node]
    expanded_nodes = [str(node) + "0" + "0"]
    while count <= 1000:
        x = return_children(node,prev_change)
        values = x + values
        changed_value = int(values[index]) - int(node)
        if changed_value == 0:
            prev_change = 0
            posneg = 0
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
        if values[index] in restricted:
            index += 1
            continue
        elif (str(values[index]) + str(prev_change) + str(posneg)) in expanded_nodes:
            index += 1
            continue
        results.append(values[index])
        node = values[index]
        values.remove(values[index])
        count += 1
        index = 0
        if int(node) == int(goal):
            expanded_nodes.append(str(node) + str(prev_change) + str(posneg))
            success = True
            break
        expanded_nodes.append(str(node) + str(prev_change) + str(posneg))

elif test_name == "I":
    #code for IDS

    pass

elif test_name == "G":
    #FINISHED
    count = 0
    prev_change = 0
    posneg = 0
    node = start_value.strip()
    values = []
    add_parent = []
    results = [node]
    while count <= 50:
        x = return_children(node,prev_change)
        for i in x:
            add_parent.append((i,node))
        values = values + add_parent
        y = lowest_heuristic_index_tuple(values)
        node = ((values[y])[0])
        parent = ((values[y])[1])
        changed_value = int(node) - int(parent)
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
        results.append(node)
        values.remove(values[y])
        greedy_expanded.append(str(node) + str(prev_change))
        if int(node) == int(goal):
            success = True
            break
        count += 1

elif test_name == "A":
    count = 0
    prev_change = 0
    posneg = 0
    node = start_value.strip()
    values = []
    add_parent = []
    results = [node]
    while count <= 1000:
        x = return_children(node,prev_change)
        for i in x:
            add_parent.append((i,node))
        values = values + add_parent
        y = get_heuristic_a(values)
        node = ((values[y])[0])
        parent = ((values[y])[1])
        changed_value = int(node) - int(parent)
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
        results.append(node)
        greedy_expanded.append(str(node) + str(prev_change))
        if int(node) == int(goal):
            success = True
            break
        count += 1
    #code for A*

elif test_name == "H":
    count = 0
    prev_change = 0
    posneg = 0
    node = start_value.strip()
    results = [node]
    while count <= 1000:
        x = return_children(node, prev_change)
        original = node
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
            node = x[y]
            if int(x[y]) == int(goal):
                success = True
                break
        else:
            success == False
            break

#below is how my code handles the values generated in the tests above

if success == True:
    #insert the direct path print here
    if test_name == "G" or test_name == "H":
        for i in results:
            i.strip()
        print((",".join(results)).strip())
    else:
        current = int(goal.zfill(3))
        final = []
        prev_changed_val = 0
        posneg = 0
        success = False
        while True:
            for i in expanded_nodes:
                value = int(i[0:3])
                posneg = int(i[4])
                changed_value = int(i[3])
                if value == current:
                    if changed_value == prev_changed_val:
                        continue
                    if str(i) == (str(start_value.strip()) + "00"):
                        success = True
                        final.insert(0,str(value).zfill(3))
                        break
                    if len(final) >= 2:
                        if final[0] == final[1]:
                            success = True
                            final.insert(0,str(value).zfill(3))
                            break
                    final.insert(0,str(value).zfill(3))
                    if posneg == 1:
                        #means we added 1 to get to this number, therefore we need to subtract to get new goal
                        if changed_value == 1:
                            current = value - 100
                            prev_changed_val = 1
                        elif changed_value == 2:
                            current = value - 10
                            prev_changed_val = 2
                        elif changed_value == 3:
                            current = value - 1
                            prev_changed_val = 3
                    elif posneg == 0:
                        #need to add 1
                        if changed_value == 1:
                            current = value + 100
                            prev_changed_val = 1
                        elif changed_value == 2:
                            current = value + 10
                            prev_changed_val = 2
                        elif changed_value == 3:
                            current = value + 1
                            prev_changed_val = 3
                else:
                    continue
            if success == True:
                break
    #correct formatting for printing the above values (final)
        for i in final:
            i.strip()
        print(",".join(final))

    for i in results:
        i.strip()
    print((",".join(results)).strip())
else:
    print("No solution found.")
    for i in results:
        i.strip()
    print((",".join(results)).strip())

print(get_level(210))

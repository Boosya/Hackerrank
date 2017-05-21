# timing out on large sets



def print_community(number):
    if people[number] == None:
        print(1)
    else:
        print(len(communities[people[number]]))

def merge_communitites(comX,comY):
    global i, people,communities
    first_el = people[comX]
    second_el = people[comY]

    if first_el == None and second_el ==  None and comX != comY:
        communities[i] = [comX,comY]
        people[comX] = i
        people[comY] = i
        i += 1
    elif first_el == None and second_el ==  None and comX == comY:
        pass
    elif first_el == None and second_el != None:
        communities[second_el].append(comX)
        people[comX] = second_el
    elif second_el == None and first_el != None:
        communities[first_el].append(comY)
        people[comY] = first_el
    elif second_el == first_el:
        pass
    else:
        communities[first_el].extend(communities[second_el])
        to_change = second_el
        for person in communities[to_change]:
            people[person] = first_el
        del communities[to_change]

def read_input():
    global i, people,communities
    nb_people, nb_queries = input().split()
    nb_people = int(nb_people)
    nb_queries = int(nb_queries)
    people = [None]*nb_people
    communities = {}
    i = 0
    for _ in range(nb_queries):
        task = input().split()
        if task[0] == "Q":
            print_community(int(task[1])-1)
        else:
            merge_communitites(int(task[1])-1,int(task[2])-1)
# def read_file(filename):
#     global i, people,communities
#     with open(filename) as f:
#         lines = f.readlines()
#         nb_people, nb_queries = lines[0].split()
#         nb_people = int(nb_people)
#         nb_queries = int(nb_queries)
#         people = [None]*nb_people
#         communities = {}
#         i = 0
#         for line in lines[1:]:
#             task = line.split()
#             if task[0] == "Q":
#                 print_community(int(task[1])-1)
#             else:
#                 merge_communitites(int(task[1])-1,int(task[2])-1)
if __name__ == "__main__":
    read_input()
    # with open("answer_my.txt", 'w') as answer_file:
        # read_file("input.txt")

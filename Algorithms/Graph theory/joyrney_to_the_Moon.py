# Journey to the Moon problem
# based on pairs of compatriots given, output amount of options 2 austranauts can be picked from 2 different countries
from collections import deque

def BFSconnectedNodes(A, node):
    # returns queue with all the nodes from A that can be found through node
    # if graph is empty, return None
    if len(A) == 0:
        return None
    # if A is not empty, create queue with nodes that can be explored
    else:
        # initialize connected queue of nodes
        connected = deque()
        # initialize explored queue and add node to explored queue
        explored = deque()
        explored.append(node)
        while len(explored) > 0: # while some nodes in explored are not expanded yet
            # get the next node in a queue
            v = explored.popleft()
            # add it to connected queue
            connected.append(v)
            # find all nodes it is connected to
            outnodes = [edge[1] for edge in A if edge[0] == v] # nodes with higher numbers than current node
            outnodes.extend([edge[0] for edge in A if edge[1] == v]) # nodes with lower numbers than current node
            # for every node it is connected to
            for node in outnodes:
                # if node hasn't been discovered yet, add it to explored
                if not node in explored and not node in connected:
                    explored.append(node)
        return connected

def findClusters(A):
    # returns clusters of connected nodes in graph A
    clusters = []
    # add all the nodes in unexplored ones
    unexplored = deque(set(node for edge in A for node in edge))
    for i in range(len(unexplored)):
        if i in unexplored:
            # get all the connected to node nodes
            cluster = list(BFSconnectedNodes(A, i))
            # add current cluster to clusters
            clusters.append(cluster)
            # remove discovered nodes from unknown
            for node in cluster:
                unexplored.remove(node)
    return clusters

def readInput():
    totalNumberOfAustranauts, nbLines = input().split()
    austranauts = []
    for _ in range(int(nbLines)):
        person1, person2 = input().split()
        austranauts.append([int(person1),int(person2)])
    return austranauts, int(totalNumberOfAustranauts)

def readFromFile(filename):
    with open(filename) as f:
        for i,line in enumerate(f):
            if i== 0:
                totalNumberOfAustranauts, nbLines = line.split()
                austranauts = []
            else:
                person1, person2 = line.split()
                austranauts.append([int(person1),int(person2)])
    return austranauts, int(totalNumberOfAustranauts)

def calculateCombinations(compatriotsGroups,totalNumberOfAustranauts, austranautsNotCompatriots):
    options = 0
    nbCompatriotsGroups = len(compatriotsGroups)
    # case 1: selecting 1 person from compatriotsGroups and 2 person from compatriotsGroups
    for i in range(nbCompatriotsGroups):
        for j in range(i+1,nbCompatriotsGroups):
            options += len(compatriotsGroups[i]) *  len(compatriotsGroups[j])
            # print(compatriotsGroups[i],compatriotsGroups[j])
            # print(len(compatriotsGroups[i]) *  len(compatriotsGroups[j]))
    # print("from group",options)
    # case 2: selecting 1 person from compatriotsGroups and 1 person from non-compatriotsGroups
    options += (totalNumberOfAustranauts - austranautsNotCompatriots) * austranautsNotCompatriots
    # print(totalNumberOfAustranauts - austranautsNotCompatriots,austranautsNotCompatriots)
    # print("from group and nin-groups",options)
    # case 3: person 1 and person 2 from non-compatriotsGroups
    options += (austranautsNotCompatriots - 1) * austranautsNotCompatriots // 2
    # print("total",options)
    return (options)

if __name__ == "__main__":
    austranauts, totalNumberOfAustranauts = readFromFile("input.txt")
    # print(austranauts,totalNumberOfAustranauts)
    # austranauts, totalNumberOfAustranauts = readInput()
    # Austranauts = [[0,1],[0,4]]
    # totalNumberOfAustranauts = 5
    austranautsCompatriots = set()
    for austranautPair in austranauts:
        austranautsCompatriots.add(austranautPair[0])
        austranautsCompatriots.add(austranautPair[1])
    austranautsNotCompatriots = totalNumberOfAustranauts - len(austranautsCompatriots)
    print(austranautsNotCompatriots)
    print(len(austranautsCompatriots))
    austranautsNotCompatriots_t = [i for i in range(totalNumberOfAustranauts) if i not in austranautsCompatriots]
    print(austranautsNotCompatriots_t, len(austranautsNotCompatriots_t))
    compatriotsGroups = findClusters(austranauts)
    # print(compatriotsGroups)
    # print("austranautsCompatriots",len(austranautsCompatriots))
    # print("austranautsNotCompatriots",austranautsNotCompatriots)
    options = calculateCombinations(compatriotsGroups,totalNumberOfAustranauts, austranautsNotCompatriots)
    print(options)

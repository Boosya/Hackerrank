class Disjoint:

    def __init__(self):
        self.sets = []

    def createSet(self, repr):
        self.sets.append([repr])

    def mergeSets(self, repr1, repr2):
        set1 = self.findSet(repr1)
        set2 = self.findSet(repr2)
        if set1 != set2:
            set1.extend(set2)
            self.sets.remove(set2)

    def findSet(self, repr1):
        for oneSet in self.sets:
            if repr1 in oneSet:
                return oneSet

    def getSets(self):
        return self.sets

    def printSetSize(self,repr):
        print(len(self.findSet(repr)))

if __name__ == "__main__":
    communities = Disjoint()
    nb_people, nb_queries = input().split()
    nb_people = int(nb_people)
    nb_queries = int(nb_queries)
    for i in range(nb_people):
        communities.createSet(i)
    for _ in range(nb_queries):
        task = input().split()
        if task[0] == "Q":
            communities.printSetSize(int(task[1])-1)
        else:
            communities.mergeSets(int(task[1])-1,int(task[2])-1)

# Journey Scheduling Problem

n = 8
Roads = [[2,1],[3,2],[4,2],[5,1],[6,1],[7,1],[8,7]]
Journey = [[4,6],[3,4],[6,3],[7,6],[4,6],[7,1],[2,6]]
JourneyDist = [[None for i in range(len(Journey)+1)] for j in range(len(Journey)+1)]
print(JourneyDist)


class Node:
    def __init__(self,vert,height):
        self.vertex = vert
        self.height = height
        self.next = None


class Queue:
    def __init__(self):
        self.head = None

    def insertion(self, value):
        insertval = self.head

        if self.head is None:
            self.head = value
        else:
            while insertval.next is not None:
                insertval = insertval.next
            insertval.next = value

    def deletion(self):
        if self.head is None:
            print("No Items to delete")
            return None
        elif self.head.next is None:
            topvert = self.head
            self.head = None
            return topvert

        else:
            topvert = self.head
            self.head = self.head.next
            return topvert


def findPaths(v):
    allPaths = []
    for item in Roads:
        if v in item:
            allPaths.append(item)
    return allPaths


def JSP():
    for item in Journey:
        totalDist = 0
        maxVert = None
        for i in range(item[1]):
            maxHeight = 0
            visited = [False for i in range(n)]
            queue = Queue()
            queue.insertion(Node(item[0],0))
            visited[item[0]-1] = True
            while queue.head is not None:
                top = queue.deletion()
                allEdges = findPaths(top.vertex)
                for edge in allEdges:
                    if not visited[edge - 1]:
                        queue.insertion(Node(edge,top.height + 1))
                        visited[edge - 1] = True
                if top.height > maxHeight:
                    maxHeight = top.height
                    maxVert = top.vertex


JourneyDist.index()
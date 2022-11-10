

class Graph:
    def __init__(self, edgesPair, edges, colors):
        self.edgesPair = edgesPair
        self.edges = edges
        self.edgeDict = {edge:set() for edge in self.edges}
        self.edgeColor = {}
        self.colorIndex = 0
        self.colors = colors


    def run(self):
            for edge in self.edges:
                for left, right in self.edgesPair:
                    if edge==left:
                        self.edgeDict[edge].add(right)
                    elif edge==right:
                        self.edgeDict[edge].add(left)

            for edge, pairs in self.edgeDict.items():
                if edge not in self.edgeColor:
                    unfitColors = [self.edgeColor[edge] for edge in pairs if edge in self.edgeColor]
                    while colors[self.colorIndex] in unfitColors:
                        if self.colorIndex < len(self.colors)-1:
                            self.colorIndex+=1
                        else:
                            self.colorIndex = 0
                            print('INSUFFICIENT COLORS!')
                            break
                    self.edgeColor[edge] = colors[self.colorIndex]
                if self.colorIndex < len(self.colors)-1:
                        self.colorIndex+=1
                else:
                        self.colorIndex = 0
    def display(self):
            for key, value in self.edgeColor.items():
                print(f'Node "{key}" color is {value}')



edgesPair = [('f','e'),('f','g'),('f','a'),
('e','g'),('e','d'),('e','a'),('a','g'),('a','b'),
('g','c'),('d','b'),('d','c'),('b','c')]

edges =  ['a','b','c','d','e','f','g']

colors = ['yellow','red','blue','green']

obj = Graph(edgesPair, edges, colors)
obj.run()
obj.display()

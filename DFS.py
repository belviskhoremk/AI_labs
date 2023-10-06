# graph={'A':['B', 'D'],
#        'B':['C', 'F'],
#        'C':['E', 'G', 'H'],
#        'G':['E', 'H'],
#        'E':['B', 'F'],
#        'F':['A'],
#        'D': ['F'],
#        'H':['A']}
graph={'1':['2', '3', '4'],
       '2':['1'],
       '3':['1', '4'],
       '4':['1', '3', '5'],
       '5':['4']}

def dfs(graph, start):

    next=start
    stack = []
    visited=[]
    stack.append(next)
    while True:
        for key, value in graph.items():
            if key==next:
                visited.append(next)
                stack.pop(0)
                for i in value[::-1]:
                    if i not in visited and i not in stack:
                        stack.insert(0, i)
                    if i in stack:
                        stack.remove(i)
                        stack.insert(0, i)

                if len(stack)==0:
                    print("visited", visited)
                    exit(0)
                next=stack[0]

                continue






if __name__ == '__main__':
    dfs(graph, '1')






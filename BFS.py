# graph={'1':['2', '3', '4'],
#        '2':['1'],
#        '3':['1', '4'],
#        '4':['1', '3', '5'],
#        '5':['4']}

graph={'1':['2', '3', '4'],
       '2':['1','5', '6'],
       '3':['8', '1'],
       '4':['9', '1'],
       '5':['2','7'],
       '6' : ['2'],
       '7' : ['5'],
       '8' : ['3'],
       '9' : ['4']}

def bfs(graph, start):
    next = start
    visited = []
    arr_queue = []
    stack = []
    visited.append(next)

    for key, values in graph.items():
        if key not in visited:
            visited.append(key)
        for value in values:
            if value not in arr_queue and value not in visited:
                arr_queue.append(value)
        visited += arr_queue
        arr_queue.clear()


    for i in range(len(visited)):
        print(visited[i], end=" ")



import time
if __name__ == '__main__':
    start_time = time.time()
    bfs(graph, "1")
    print("\n--- %s seconds ---" % (time.time() - start_time))


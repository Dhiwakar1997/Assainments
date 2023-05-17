import heapq

#Given Graph
graph = {
'A': {'B': 2, 'D': 1, 'C': 5},
'B': {'A': 2, 'D': 2, 'C': 3},
'C': {'B': 3, 'D': 3, 'E': 1, 'F': 5, 'A': 5},
'D': {'A': 1, 'B': 2, 'C': 3, 'E': 1},
'E': {'D': 1, 'C': 1, 'F': 2},
'F': {'C': 5, 'E': 2}
}

def state_routing( start_vertex, graph):
    distance = {node: float('inf') for node in graph}
    distance[start_vertex] = 0
    pq = [(0, start_vertex)]
    while pq:
        (dist, curr_node) = heapq.heappop(pq)
        if dist > distance[curr_node]:
           continue
        for neighbor, weight in graph[curr_node].items():
            new_distance = dist + weight
            if new_distance < distance[neighbor]:
                distance[neighbor] = new_distance
                heapq.heappush(pq, (new_distance, neighbor))
    return distance

start_vertex = input("Enter starting vertex: ")
lsr = state_routing(start_vertex,graph)
print(lsr)
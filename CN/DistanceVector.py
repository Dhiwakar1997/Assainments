
distance_table = {
    'u': {'u': 0,'v': 1, 'y': 2, 'x': float('inf'), 'z': float('inf')},
    'v': {'v': 0, 'u': 1,  'x': 3, 'z': 6, 'y': float('inf')},
    'x': {'x': 0,'v': 3, 'y': 3, 'z': 2, 'u': float('inf')},
    'y': {'y': 0, 'u': 2, 'x': 3, 'v': float('inf'), 'z': float('inf')},
    'z': {'z': 0, 'v': 6, 'x': 2, 'y': float('inf'), 'u': float('inf')}
}


for vertex in distance_table:

    for neighbor_vertex in distance_table[vertex]:
        if distance_table[vertex][neighbor_vertex]!=float('inf') and vertex!=neighbor_vertex:
            
            for neighbor_paths in distance_table[neighbor_vertex]:
                if distance_table[neighbor_vertex][neighbor_paths]==float('inf'):
                    continue
                if distance_table[vertex][neighbor_paths]> distance_table[vertex][neighbor_vertex]+distance_table[neighbor_vertex][neighbor_paths]:

                    distance_table[vertex][neighbor_paths] = distance_table[vertex][neighbor_vertex]+distance_table[neighbor_vertex][neighbor_paths]


print("Distance table entries at node z:")
for node in sorted(distance_table):
    print(f"{node}: {distance_table[node]['z']}")

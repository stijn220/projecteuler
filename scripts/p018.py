# By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

# 3
# 7 4
# 2 4 6
# 8 5 9 3

# That is, 3 + 7 + 4 + 9 = 23.

# Find the maximum total from top to bottom of the triangle below:

# 75
# 95 64
# 17 47 82
# 18 35 87 10
# 20 04 82 47 65
# 19 01 23 75 03 34
# 88 02 77 73 07 63 67
# 99 65 04 28 06 16 70 92
# 41 41 26 56 83 40 80 70 33
# 41 48 72 33 47 32 37 16 94 29
# 53 71 44 65 25 43 91 52 97 51 14
# 70 11 33 28 77 73 17 78 39 68 17 57
# 91 71 52 38 17 14 91 43 58 50 27 29 48
# 63 66 04 68 89 53 67 30 73 16 69 87 40 31
# 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

# NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! (c;
from euler import solution

data_tiangle = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""


@solution
def solve(data):
    data_list = []
    data_index = []
    size = 0

    for line_i in range(0, len(data.splitlines())):
        line = data.splitlines()[line_i]
        temp_list = []
        for number_i in range(0,len(line.split(" "))):
            number = line.split(" ")[number_i]
            temp_list.append(100 - int(number))
            data_index.append((number_i,line_i))
            size += 1
        data_list.append(temp_list)

    adj_matrix = [[0] * size for _ in range(size)]
    for i in range(0, len(data_list) - 1):
        for j in range(0, len(data_list[i])):
            adj_matrix[data_index.index((j,i))][data_index.index((j,i+1))] = data_list[i+1][j]
            adj_matrix[data_index.index((j,i))][data_index.index((j+1,i+1))] = data_list[i+1][j+1]

    start = 0

    distances = [float('inf')] * size
    visited = [False] * size

    distances[start] = data_list[data_index[0][0]][data_index[0][1]]

    # Dijkstra algoritme
    for _ in range(size):
        min_distance = float('inf')
        u = None

        for i in range(size):
            if not visited[i] and distances[i] < min_distance:
                min_distance = distances[i]
                u = i
        if u is None:
            break
        visited[u] = True

        for v in range(size):
            if adj_matrix[u][v] != 0 and not visited[v]:
                alt = distances[u] + adj_matrix[u][v]
                if alt < distances[v]:
                    distances[v] = alt
    return len(data_list) * 100 - min(distances[-len(data_list):])

if __name__ == "__main__":
    solve(data_tiangle)
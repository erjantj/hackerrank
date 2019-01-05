import sys

def get_cost(curr_set, previous_v, min_cost_dp):
    curr_set_array = list(curr_set)
    curr_set_array.remove(previous_v)
    return min_cost_dp.get((previous_v, tuple(curr_set_array)),0)

def tsm(graph, s):
    graph_len = len(graph)

    # Generate sets
    all_sets = [(s,)]
    for i in range(graph_len):
        if i != s:
            all_sets.append((s, i))
    for i in range(graph_len):
        if i != s:
            for j in range(i, graph_len):
                if i!=j:
                    all_sets.append((i,j))


    min_cost_dp = {}
    parent = {}

    for curr_set in all_sets:
        for v in range(graph_len):
            if v == s:
                continue
            if v in all_sets:
                continue

            index = (v,curr_set)

            min_cost = sys.maxsize
            min_pervious_v = s

            for previous_v in curr_set:
                cost = graph[previous_v][v] + get_cost(curr_set, previous_v, min_cost_dp)
                if cost < min_cost:
                    min_cost = cost
                    min_pervious_v = previous_v

            if len(curr_set) == 0:
                min_cost = graph[s][v]

            min_cost_dp[index] = min_cost
            parent[index] = min_pervious_v

    curr_set_array = []
    for i in range(graph_len):
        curr_set_array.append(i)

    curr_set = tuple(curr_set_array)
    min_cost = sys.maxsize
    min_pervious_v = -1

    for k in curr_set:
        print(k, curr_set)
        cost = graph[k][s] + get_cost(curr_set, k, min_cost_dp);
        if cost < min_cost:
            min_cost = cost;
            min_pervious_v = k;

    for key, val in min_cost_dp.items():
        print(key, val)

graph = [[0,1,15,6], [2,0,7,3],[9,6,0,12],[10,4,8,0]]

s = 0
print(tsm(graph, s))
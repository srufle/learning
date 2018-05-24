#!/bin/python3

# C:\code\grokking_algorithms_rufle\grokking_examples07.py
import operator
import random
from collections import deque

def bfs_search(graph, name, check_func):
    search_queue = deque()
    search_queue += graph[name]

    searched = []
    while search_queue:
        person = search_queue.popleft()
        if not person in searched:
            if check_func(person):
                print(f"checking {person} succeeded !!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)

    print(f"No match for {name} found :(")
    return False

def bfs_search2(graph, start_node, end_node):
    # maintain a queue of paths
    candidate_paths = deque()
    # push the first path into the queue
    candidate_paths.append([start_node])
    while candidate_paths:
        # get the first path from the queue
        path = candidate_paths.pop()
        # get the last node from the path
        node = path[-1]
        # path found
        if node == end_node:
            return path
        # enumerate all adjacent nodes, construct a new path and push it into the queue
        for adjacent in graph.get(node, []):
            new_path = list(path)
            new_path.append(adjacent)
            candidate_paths.append(new_path)

def dijkstra_search(graph, costs, parents, start_node, end_node):
    processed = [start_node]
    node = find_lowest_cost_node(costs, processed)
    while node is not None:
        cost = costs[node]
        neighbors = graph[node]
        for n in neighbors.keys():
            new_cost = cost + neighbors[n]
            if costs[n] > new_cost:
                costs[n] = new_cost
            parents[n] = node
        processed.append(node)
        node = find_lowest_cost_node(costs, processed)

    return parents

def find_lowest_cost_node(costs, processed):
    lowest_cost = float("inf")
    lowest_cost_node = None
    for node in costs:
        cost = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

def find_jonny(name):
    return name == "jonny"

def main():
    infinity = float("inf")
    some_graph = {
        "you": ["alice", "bob", "claire"],
        "alice": ["peggy"],
        "bob": ["anuj", "peggy"],
        "claire": ["thom", "jonny"],
        "anuj": [],
        "peggy": [],
        "thom": [],
        "jonny": []
    }

    result = bfs_search(some_graph, "you", find_jonny)
    print(f"bfs_search of '{some_graph}' is '{result}'")

    some_graph = {
        '1': ['2', '3', '4'],
        '2': ['5', '6'],
        '5': ['9', '10'],
        '4': ['7', '8'],
        '7': ['11', '12'],
        '12': ['13', '14']
    }
    result = bfs_search2(some_graph, "1", "11")
    print(f"bfs_search2 of '{some_graph}' is '{result}'")

    result = bfs_search2(some_graph, "1", "14")
    print(f"bfs_search2 of '{some_graph}' is '{result}'")

    some_graph = {
        "you": ["alice", "bob", "claire"],
        "alice": ["peggy"],
        "bob": ["anuj", "peggy"],
        "claire": ["thom", "jonny"],
        "anuj": [],
        "peggy": [],
        "thom": [],
        "jonny": []
    }
    result = bfs_search2(some_graph, "you", "jonny")
    print(f"bfs_search2 of '{some_graph}' is '{result}'")

    # result = bfs_search2(some_graph, "you", "anuj")
    # print(f"bfs_search2 of '{some_graph}' is '{result['path']}'")

    some_graph = {}
    some_graph["start"] = {}
    some_graph["start"]["A"] = 6
    some_graph["start"]["B"] = 2
    some_graph["A"] = {}
    some_graph["A"]["finish"] = 1
    some_graph["B"] = {}
    some_graph["B"]["A"] = 3
    some_graph["B"]["finish"] = 5
    some_graph["finish"] = {}

    some_costs = {}
    some_costs["A"] = 6
    some_costs["B"] = 2
    some_costs["finish"] = infinity

    some_parents = {}
    some_parents["A"] = "start"
    some_parents["B"] = "start"
    some_parents["finish"] = None

    result = dijkstra_search(some_graph, some_costs, some_parents, "start", "finish", )
    print(f"dijkstra_search of '{some_graph}' is '{result}'")

    some_graph = {}
    some_graph["book"] = {}
    some_graph["book"]["poster"] = 0
    some_graph["book"]["rare_lp"] = 5
    some_graph["poster"] = {}
    some_graph["poster"]['bass_guitar'] = 30
    some_graph["poster"]['drum_set'] = 35
    some_graph["rare_lp"] = {}
    some_graph["rare_lp"]["bass_guitar"] = 15
    some_graph["rare_lp"]["drum_set"] = 20
    some_graph["bass_guitar"] = {}
    some_graph["bass_guitar"]["piano"] = 20
    some_graph["drum_set"] = {}
    some_graph["drum_set"]["piano"] = 10
    some_graph["piano"] = {}

    some_costs = {}
    some_costs["book"] = 0
    some_costs["poster"] = 0
    some_costs["rare_lp"] = 5
    some_costs["bass_guitar"] = infinity
    some_costs["drum_set"] = infinity
    some_costs["piano"] = infinity

    some_parents = {}
    some_parents["rare_lp"] = "book"
    some_parents["poster"] = "book"
    some_parents["bass_guitar"] = "poster"
    some_parents["drum_set"] = "poster"
    some_parents["piano"] = None

    result = dijkstra_search(some_graph, some_costs, some_parents, "book", "piano")
    print(f"dijkstra_search of '{some_graph}' is '{result}'")

main()

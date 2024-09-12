"""
CSCI-603: Lab 9
Author: Disha Revandkar (dr6742@rit.edu)
Author: Revaa Naik      (rn7416@rit.edu)

This program shows the simulation of painting the cows

"""
from graph import Graph
import math
import sys

def readFile(filename):
    """
    This function takes the filename as parameter and reads the text file and
    appends every word that is read from the file to a list
    :return: list that has the data read from file
    """

    file = []

    with open(filename) as f:
        for words in f.readlines():
            words = words.strip().split()
            file.append(words)
    return file


def createGraph(file):
    """
    This function creates a link between the cows and the paint balls by calculating the
    distance between the paint balls and cows and stores them in a dictionary
    :return: dictionary containing all the paint balls and the cows that it paints
    """
    cow_dict = {}

    for word in file:
        if word[0] == 'paintball':
            node = word[1]
            x = int(word[2])
            y = int(word[3])
            z = int(word[4])
            node_tup = ()
            for i in file:
                node_i = i[1]
                x_i = int(i[2])
                y_i = int(i[3])
                if node_i == node:
                    continue

                dist = (x_i - x) ** 2 + (y_i - y) ** 2
                if math.sqrt(dist) < z or math.sqrt(dist) == z:
                    node_tup += (node_i,)
            cow_dict[node] = node_tup
        else:
            node = word[1]
            cow_dict[node] = ()

    return cow_dict


# def initialize_connection_path(graph, node):
#     print("Triggering " + node + " paintball...")


def connection_path(graph, node, paints, color = None):
    """
    This function displays the name of the cows that are colored and the paint balls that are triggered
    :return: None
    """
    visited = set()
    if node not in visited:
        visited.add(node)
        if node not in paints:
            print(f"{node} is painted {color}")
        for neighbour in graph[node]:
            if neighbour in paints:
                print(f"{neighbour} paintball is triggered by {node} paintball ")
            connection_path(graph, neighbour, paints, node)


def simulation():
    """
    This function creates a graph and displays the adjacency list for the created graph.
    It also shows the simulation of when the paint balls are triggered and the cows that
    are coloured.
    :return: None
    """

    filename = (sys.argv[1])
    file = readFile(filename)
    print("Field of Dreams")
    print("---------------")
    cow_dict = createGraph(file)
    cowGraph = Graph()
    paints = set()
    for val in file:
        if val[0] == "paintball":
            paints.add(val[1])
    # print(paints)

    for state, neighbors in cow_dict.items():
        for neighbor in neighbors:
            cowGraph.addEdge(state, neighbor)

    for state in cowGraph:
        print(state)

    print()
    print("Beginning Simulation...")
    for val in file:
        if val[0] == "paintball":
            # paints.add(val[1])
            print("Triggering " + val[1] + " paintball...")
            connection_path(cow_dict, val[1], paints, val[1])

def main():
    """
    This is the main function and it does the error handling for the files
    :return: None
    """
    try:
        simulation()

    except FileNotFoundError:
        print("File not found:", sys.argv[1])
        sys.exit()

    except:
        print("Usage: python3 holi.py {filename}")
        sys.exit()


if __name__ == '__main__':
    main()
from room import Room
from player import Player
from world import World

import random
from ast import literal_eval


# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']


def traverse(graph):
    # placeholder for all
    maze = []
    # placeholder for rooms
    map_ = []
    # set of visited rooms
    visited = set()
    # initialize maze with 0
    maze.append(0)

    while len(visited) < len(graph):
        # Holder for current room
        current = maze[-1]
        # Add to visited
        visited.add(current)
        # Grab all possible exits for current room
        conns = graph[current][-1]
        unvisited_conns = []
        # If any connected rooms have not been visited yet, we add it to list if unvisited rooms
        for k, v in conns.items():
            if v not in visited:
                unvisited_conns.append(v)
        # This is basically checking for a dead end. If there are rooms connected that we haven't visited, we visit them.
        # If there aren't, we go back to last room
        if len(unvisited_conns) > 0:
            room = unvisited_conns[0]
            maze.append(room)
        else:
            room = maze[-2]
            maze.pop()
        # Loop through the curr rooms exits. Find the exit that equals the next room to be visited and pass that key into the map_
        for last_room, exits in conns.items():
            if exits == room:
                map_.append(last_room)
    # print(rooms)
    return map_
# !!!! TESTS PASSED: 997 moves, 500 rooms visited !!!!


traversal_path = traverse(room_graph)

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")

#######
# UNCOMMENT TO WALK AROUND
# #######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")

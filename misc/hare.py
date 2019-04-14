looped_list = [ [0,1], [1,2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 3], [7, 8] ]


# in straight_list, node 0 points to node 1, and so on, all the way to the last node (8)
# thus creating a straight linked list with no loops.

straight_list = [ [0,1], [1,2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8] ]


def is_loopy(path):
  tortoise = path[0] # slow pointer, starts at the beginning of the list
  hare = path[0] # fast pointer, also starts at the beginning of the list
  end = path[-1] # point to the last node
  while True:
    if hare == end:
      return False
    hare = path[hare[1]]    # move the fast pointer to the next node

    if hare == end:
      return False
    hare = path[hare[1]] # move the fast pointer to gain twice the speed
    print hare
    tortoise = path[tortoise[1]]    # move the slow pointer to the next node
    if hare == tortoise:
      return True


print looped_list
print is_loopy(looped_list)
print
print straight_list
print is_loopy(straight_list)
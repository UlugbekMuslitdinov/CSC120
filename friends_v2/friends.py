from linked_list import LinkedList, Node

filename = input('Input file: ')
friend_name1 = input('Name 1: ')
friend_name2 = input('Name 2: ')
f = open(filename, "r")
contents = f.read().splitlines()
friendList = LinkedList()
common = []
for i in contents:
    friends_names = i.split()
    friend1_name, friend2_name = friends_names[0], friends_names[1]
    current1, current2 = friendList.get_head(), friendList.get_head()
    friend1,  friend2 = None, None
    while current1 != None:
        if current1.name == friend1_name:
            friend1 = current1
            friend1.add_node(Node(friend2_name))
        current1 = current1.next
    while current2 != None:
        if current2.name == friend2_name:
            friend2 = current2
            friend2.add_node(Node(friend1_name))
        current2 = current2.next
    if friend1 is None:
        friend1 = Node(friend1_name)
        friendList.add_to_head(friend1)
        friend1.add_node(Node(friend2_name))
    if friend2 is None:
        friend2 = Node(friend2_name)
        friendList.add_to_head(friend2)
        friend2.add_node(Node(friend1_name))
current1 = friendList.get_head()
current2 = friendList.get_head()
friend1, friend2 = None, None
while current1 is not None:
    if current1.name == friend_name1:
        friend1 = current1
    current1 = current1.next
if friend1 == None:
    print("ERROR: Unknown person " + friend_name1)
while current2 is not None:
    if current2.name == friend_name2:
        friend2 = current2
    current2 = current2.next
if friend2 == None:
    print("ERROR: Unknown person " + friend_name2)
if friend1 != None and friend2 != None:
    for friend in friend1.get_nodes_list():
        if friend in friend2.get_nodes_list():
            common.append(friend)
if len(common) != 0:
    print("Friends in common:")
    for friend in sorted(common):
        print(friend)

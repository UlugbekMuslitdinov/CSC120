"""
    File: friends.py
    Author: Ulugbek Muslitdinov - CSC 120 FA22 001
    Purpose: Find the common friends of two people by reading the file and creating the LinkedList object and the Friend object.
"""

# import LinkedList and Friend classes from linkedlist.py
from linked_list import LinkedList, Friend


def main():
    """
    This function is used to read the file and create the LinkedList object and the Friend object,
    and prompt the user to enter the names of two people and print the common friends of two people.
    """
    filename = str(input('Input file: '))
    f = open(filename, "r").read().splitlines()
    friends = LinkedList()
    for line in f:
        friends_names = line.split()
        friend1_name = friends_names[0]
        friend2_name = friends_names[1]
        friend1_current = friends._head
        friend2_current = friends._head
        friend1 = None
        friend2 = None
        while friend1_current is not None:
            if friend1_current.value == friend1_name:
                friend1 = friend1_current
                break
            friend1_current = friend1_current.next
        while friend2_current is not None:
            if friend2_current.value == friend2_name:
                friend2 = friend2_current
                break
            friend2_current = friend2_current.next
        if friend1 is None:
            friend1 = Friend(friend1_name)
            friends.add(friend1)
        if friend2 is None:
            friend2 = Friend(friend2_name)
            friends.add(friend2)
        friend1.add_friend(Friend(friend2_name))
        friend2.add_friend(Friend(friend1_name))
    friend1_input = str(input('Name 1: '))
    friend2_input = str(input('Name 2: '))
    friend1_current = friends._head
    friend2_current = friends._head
    friend1 = None
    friend2 = None
    while friend1_current is not None:
        if friend1_current.value == friend1_input:
            friend1 = friend1_current
            break
        friend1_current = friend1_current.next
    while friend2_current is not None:
        if friend2_current.value == friend2_input:
            friend2 = friend2_current
            break
        friend2_current = friend2_current.next
    if friend1 is None:
        print("ERROR: Unknown person " + friend1_input)
    if friend2 is None:
        print("ERROR: Unknown person " + friend2_input)
    common_friends = []
    if friend1 is not None and friend2 is not None:
        for friend in friend1.get_friends():
            if friend in friend2.get_friends():
                common_friends.append(friend)
    if len(common_friends) > 0:
        print("Friends in common:")
        for friend in common_friends:
            print(friend)


main()

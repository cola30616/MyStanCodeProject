"""
File: add2.py
Name:
------------------------
TODO:
"""

import sys


class ListNode:
    def __init__(self, data=0, pointer=None):
        self.val = data
        self.next = pointer


def add_2_numbers(l1: ListNode, l2: ListNode) -> ListNode:
    #######################
    # calculate total value
    count_1 = count_2 = num_1 = num_2 = 0
    while l1 is not None:
        num_1 += l1.val * (10 ** count_1)
        l1 = l1.next
        count_1 += 1
    while l2 is not None:
        num_2 += l2.val * (10 ** count_2)
        l2 = l2.next
        count_2 += 1
    total = num_1 + num_2
    ################################
    # first way to solve
    # head -> None,  cur -> None
    l3 = cur = None
    # if the total == 0 , return 0
    if total == 0:
        l3 = ListNode()
        return l3

    else:
        while total > 0:
            if l3 is None:  # create head
                l3 = ListNode(total % 10)
                total //= 10
                cur = l3
            else:  # link to another node
                cur.next = ListNode(total % 10)
                total //= 10
                cur = cur.next
    return l3

    # second way to solve
    # dummy = cur = ListNode(total % 10)
    # total //= 10
    # if total == 0:
    #     return dummy
    # else:
    #     while total > 0:
    #         cur.next = ListNode(total % 10)
    #         total //= 10
    #         cur = cur.next
    # return dummy

    #######################
    #######################


####### DO NOT EDIT CODE BELOW THIS LINE ########


def traversal(head):
    """
    :param head: ListNode, the first node to a linked list
    -------------------------------------------
    This function prints out the linked list starting with head
    """
    cur = head
    while cur.next is not None:
        print(cur.val, end='->')
        cur = cur.next
    print(cur.val)


def main():
    args = sys.argv[1:]
    if not args:
        print('Error: Please type"python3 add2.py test1"')
    else:
        if args[0] == 'test1':
            l1 = ListNode(2, None)
            l1.next = ListNode(4, None)
            l1.next.next = ListNode(3, None)
            l2 = ListNode(5, None)
            l2.next = ListNode(6, None)
            l2.next.next = ListNode(4, None)
            ans = add_2_numbers(l1, l2)
            print('---------test1---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test2':
            l1 = ListNode(9, None)
            l1.next = ListNode(9, None)
            l1.next.next = ListNode(9, None)
            l1.next.next.next = ListNode(9, None)
            l1.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next = ListNode(9, None)
            l1.next.next.next.next.next.next = ListNode(9, None)
            l2 = ListNode(9, None)
            l2.next = ListNode(9, None)
            l2.next.next = ListNode(9, None)
            l2.next.next.next = ListNode(9, None)
            ans = add_2_numbers(l1, l2)
            print('---------test2---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        elif args[0] == 'test3':
            l1 = ListNode(0, None)
            l2 = ListNode(0, None)
            ans = add_2_numbers(l1, l2)
            print('---------test3---------')
            print('l1: ', end='')
            traversal(l1)
            print('l2: ', end='')
            traversal(l2)
            print('ans: ', end='')
            traversal(ans)
            print('-----------------------')
        else:
            print('Error: Please type"python3 add2.py test1"')


if __name__ == '__main__':
    main()

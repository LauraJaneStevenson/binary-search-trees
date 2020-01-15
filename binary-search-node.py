from math import floor

class TreeNode(object):
    """Binary tree node."""

    def __init__(self, data, left=None, right=None):
        self.data = data

        self.left = left
        self.right = right

    def __repr__(self):
        """Debugging-friendly representation."""

        return f"<BinaryNode {self.data}>"

class ListNode(object):
    """Binary tree node."""

    def __init__(self, data):
        self.data = data

        self.next = None

    def __repr__(self):
        """Debugging-friendly representation."""

        return f"<ListNode {self.data}>"


# ListNode(floor(lst[len(lst/2)])


def create_linked(lst = [-10,-3,0,5,9]):

	ll = []

	for i in range(len(lst)):

		ll.append(ListNode(lst[i]))

	for i in range(len(ll) - 1):

		ll[i].next = ll[i + 1]

	current = ll[0]

	while current != None:

		print(current.data)
		current = current.next

	return ll[0]


# split into 2 functions 
# 1st function find and return middle use slow and fast counter 
# 2nd function get the middle node and set it to root of tree
# base case for just one element in linked list 

# set right and left nodes by recursively calling 2nd fucntion, passing in head of the tree to left 
# and 


def find_middle(ll):

	prev = None
	fast = ll
	slow = ll

	while fast != None and fast.next != None:

		prev = slow
		slow = slow.next
		fast = fast.next.next

	# disconnect halfs of linked list
	if prev:

		prev.next = None

	return slow




linked_list = create_linked()

# print(find_middle(linked_list))


def sorted_list(head):

	# check if linked list is empty
	if not head:

		return None

	mid = find_middle(head)
	# print(mid)

	tree = TreeNode(mid.data)

	# check if there is just one node in linked list
	if head == mid:

	 	return tree

	tree.left = sorted_list(head)
	tree.right = sorted_list(mid.next)

	return tree


print(sorted_list(linked_list))











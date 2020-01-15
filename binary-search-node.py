# from math import floor

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



def create_linked(lst = [-10,-3,0,5,9]):
	"""given a sorted list returns a singly linked list"""

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


def find_middle(ll):
	"""Given a linked list returns middle node"""

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


def create_bst(head):
	"""Given a sorted linked list returns a BST"""

	# check if linked list is empty
	if not head:

		return None

	# get middle node of list
	mid = find_middle(head)
	
	# create tree node with mid as root 
	tree = TreeNode(mid.data)

	# check if there is just one node in linked list
	if head == mid:

		# return node
	 	return tree

	# recursively call function to create left and right child trees 
	# with halves of list
	tree.left = create_bst(head)
	tree.right = create_bst(mid.next)

	# return
	return tree

def find_lca(tree,n1,n2):
	"""Given a bst and 2 nodes, return the least common ancestor or the given nodes"""
	

	parent = tree
	

	while parent:

		if n1.data < parent.data and n2.data < parent.data:

			parent = parent.left

		if n1.data < parent.data and n2.data < parent.data:

			parent = parent.right

		else:

			return parent

	return None


linked_list = create_linked()

bst = create_bst(linked_list)

print(find_lca(bst,TreeNode(-10),TreeNode(-3)))













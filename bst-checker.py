from BinaryTreeNode import BinaryTreeNode
import math
# testcase 1 >>> True
n1 = BinaryTreeNode(50)
n1.insert_left(25)
n1.insert_right(75)
n1.right.insert_right(87.5)
n1.left.insert_left(12.5)
n1.left.insert_right(37.5)

# testcase 2 >>> False
n2 = BinaryTreeNode(50)
n2.insert_left(25)
n2.insert_right(75)
n2.left.insert_left(100)
n2.left.insert_right(37.5)
n2.left.left.insert_left(6.25)

def validate(tree):

	root = tree.value
	to_visit = [(tree, -float('inf'),float('inf'))]

	while to_visit:

		current, lower,higher = to_visit.pop(0)

		if not lower <= current.value <= higher:
			return False
		if current.right:
			to_visit.append((current.right,current.value,higher))
		if current.left:
			to_visit.append((current.left,lower,current.value))

	return True

		

print(validate(n1))
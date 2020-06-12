class BinaryTreeNode(object):

    def __init__(self, value,root):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right

    def delete(self,root):

        if self.right and self.left:
            current = self.left
            while current.right:
                current = current.right
            self.data = current.data
            current.find_parent(root).right = None
        elif self.right:
            parent = self.find_parent(root)
            parent.right = self.right
        elif self.left:
            parent = self.find_parent(root)
            parent.left = self.left




    def find_parent(self,root):

        to_visit = [root]

        while to_visit:
            current = to_visit.pop(0)
            if current.right.value == self.value:
                return current
            if current.left.value == self.value:
                return current 
            if current.right:
                to_visit.append(current.right)
            if current.left:
                to_visit.append(current.left)

    def __repr__(self):
        return f"Tree Node:{self.value}"



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
n2.left.insert_left(12.5)
n2.left.insert_right(37.5)
n2.left.left.insert_left(6.25)

print(n1.right.find_parent(n1))

def check_super_balanced(tree):

    to_visit = [(tree,0)]

    levels = []

    while to_visit:

        current, level = to_visit.pop()

        if not current.left and not current.right:
            if level not in levels:
                levels.append(level)

        if len(levels) > 2:
            return False

        if current.left:
            to_visit.append((current.left, level+1))

        if current.right:
            to_visit.append((current.right, level+1))
    return True



def is_valid(tree):
	"""Returns T or F whether BST is valid"""

	to_visit = [(tree,-float('inf'),float('inf'))]

	while to_visit:
       
		current,lower,upper = to_visit.pop(0)

		if current.value <= lower or current.value >= upper:
			return False 

		if current.left:
			to_visit.append((current.left,lower,current.value))

		if current.right:
			to_visit.append((current.right,current.value,upper))


	return True


def second_largest(tree):

	to_visit = [(tree,tree)]

	while to_visit:

		current, parent = to_visit.pop()

		if not current.right:
			return parent.value

		else:
			to_visit.append((current.right,current))



# print(check_super_balanced(n2))
# print(is_valid(n1))
# print(second_largest(n1))
















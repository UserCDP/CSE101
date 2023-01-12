"""Copyright Daniela COjocaru 2022, I mean 3, 2023"""

class Node:
    def __init__(self, key, value, left, right):
        self.key = key
        self.value = value
        self.left = left
        self.right = right

    def __eq__(self, other):
        return self.key == other.key \
           and self.value == other.value \
           and self.left == other.left \
           and self.right == other.right

    def __repr__(self):
        return f'Node({repr(self.key)}, {repr(self.value)}, {repr(self.left)}, {repr(self.right)})'

    def __str__(self):
        lines, _ = self._str_aux()
        return '\n'.join(lines)

    def _str_aux(self):
        # Recursive helper for __str__.
        # Returns lines (to be joined) and the horizontal position where
        # a branch from an eventual parent should be attached.
        label = f'{self.key}: {self.value}'

        # Leaf case
        if self.right is None and self.left is None:
            return [label], len(label) // 2

        if self.left is None:
            llines, lpos, lwidth, ltop0, ltop1, lfill = [], 0, 0, '', '', ''
        else:  # Recurse left
            llines, lpos = self.left._str_aux()
            lwidth = len(llines[0])
            ltop0 = lpos*' ' + ' ' + (lwidth - lpos - 1)*'_'
            ltop1 = lpos*' ' + '/' + (lwidth - lpos - 1)*' '
            lfill = lwidth*' '

        if self.right is None:
            rlines, rpos, rwidth, rtop0, rtop1, rfill = [], 0, 0, '', '', ''
        else:  # Recurse right
            rlines, rpos = self.right._str_aux()
            rwidth = len(rlines[0])
            rtop0 = rpos*'_' + ' ' + (rwidth - rpos - 1)*' '
            rtop1 = rpos*' ' + '\\' + (rwidth - rpos - 1)*' '
            rfill = rwidth*' '

        cfill = len(label)*' '

        # Extend llines or rlines to same length, filling with spaces (or '')
        maxlen = max(len(llines), len(rlines))
        llines.extend(lfill for _ in range(maxlen - len(llines)))
        rlines.extend(rfill for _ in range(maxlen - len(rlines)))

        res = []
        res.append(ltop0 + label + rtop0)
        res.append(ltop1 + cfill + rtop1)
        res.extend(lline + cfill + rline for (lline, rline) in zip(llines, rlines))

        return res, lwidth + len(label) // 2

    # Exercise 2
    def search (self, key):
        """Search a key in the tree"""
        if key == self.key:
            return self.value
        if key < self.key:
            if self.left is None:
                return None
            return self.left.search(key)
        if key > self.key:
            if self.right is None:
                return None
            return self.right.search (key)

    # Exercise 3
    def print_in_order(self):
        """Print the nodes in order"""
        if self:
            if self.left:
                self.left.print_in_order()
            print (f"{self.key}: {self.value}")
            if self.right:
                self.right.print_in_order()

    # Exercise 4
    def add(self, key, value):
        """Add a new node to the tree"""
        if key < self.key:
            if self.left is None:
                new = Node(key, [value], None, None)
                self.left = new
            else:
                self.left.add(key, value)
        if key > self.key:
            if self.right is None:
                new = Node(key, [value], None, None)
                self.right = new
            else:
                self.right.add(key, value)
        if key == self.key:
            if value not in self.value:
                self.value.append(value)

    # Exercise 6
    def write_in_order(self, filename):
        """Write the nodes of the tree in ascending order"""
        outfile = open(filename, 'w', encoding="utf8")
        self.write_in_order_rec(outfile)

    def write_in_order_rec(self, file):
        """The recursive aid for write_in_order"""
        if self.left:
            self.left.write_in_order_rec(file)
        file.write(f"{self.key}: {self.value}\n")
        if self.right:
            self.right.write_in_order_rec(file)

    # Exercise 8
    def height(self):
        """CAlculate the longest string of nodes starting from the root"""
        if (self is None) or (self.right is None and self.left is None):
            return 0

        if self.right and self.left:
            return 1 + max(self.right.height(), self.left.height())

        if self.right:
            return 1 + self.right.height()
        if self.left:
            return 1 + self.left.height()

    # Exercise 9 Part 1
    def list_in_order(self):
        """Put the elements of the tree in an sorted list"""
        result = []
        stack = [self]
        node = None
        while stack:
            if node is None:
                node = stack.pop()
            if node is not None:
                result.append((node.key, node.value))
                stack.append(node.right)
                node = node.left
        return sorted(result)

## End of Node Class

# Exercise 1
def example_bst():
    """Create the example tree and return its root"""
    n3 = Node(3, 'Three', None, None)
    n7 = Node(7, 'Seven', None, None)
    n6 = Node(6, 'Six', None, n7)
    n4 = Node(4, 'Four', n3, n6)
    n13 = Node(13, 'Thirteen', None, None)
    n14 = Node(14, 'Fourteen', n13, None)
    n10 = Node(10, 'Ten', None, n14)
    n8 = Node(8, 'Eight', n4, n10)
    return n8

# Exercise 5
def split_in_words_and_lowercase(line):
    """Split a line of text into a list of lower-case words."""
    parts = line.strip('\n').replace('-', ' ').replace("'", " ").replace('"', ' ').split()
    parts = [p.strip('",._;?!:()[]').lower() for p in parts]
    return [p for p in parts if p != '']

def construct_bst_for_indexing(filename):
    """Construct the binary search tree"""
    infile = open(filename, 'r', encoding="utf8")
    lines = []
    for line in infile:
        lines.append(split_in_words_and_lowercase(line))

    tree = Node(lines[0][0], [1], None, None)

    k = 1
    for line in lines:
        for word in line:
            tree.add(word, k)
        k += 1
    return tree

# Exercise 7
def generate_index(textfile, indexfile):
    tree = construct_bst_for_indexing(textfile)
    tree.write_in_order(indexfile)

# Exercise 9 Part 2
def balanced_bst(sorted_list):
    return balanced_bst_rec(sorted_list, 0, len(sorted_list))

def balanced_bst_rec(sorted_list, lower, upper):
    mid = (lower+upper)//2
    (key, value) = sorted_list[mid]
    
    if lower == upper-1:
        return Node(key, value, None, None)

    if lower < upper - 1:
        a = balanced_bst_rec(sorted_list, lower, mid)
        b = balanced_bst_rec(sorted_list, mid+1, upper)
        root = Node(key, value, a, b)
        return root

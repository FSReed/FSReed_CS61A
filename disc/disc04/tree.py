# Question 1.1:
def height(t):
    """Return the height of a tree.
    >>> t = tree(3, [tree(5, [tree(1)]), tree(2)])
    >>> height(t)
    2
    """
    if is_leaf(t):
        return 0
    else:
        max_list = [height(branch) for branch in branches(t)]
        return max(max_list) + 1


# Question 1.2:
def max_path_sum(t):
    """Return the maximum path sum of the tree.
    >>> t = tree(1, [tree(5, [tree(1), tree(3)]), tree(10)])
    >>> max_path_sum(t)
    11
    """
    if is_leaf(t):
        return label(t)
    else:
        return max([max_path_sum(branch) for branch in branches(t)]) + label(t)


# Question 1.3:
def square_tree(t):
    """Return a tree with the square of every element in t
    >>> numbers = tree(1,
    ...                 [tree(2,
    ...                     [tree(3),
    ...                     tree(4)]),
    ...                 tree(5,
    ...                     [tree(6,
    ...                         [tree(7)]),
    ...                     tree(8)])])
    >>> print_tree(square_tree(numbers))
    1
      4
        9
        16
      25
        36
          49
        64
    """
    if is_leaf(t):
        return tree(label(t) ** 2)
    else:
        new_branches = [square_tree(branch) for branch in branches(t)]
        return tree(label(t) ** 2, new_branches)


# Question 1.4:

"""Tutorial: 
Write a function that takes in a tree and a value x and returns a list
containing the nodes along the path required to get from the root of the tree to a
node containing x.
If x is not present in the tree, return None. Assume that the entries of the tree are
unique
"""


def find_path(tree, x):
    """
    >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10) # returns None
    """
    if is_leaf(tree) and label(tree) == x:
        return [x]
    for branch in branches(tree):
        if find_path(branch, x):
            return [label(tree)] + find_path(branch, x)


# Question 2.2:
"""
Write a function that takes in a tree consisting of '0's and '1's t and a list of ”binary
numbers” nums and returns a new tree that contains only the numbers in nums that
exist in t. If there are no numbers in nums that exist in t, return None.
Definition:
Each binary number is represented as a string. A binary number n
exists in t if there is some path from the root to leaf of t whose values are equal to
n.
"""
def prune_binary(t, nums):
    if _________________________:
        if _____________:
            return t
        return None
    else:
        next_valid_nums = __________________________
        new_branches = []
        for ____________________:
            pruned_branch = prune_binary(_____, next_valid_nums)
        if pruned_branch is not None:
            new_branches = new_branches + [__________]
        if not new_branches:
            return None
        return __

def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch), "All the branches must be a tree."
    return [label] + list(branches)


def label(tree):
    return tree[0]


def branches(tree):
    return tree[1:]


def is_tree(T):
    if (type(T) != list) or len(T) < 1:
        return False
    for branch in branches(T):
        if not is_tree(branch):
            return False
    return True


def is_leaf(tree):
    # NOTE:
    # "not []" equals to True. "not [1]" equals to False.
    return not branches(tree)


def fib_tree(n):
    """Construct a fibonacci tree.
    >>> fib_tree(1)
    [1]
    >>> fib_tree(3)
    [2, [1], [1, [0], [1]]]
    >>> fib_tree(5)
    [5, [2, [1], [1, [0], [1]]], [3, [1, [0], [1]], [2, [1], [1, [0], [1]]]]]
    """
    if n <= 1:
        return tree(n)
    else:
        left, right = fib_tree(n - 2), fib_tree(n - 1)
        fib_number = label(left) + label(right)
        return tree(fib_number, [left, right])


def count_leaves(tree):
    if is_leaf(tree):
        return 1
    else:
        return sum([count_leaves(branch) for branch in branches(tree)])


def print_tree(t, indent=0):
    """Print a representation of this tree in which each label is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> print_tree(fib_tree(4))
    3
      1
        0
        1
      2
        1
        1
          0
          1
    """
    print("  " * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

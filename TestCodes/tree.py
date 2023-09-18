# Show a case about how to create a tree structure recursively.


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

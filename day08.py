from pathlib import Path

sample_trees = """30373
25512
65332
33549
35390"""


def is_visible(i: int, j: int, trees: list[list[int]]) -> bool:
    tree = trees[i][j]
    left_items = trees[i][:j] or [-1]
    right_items = trees[i][j + 1 :] or [-1]
    top_items = [row[j] for row in trees[:i]] or [-1]
    bottom_items = [row[j] for row in trees[i + 1 :]] or [-1]

    # print(left_items, right_items, top_items, bottom_items)

    return (
        max(left_items) < tree
        or max(right_items) < tree
        or max(top_items) < tree
        or max(bottom_items) < tree
    )


def get_visible_trees(trees: str) -> int:
    tree_lists = [list(map(int, tree)) for tree in trees.splitlines()]

    return sum(
        is_visible(i, j, tree_lists)
        for i in range(len(tree_lists))
        for j in range(len(tree_lists[i]))
    )


print(get_visible_trees(sample_trees))

tree_lists = [list(map(int, tree)) for tree in sample_trees.splitlines()]

print("HERE")
assert is_visible(1, 1, tree_lists) == True
assert is_visible(1, 2, tree_lists) == True
assert is_visible(1, 3, tree_lists) == False
assert is_visible(2, 1, tree_lists) == True
assert is_visible(2, 2, tree_lists) == False
assert is_visible(2, 3, tree_lists) == True


print(is_visible(2, 2, tree_lists))
print(is_visible(0, 0, tree_lists))

assert get_visible_trees(sample_trees) == 21

trees = Path("day08").read_text()

print(get_visible_trees(trees))


def get_viewing_score(i, j, trees):
    tree = trees[i][j]
    left_items = list(reversed(trees[i][:j])) or []
    right_items = trees[i][j + 1 :] or []
    top_items = [row[j] for row in reversed(trees[:i])] or []
    bottom_items = [row[j] for row in trees[i + 1 :]] or []

    def get_score(items):
        for idx, item in enumerate(items):
            if item >= tree:
                return idx + 1
        return len(items)

    return (
        get_score(left_items)
        * get_score(right_items)
        * get_score(top_items)
        * get_score(bottom_items)
    )


assert get_viewing_score(1, 2, tree_lists) == 4

assert get_viewing_score(3, 2, tree_lists) == 8


def get_max_viewing_score(trees: str) -> int:
    tree_lists = [list(map(int, tree)) for tree in trees.splitlines()]

    return max(
        get_viewing_score(i, j, tree_lists)
        for i in range(len(tree_lists))
        for j in range(len(tree_lists[i]))
    )


assert get_max_viewing_score(sample_trees) == 8

print(get_max_viewing_score(trees))

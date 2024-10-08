#!/usr/bin/python3
"""
lock boxes using graph theory
"""


def canUnlockAll(boxes):
    """You have `n` number of locked boxes in front of you.
    Each box is numbered sequentially from
    `0` to `n - 1` and each box may contain keys to the other boxes.

    - **Prototype:** `def canUnlockAll(boxes)`
    - `boxes` is a list of lists.
    - A key with the same number as a box opens that box.
    - You can assume all keys will be positive integers.
    - There can be keys that do not have boxes.
    - The first box `boxes[0]` is unlocked.
    - Return `True` if all boxes can be opened, else return `False`.

    Args:
        boxes (List of List):
    """
    set = {0}
    keys = boxes[0]
    for key in keys:
        if key not in set and key < len(boxes):
            set.add(key)
            keys.extend(boxes[key])
    if len(boxes) == len(set):
        return True
    return False

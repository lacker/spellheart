#!/usr/bin/env python3

words = [line.strip() for line in open("./words_alpha.txt").readlines()]

print("loaded dictionary with", len(words), "words")


def canonicalize(word):
    letters = set()
    for letter in word:
        letters.add(letter)
    return "".join(sorted(list(letters))) + f" ({len(word)})"


cmap = {}
for word in words:
    key = canonicalize(word)
    if key not in cmap:
        cmap[key] = []
    cmap[key].append(word)


def check(word):
    can = canonicalize(word)
    words = cmap.get(can, [])

    if len(words) > 1:
        print("collision:", words)
        return

    print(can.upper(), "=>", word)


# under bed
check("buttercup")
check("snapdragon")
check("foxglove")
check("morningglory")
check("bluebell")
check("goldenrod")

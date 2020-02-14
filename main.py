#!/usr/bin/env python3
#
# A puzzle generator

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


def check(word, ignore_collision=False):
    can = canonicalize(word)
    words = cmap.get(can, [])

    if not ignore_collision and len(words) > 1:
        print("collision:", words)
        return

    print(can.upper(), "=>", word)


# With the puzzles printed out, you can use a letter multiple times.
# Write out the blanks and put a circle where the clue-letter or clue-letters go

# under bed
# theme: flowers
check("buttercup")
check("snapdragon")
check("foxglove")
check("morningglory")
check("bluebell")
check("goldenrod")

# colander
# theme: trees
check("sycamore", True)
check("redwood", True)
check("willow")
check("manzanita")
check("cedar", True)
check("eucalyptus")
check("redbud", True)

# dustpan
# theme: animals
check("mallard")
check("bluewhale")
check("squirrel", True)
check("seaotter", True)
check("opossum", True)
check("bananaslug")

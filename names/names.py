import time
from bst import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

# Runtime: 13.13 seconds
# Big O: O(n^2)
# duplicates = []
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

# ----  Refactored solution ----
# Runtime: 0.19 seconds
# Big O: O(n) * O(log n) = O(n log n)

duplicates = []
bst_initiated = False

# build a bst to compare names_2 against it
for name_1 in names_1:  # O(n)
    if not bst_initiated:
        # create a bst passing in the first name to get things going
        bst = BinarySearchTree(name_1)
        bst_initiated = True
    else:
        # fill the bst with the rest of names
        bst.insert(name_1)

# compare names_2 to names_1
for name_2 in names_2:  # O(log n)
    if bst.contains(name_2):
        duplicates.append(name_2)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?

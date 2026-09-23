import csv
import time

# Record the start time
start_time = time.time()

class Node:
    def __init__(self, data, axis=None, left=None, right=None):
        self.data = data  # Data tuple: (Name, Awards, Publications)
        self.axis = axis  # Dimension for division
        self.left = left   # Left subtree
        self.right = right  # Right subtree

class KDTree:
    def __init__(self):
        self.root = None

    def build_kd_tree(self, data, depth=0):
        if not data:
            return None

        axis = depth % 3  # Three dimensions: 0 for Name, 1 for Awards, 2 for Publications

        data.sort(key=lambda x: x[axis])  # Sorting data based on the current axis

        median = len(data) // 2

        return Node(
            data[median],
            axis,
            self.build_kd_tree(data[:median], depth + 1),
            self.build_kd_tree(data[median + 1:], depth + 1)
        )

    def build_from_csv(self, file_path):
        data = []
        with open(file_path, 'r', newline='', encoding='UTF-8') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip header row
            for row in csv_reader:
                name, awards, publications, _ = row  # Ignore the fourth element (education)
                data.append((name, int(awards), int(publications)))

        self.root = self.build_kd_tree(data)

    def search_kd_tree(self, target_range, awards_range, publications_range, node=None):
        if node is None:
            node = self.root

        if node is None:
            return []

        results = []

        name, awards, publications = node.data

        if target_range[0] <= name[0] <= target_range[1] and awards > awards_range and publications_range[0] <= publications <= publications_range[1]:
            results.append(node.data)

        if node.left is not None and name[0] >= target_range[0]:
            results += self.search_kd_tree(target_range, awards_range, publications_range, node.left)

        if node.right is not None and name[0] <= target_range[1]:
            results += self.search_kd_tree(target_range, awards_range, publications_range, node.right)

        return results

# Usage
kd_tree = KDTree()
kd_tree.build_from_csv('output.csv')

# Search scientists based on specified criteria
results = kd_tree.search_kd_tree(('A', 'Z'), 0, (0,30))
results2 = kd_tree.search_kd_tree(('A', 'K'), 2, (2, 20))
results3 = kd_tree.search_kd_tree(('C', 'K'), 1, (5, 25))
results4 = kd_tree.search_kd_tree(('D', 'L'), 6, (0, 50))
results5 = kd_tree.search_kd_tree(('J', 'P'), 2, (5, 45))
results6 = kd_tree.search_kd_tree(('A', 'Z'), 7, (0, 50))
results7 = kd_tree.search_kd_tree(('B', 'N'), 2, (1, 17))
results8 = kd_tree.search_kd_tree(('T', 'Z'), 5, (10, 40))
results9 = kd_tree.search_kd_tree(('D', 'P'), 2, (5, 15))
results10 = kd_tree.search_kd_tree(('A', 'V'), 5, (4, 70))
results11 = kd_tree.search_kd_tree(('C', 'W'), 0, (1, 4))
results12 = kd_tree.search_kd_tree(('E', 'H'), 8, (3, 9))
results13 = kd_tree.search_kd_tree(('K', 'N'), 2, (5, 10))
results14 = kd_tree.search_kd_tree(('F', 'R'), 4, (1, 6))
results15 = kd_tree.search_kd_tree(('C', 'Z'), 0, (3, 11))
results16 = kd_tree.search_kd_tree(('A', 'O'), 3, (2, 11))
results17 = kd_tree.search_kd_tree(('G', 'X'), 0, (1, 15))
results18 = kd_tree.search_kd_tree(('A', 'Z'), 5, (5, 40))
results19 = kd_tree.search_kd_tree(('C', 'X'), 3, (7, 30))
results20 = kd_tree.search_kd_tree(('H', 'Z'), 1, (2, 50))

print(results)
print(results2)
print(results3)
print(results4)
print(results5)
print(results6)
print(results7)
print(results8)
print(results9)
print(results10)
print(results11)
print(results12)
print(results13)
print(results14)
print(results15)
print(results16)
print(results17)
print(results18)
print(results19)
print(results20)
# Record the end time
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time

print(f"Total running time: {elapsed_time} seconds")
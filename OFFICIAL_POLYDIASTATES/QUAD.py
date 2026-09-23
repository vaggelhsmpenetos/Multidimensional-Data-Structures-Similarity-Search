import time

# Record the start time
start_time = time.time()
class Node:
    def __init__(self, name, awards, publications, education=None):
        self.name = name
        self.awards = awards
        self.publications = publications
        self.education = education
        self.children = [None] * 4

class QuadTree:
    def __init__(self):
        self.root = None
        self.steps = 0

    def insert(self, node, data):
        self.steps += 1  # Αύξηση του μετρητή κατά ένα για κάθε βήμα
        if not node:
            self.root = Node(data[0], int(data[1]), int(data[2]), data[3] if len(data) > 3 else None)
            return

        current_node = node
        while True:
            child_index = 0   
            if current_node.name < data[0]:
                child_index = 0
            elif current_node.name >= data[0]:
                child_index = 1
            else:
                child_index = 2 if current_node.name < data[0] else 3

            if not current_node.children[child_index]:
                current_node.children[child_index] = Node(data[0], int(data[1]), int(data[2]), data[3] if len(data) > 3 else None)
                return

            current_node = current_node.children[child_index]

    def search_and_print(self, node, prefixes, awards, min_publications, max_publications):
        self.steps += 1
        if node:
            for prefix in prefixes:
                if node.name.startswith(prefix) and node.awards > awards and min_publications <= node.publications <= max_publications:
                    print(f"Name: {node.name}, Awards: {node.awards}, Publications: {node.publications} ")
            for i in range(4):
                child = node.children[i]
                if child:
                    self.search_and_print(child, prefixes, awards, min_publications, max_publications)

# Λειτουργία για δημιουργία και την εισαγωγή δεδομένων από το CSV αρχείο
def create_quad_tree_from_csv(file_path):
    quad_tree = QuadTree()
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()[1:]
        for line in lines:
            data = line.strip().split(',')

            # Προσθήκη ελέγχου για το μέγεθος της λίστας
            if len(data) >= 3:
                # Προσθήκη ελέγχου για την αριθμητική τιμή
                awards = int(data[1]) if data[1].isdigit() else 0
                publications = int(data[2]) if data[2].isdigit() else 0

                quad_tree.insert(quad_tree.root, [data[0], awards, publications, None])
    return quad_tree

if __name__ == "__main__":
    quad_tree = create_quad_tree_from_csv('output.csv')

    prefixes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    quad_tree.search_and_print(quad_tree.root, prefixes, 0, 0, 30)
    print(f"Number of steps: {quad_tree.steps}")

    prefixes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
    quad_tree.search_and_print(quad_tree.root, prefixes, 2, 2, 20)
    print(f"Number of steps: {quad_tree.steps}")

    prefixes = ['C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']
    quad_tree.search_and_print(quad_tree.root, prefixes, 1, 5, 25)
    print(f"Number of steps: {quad_tree.steps}")

    prefixes = ['D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
    quad_tree.search_and_print(quad_tree.root, prefixes, 6, 0, 50)
    print(f"Number of steps: {quad_tree.steps}")

    prefixes = ['J', 'K', 'L', 'M', 'N', 'O', 'P']
    quad_tree.search_and_print(quad_tree.root, prefixes, 2, 5, 45)
    print(f"Number of steps: {quad_tree.steps}")

    prefixes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    quad_tree.search_and_print(quad_tree.root, prefixes, 7, 0, 50)
    print(f"Number of steps: {quad_tree.steps}")

    prefixes = ['B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N']
    quad_tree.search_and_print(quad_tree.root, prefixes, 2, 1, 17)
    print(f"Number of steps: {quad_tree.steps}")

    prefixes = ['T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    quad_tree.search_and_print(quad_tree.root, prefixes, 5, 10, 40)
    print(f"Number of steps: {quad_tree.steps}")

    prefixes = ['D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']
    quad_tree.search_and_print(quad_tree.root, prefixes, 2, 5, 15)
    print(f"Number of steps: {quad_tree.steps}")

    prefixes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V']
    quad_tree.search_and_print(quad_tree.root, prefixes, 5, 4, 70)
    print(f"Number of steps: {quad_tree.steps}")

    prefixes = ['C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W']
    quad_tree.search_and_print(quad_tree.root, prefixes, 0, 1, 4)
    print(f"Number of steps: {quad_tree.steps}")

    prefixes = ['E', 'F', 'G', 'H',]
    quad_tree.search_and_print(quad_tree.root, prefixes, 8, 3, 9)
    print(f"Number of steps: {quad_tree.steps}")

    prefixes = ['K', 'L', 'M', 'N']
    quad_tree.search_and_print(quad_tree.root, prefixes, 2, 5, 10)
    print(f"Number of steps: {quad_tree.steps}")

    prefixes = ['F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R']
    quad_tree.search_and_print(quad_tree.root, prefixes, 4, 1, 6)
    print(f"Number of steps: {quad_tree.steps}")

    prefixes = ['F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R']
    quad_tree.search_and_print(quad_tree.root, prefixes, 0, 3, 11)
    print(f"Number of steps: {quad_tree.steps}")

    prefixes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O']
    quad_tree.search_and_print(quad_tree.root, prefixes, 3, 2, 11)
    print(f"Number of steps: {quad_tree.steps}")

    prefixes = ['G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X']
    quad_tree.search_and_print(quad_tree.root, prefixes, 0, 1, 15)
    print(f"Number of steps: {quad_tree.steps}")

    prefixes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    quad_tree.search_and_print(quad_tree.root, prefixes, 5, 5, 40)
    print(f"Number of steps: {quad_tree.steps}")

    prefixes = ['C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X']
    quad_tree.search_and_print(quad_tree.root, prefixes, 3, 7, 30)
    print(f"Number of steps: {quad_tree.steps}")

    prefixes = ['H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    quad_tree.search_and_print(quad_tree.root, prefixes, 1, 2, 50)
    print(f"Number of steps: {quad_tree.steps}")

# Record the end time
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time

print(f"Total running time: {elapsed_time} seconds")
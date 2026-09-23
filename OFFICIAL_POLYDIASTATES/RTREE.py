import csv
import time

# Record the start time
start_time = time.time()
class Node:
    def __init__(self, is_leaf=True):
        self.is_leaf = is_leaf
        self.children = []
        self.entries = []
        self.bounding_box = None

    def add_entry(self, entry):
        self.entries.append(entry)
        if not self.is_leaf and len(self.entries) > 1:
            self.split_node()
        else:
            self.update_bounding_box()

    def update_bounding_box(self):
        if not self.children:
            return

        min_x = min(child.bounding_box['min_x'] for child in self.children)
        max_x = max(child.bounding_box['max_x'] for child in self.children)
        min_y = min(child.bounding_box['min_y'] for child in self.children)
        max_y = max(child.bounding_box['max_y'] for child in self.children)
        min_z = min(child.bounding_box['min_z'] for child in self.children)
        max_z = max(child.bounding_box['max_z'] for child in self.children)

        self.bounding_box = {'min_x': min_x, 'max_x': max_x, 'min_y': min_y, 'max_y': max_y, 'min_z': min_z, 'max_z': max_z}

    def split_node(self):
        entries = self.entries
        split_point = len(entries) // 2

        left_node = Node(is_leaf=self.is_leaf)
        right_node = Node(is_leaf=self.is_leaf)

        left_node.entries = entries[:split_point]
        right_node.entries = entries[split_point:]

        self.entries = []

        self.add_entry(left_node)
        self.add_entry(right_node)

        self.update_bounding_box()

class RTree:
    def __init__(self, max_entries=4):
        self.root = Node()
        self.max_entries = max_entries
        self.steps = 0

    def insert(self, entry):
        leaf = self.choose_leaf(self.root, entry)
        leaf.add_entry(entry)

    def choose_leaf(self, node, entry):
        if node.is_leaf:
            self.steps += 1
            return node

        min_child = min(node.children, key=lambda child: self.distance(child.bounding_box, entry))
        return self.choose_leaf(min_child, entry)

    def distance(self, bounding_box, entry):
        return abs(bounding_box['min_x'] - entry['x']) + abs(bounding_box['min_y'] - entry['y']) + abs(bounding_box['min_z'] - entry['z'])

    def search(self, query_params):
        found_entries = []
        self._search(self.root, query_params, found_entries)
        return found_entries

    def _search(self, node, query_params, found_entries):
     if node.is_leaf:
        
        for entry in node.entries:
            if (
                query_params['query_letter'][0] <= entry['name'][0] <= query_params['query_letter'][1] and
                int(entry['awards']) >= query_params['min_awards'] and
                query_params['min_publications'] <= int(entry['publications']) <= query_params['max_publications']
            ):
                #self.steps += 1
                found_entries.append(entry)
     else:
        for child in node.children:
            if self.overlap(query_params['query_letter'], child.bounding_box):
                self.steps += 1
                self._search(child, query_params, found_entries)

    def overlap(self, query_letter, bounding_box):
        return query_letter <= bounding_box['max_x'][0] and query_letter >= bounding_box['min_x'][0]

def load_data_from_csv(file_path):
    entries = []
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            entries.append({
                'name': row['name'],
                'awards': int(row['awards']),
                'publications': int(row.get('publications', 0)),
            })
    return entries

my_rtree = RTree()
entries = load_data_from_csv('output.csv')
for entry in entries:
    my_rtree.insert(entry)

# Ορίστε τα query parameters για κάθε αναζήτηση
queries = [
    {'query_letter': ('A', 'Z'), 'min_awards': 0, 'min_publications': 0, 'max_publications': 30},
    {'query_letter': ('A', 'K'), 'min_awards': 2, 'min_publications': 2, 'max_publications': 20},
    {'query_letter': ('C', 'K'), 'min_awards': 1, 'min_publications': 5, 'max_publications': 25},
    {'query_letter': ('D', 'L'), 'min_awards': 6, 'min_publications': 0, 'max_publications': 50},
    {'query_letter': ('J', 'P'), 'min_awards': 2, 'min_publications': 5, 'max_publications': 45},
    {'query_letter': ('A', 'Z'), 'min_awards': 7, 'min_publications': 0, 'max_publications': 50},
    {'query_letter': ('B', 'N'), 'min_awards': 2, 'min_publications': 1, 'max_publications': 17},
    {'query_letter': ('T', 'Z'), 'min_awards': 5, 'min_publications': 10, 'max_publications': 40},
    {'query_letter': ('D', 'P'), 'min_awards': 2, 'min_publications': 5, 'max_publications': 15},
    {'query_letter': ('A', 'V'), 'min_awards': 5, 'min_publications': 4, 'max_publications': 70},
    {'query_letter': ('C', 'W'), 'min_awards': 0, 'min_publications': 1, 'max_publications': 4},
    {'query_letter': ('E', 'H'), 'min_awards': 8, 'min_publications': 3, 'max_publications': 9},
    {'query_letter': ('K', 'N'), 'min_awards': 2, 'min_publications': 5, 'max_publications': 10},
    {'query_letter': ('F', 'R'), 'min_awards': 4, 'min_publications': 1, 'max_publications': 6},
    {'query_letter': ('C', 'Z'), 'min_awards': 0, 'min_publications': 3, 'max_publications': 11},
    {'query_letter': ('A', 'O'), 'min_awards': 3, 'min_publications': 2, 'max_publications': 11},
    {'query_letter': ('G', 'X'), 'min_awards': 0, 'min_publications': 1, 'max_publications': 15},
    {'query_letter': ('A', 'Z'), 'min_awards': 5, 'min_publications': 5, 'max_publications': 40},
    {'query_letter': ('C', 'X'), 'min_awards': 3, 'min_publications': 7, 'max_publications': 30},
    {'query_letter': ('H', 'Z'), 'min_awards': 1, 'min_publications': 2, 'max_publications': 50}
    # Προσθέστε όσα queries χρειάζεστε
    ]

# Εκτελείτε τις αναζητήσεις
for query_params in queries:
    found_entries = my_rtree.search(query_params)

    # Εκτύπωση αποτελεσμάτων
    print(f"Αποτελέσματα για query με παραμέτρους: {query_params}")
    if not found_entries:
        print("Δεν βρέθηκαν καταχωρήσεις.")
    else:
        for entry in found_entries:
            print(entry)
     # Επαναφορά του μετρητή για το επόμενο query
    print("\n")

# Record the end time
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time

print(f"Total running time: {elapsed_time} seconds")

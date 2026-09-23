import csv
from sortedcontainers import SortedDict
import time

# Record the start time
start_time = time.time()
data = []

with open('output.csv', 'r', encoding='UTF-8') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip header
    for row in reader:
        surname, awards, publications, education = row
        data.append({'surname': surname, 'awards': int(awards), 'publications': int(publications), 'education': education})



class RangeTree:
    def __init__(self):
        self.tree_surname = SortedDict()

    def insert(self, surname, awards, publications):
        if surname not in self.tree_surname:
            self.tree_surname[surname] = SortedDict()

        if awards not in self.tree_surname[surname]:
            self.tree_surname[surname][awards] = SortedDict()

        self.tree_surname[surname][awards][publications] = None

    def query(self, surname_range, awards_range, publications_range):
        result = []

        for surname in self.tree_surname.irange(surname_range[0], surname_range[1]):
            if surname < surname_range[0] or surname > surname_range[1]:
                continue

            for awards in self.tree_surname[surname].irange(awards_range[0], awards_range[1]):
                if awards < awards_range[0] or awards > awards_range[1]:
                    continue

                for publications in self.tree_surname[surname][awards].irange(publications_range[0], publications_range[1]):
                    if publications < publications_range[0] or publications > publications_range[1]:
                        continue

                    result.append({'surname': surname, 'awards': awards, 'publications': publications})

        return result

# Build the range tree
range_tree = RangeTree()
for entry in data:
    range_tree.insert(entry['surname'], entry['awards'], entry['publications'])

# Example query
#result_query = range_tree.query(('A', 'G'), (5, float('inf')), (100, 200))

# Print the results


# Example query
results = range_tree.query(('A', 'Z'), (0, float('inf')), (0, 200))
results2 = range_tree.query(('A', 'K'), (2, float('inf')),(2, 20))
results3 = range_tree.query(('C', 'K'), (1, float('inf')), (5, 25))
results4 = range_tree.query(('D', 'L'), (6, float('inf')), (0, 50))
results5 = range_tree.query(('J', 'P'), (2, float('inf')), (5, 45))
results6 = range_tree.query(('A', 'Z'), (7, float('inf')), (0, 50))
results7 = range_tree.query(('B', 'N'), (2, float('inf')), (1, 17))
results8 = range_tree.query(('T', 'Z'), (5, float('inf')), (10, 40))
results9 = range_tree.query(('D', 'P'), (2, float('inf')), (5, 15))
results10 = range_tree.query(('A', 'V'), (5, float('inf')), (4, 70))
results11 = range_tree.query(('C', 'W'), (0, float('inf')), (1, 4))
results12 = range_tree.query(('E', 'H'), (8, float('inf')), (3, 9))
results13 = range_tree.query(('K','N'), (2, float('inf')), (5, 10))
results14 = range_tree.query(('F','R'), (4, float('inf')), (1, 6))
results15 = range_tree.query(('C','Z'), (0, float('inf')), (3, 11))
results16 = range_tree.query(('A','O'), (3, float('inf')), (2, 11))
results17 = range_tree.query(('G','X'), (0, float('inf')), (1, 15))
results18 = range_tree.query(('A','Z'), (5, float('inf')), (5, 40))
results19 = range_tree.query(('C','X'), (3, float('inf')), (7, 30))
results20 = range_tree.query(('K','N'), (1, float('inf')), (2, 50))


# # Print the results
# for result in results:
#     print(result)
# # Print the results
# for result in results2:
#     print(result)
# # Print the results
# for result in results3:
#     print(result)
# # Print the results
# for result in results4:
#     print(result)
# # Print the results
# for result in results5:
#     print(result)
# # Print the results
# for result in results6:
#     print(result)
# # Print the results
# for result in results7:
#     print(result)
# # Print the results
# for result in results8:
#     print(result)
# # Print the results
# for result in results9:
#     print(result)
# # Print the results
# for result in results10:
#     print(result)
# # Print the results
# for result in results11:
#     print(result)
# Print the results
for result in results12:
    print(result)
# # Print the results
# for result in results13:
#     print(result)
# # Print the results
# for result in results14:
#     print(result)
# # Print the results
# for result in results15:
#     print(result)
# # Print the results
# for result in results16:
#     print(result)
# # Print the results
# for result in results17:
#     print(result)
# # Print the results
# for result in results18:
#     print(result)
# # Print the results
# for result in results19:
#     print(result)
# # Print the results
# for result in results20:
#     print(result)


# Record the end time
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time

print(f"Total running time: {elapsed_time} seconds")
import csv
from random import shuffle

def shingle(text: str, k: int):
    shingles = []
    for i in range(len(text) - k + 1):
        shingles.append(text[i:i+k])
    return set(shingles)

def jaccard(x, y):
    intersection_size = len(x.intersection(y))
    union_size = len(x.union(y))

    # Ελέγχουμε για μηδενικό μέγεθος του x.union(y) πριν τον υπολογισμό
    return intersection_size / union_size if union_size > 0 else 0

def create_hash_func(size: int):
    hash_ex = list(range(1, size + 1))
    shuffle(hash_ex)
    return hash_ex

def build_minhash_func(vocab_size: int, nbits: int):
    hashes = []
    for _ in range(nbits):
        hashes.append(create_hash_func(vocab_size))
    return hashes

def create_hash(vector: list, minhash_func):
    signature = []
    for func in minhash_func:
        for i in range(1, len(vector) + 1):
            idx = func.index(i)
            signature_val = vector[idx]
            if signature_val == 1:
                signature.append(idx)
                break
    return signature

def minhash_set(data, minhash_func):
    signature = create_hash(data, minhash_func)
    return set(signature)

def process_csv(file_path):
    scientists = []

    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # skip header row
        for row in reader:
            name, _, _, education = row
            scientists.append((name, education))

    return scientists

def main():
    file_path = 'output.csv'  # Αντικαταστήστε με την πραγματική διαδρομή του αρχείου CSV
    scientists = process_csv(file_path)

    k = 1
    vocab = set()

    # Εξαγωγή shingles και δημιουργία λεξιλογίου
    for _, education in scientists:
        education_shingles = shingle(education, k)
        vocab.update(education_shingles)

    vocab = list(vocab)
    minhash_func = build_minhash_func(len(vocab), 10)

    results = []  # Νέα λίστα για την αποθήκευση των αποτελεσμάτων

    for name, education in scientists:
        education_shingles = shingle(education, k)
        education_1hot = [1 if x in education_shingles else 0 for x in vocab]

        education_sig = create_hash(education_1hot, minhash_func)
        vocab_sig = create_hash([1 if x in vocab else 0 for x in vocab], minhash_func)

        education_sig_set = set(education_sig)
        vocab_sig_set = set(vocab_sig)
    
        jaccard_similarity = jaccard(education_sig_set, vocab_sig_set)
        
        results.append((name, jaccard_similarity * 100))  # Προσθήκη στα αποτελέσματα

    # Εκτύπωση των αποτελεσμάτων ή αποθήκευσή τους σε ένα αρχείο
    for name, similarity in results:
        print(f"{name}: Jaccard Similarity: {similarity:.2f}%")

    print(results)

if __name__ == "__main__":
    main()

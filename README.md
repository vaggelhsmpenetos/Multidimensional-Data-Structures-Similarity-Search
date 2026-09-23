# Multidimensional Data Structures & Similarity Search

## 📌 Project Overview

This project focuses on the **implementation and experimental evaluation of multidimensional data structures** for efficient indexing and querying of real-world textual data.

The project uses a dataset of **computer scientists** collected from Wikipedia. Each record contains multiple attributes, including the scientist's surname, number of awards, educational background, and number of DBLP records.

The main objective is to implement and experimentally compare different multidimensional indexing techniques combined with **Locality-Sensitive Hashing (LSH)** for similarity search.

---

## 📊 Dataset

The dataset consists of computer scientists collected from the following Wikipedia page:

🔗 [List of Computer Scientists](https://en.wikipedia.org/wiki/List_of_computer_scientists)

Each record contains the following attributes:

| Attribute | Description |
|-----------|-------------|
| `Surname` | The scientist's surname |
| `#Awards` | Number of awards received |
| `Education` | Textual information describing the scientist's educational background |
| `#DBLP_Record` | Number of publications/records associated with the scientist in DBLP |

The multidimensional index is constructed using the following three attributes:

- `Surname`
- `#Awards`
- `#DBLP_Record`

The `Education` attribute is used for the subsequent similarity search.

---

## 🌳 Multidimensional Indexing

Four different multidimensional indexing structures were implemented and experimentally evaluated:

- **k-d Trees**
- **Quad Trees**
- **Range Trees**
- **R-Trees**

These structures are used to efficiently filter the dataset according to multiple user-defined conditions.

For example, a query can identify computer scientists whose:

- surname belongs to a specific alphabetical range,
- number of awards exceeds a given threshold,
- number of DBLP records falls within a specified range.

This allows multiple filtering conditions to be processed through the multidimensional index before performing similarity search.

---

## 🔎 Similarity Search with LSH

After retrieving the relevant records through the multidimensional index, similarity queries are performed on the **Education** attribute.

**Locality-Sensitive Hashing (LSH)** is used to efficiently identify records with similar educational backgrounds according to a predefined similarity threshold.

For example, a query can search for computer scientists satisfying conditions such as:

> Surname in the range `[A, G]`, more than 4 awards, between 100 and 200 DBLP records, and an education similarity greater than 50%.

This combines **multidimensional filtering** with **text similarity search** within the same query process.

---

## ⚙️ Query Processing

The implemented system supports multidimensional filtering and similarity-based queries.

A typical query follows the following process:

```text
Input Query
    │
    ▼
Multidimensional Filtering
    │
    ├── Surname Range
    ├── Awards Threshold
    └── DBLP Records Range
    │
    ▼
Candidate Records
    │
    ▼
LSH Similarity Search
    │
    ▼
Similarity Filtering
    │
    ▼
Final Results

# Multidimensional Data Structures & Similarity Search

## Project Overview

This project focuses on the **implementation and experimental evaluation of multidimensional data structures** for efficient indexing and querying of real-world textual data.

The project uses a dataset of **computer scientists** collected from Wikipedia, where each record is represented using multiple attributes, including the scientist's surname, number of awards, educational background, and number of DBLP records.

The main objective is to investigate and compare different multidimensional indexing techniques combined with **Locality-Sensitive Hashing (LSH)** for similarity search.

## Dataset

The dataset consists of computer scientists obtained from the [List of Computer Scientists](https://en.wikipedia.org/wiki/List_of_computer_scientists) on Wikipedia.

Each record contains the following attributes:

- **Surname** — the scientist's surname
- **#Awards** — number of awards received
- **Education** — textual information describing the scientist's educational background
- **#DBLP_Record** — number of publications/records associated with the scientist in DBLP

The multidimensional index is constructed using the following three attributes:

- `Surname`
- `#Awards`
- `#DBLP_Record`

The `Education` attribute is subsequently used for similarity-based querying.

## Multidimensional Indexing

Four different multidimensional indexing approaches were implemented and experimentally evaluated:

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

## Similarity Search with LSH

After retrieving the relevant records through the multidimensional index, similarity queries are performed on the **Education** attribute.

**Locality-Sensitive Hashing (LSH)** is used to efficiently identify records with similar educational backgrounds based on a predefined similarity threshold.

For example, a query can search for computer scientists satisfying conditions such as:

> Surname in the range `[A, G]`, more than 4 awards, between 100 and 200 DBLP records, and an education similarity greater than 50%.

This combines **multidimensional filtering** with **text similarity search** in a single query workflow.

## Experimental Evaluation

The project includes an experimental comparison of the following approaches:

| Multidimensional Index | Similarity Search |
|------------------------|-------------------|
| k-d Tree               | LSH               |
| Quad Tree              | LSH               |
| Range Tree             | LSH               |
| R-Tree                 | LSH               |

The different approaches are evaluated experimentally to investigate their behavior and performance when processing multidimensional filtering and similarity queries over the dataset.

## Main Concepts

The project provides practical experience with:

- Multidimensional data structures
- Spatial and multidimensional indexing
- k-d Trees
- Quad Trees
- Range Trees
- R-Trees
- Locality-Sensitive Hashing (LSH)
- Similarity Search
- Range Queries
- Multidimensional Query Processing
- Experimental Performance Evaluation
- Real-world Data Collection and Processing

## Technologies

- **Python**
- **Data Structures & Algorithms**
- **Web Scraping / Data Collection**
- **Locality-Sensitive Hashing (LSH)**

## Academic Context

This project was developed as part of the course:

**Study, Implementation and Experimental Evaluation of Multidimensional Data Structures and Their Applications**

Department of Computer Engineering and Informatics.

**Supervisors:**

- Spyros Sioutas — Professor
- Konstantinos Tsichlas — Associate Professor

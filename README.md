# Database Design & SQL Basics - Week 4 Research Project

## Project Overview

This repository contains a comprehensive research report on database design principles and SQL fundamentals, covering relational database concepts, query mechanics, and performance optimization strategies.

## Project Structure

```
├── diagrams/                      # Entity-relationship diagrams, schema designs, and visual aids
├── output/                        # Generated PDF report and supplementary materials
├── scripts/                       # SQL demonstration scripts and query examples
│   ├── database_designs_Q1.py    # Python script for Question 1 demonstrations
│   ├── database_designs_Q2.py    # Python script for Question 2 demonstrations
│   ├── generate_pdf_report.py    # Automated PDF report generator
│   ├── generate_sql_diagrams.py  # Script to create SQL visualization diagrams
│   └── main.tex                  # LaTeX source for formatted report
├── sql/                           # Database schema definitions and sample data
│   ├── q5_join_examples.sql      # JOIN operations demonstrations (Question 5)
│   └── q6_groupby_examples.sql   # GROUP BY and aggregation examples (Question 6)
├── README.md                      # Project documentation (this file)
├── references.md                  # Comprehensive bibliography and citation list
├── references_q1.bib              # BibTeX references for Question 1
└── references_q2.bib              # BibTeX references for Question 2
```

## Research Topics Covered

### 1. Relational Model Foundations
Exploration of core relational database principles including relations, tuples, attributes, and domains. Analysis of logical data independence and its critical role in separating conceptual schemas from physical storage implementations in modern database management systems.

### 2. Keys & Constraints in Design Quality
Comprehensive differentiation of key types (candidate, primary, surrogate, foreign) and detailed examination of integrity constraints (NOT NULL, UNIQUE, CHECK, referential integrity). Discussion of how these mechanisms prevent insertion, deletion, and update anomalies.

### 3. Normalization vs. Denormalization
Comparative analysis of normal forms (1NF through BCNF) with practical examples of violations and remediation strategies. Balanced examination of when denormalization is strategically justified for analytical workloads, data warehousing, and read-heavy applications.

### 4. Conceptual vs. Logical vs. Physical Design
Three-tier database design methodology covering:
- **Conceptual:** Entity-Relationship modeling, business requirements capture
- **Logical:** Relational schema design, normalization, key identification
- **Physical:** Implementation details, indexing strategies, storage optimization

### 5. JOIN Semantics & Join Strategies
Technical deep-dive into SQL join operations:
- Join types: INNER, LEFT/RIGHT OUTER, FULL OUTER, CROSS
- NULL handling in join predicates and result sets
- Query optimizer join algorithms: nested loop, hash join, merge join
- Cost-based optimization and join order selection

### 6. GROUP BY, Aggregation & Set Semantics
Detailed examination of SQL aggregation mechanics:
- GROUP BY clause and partition formation
- HAVING clause for filtered aggregation
- Aggregate functions: SUM, COUNT, AVG, MIN, MAX
- NULL behavior in aggregation (COUNT(*) vs. COUNT(column))
- Common pitfalls: non-aggregated columns in SELECT lists

### 7. Transactions, Isolation & Integrity
ACID properties and transaction management:
- Atomicity, Consistency, Isolation, Durability explained
- SQL isolation levels: READ UNCOMMITTED, READ COMMITTED, REPEATABLE READ, SERIALIZABLE
- Concurrency anomalies: dirty reads, non-repeatable reads, phantom rows
- Synergy between constraints and transactions for data integrity

### 8. Indexing for Query Performance
Index architecture and performance optimization:
- B-tree index structure and use cases
- Hash indexes for equality predicates
- Bitmap indexes for low-cardinality columns
- Trade-offs: query speedup vs. write overhead
- Index selection for JOIN operations and GROUP BY clauses

## Methodology

This research project synthesizes information from multiple authoritative sources:

- **Academic textbooks:** Foundational database theory (Elmasri & Navathe, Date, Silberschatz et al.)
- **Vendor documentation:** PostgreSQL, MySQL, SQL Server, Oracle, SQLite official manuals
- **Research papers:** Peer-reviewed publications on query optimization and indexing
- **Industry resources:** Reputable technical blogs and database practitioner guides

All sources are properly cited using academic citation standards. See `references.md` and `.bib` files for complete bibliographic information.

## Key Deliverables

1. **PDF Report** (`output/` directory)
   - Structured responses to all 8 research questions
   - Integrated diagrams and visual explanations
   - 1,500–2,000 word count
   - Comprehensive citations

2. **Supporting Materials**
   - ER diagrams illustrating design concepts
   - SQL scripts demonstrating query patterns
   - Schema definitions showing normalization stages
   - Performance comparison data (where applicable)

## SQL Demonstrations

The `sql/` directory contains practical examples:
- Schema definitions for normalized vs. denormalized designs
- Sample queries demonstrating different JOIN types
- GROUP BY examples with various aggregate functions
- Index creation statements and performance annotations

The `scripts/` directory includes:
- Query execution demonstrations
- Transaction isolation level examples
- Index impact analysis scripts

## Diagrams & Visual Aids

The `diagrams/` directory features:
- Entity-Relationship diagrams (ERDs)
- Normalization progression visualizations
- Join operation Venn diagrams
- B-tree index structure illustrations
- Query execution plan examples

## Academic Integrity

This report represents original research and synthesis. All external sources are properly attributed. Direct quotations are minimized in favor of paraphrased explanations demonstrating understanding. Where specific technical definitions or algorithms are referenced, appropriate citations are provided.

## Learning Outcomes

Upon completing this research project, the team has achieved:

1. Deep understanding of relational database theoretical foundations
2. Practical knowledge of SQL query mechanics and optimization
3. Ability to design normalized schemas and justify denormalization decisions
4. Competence in analyzing query performance and applying indexing strategies
5. Comprehension of transaction management and data integrity mechanisms

## Tools & Technologies Referenced

- **Database Systems:** PostgreSQL, MySQL, SQL Server, Oracle Database, SQLite
- **Modeling Tools:** ER diagram notation, UML class diagrams
- **Query Analysis:** EXPLAIN/EXPLAIN ANALYZE output interpretation
- **Standards:** SQL:2016 standard (ISO/IEC 9075)

## Future Extensions

This foundational research can be extended to cover:
- NoSQL database models and CAP theorem trade-offs
- Distributed database systems and sharding strategies
- Advanced query optimization techniques (materialized views, partition pruning)
- Database security and access control mechanisms
- Temporal databases and slowly changing dimensions

## Contributors

This research project was completed collaboratively as a group assignment for Week 4 database fundamentals coursework.

## References

Complete bibliographic references are maintained in:
- `references.md` - Formatted reference list
- `references_q1.bib` - BibTeX entries for Question 1 sources
- `references_q2.bib` - BibTeX entries for Question 2 sources

Additional `.bib` files for the remaining questions follow similar naming conventions.



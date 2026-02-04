"""
SQL Research Document Generator for Q5 & Q6
===========================================

This script generates a comprehensive PDF report covering:
- Q5: JOIN Semantics & Join Strategies
- Q6: GROUP BY, Aggregation & Set Semantics

Including diagrams, code examples, and proper citations.
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER, TA_LEFT
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, Image
from reportlab.lib import colors
from reportlab.pdfgen import canvas
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from datetime import datetime
import os

class SQLResearchReport:
    def __init__(self, filename="SQL_Research_Q5_Q6.pdf"):
        self.filename = filename
        self.doc = SimpleDocTemplate(filename, pagesize=A4,
                                     rightMargin=72, leftMargin=72,
                                     topMargin=72, bottomMargin=18)
        self.story = []
        self.styles = getSampleStyleSheet()
        self._add_custom_styles()
        
    def _add_custom_styles(self):
        """Add custom paragraph styles"""
        # Title style
        self.styles.add(ParagraphStyle(
            name='CustomTitle',
            parent=self.styles['Heading1'],
            fontSize=24,
            textColor=colors.HexColor('#1a1a1a'),
            spaceAfter=30,
            alignment=TA_CENTER,
            fontName='Helvetica-Bold'
        ))
        
        # Section heading
        self.styles.add(ParagraphStyle(
            name='SectionHeading',
            parent=self.styles['Heading2'],
            fontSize=16,
            textColor=colors.HexColor('#2c5282'),
            spaceAfter=12,
            spaceBefore=12,
            fontName='Helvetica-Bold'
        ))
        
        # Subsection heading
        self.styles.add(ParagraphStyle(
            name='SubsectionHeading',
            parent=self.styles['Heading3'],
            fontSize=13,
            textColor=colors.HexColor('#2d3748'),
            spaceAfter=10,
            spaceBefore=10,
            fontName='Helvetica-Bold'
        ))
        
        # Body text
        self.styles.add(ParagraphStyle(
            name='BodyJustified',
            parent=self.styles['BodyText'],
            fontSize=11,
            alignment=TA_JUSTIFY,
            spaceAfter=12,
            leading=14
        ))
        
        # Code style
        self.styles.add(ParagraphStyle(
            name='SQLCode',
            parent=self.styles['Normal'],
            fontSize=9,
            fontName='Courier',
            textColor=colors.HexColor('#1a202c'),
            leftIndent=10,
            spaceAfter=10
        ))
        
        # Citation style
        self.styles.add(ParagraphStyle(
            name='Citation',
            parent=self.styles['Normal'],
            fontSize=9,
            textColor=colors.HexColor('#4a5568'),
            leftIndent=20,
            spaceAfter=6
        ))
    
    def add_title_page(self):
        """Add title page"""
        self.story.append(Spacer(1, 1.5*inch))
        
        title = Paragraph("Database Design & SQL Basics", self.styles['CustomTitle'])
        self.story.append(title)
        self.story.append(Spacer(1, 0.3*inch))
        
        subtitle = Paragraph("Research Report: Questions 5 & 6", self.styles['Heading2'])
        subtitle.alignment = TA_CENTER
        self.story.append(subtitle)
        self.story.append(Spacer(1, 0.5*inch))
        
        # Topics covered
        topics = Paragraph(
            "<b>Topics Covered:</b><br/>"
            "• JOIN Semantics & Join Strategies<br/>"
            "• GROUP BY, Aggregation & Set Semantics",
            self.styles['Normal']
        )
        topics.alignment = TA_CENTER
        self.story.append(topics)
        self.story.append(Spacer(1, 1*inch))
        
        # Date and details
        date_text = Paragraph(
            f"<b>Submission Date:</b> 06 February 2026<br/>"
            f"<b>Generated:</b> {datetime.now().strftime('%d %B %Y')}<br/>"
            f"<b>Word Count:</b> ~1,800 words",
            self.styles['Normal']
        )
        date_text.alignment = TA_CENTER
        self.story.append(date_text)
        
        self.story.append(PageBreak())
    
    def add_q5_content(self):
        """Add Q5: JOIN Semantics & Join Strategies"""
        
        # Question header
        header = Paragraph(
            "Q5. JOIN Semantics & Join Strategies (5 marks)",
            self.styles['SectionHeading']
        )
        self.story.append(header)
        self.story.append(Spacer(1, 0.1*inch))
        
        # Introduction
        intro = Paragraph(
            "Join operations are fundamental to relational database systems, enabling the combination "
            "of data from multiple tables based on related columns. Understanding join semantics, "
            "the behavior of NULL values in joins, and the underlying algorithms that database "
            "optimizers employ is essential for writing efficient queries and designing robust "
            "database applications. This section explores various join types, their semantic "
            "implications, and the algorithmic strategies databases use to execute them.",
            self.styles['BodyJustified']
        )
        self.story.append(intro)
        self.story.append(Spacer(1, 0.2*inch))
        
        # 5.1 Join Types and Semantics
        section1 = Paragraph("5.1 Join Types and Their Semantics", self.styles['SubsectionHeading'])
        self.story.append(section1)
        
        # INNER JOIN
        subsection1 = Paragraph("<b>5.1.1 INNER JOIN</b>", self.styles['Normal'])
        self.story.append(subsection1)
        
        inner_join_text = Paragraph(
            "An INNER JOIN returns only the rows where there is a match in both tables based on the "
            "join condition. It is the most restrictive join type and is the default when JOIN is "
            "specified without qualification. The result set includes only tuples where the join "
            "predicate evaluates to TRUE, excluding all NULL matches (Date, 2012).",
            self.styles['BodyJustified']
        )
        self.story.append(inner_join_text)
        
        # Code example
        code1 = Paragraph(
            "<font face='Courier' size=9>"
            "-- INNER JOIN example<br/>"
            "SELECT employees.name, departments.dept_name<br/>"
            "FROM employees<br/>"
            "INNER JOIN departments ON employees.dept_id = departments.dept_id;<br/>"
            "-- Result: Only employees with valid department assignments"
            "</font>",
            self.styles['SQLCode']
        )
        self.story.append(code1)
        
        # LEFT OUTER JOIN
        subsection2 = Paragraph("<b>5.1.2 LEFT OUTER JOIN (LEFT JOIN)</b>", self.styles['Normal'])
        self.story.append(subsection2)
        
        left_join_text = Paragraph(
            "A LEFT OUTER JOIN returns all rows from the left table and matching rows from the right "
            "table. When no match exists, NULL values are returned for columns from the right table. "
            "This preserves all tuples from the left relation regardless of whether they satisfy the "
            "join predicate, making it useful for identifying unmatched records (Elmasri & Navathe, 2015).",
            self.styles['BodyJustified']
        )
        self.story.append(left_join_text)
        
        code2 = Paragraph(
            "<font face='Courier' size=9>"
            "-- LEFT JOIN example<br/>"
            "SELECT employees.name, departments.dept_name<br/>"
            "FROM employees<br/>"
            "LEFT JOIN departments ON employees.dept_id = departments.dept_id;<br/>"
            "-- Result: All employees, even those without departments (dept_name = NULL)"
            "</font>",
            self.styles['SQLCode']
        )
        self.story.append(code2)
        
        # RIGHT OUTER JOIN
        subsection3 = Paragraph("<b>5.1.3 RIGHT OUTER JOIN (RIGHT JOIN)</b>", self.styles['Normal'])
        self.story.append(subsection3)
        
        right_join_text = Paragraph(
            "A RIGHT OUTER JOIN is the mirror image of LEFT JOIN, returning all rows from the right "
            "table and matching rows from the left table. NULL values appear for left table columns "
            "when no match exists. While less commonly used (as queries can be rewritten as LEFT JOINs "
            "by reversing table order), it provides semantic clarity in certain contexts (Ramakrishnan & Gehrke, 2003).",
            self.styles['BodyJustified']
        )
        self.story.append(right_join_text)
        
        # FULL OUTER JOIN
        subsection4 = Paragraph("<b>5.1.4 FULL OUTER JOIN</b>", self.styles['Normal'])
        self.story.append(subsection4)
        
        full_join_text = Paragraph(
            "A FULL OUTER JOIN combines the results of both LEFT and RIGHT joins, returning all rows "
            "from both tables. Rows without matches in either direction have NULL values for the "
            "non-matching table's columns. This is particularly valuable for data reconciliation tasks "
            "where identifying mismatches in both directions is necessary (PostgreSQL Documentation, 2024).",
            self.styles['BodyJustified']
        )
        self.story.append(full_join_text)
        
        code3 = Paragraph(
            "<font face='Courier' size=9>"
            "-- FULL OUTER JOIN example<br/>"
            "SELECT e.name, d.dept_name<br/>"
            "FROM employees e<br/>"
            "FULL OUTER JOIN departments d ON e.dept_id = d.dept_id;<br/>"
            "-- Result: All employees + all departments, with NULLs where unmatched"
            "</font>",
            self.styles['SQLCode']
        )
        self.story.append(code3)
        
        # CROSS JOIN
        subsection5 = Paragraph("<b>5.1.5 CROSS JOIN (Cartesian Product)</b>", self.styles['Normal'])
        self.story.append(subsection5)
        
        cross_join_text = Paragraph(
            "A CROSS JOIN produces the Cartesian product of two tables, combining every row from the "
            "first table with every row from the second table. If table A has m rows and table B has "
            "n rows, the result contains m × n rows. While rarely needed in production queries, CROSS "
            "JOINs are useful for generating combinations, test data, or when followed by filtering "
            "conditions (Garcia-Molina et al., 2009).",
            self.styles['BodyJustified']
        )
        self.story.append(cross_join_text)
        
        self.story.append(Spacer(1, 0.15*inch))
        
        # 5.2 NULL Behavior in Joins
        section2 = Paragraph("5.2 NULL Values and Join Semantics", self.styles['SubsectionHeading'])
        self.story.append(section2)
        
        null_behavior = Paragraph(
            "NULL values require special consideration in join operations due to SQL's three-valued "
            "logic (TRUE, FALSE, UNKNOWN). When a join predicate involves NULL values, the comparison "
            "results in UNKNOWN, not TRUE, causing the row to be excluded from INNER JOIN results. "
            "This behavior aligns with Codd's relational model but can be counterintuitive. For "
            "example, 'NULL = NULL' evaluates to UNKNOWN, not TRUE, meaning two NULL values are not "
            "considered equal in join conditions. Outer joins preserve rows with NULL values, but the "
            "NULL semantics still affect which rows are matched versus which are padded with NULLs "
            "(Date & Darwen, 1997; Microsoft SQL Server Documentation, 2024).",
            self.styles['BodyJustified']
        )
        self.story.append(null_behavior)
        
        code4 = Paragraph(
            "<font face='Courier' size=9>"
            "-- NULL behavior demonstration<br/>"
            "SELECT * FROM table1 t1<br/>"
            "INNER JOIN table2 t2 ON t1.col = t2.col;<br/>"
            "-- Rows where either col is NULL are excluded<br/><br/>"
            "-- To include NULL matches, use:<br/>"
            "SELECT * FROM table1 t1<br/>"
            "INNER JOIN table2 t2 ON (t1.col = t2.col OR (t1.col IS NULL AND t2.col IS NULL));"
            "</font>",
            self.styles['SQLCode']
        )
        self.story.append(code4)
        self.story.append(Spacer(1, 0.15*inch))
        
        # 5.3 Join Algorithms
        section3 = Paragraph("5.3 Join Algorithms and Optimizer Strategies", self.styles['SubsectionHeading'])
        self.story.append(section3)
        
        algo_intro = Paragraph(
            "Database query optimizers select from several join algorithms based on table sizes, "
            "available indexes, memory constraints, and data distribution. The three primary algorithms "
            "are nested loop joins, hash joins, and merge joins, each with distinct performance "
            "characteristics (Ramakrishnan & Gehrke, 2003).",
            self.styles['BodyJustified']
        )
        self.story.append(algo_intro)
        
        # Nested Loop Join
        subsection6 = Paragraph("<b>5.3.1 Nested Loop Join</b>", self.styles['Normal'])
        self.story.append(subsection6)
        
        nested_loop = Paragraph(
            "The nested loop join iterates through each row in the outer table and, for each row, "
            "scans the inner table for matching rows. The basic algorithm has O(n × m) complexity, "
            "making it inefficient for large tables. However, when an index exists on the join column "
            "of the inner table (creating an 'index nested loop join'), the inner table lookup becomes "
            "O(log m), significantly improving performance. Optimizers favor this approach when one "
            "table is small or when highly selective predicates reduce the outer table's effective "
            "size (Oracle Database Documentation, 2024).",
            self.styles['BodyJustified']
        )
        self.story.append(nested_loop)
        
        # Hash Join
        subsection7 = Paragraph("<b>5.3.2 Hash Join</b>", self.styles['Normal'])
        self.story.append(subsection7)
        
        hash_join = Paragraph(
            "Hash joins build an in-memory hash table from the smaller input (the 'build' phase), "
            "then probe this hash table with rows from the larger input (the 'probe' phase). With "
            "adequate memory, hash joins achieve O(n + m) complexity, making them highly efficient "
            "for large equi-joins. The algorithm is particularly effective when no suitable indexes "
            "exist and both tables are large. However, hash joins require sufficient memory for the "
            "hash table; when memory is inadequate, the database must partition data to disk (grace "
            "hash join), increasing I/O costs. Additionally, hash joins only support equality "
            "predicates, not range conditions (PostgreSQL Documentation, 2024; Graefe, 1993).",
            self.styles['BodyJustified']
        )
        self.story.append(hash_join)
        
        # Merge Join
        subsection8 = Paragraph("<b>5.3.3 Merge Join (Sort-Merge Join)</b>", self.styles['Normal'])
        self.story.append(subsection8)
        
        merge_join = Paragraph(
            "Merge joins require both inputs to be sorted on the join key. The algorithm then performs "
            "a synchronized scan through both sorted sets, merging matching rows. If the data is "
            "already sorted (due to indexes or prior operations), merge joins are extremely efficient "
            "with O(n + m) complexity. When sorting is required, the total complexity becomes "
            "O(n log n + m log m + n + m). Merge joins excel for large tables with available sort "
            "orders and support both equality and range predicates. They are particularly advantageous "
            "when the join output needs to be sorted anyway, eliminating duplicate sort operations "
            "(Elmasri & Navathe, 2015; MySQL Documentation, 2024).",
            self.styles['BodyJustified']
        )
        self.story.append(merge_join)
        
        # Optimizer decision factors
        subsection9 = Paragraph("<b>5.3.4 Optimizer Selection Criteria</b>", self.styles['Normal'])
        self.story.append(subsection9)
        
        optimizer = Paragraph(
            "Query optimizers analyze multiple factors when choosing join algorithms: table "
            "cardinalities, selectivity of predicates, available indexes, memory availability, data "
            "distribution statistics, and existing sort orders. Cost-based optimizers estimate I/O "
            "costs, CPU costs, and memory requirements for each algorithm, selecting the strategy with "
            "the lowest total cost. Modern optimizers may also consider parallel execution capabilities, "
            "choosing algorithms that parallelize effectively. The EXPLAIN or EXPLAIN PLAN commands "
            "reveal the optimizer's chosen strategy, enabling developers to understand and tune query "
            "performance (Garcia-Molina et al., 2009; PostgreSQL Documentation, 2024).",
            self.styles['BodyJustified']
        )
        self.story.append(optimizer)
        
        self.story.append(PageBreak())
    
    def add_q6_content(self):
        """Add Q6: GROUP BY, Aggregation & Set Semantics"""
        
        # Question header
        header = Paragraph(
            "Q6. GROUP BY, Aggregation & Set Semantics (5 marks)",
            self.styles['SectionHeading']
        )
        self.story.append(header)
        self.story.append(Spacer(1, 0.1*inch))
        
        # Introduction
        intro = Paragraph(
            "Aggregation and grouping operations are essential for data analysis and reporting, "
            "enabling the summarization of large datasets into meaningful insights. SQL provides "
            "powerful constructs for grouping rows based on common values and applying aggregate "
            "functions to compute statistics. Understanding how GROUP BY, HAVING, and aggregate "
            "functions interact, particularly in the presence of NULL values, is crucial for correct "
            "query formulation and avoiding common pitfalls.",
            self.styles['BodyJustified']
        )
        self.story.append(intro)
        self.story.append(Spacer(1, 0.2*inch))
        
        # 6.1 GROUP BY Mechanics
        section1 = Paragraph("6.1 GROUP BY Clause Mechanics", self.styles['SubsectionHeading'])
        self.story.append(section1)
        
        groupby_mechanics = Paragraph(
            "The GROUP BY clause partitions rows into groups based on the values of specified columns. "
            "All rows sharing the same values in the GROUP BY columns form a single group. Aggregate "
            "functions (SUM, COUNT, AVG, MIN, MAX) then operate on each group independently, producing "
            "one result row per group. Conceptually, GROUP BY transforms a relation with n rows into a "
            "relation with g groups, where g ≤ n. NULL values in grouping columns are treated as equal "
            "to each other, placing all rows with NULL in the same group (Date, 2012; Elmasri & Navathe, 2015).",
            self.styles['BodyJustified']
        )
        self.story.append(groupby_mechanics)
        
        code5 = Paragraph(
            "<font face='Courier' size=9>"
            "-- Basic GROUP BY example<br/>"
            "SELECT department_id, COUNT(*) as employee_count, AVG(salary) as avg_salary<br/>"
            "FROM employees<br/>"
            "GROUP BY department_id;<br/>"
            "-- Each row in result represents one department with aggregated values"
            "</font>",
            self.styles['SQLCode']
        )
        self.story.append(code5)
        
        groupby_rules = Paragraph(
            "A fundamental rule of GROUP BY is that any column in the SELECT list that is not part of "
            "an aggregate function must appear in the GROUP BY clause. This ensures deterministic "
            "results—without this restriction, the database would need to arbitrarily choose which "
            "value to return from multiple rows in a group. Modern SQL standards and most databases "
            "enforce this rule, although some systems (like MySQL with certain settings) permit "
            "non-deterministic queries, which should be avoided (MySQL Documentation, 2024).",
            self.styles['BodyJustified']
        )
        self.story.append(groupby_rules)
        
        code6 = Paragraph(
            "<font face='Courier' size=9>"
            "-- INCORRECT: name not in GROUP BY<br/>"
            "SELECT department_id, name, COUNT(*)<br/>"
            "FROM employees<br/>"
            "GROUP BY department_id;  -- ERROR or non-deterministic<br/><br/>"
            "-- CORRECT: Only grouped/aggregated columns<br/>"
            "SELECT department_id, COUNT(*), MAX(name) as example_name<br/>"
            "FROM employees<br/>"
            "GROUP BY department_id;"
            "</font>",
            self.styles['SQLCode']
        )
        self.story.append(code6)
        self.story.append(Spacer(1, 0.15*inch))
        
        # 6.2 HAVING Clause
        section2 = Paragraph("6.2 HAVING Clause for Group Filtering", self.styles['SubsectionHeading'])
        self.story.append(section2)
        
        having_clause = Paragraph(
            "While WHERE filters individual rows before grouping, HAVING filters groups after aggregation. "
            "HAVING conditions can reference aggregate functions, enabling queries like 'find departments "
            "with more than 10 employees' or 'show products with average sales above $1000'. The logical "
            "query processing order is: WHERE → GROUP BY → aggregate computation → HAVING → SELECT → ORDER BY. "
            "Using WHERE instead of HAVING when possible is more efficient, as it reduces the number of "
            "rows before the expensive grouping operation (Ramakrishnan & Gehrke, 2003; PostgreSQL Documentation, 2024).",
            self.styles['BodyJustified']
        )
        self.story.append(having_clause)
        
        code7 = Paragraph(
            "<font face='Courier' size=9>"
            "-- HAVING example: departments with avg salary > 50000<br/>"
            "SELECT department_id, AVG(salary) as avg_salary, COUNT(*) as emp_count<br/>"
            "FROM employees<br/>"
            "WHERE active = 1  -- Filter rows before grouping<br/>"
            "GROUP BY department_id<br/>"
            "HAVING AVG(salary) > 50000  -- Filter groups after aggregation<br/>"
            "ORDER BY avg_salary DESC;"
            "</font>",
            self.styles['SQLCode']
        )
        self.story.append(code7)
        self.story.append(Spacer(1, 0.15*inch))
        
        # 6.3 Aggregate Functions
        section3 = Paragraph("6.3 Aggregate Functions: SUM, COUNT, AVG, MIN, MAX", self.styles['SubsectionHeading'])
        self.story.append(section3)
        
        aggregates_intro = Paragraph(
            "SQL provides five standard aggregate functions, each with specific NULL handling behaviors:",
            self.styles['BodyJustified']
        )
        self.story.append(aggregates_intro)
        
        # Create aggregate functions table
        agg_data = [
            ['Function', 'Description', 'NULL Behavior'],
            ['COUNT(*)', 'Counts all rows in group', 'Counts rows with NULL values'],
            ['COUNT(column)', 'Counts non-NULL values', 'Ignores NULL values'],
            ['SUM(column)', 'Sums numeric values', 'Ignores NULLs; returns NULL if all NULL'],
            ['AVG(column)', 'Computes arithmetic mean', 'Ignores NULLs in calculation'],
            ['MIN(column)', 'Finds minimum value', 'Ignores NULLs'],
            ['MAX(column)', 'Finds maximum value', 'Ignores NULLs']
        ]
        
        agg_table = Table(agg_data, colWidths=[1.2*inch, 2.2*inch, 2*inch])
        agg_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#2c5282')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 10),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 1), (-1, -1), 9),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
            ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ]))
        self.story.append(agg_table)
        self.story.append(Spacer(1, 0.15*inch))
        
        # 6.4 COUNT(*) vs COUNT(column)
        section4 = Paragraph("6.4 COUNT(*) vs COUNT(column): Critical Distinction", self.styles['SubsectionHeading'])
        self.story.append(section4)
        
        count_distinction = Paragraph(
            "The difference between COUNT(*) and COUNT(column) is one of the most important concepts "
            "in SQL aggregation. COUNT(*) counts all rows in the group, regardless of NULL values in "
            "any column. COUNT(column) counts only rows where the specified column contains a non-NULL "
            "value. This distinction is critical for data quality analysis and understanding dataset "
            "completeness. For instance, COUNT(*) - COUNT(column) reveals the number of NULL values "
            "in that column (Date, 2012; Microsoft SQL Server Documentation, 2024).",
            self.styles['BodyJustified']
        )
        self.story.append(count_distinction)
        
        code8 = Paragraph(
            "<font face='Courier' size=9>"
            "-- Demonstrating COUNT(*) vs COUNT(column)<br/>"
            "SELECT <br/>"
            "    department_id,<br/>"
            "    COUNT(*) as total_employees,<br/>"
            "    COUNT(email) as employees_with_email,<br/>"
            "    COUNT(*) - COUNT(email) as employees_without_email,<br/>"
            "    COUNT(DISTINCT manager_id) as unique_managers<br/>"
            "FROM employees<br/>"
            "GROUP BY department_id;"
            "</font>",
            self.styles['SQLCode']
        )
        self.story.append(code8)
        
        self.story.append(Spacer(1, 0.15*inch))
        
        # 6.5 NULL Behavior in Aggregates
        section5 = Paragraph("6.5 NULL Value Behavior in Aggregation", self.styles['SubsectionHeading'])
        self.story.append(section5)
        
        null_aggregation = Paragraph(
            "Understanding NULL behavior in aggregate functions prevents subtle bugs and incorrect "
            "results. Most aggregate functions (SUM, AVG, MIN, MAX, COUNT(column)) ignore NULL values "
            "entirely during computation. This means AVG(salary) computes the average of non-NULL "
            "salaries, not the average including NULLs as zero. If all values in a group are NULL, "
            "SUM, AVG, MIN, and MAX return NULL, not zero. COUNT(column) returns 0 for an all-NULL "
            "group, while COUNT(*) returns the number of rows. To include NULLs as zero in calculations, "
            "explicit COALESCE or IFNULL conversion is required (Elmasri & Navathe, 2015; Oracle Database "
            "Documentation, 2024).",
            self.styles['BodyJustified']
        )
        self.story.append(null_aggregation)
        
        code9 = Paragraph(
            "<font face='Courier' size=9>"
            "-- NULL behavior examples<br/>"
            "-- Sample data: values = [100, NULL, 200, NULL]<br/><br/>"
            "SELECT <br/>"
            "    SUM(value) as sum_result,           -- 300 (ignores NULLs)<br/>"
            "    AVG(value) as avg_result,           -- 150 (300/2, not 300/4)<br/>"
            "    COUNT(*) as count_all,              -- 4<br/>"
            "    COUNT(value) as count_non_null,     -- 2<br/>"
            "    SUM(COALESCE(value, 0)) as sum_with_nulls_as_zero  -- 300<br/>"
            "FROM table;"
            "</font>",
            self.styles['SQLCode']
        )
        self.story.append(code9)
        self.story.append(Spacer(1, 0.15*inch))
        
        # 6.6 Common Pitfalls
        section6 = Paragraph("6.6 Common Pitfalls and Best Practices", self.styles['SubsectionHeading'])
        self.story.append(section6)
        
        pitfall1 = Paragraph("<b>6.6.1 Non-Aggregated Columns in SELECT</b>", self.styles['Normal'])
        self.story.append(pitfall1)
        
        pitfall1_text = Paragraph(
            "The most common GROUP BY error is including non-aggregated columns in the SELECT clause "
            "that don't appear in GROUP BY. This produces non-deterministic results or errors depending "
            "on the database system. Some databases (MySQL with sql_mode not set to ONLY_FULL_GROUP_BY) "
            "allow this but return arbitrary values, leading to incorrect analysis. Always ensure every "
            "non-aggregated column in SELECT appears in GROUP BY (Ramakrishnan & Gehrke, 2003).",
            self.styles['BodyJustified']
        )
        self.story.append(pitfall1_text)
        
        pitfall2 = Paragraph("<b>6.6.2 Aggregating Already Aggregated Results</b>", self.styles['Normal'])
        self.story.append(pitfall2)
        
        pitfall2_text = Paragraph(
            "Aggregate functions cannot be nested directly (e.g., SUM(COUNT(*)) is invalid). To "
            "aggregate aggregates, use subqueries or Common Table Expressions (CTEs). For example, "
            "to find the maximum average salary across departments, compute department averages in "
            "a subquery, then apply MAX to those results (PostgreSQL Documentation, 2024).",
            self.styles['BodyJustified']
        )
        self.story.append(pitfall2_text)
        
        code10 = Paragraph(
            "<font face='Courier' size=9>"
            "-- INCORRECT: Cannot nest aggregates<br/>"
            "SELECT MAX(AVG(salary)) FROM employees GROUP BY department_id;<br/><br/>"
            "-- CORRECT: Use subquery<br/>"
            "SELECT MAX(avg_sal) FROM (<br/>"
            "    SELECT AVG(salary) as avg_sal<br/>"
            "    FROM employees<br/>"
            "    GROUP BY department_id<br/>"
            ") dept_averages;"
            "</font>",
            self.styles['SQLCode']
        )
        self.story.append(code10)
        
        pitfall3 = Paragraph("<b>6.6.3 Empty Groups and Division by Zero</b>", self.styles['Normal'])
        self.story.append(pitfall3)
        
        pitfall3_text = Paragraph(
            "When computing ratios or percentages, be aware that COUNT can return 0, leading to "
            "division by zero errors. Use NULLIF or CASE expressions to handle this gracefully. "
            "Additionally, remember that an empty table with GROUP BY produces no result rows, not "
            "a single row with NULL aggregates, which differs from aggregating without GROUP BY "
            "(Date, 2012; MySQL Documentation, 2024).",
            self.styles['BodyJustified']
        )
        self.story.append(pitfall3_text)
        
        self.story.append(Spacer(1, 0.15*inch))
        
        # 6.7 Set Semantics
        section7 = Paragraph("6.7 Set Semantics: DISTINCT and GROUP BY Interaction", self.styles['SubsectionHeading'])
        self.story.append(section7)
        
        set_semantics = Paragraph(
            "SQL operates on multisets (bags) by default, allowing duplicate rows. The DISTINCT keyword "
            "enforces set semantics by eliminating duplicates. When used with aggregates, DISTINCT "
            "operates within each group. For example, COUNT(DISTINCT customer_id) counts unique customers "
            "per group, not total orders. This is particularly useful for metrics like unique visitors, "
            "distinct products, or unique events. Note that DISTINCT adds overhead as it requires sorting "
            "or hashing to identify duplicates (Garcia-Molina et al., 2009; PostgreSQL Documentation, 2024).",
            self.styles['BodyJustified']
        )
        self.story.append(set_semantics)
        
        code11 = Paragraph(
            "<font face='Courier' size=9>"
            "-- DISTINCT in aggregation<br/>"
            "SELECT <br/>"
            "    product_id,<br/>"
            "    COUNT(*) as total_orders,<br/>"
            "    COUNT(DISTINCT customer_id) as unique_customers,<br/>"
            "    SUM(quantity) as total_quantity,<br/>"
            "    SUM(DISTINCT quantity) as sum_of_distinct_quantities<br/>"
            "FROM orders<br/>"
            "GROUP BY product_id;"
            "</font>",
            self.styles['SQLCode']
        )
        self.story.append(code11)
        
        self.story.append(PageBreak())
    
    def add_references(self):
        """Add references section"""
        header = Paragraph("References", self.styles['SectionHeading'])
        self.story.append(header)
        self.story.append(Spacer(1, 0.1*inch))
        
        references = [
            "Date, C. J. (2012). <i>Database Design and Relational Theory: Normal Forms and All That Jazz</i>. O'Reilly Media.",
            
            "Date, C. J., & Darwen, H. (1997). <i>A Guide to the SQL Standard</i> (4th ed.). Addison-Wesley.",
            
            "Elmasri, R., & Navathe, S. B. (2015). <i>Fundamentals of Database Systems</i> (7th ed.). Pearson.",
            
            "Garcia-Molina, H., Ullman, J. D., & Widom, J. (2009). <i>Database Systems: The Complete Book</i> (2nd ed.). Prentice Hall.",
            
            "Graefe, G. (1993). Query Evaluation Techniques for Large Databases. <i>ACM Computing Surveys</i>, 25(2), 73-169.",
            
            "Microsoft SQL Server Documentation. (2024). <i>Joins (SQL Server)</i>. Retrieved from https://learn.microsoft.com/en-us/sql/relational-databases/performance/joins",
            
            "MySQL Documentation. (2024). <i>MySQL 8.0 Reference Manual</i>. Retrieved from https://dev.mysql.com/doc/refman/8.0/en/",
            
            "Oracle Database Documentation. (2024). <i>Database SQL Language Reference</i>. Retrieved from https://docs.oracle.com/en/database/oracle/oracle-database/",
            
            "PostgreSQL Documentation. (2024). <i>PostgreSQL 16 Documentation</i>. Retrieved from https://www.postgresql.org/docs/16/",
            
            "Ramakrishnan, R., & Gehrke, J. (2003). <i>Database Management Systems</i> (3rd ed.). McGraw-Hill."
        ]
        
        for ref in references:
            p = Paragraph(ref, self.styles['Citation'])
            self.story.append(p)
            self.story.append(Spacer(1, 0.08*inch))
    
    def generate_pdf(self):
        """Generate the PDF document"""
        self.add_title_page()
        self.add_q5_content()
        self.add_q6_content()
        self.add_references()
        
        # Build PDF
        self.doc.build(self.story)
        print(f"✓ PDF generated successfully: {self.filename}")
        print(f"✓ File location: {os.path.abspath(self.filename)}")

def main():
    """Main execution function"""
    print("=" * 70)
    print("SQL RESEARCH REPORT GENERATOR - Q5 & Q6")
    print("=" * 70)
    print("\nGenerating comprehensive PDF report...")
    print("Topics: JOIN Semantics & GROUP BY Aggregation")
    print()
    
    report = SQLResearchReport("SQL_Research_Q5_Q6.pdf")
    report.generate_pdf()
    
    print("\n" + "=" * 70)
    print("REPORT GENERATION COMPLETE!")
    print("=" * 70)

if __name__ == "__main__":
    main()
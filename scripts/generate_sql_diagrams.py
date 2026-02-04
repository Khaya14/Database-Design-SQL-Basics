#!/usr/bin/env python3
"""
Green-themed SQL Diagrams Generator for Q5 & Q6
Generates professional diagrams with green color scheme
"""

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle, FancyArrowPatch
import numpy as np

# Define green color palette
COLORS = {
    'primary': '#2D5016',      # Dark forest green
    'secondary': '#4A7C2C',    # Medium green
    'accent': '#6B9F3E',       # Light green
    'highlight': '#8BC34A',    # Bright green
    'light': '#C5E1A5',        # Very light green
    'background': '#F1F8E9',   # Cream green background
    'text': '#1B5E20',         # Dark green text
    'white': '#FFFFFF',
    'border': '#558B2F'        # Green border
}

def set_green_style():
    """Set matplotlib style with green theme"""
    plt.style.use('default')
    plt.rcParams['figure.facecolor'] = COLORS['background']
    plt.rcParams['axes.facecolor'] = COLORS['white']
    plt.rcParams['axes.edgecolor'] = COLORS['border']
    plt.rcParams['axes.labelcolor'] = COLORS['text']
    plt.rcParams['text.color'] = COLORS['text']
    plt.rcParams['xtick.color'] = COLORS['text']
    plt.rcParams['ytick.color'] = COLORS['text']
    plt.rcParams['font.size'] = 10
    plt.rcParams['axes.titlesize'] = 14
    plt.rcParams['axes.titleweight'] = 'bold'

def create_join_venn_diagrams():
    """Create Venn diagrams showing different JOIN types with green theme"""
    set_green_style()
    
    fig, axes = plt.subplots(2, 3, figsize=(15, 10))
    fig.suptitle('SQL JOIN Types - Visual Guide', fontsize=18, fontweight='bold', 
                 color=COLORS['primary'], y=0.98)
    
    join_types = [
        ('INNER JOIN', 'only_intersection'),
        ('LEFT JOIN', 'left_and_intersection'),
        ('RIGHT JOIN', 'right_and_intersection'),
        ('FULL OUTER JOIN', 'all'),
        ('LEFT EXCLUDING JOIN', 'only_left'),
        ('RIGHT EXCLUDING JOIN', 'only_right')
    ]
    
    for idx, (join_name, join_type) in enumerate(join_types):
        ax = axes[idx // 3, idx % 3]
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.set_aspect('equal')
        ax.axis('off')
        
        # Draw circles
        left_circle = Circle((3.5, 5), 2.5, fill=False, edgecolor=COLORS['primary'], 
                            linewidth=3, linestyle='-')
        right_circle = Circle((6.5, 5), 2.5, fill=False, edgecolor=COLORS['secondary'], 
                             linewidth=3, linestyle='-')
        
        # Fill based on join type
        if join_type == 'only_intersection':
            # INNER JOIN - only intersection
            intersection = Circle((5, 5), 1.3, color=COLORS['highlight'], alpha=0.7, zorder=1)
            ax.add_patch(intersection)
        elif join_type == 'left_and_intersection':
            # LEFT JOIN
            left_fill = Circle((3.5, 5), 2.5, color=COLORS['accent'], alpha=0.5, zorder=1)
            ax.add_patch(left_fill)
        elif join_type == 'right_and_intersection':
            # RIGHT JOIN
            right_fill = Circle((6.5, 5), 2.5, color=COLORS['secondary'], alpha=0.5, zorder=1)
            ax.add_patch(right_fill)
        elif join_type == 'all':
            # FULL OUTER JOIN
            left_fill = Circle((3.5, 5), 2.5, color=COLORS['accent'], alpha=0.5, zorder=1)
            right_fill = Circle((6.5, 5), 2.5, color=COLORS['secondary'], alpha=0.5, zorder=1)
            ax.add_patch(left_fill)
            ax.add_patch(right_fill)
        elif join_type == 'only_left':
            # LEFT EXCLUDING JOIN
            left_fill = Circle((3.5, 5), 2.5, color=COLORS['accent'], alpha=0.5, zorder=1)
            ax.add_patch(left_fill)
            # Cover intersection
            intersection_cover = Circle((5, 5), 1.3, color=COLORS['white'], zorder=2)
            ax.add_patch(intersection_cover)
        elif join_type == 'only_right':
            # RIGHT EXCLUDING JOIN
            right_fill = Circle((6.5, 5), 2.5, color=COLORS['secondary'], alpha=0.5, zorder=1)
            ax.add_patch(right_fill)
            # Cover intersection
            intersection_cover = Circle((5, 5), 1.3, color=COLORS['white'], zorder=2)
            ax.add_patch(intersection_cover)
        
        ax.add_patch(left_circle)
        ax.add_patch(right_circle)
        
        # Labels
        ax.text(2.5, 8.5, join_name, fontsize=12, fontweight='bold', 
               ha='left', color=COLORS['primary'])
        ax.text(2, 5, 'Table A', fontsize=10, ha='center', fontweight='bold',
               color=COLORS['text'])
        ax.text(8, 5, 'Table B', fontsize=10, ha='center', fontweight='bold',
               color=COLORS['text'])
        
        # Add SQL syntax
        sql_syntax = {
            'INNER JOIN': 'SELECT * FROM A\nINNER JOIN B\nON A.id = B.id',
            'LEFT JOIN': 'SELECT * FROM A\nLEFT JOIN B\nON A.id = B.id',
            'RIGHT JOIN': 'SELECT * FROM A\nRIGHT JOIN B\nON A.id = B.id',
            'FULL OUTER JOIN': 'SELECT * FROM A\nFULL OUTER JOIN B\nON A.id = B.id',
            'LEFT EXCLUDING JOIN': 'SELECT * FROM A\nLEFT JOIN B\nON A.id = B.id\nWHERE B.id IS NULL',
            'RIGHT EXCLUDING JOIN': 'SELECT * FROM A\nRIGHT JOIN B\nON A.id = B.id\nWHERE A.id IS NULL'
        }
        
        ax.text(5, 1.2, sql_syntax[join_name], fontsize=7, ha='center', 
               va='top', family='monospace', color=COLORS['text'],
               bbox=dict(boxstyle='round,pad=0.5', facecolor=COLORS['light'], 
                        edgecolor=COLORS['border'], alpha=0.8))
    
    plt.tight_layout()
    plt.savefig('/home/claude/join_venn_diagrams_green.png', dpi=300, bbox_inches='tight',
                facecolor=COLORS['background'])
    plt.close()

def create_join_results_example():
    """Create a visual example of JOIN results with green theme"""
    set_green_style()
    
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Title
    ax.text(7, 9.5, 'JOIN Results Example', fontsize=16, fontweight='bold', 
           ha='center', color=COLORS['primary'])
    
    # Sample data
    employees = [
        ['ID', 'Name', 'Dept_ID'],
        ['1', 'Alice', '10'],
        ['2', 'Bob', '20'],
        ['3', 'Charlie', 'NULL'],
        ['4', 'Diana', '30']
    ]
    
    departments = [
        ['ID', 'Dept_Name'],
        ['10', 'Sales'],
        ['20', 'Engineering'],
        ['40', 'Marketing']
    ]
    
    # Draw Employees table
    table_x, table_y = 0.5, 6.5
    ax.text(2, table_y + 1.5, 'Employees Table', fontsize=11, fontweight='bold',
           color=COLORS['primary'])
    
    for i, row in enumerate(employees):
        y = table_y - i * 0.4
        for j, cell in enumerate(row):
            x = table_x + j * 1.3
            color = COLORS['accent'] if i == 0 else COLORS['light']
            rect = Rectangle((x, y-0.35), 1.2, 0.35, facecolor=color, 
                           edgecolor=COLORS['border'], linewidth=1.5)
            ax.add_patch(rect)
            ax.text(x + 0.6, y - 0.175, cell, ha='center', va='center', 
                   fontsize=9, fontweight='bold' if i == 0 else 'normal',
                   color=COLORS['text'])
    
    # Draw Departments table
    dept_x = 5.5
    ax.text(6.2, table_y + 1.5, 'Departments Table', fontsize=11, fontweight='bold',
           color=COLORS['primary'])
    
    for i, row in enumerate(departments):
        y = table_y - i * 0.4
        for j, cell in enumerate(row):
            x = dept_x + j * 1.5
            color = COLORS['secondary'] if i == 0 else COLORS['light']
            rect = Rectangle((x, y-0.35), 1.4, 0.35, facecolor=color, 
                           edgecolor=COLORS['border'], linewidth=1.5)
            ax.add_patch(rect)
            ax.text(x + 0.7, y - 0.175, cell, ha='center', va='center', 
                   fontsize=9, fontweight='bold' if i == 0 else 'normal',
                   color=COLORS['text'])
    
    # INNER JOIN result
    inner_results = [
        ['Name', 'Dept_ID', 'Dept_Name'],
        ['Alice', '10', 'Sales'],
        ['Bob', '20', 'Engineering']
    ]
    
    result_y = 3.5
    ax.text(2, result_y + 1.8, 'INNER JOIN Result', fontsize=11, fontweight='bold',
           color=COLORS['primary'])
    ax.text(2, result_y + 1.4, 'SELECT e.Name, e.Dept_ID, d.Dept_Name', 
           fontsize=8, family='monospace', color=COLORS['text'])
    ax.text(2, result_y + 1.1, 'FROM Employees e INNER JOIN Departments d', 
           fontsize=8, family='monospace', color=COLORS['text'])
    ax.text(2, result_y + 0.8, 'ON e.Dept_ID = d.ID', 
           fontsize=8, family='monospace', color=COLORS['text'])
    
    for i, row in enumerate(inner_results):
        y = result_y - i * 0.4
        for j, cell in enumerate(row):
            x = 0.5 + j * 1.5
            color = COLORS['highlight'] if i == 0 else COLORS['light']
            rect = Rectangle((x, y-0.35), 1.4, 0.35, facecolor=color, 
                           edgecolor=COLORS['border'], linewidth=1.5)
            ax.add_patch(rect)
            ax.text(x + 0.7, y - 0.175, cell, ha='center', va='center', 
                   fontsize=9, fontweight='bold' if i == 0 else 'normal',
                   color=COLORS['text'])
    
    # LEFT JOIN result
    left_results = [
        ['Name', 'Dept_ID', 'Dept_Name'],
        ['Alice', '10', 'Sales'],
        ['Bob', '20', 'Engineering'],
        ['Charlie', 'NULL', 'NULL'],
        ['Diana', '30', 'NULL']
    ]
    
    ax.text(8, result_y + 1.8, 'LEFT JOIN Result', fontsize=11, fontweight='bold',
           color=COLORS['primary'])
    ax.text(8, result_y + 1.4, 'SELECT e.Name, e.Dept_ID, d.Dept_Name', 
           fontsize=8, family='monospace', color=COLORS['text'])
    ax.text(8, result_y + 1.1, 'FROM Employees e LEFT JOIN Departments d', 
           fontsize=8, family='monospace', color=COLORS['text'])
    ax.text(8, result_y + 0.8, 'ON e.Dept_ID = d.ID', 
           fontsize=8, family='monospace', color=COLORS['text'])
    
    for i, row in enumerate(left_results):
        y = result_y - i * 0.4
        for j, cell in enumerate(row):
            x = 6.5 + j * 1.5
            color = COLORS['accent'] if i == 0 else COLORS['light']
            rect = Rectangle((x, y-0.35), 1.4, 0.35, facecolor=color, 
                           edgecolor=COLORS['border'], linewidth=1.5)
            ax.add_patch(rect)
            
            # Highlight NULLs in orange-ish green
            text_color = COLORS['text']
            if cell == 'NULL' and i > 0:
                rect.set_facecolor('#FFE082')  # Light amber for NULL visibility
                text_color = '#E65100'  # Darker orange for NULL text
            
            ax.text(x + 0.7, y - 0.175, cell, ha='center', va='center', 
                   fontsize=9, fontweight='bold' if i == 0 else 'normal',
                   color=text_color)
    
    # Add notes
    note_text = "Note: LEFT JOIN includes all rows from Employees (left table),\neven if there's no match in Departments. Unmatched rows show NULL."
    ax.text(7, 0.3, note_text, fontsize=9, ha='center', style='italic',
           color=COLORS['text'],
           bbox=dict(boxstyle='round,pad=0.8', facecolor=COLORS['light'], 
                    edgecolor=COLORS['border'], alpha=0.8))
    
    plt.savefig('/home/claude/join_results_example_green.png', dpi=300, bbox_inches='tight',
                facecolor=COLORS['background'])
    plt.close()

def create_join_algorithms_comparison():
    """Create comparison of different join algorithms with green theme"""
    set_green_style()
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))
    fig.suptitle('JOIN Algorithm Performance Comparison', fontsize=16, fontweight='bold',
                color=COLORS['primary'])
    
    # Algorithm complexity comparison
    algorithms = ['Nested Loop', 'Hash Join', 'Merge Join']
    small_data = [10, 5, 7]
    large_data = [95, 20, 25]
    sorted_data = [80, 18, 8]
    
    x = np.arange(len(algorithms))
    width = 0.25
    
    bars1 = ax1.bar(x - width, small_data, width, label='Small Tables (<1K rows)',
                   color=COLORS['highlight'], edgecolor=COLORS['border'], linewidth=1.5)
    bars2 = ax1.bar(x, large_data, width, label='Large Tables (>100K rows)',
                   color=COLORS['accent'], edgecolor=COLORS['border'], linewidth=1.5)
    bars3 = ax1.bar(x + width, sorted_data, width, label='Pre-sorted Data',
                   color=COLORS['secondary'], edgecolor=COLORS['border'], linewidth=1.5)
    
    ax1.set_xlabel('Join Algorithm', fontweight='bold', color=COLORS['text'])
    ax1.set_ylabel('Relative Time (arbitrary units)', fontweight='bold', color=COLORS['text'])
    ax1.set_title('Execution Time by Data Characteristics', fontweight='bold', color=COLORS['primary'])
    ax1.set_xticks(x)
    ax1.set_xticklabels(algorithms)
    ax1.legend(facecolor=COLORS['light'], edgecolor=COLORS['border'])
    ax1.grid(axis='y', alpha=0.3, color=COLORS['border'])
    ax1.set_facecolor(COLORS['white'])
    
    # Add value labels on bars
    for bars in [bars1, bars2, bars3]:
        for bar in bars:
            height = bar.get_height()
            ax1.text(bar.get_x() + bar.get_width()/2., height,
                    f'{int(height)}', ha='center', va='bottom', fontsize=8,
                    color=COLORS['text'])
    
    # Algorithm characteristics
    ax2.axis('off')
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 10)
    
    characteristics = [
        ('Nested Loop Join', [
            '• Simple implementation',
            '• O(n × m) complexity',
            '• Good for small tables',
            '• Works with any join condition',
            '• No memory overhead',
            '• Can use indexes effectively'
        ], COLORS['highlight']),
        ('Hash Join', [
            '• O(n + m) average case',
            '• Builds hash table in memory',
            '• Excellent for equality joins',
            '• Memory intensive',
            '• Fast for large datasets',
            '• Requires sufficient RAM'
        ], COLORS['accent']),
        ('Merge Join', [
            '• O(n + m) if data sorted',
            '• Requires sorted inputs',
            '• Memory efficient',
            '• Good for pre-sorted data',
            '• Stream-based processing',
            '• Optimal for range joins'
        ], COLORS['secondary'])
    ]
    
    y_start = 9
    for algo_name, points, color in characteristics:
        # Title box
        rect = FancyBboxPatch((0.5, y_start - 0.5), 9, 0.6, 
                             boxstyle="round,pad=0.1", 
                             facecolor=color, edgecolor=COLORS['border'], 
                             linewidth=2, alpha=0.8)
        ax2.add_patch(rect)
        ax2.text(5, y_start - 0.2, algo_name, fontsize=11, fontweight='bold',
                ha='center', va='center', color=COLORS['white'])
        
        # Characteristics
        for i, point in enumerate(points):
            ax2.text(1, y_start - 1.0 - i*0.35, point, fontsize=8, va='top',
                    color=COLORS['text'])
        
        y_start -= 3.3
    
    plt.tight_layout()
    plt.savefig('/home/claude/join_algorithms_comparison_green.png', dpi=300, 
                bbox_inches='tight', facecolor=COLORS['background'])
    plt.close()

def create_groupby_visualization():
    """Create GROUP BY process visualization with green theme"""
    set_green_style()
    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 8))
    fig.suptitle('GROUP BY Process Visualization', fontsize=16, fontweight='bold',
                color=COLORS['primary'])
    
    # Before GROUP BY
    ax1.set_title('Before GROUP BY', fontsize=12, fontweight='bold', color=COLORS['primary'])
    ax1.set_xlim(0, 6)
    ax1.set_ylim(0, 10)
    ax1.axis('off')
    
    sales_data = [
        ['Product', 'Region', 'Amount'],
        ['Laptop', 'East', '1000'],
        ['Phone', 'West', '500'],
        ['Laptop', 'West', '1200'],
        ['Tablet', 'East', '800'],
        ['Phone', 'East', '450'],
        ['Laptop', 'East', '1100'],
        ['Tablet', 'West', '750']
    ]
    
    table_y = 8
    for i, row in enumerate(sales_data):
        y = table_y - i * 0.5
        for j, cell in enumerate(row):
            x = 0.5 + j * 1.8
            color = COLORS['accent'] if i == 0 else COLORS['light']
            rect = Rectangle((x, y-0.4), 1.7, 0.4, facecolor=color, 
                           edgecolor=COLORS['border'], linewidth=1.5)
            ax1.add_patch(rect)
            ax1.text(x + 0.85, y - 0.2, cell, ha='center', va='center', 
                    fontsize=9, fontweight='bold' if i == 0 else 'normal',
                    color=COLORS['text'])
    
    # SQL Query
    query = "SELECT Product,\n  COUNT(*) as Sales_Count,\n  SUM(Amount) as Total\nFROM Sales\nGROUP BY Product"
    ax1.text(3, 2, query, fontsize=9, family='monospace', ha='center',
            bbox=dict(boxstyle='round,pad=0.8', facecolor=COLORS['light'], 
                     edgecolor=COLORS['border'], linewidth=2, alpha=0.9),
            color=COLORS['text'])
    
    # After GROUP BY
    ax2.set_title('After GROUP BY', fontsize=12, fontweight='bold', color=COLORS['primary'])
    ax2.set_xlim(0, 8)
    ax2.set_ylim(0, 10)
    ax2.axis('off')
    
    grouped_data = [
        ['Product', 'Sales_Count', 'Total'],
        ['Laptop', '3', '3300'],
        ['Phone', '2', '950'],
        ['Tablet', '2', '1550']
    ]
    
    result_y = 7
    for i, row in enumerate(grouped_data):
        y = result_y - i * 0.6
        for j, cell in enumerate(row):
            x = 1 + j * 2
            color = COLORS['highlight'] if i == 0 else COLORS['light']
            rect = Rectangle((x, y-0.5), 1.9, 0.5, facecolor=color, 
                           edgecolor=COLORS['border'], linewidth=2)
            ax2.add_patch(rect)
            ax2.text(x + 0.95, y - 0.25, cell, ha='center', va='center', 
                    fontsize=10, fontweight='bold' if i == 0 else 'normal',
                    color=COLORS['text'])
    
    # Add grouping visualization
    ax2.text(4, 4.5, 'Grouping Process:', fontsize=10, fontweight='bold', 
            ha='center', color=COLORS['primary'])
    
    groups = [
        ('Laptop group (3 rows)', '→ COUNT: 3, SUM: 3300'),
        ('Phone group (2 rows)', '→ COUNT: 2, SUM: 950'),
        ('Tablet group (2 rows)', '→ COUNT: 2, SUM: 1550')
    ]
    
    y_pos = 4
    colors_cycle = [COLORS['accent'], COLORS['secondary'], COLORS['highlight']]
    for i, (group, result) in enumerate(groups):
        # Group box
        rect = FancyBboxPatch((1, y_pos - 0.4 - i*0.7), 2.5, 0.5,
                             boxstyle="round,pad=0.05",
                             facecolor=colors_cycle[i], 
                             edgecolor=COLORS['border'], 
                             linewidth=1.5, alpha=0.6)
        ax2.add_patch(rect)
        ax2.text(2.25, y_pos - 0.15 - i*0.7, group, ha='center', va='center',
                fontsize=8, fontweight='bold', color=COLORS['white'])
        
        # Arrow
        arrow = FancyArrowPatch((3.6, y_pos - 0.15 - i*0.7), 
                               (4.5, y_pos - 0.15 - i*0.7),
                               arrowstyle='->', mutation_scale=20, 
                               linewidth=2, color=COLORS['border'])
        ax2.add_patch(arrow)
        
        # Result
        ax2.text(6.5, y_pos - 0.15 - i*0.7, result, ha='center', va='center',
                fontsize=8, color=COLORS['text'],
                bbox=dict(boxstyle='round,pad=0.3', facecolor=COLORS['light'],
                         edgecolor=COLORS['border'], alpha=0.8))
    
    # Note
    note = "GROUP BY collects rows with same Product value\nand applies aggregate functions to each group"
    ax2.text(4, 0.5, note, fontsize=9, ha='center', style='italic',
            color=COLORS['text'],
            bbox=dict(boxstyle='round,pad=0.6', facecolor=COLORS['light'],
                     edgecolor=COLORS['border'], alpha=0.8))
    
    plt.tight_layout()
    plt.savefig('/home/claude/groupby_visualization_green.png', dpi=300, 
                bbox_inches='tight', facecolor=COLORS['background'])
    plt.close()

def create_count_comparison():
    """Create COUNT(*) vs COUNT(column) comparison with green theme"""
    set_green_style()
    
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 10)
    ax.axis('off')
    
    # Title
    ax.text(6, 9.5, 'COUNT(*) vs COUNT(column) Comparison', fontsize=16, 
           fontweight='bold', ha='center', color=COLORS['primary'])
    
    # Sample table
    sample_data = [
        ['ID', 'Name', 'Email', 'Phone'],
        ['1', 'Alice', 'alice@ex.com', '555-0001'],
        ['2', 'Bob', 'bob@ex.com', 'NULL'],
        ['3', 'Charlie', 'NULL', '555-0003'],
        ['4', 'Diana', 'diana@ex.com', 'NULL'],
        ['5', 'Eve', 'eve@ex.com', '555-0005']
    ]
    
    table_y = 7.5
    ax.text(3, table_y + 0.8, 'Sample Users Table', fontsize=11, 
           fontweight='bold', color=COLORS['primary'])
    
    for i, row in enumerate(sample_data):
        y = table_y - i * 0.45
        for j, cell in enumerate(row):
            x = 0.5 + j * 1.5
            color = COLORS['accent'] if i == 0 else COLORS['light']
            rect = Rectangle((x, y-0.4), 1.4, 0.4, facecolor=color, 
                           edgecolor=COLORS['border'], linewidth=1.5)
            ax.add_patch(rect)
            
            # Highlight NULLs
            text_color = COLORS['text']
            if cell == 'NULL':
                rect.set_facecolor('#FFE082')
                text_color = '#E65100'
            
            ax.text(x + 0.7, y - 0.2, cell, ha='center', va='center', 
                   fontsize=9, fontweight='bold' if i == 0 else 'normal',
                   color=text_color)
    
    # COUNT examples
    examples_y = 4.5
    
    examples = [
        ("COUNT(*)", "5", "Counts all rows, including NULLs", COLORS['highlight']),
        ("COUNT(Email)", "4", "Counts non-NULL Email values only", COLORS['accent']),
        ("COUNT(Phone)", "3", "Counts non-NULL Phone values only", COLORS['secondary']),
        ("COUNT(DISTINCT Email)", "4", "Counts unique non-NULL Emails", COLORS['primary'])
    ]
    
    for i, (query, result, description, color) in enumerate(examples):
        y = examples_y - i * 0.9
        
        # Query box
        query_rect = FancyBboxPatch((0.5, y - 0.25), 3, 0.5,
                                   boxstyle="round,pad=0.1",
                                   facecolor=color, 
                                   edgecolor=COLORS['border'],
                                   linewidth=2, alpha=0.7)
        ax.add_patch(query_rect)
        ax.text(2, y, query, ha='center', va='center', fontsize=10,
               fontweight='bold', family='monospace', color=COLORS['white'])
        
        # Arrow
        arrow = FancyArrowPatch((3.6, y), (4.3, y),
                               arrowstyle='->', mutation_scale=25,
                               linewidth=2.5, color=COLORS['border'])
        ax.add_patch(arrow)
        
        # Result box
        result_circle = Circle((5, y), 0.35, facecolor=COLORS['highlight'],
                              edgecolor=COLORS['border'], linewidth=2)
        ax.add_patch(result_circle)
        ax.text(5, y, result, ha='center', va='center', fontsize=14,
               fontweight='bold', color=COLORS['white'])
        
        # Description
        ax.text(6, y, description, ha='left', va='center', fontsize=9,
               color=COLORS['text'])
    
    # Key differences box
    key_box_y = 0.8
    diff_text = [
        "Key Differences:",
        "• COUNT(*) counts rows (never returns NULL)",
        "• COUNT(column) counts non-NULL values in that column",
        "• COUNT(DISTINCT column) counts unique non-NULL values",
        "• COUNT(1) is equivalent to COUNT(*) - counts all rows"
    ]
    
    rect = FancyBboxPatch((0.5, key_box_y - 1.3), 11, 1.5,
                         boxstyle="round,pad=0.15",
                         facecolor=COLORS['light'], 
                         edgecolor=COLORS['border'],
                         linewidth=2, alpha=0.9)
    ax.add_patch(rect)
    
    for i, line in enumerate(diff_text):
        weight = 'bold' if i == 0 else 'normal'
        ax.text(1, key_box_y - 0.3 - i*0.25, line, ha='left', va='top',
               fontsize=9, fontweight=weight, color=COLORS['text'])
    
    plt.savefig('/home/claude/count_comparison_green.png', dpi=300, 
                bbox_inches='tight', facecolor=COLORS['background'])
    plt.close()

def create_null_aggregation_behavior():
    """Create diagram showing NULL behavior in aggregations with green theme"""
    set_green_style()
    
    fig, ax = plt.subplots(figsize=(14, 10))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 12)
    ax.axis('off')
    
    # Title
    ax.text(7, 11.5, 'NULL Behavior in Aggregate Functions', fontsize=16, 
           fontweight='bold', ha='center', color=COLORS['primary'])
    
    # Sample data table
    data = [
        ['Employee', 'Department', 'Salary', 'Bonus'],
        ['Alice', 'Sales', '50000', '5000'],
        ['Bob', 'Sales', 'NULL', '3000'],
        ['Charlie', 'IT', '60000', 'NULL'],
        ['Diana', 'IT', '55000', '4000'],
        ['Eve', 'Sales', '52000', 'NULL']
    ]
    
    table_y = 10
    ax.text(3.5, table_y + 0.6, 'Employee Data', fontsize=11, 
           fontweight='bold', color=COLORS['primary'])
    
    for i, row in enumerate(data):
        y = table_y - i * 0.45
        for j, cell in enumerate(row):
            x = 0.3 + j * 1.7
            color = COLORS['accent'] if i == 0 else COLORS['light']
            rect = Rectangle((x, y-0.4), 1.6, 0.4, facecolor=color, 
                           edgecolor=COLORS['border'], linewidth=1.5)
            ax.add_patch(rect)
            
            text_color = COLORS['text']
            if cell == 'NULL':
                rect.set_facecolor('#FFE082')
                text_color = '#E65100'
            
            ax.text(x + 0.8, y - 0.2, cell, ha='center', va='center', 
                   fontsize=9, fontweight='bold' if i == 0 else 'normal',
                   color=text_color)
    
    # Aggregate function results
    results_y = 6.5
    
    aggregates = [
        ('COUNT(*)', '5', 'Counts all rows'),
        ('COUNT(Salary)', '4', 'Ignores NULL (Bob has no salary)'),
        ('COUNT(Bonus)', '3', 'Ignores NULLs (Charlie & Eve)'),
        ('AVG(Salary)', '54,250', 'Average of non-NULL: (50k+60k+55k+52k)/4'),
        ('SUM(Salary)', '217,000', 'Sum of non-NULL values only'),
        ('SUM(Bonus)', '12,000', 'Sum: 5000+3000+4000 (ignores NULLs)'),
        ('MAX(Salary)', '60,000', 'Maximum non-NULL value'),
        ('MIN(Bonus)', '3,000', 'Minimum non-NULL value')
    ]
    
    ax.text(7, results_y + 0.8, 'Aggregate Function Results', fontsize=12, 
           fontweight='bold', ha='center', color=COLORS['primary'])
    
    for i, (func, result, explanation) in enumerate(aggregates):
        y = results_y - i * 0.55
        
        # Function box
        func_rect = FancyBboxPatch((0.3, y - 0.22), 2.5, 0.44,
                                  boxstyle="round,pad=0.08",
                                  facecolor=COLORS['accent'], 
                                  edgecolor=COLORS['border'],
                                  linewidth=1.5, alpha=0.7)
        ax.add_patch(func_rect)
        ax.text(1.55, y, func, ha='center', va='center', fontsize=9,
               fontweight='bold', family='monospace', color=COLORS['white'])
        
        # Result box
        result_rect = FancyBboxPatch((3, y - 0.22), 1.8, 0.44,
                                    boxstyle="round,pad=0.08",
                                    facecolor=COLORS['highlight'], 
                                    edgecolor=COLORS['border'],
                                    linewidth=1.5)
        ax.add_patch(result_rect)
        ax.text(3.9, y, result, ha='center', va='center', fontsize=9,
               fontweight='bold', color=COLORS['white'])
        
        # Explanation
        ax.text(5.2, y, explanation, ha='left', va='center', fontsize=8,
               color=COLORS['text'])
    
    # Important notes section
    notes_y = 1.8
    notes_title = "Important NULL Behavior Rules:"
    notes = [
        "1. Most aggregate functions (SUM, AVG, MIN, MAX) ignore NULL values",
        "2. COUNT(column) counts only non-NULL values in that column",
        "3. COUNT(*) counts all rows, including those with NULLs",
        "4. If ALL values are NULL, most aggregates return NULL (not 0)",
        "5. AVG ignores NULLs: AVG(10, NULL, 20) = 15, not 10",
        "6. GROUP BY treats NULL as a distinct group value"
    ]
    
    notes_rect = FancyBboxPatch((0.3, notes_y - 1.6), 13.4, 1.8,
                               boxstyle="round,pad=0.15",
                               facecolor=COLORS['light'], 
                               edgecolor=COLORS['border'],
                               linewidth=2, alpha=0.9)
    ax.add_patch(notes_rect)
    
    ax.text(7, notes_y, notes_title, ha='center', va='top',
           fontsize=10, fontweight='bold', color=COLORS['primary'])
    
    for i, note in enumerate(notes):
        ax.text(0.8, notes_y - 0.35 - i*0.22, note, ha='left', va='top',
               fontsize=8, color=COLORS['text'])
    
    plt.savefig('/home/claude/null_aggregation_behavior_green.png', dpi=300, 
                bbox_inches='tight', facecolor=COLORS['background'])
    plt.close()

def main():
    """Generate all SQL diagrams with green theme"""
    print("Generating green-themed SQL diagrams...")
    print("=" * 60)
    
    diagrams = [
        ("JOIN Venn Diagrams", create_join_venn_diagrams),
        ("JOIN Results Example", create_join_results_example),
        ("JOIN Algorithms Comparison", create_join_algorithms_comparison),
        ("GROUP BY Visualization", create_groupby_visualization),
        ("COUNT Comparison", create_count_comparison),
        ("NULL Aggregation Behavior", create_null_aggregation_behavior)
    ]
    
    for name, func in diagrams:
        try:
            print(f"Creating {name}...")
            func()
            print(f"✓ {name} created successfully")
        except Exception as e:
            print(f"✗ Error creating {name}: {str(e)}")
    
    print("=" * 60)
    print("All green-themed diagrams generated successfully!")
    print("\nGenerated files:")
    print("  - join_venn_diagrams_green.png")
    print("  - join_results_example_green.png")
    print("  - join_algorithms_comparison_green.png")
    print("  - groupby_visualization_green.png")
    print("  - count_comparison_green.png")
    print("  - null_aggregation_behavior_green.png")

if __name__ == "__main__":
    main()

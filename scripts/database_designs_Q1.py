import matplotlib.pyplot as plt

def generate_q1_diagram():
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.axis('off')

    # Sample data for table
    col_labels = ['ID (Integer domain: 1-999)', 'Name (String domain: A-Z)', 'Age (Integer domain: 0-150)']
    row_labels = ['Tuple 1', 'Tuple 2']
    cell_text = [['1', 'Aobakwe', '21'], ['2', 'Celimpilo', '24']]

    # Create table
    table = ax.table(cellText=cell_text, rowLabels=row_labels, colLabels=col_labels, cellLoc='center', loc='center', bbox=[0.1, 0.3, 0.8, 0.4], cellColours=[['#f0FFF0']*3]*2)

    # Header row
    for i in range(len(col_labels)):
        table[(0, i)].set_facecolor('#c8e6c9')

    # Add labels
    ax.text(0.5, 0.85, 'Relation (Table): Employee', fontsize=14, ha='center', color='#2e7d32')
    ax.text(0.05, 0.5, 'Tuples (Rows)', fontsize=12, va='center', rotation=90, color='#388e3c')
    ax.text(0.5, 0.75, 'Attributes (Columns)', fontsize=12, ha='center', color='#388e3c')
    ax.text(0.5, 0.2, 'Domains: Defined peermissable values for each attribute', fontsize=12, ha='center', color='#4caf50')

    # Logical independence box
    ax.text(0.5, 0.1, 'Logical Independence: Schema changes wihtout affecting physical storage or apps', fontsize=10, ha='center', color='#1b5e20', bbox=dict(facecolor='#e8f5e9', boxstyle='round, pad=0.5'))

    plt.savefig('q1_relational_model_diagram.png', dpi=150, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    generate_q1_diagram()
    print("Q1 diagram generated: q1_relational_model_diagram.png")
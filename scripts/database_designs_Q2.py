import matplotlib.pyplot as plt
from matplotlib.patches import FancyArrowPatch

def generate_q2_diagram():
    fig, ax = plt.subplots(figsize=(10, 7))
    ax.axis('off')

    # Employee Table
    ax.text(0.2, 0.8, 'Employee Table', fontsize=12, ha='center', color='#2e7d32')
    emp_cols = ['EmpID (Primary Key, Surrogate: Auto-gen int)', 'Name (NOT NULL, UNIQUE)', 'DeptID (Foreign Key)']
    emp_data = [['1', 'Aobakwe', 'D1'], ['2', 'Celimpilo', 'D2']]
    emp_table = ax.table(cellText=emp_data, colLabels=emp_cols, loc='upper left', bbox=[0.05, 0.5, 0.4, 0.25], cellColours=[['#f0fff0']*3]*2)

    # Header for Employee table
    for i in range(len(emp_cols)):
        emp_table[(0, i)].set_facecolor('#c8e6c9')

    # Department table
    ax.text(0.8, 0.8, 'Department Table', fontsize=12, ha='center', color='#2e7d32')
    dept_cols = ['DeptID (Primary Key, Candidate Key)', 'DeptName (CHECK: Length > 3)']
    dept_data = [['D1', 'HR'], ['D2', 'IT']]
    dept_table = ax.table(cellText=dept_data, colLabels=dept_cols, loc='upper right', bbox=[0.55, 0.5, 0.4, 0.25], cellColours=[['#f0fff0']*2]*2)

    # Header for Department table
    for i in range(len(dept_cols)):
        dept_table[(0, i)].set_facecolor('#c8ec69')

    # Arrow
    arrow = FancyArrowPatch((0.45, 0.6), (0.55, 0.6), arrowstyle='->', mutation_scale=20, linewidth=1.5, color='#2e7d32')
    ax.add_patch(arrow)
    ax.text(0.5, 0.65, 'Referential Constraint (Foreign Key)', fontsize=10, ha='center', color='#1b5e20')

    # Notes on keys and constraints
    ax.text(0.5, 0.3, 'Candidate Key: Minimal unique identifier', fontsize=10, ha='center', color='#388e3c')
    ax.text(0.5, 0.25, 'Surrogate Key: System-generated', fontsize=10, ha='center', color='#388e3c')
    ax.text(0.5, 0.2, 'Constraints Prevent Anomalies: UNIQUE avoids duplicates, NOT NULL avoids missing data,', fontsize=10, ha='center', color='#4caf50')
    ax.text(0.5, 0.15, 'CHECK vailidates rules, Referential avoids invalid references/orphans.', fontsize=10, ha='center', color='#4caf50')

    plt.savefig('q2_keys_constraints_diagram.png', dpi=150, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    generate_q2_diagram()
    print("Q2 diagram generated: q2_keys_constraints_diagram.png") 
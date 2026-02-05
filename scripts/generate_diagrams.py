"""
Generate Professional Diagram PNGs
Creates B-Tree and Transaction Flow diagrams as PNG images
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_btree_diagram():
    """Create B-Tree Index Structure diagram"""
    width, height = 1200, 900
    img = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(img)
    try:
        title_font = ImageFont.truetype("arial.ttf", 36)
        header_font = ImageFont.truetype("arial.ttf", 24)
        text_font = ImageFont.truetype("arial.ttf", 20)
        small_font = ImageFont.truetype("arial.ttf", 16)
    except:
        title_font = ImageFont.load_default()
        header_font = ImageFont.load_default()
        text_font = ImageFont.load_default()
        small_font = ImageFont.load_default()
    root_color = '#3498db'
    branch_color = '#9b59b6'
    leaf_color = '#1abc9c'
    title = "B-Tree Index Structure"
    title_bbox = draw.textbbox((0, 0), title, font=title_font)
    title_width = title_bbox[2] - title_bbox[0]
    draw.text((width//2 - title_width//2, 40), title, fill='black', font=title_font)
    root_x, root_y = width//2 - 100, 120
    root_w, root_h = 200, 80
    draw.rectangle([root_x, root_y, root_x + root_w, root_y + root_h], fill=root_color, outline='black', width=3)
    draw.text((root_x + 50, root_y + 15), "Root Node", fill='white', font=header_font)
    draw.text((root_x + 85, root_y + 50), "[50]", fill='white', font=text_font)
    draw.line([root_x + 50, root_y + root_h, 300, 280], fill='black', width=3)
    draw.polygon([(300, 280), (295, 270), (305, 270)], fill='black')
    draw.line([root_x + 150, root_y + root_h, 700, 280], fill='black', width=3)
    draw.polygon([(700, 280), (695, 270), (705, 270)], fill='black')
    branch1_x, branch1_y = 200, 280
    branch_w, branch_h = 200, 80
    draw.rectangle([branch1_x, branch1_y, branch1_x + branch_w, branch1_y + branch_h], fill=branch_color, outline='black', width=3)
    draw.text((branch1_x + 70, branch1_y + 15), "Branch", fill='white', font=header_font)
    draw.text((branch1_x + 85, branch1_y + 50), "[25]", fill='white', font=text_font)
    branch2_x, branch2_y = 600, 280
    draw.rectangle([branch2_x, branch2_y, branch2_x + branch_w, branch2_y + branch_h], fill=branch_color, outline='black', width=3)
    draw.text((branch2_x + 70, branch2_y + 15), "Branch", fill='white', font=header_font)
    draw.text((branch2_x + 85, branch2_y + 50), "[75]", fill='white', font=text_font)
    draw.line([branch1_x + 50, branch1_y + branch_h, 150, 480], fill='black', width=2)
    draw.polygon([(150, 480), (147, 473), (153, 473)], fill='black')
    draw.line([branch1_x + 150, branch1_y + branch_h, 350, 480], fill='black', width=2)
    draw.polygon([(350, 480), (347, 473), (353, 473)], fill='black')
    draw.line([branch2_x + 50, branch2_y + branch_h, 550, 480], fill='black', width=2)
    draw.polygon([(550, 480), (547, 473), (553, 473)], fill='black')
    draw.line([branch2_x + 150, branch2_y + branch_h, 750, 480], fill='black', width=2)
    draw.polygon([(750, 480), (747, 473), (753, 473)], fill='black')
    leaf_w, leaf_h = 180, 80
    leaf_y = 480
    leaves = [
        (60, "Leaf", "10, 20"),
        (260, "Leaf", "30, 40"),
        (460, "Leaf", "60, 70"),
        (660, "Leaf", "80, 90")
    ]
    for leaf_x, leaf_label, leaf_value in leaves:
        draw.rectangle([leaf_x, leaf_y, leaf_x + leaf_w, leaf_y + leaf_h], fill=leaf_color, outline='black', width=2)
        draw.text((leaf_x + 65, leaf_y + 15), leaf_label, fill='black', font=text_font)
        draw.text((leaf_x + 50, leaf_y + 50), leaf_value, fill='black', font=text_font)
    legend_y = 620
    legend_size = 30
    draw.rectangle([100, legend_y, 100 + legend_size, legend_y + legend_size], fill=root_color, outline='black', width=2)
    draw.text((140, legend_y + 5), "Root Node", fill='black', font=small_font)
    draw.rectangle([300, legend_y, 300 + legend_size, legend_y + legend_size], fill=branch_color, outline='black', width=2)
    draw.text((340, legend_y + 5), "Branch Nodes", fill='black', font=small_font)
    draw.rectangle([540, legend_y, 540 + legend_size, legend_y + legend_size], fill=leaf_color, outline='black', width=2)
    draw.text((580, legend_y + 5), "Leaf Nodes (Data)", fill='black', font=small_font)
    return img

def create_transaction_flow_diagram():
    """Create Transaction Flow with Constraint Checking diagram"""
    width, height = 1200, 1100
    img = Image.new('RGB', (width, height), color='white')
    draw = ImageDraw.Draw(img)
    try:
        title_font = ImageFont.truetype("arial.ttf", 36)
        header_font = ImageFont.truetype("arial.ttf", 22)
        text_font = ImageFont.truetype("arial.ttf", 18)
        small_font = ImageFont.truetype("arial.ttf", 16)
    except:
        title_font = ImageFont.load_default()
        header_font = ImageFont.load_default()
        text_font = ImageFont.load_default()
        small_font = ImageFont.load_default()
    start_color = '#3498db'
    error_color = '#e74c3c'
    success_color = '#95e1d3'
    commit_color = '#2ecc71'
    final_color = '#f39c12'
    title = "Transaction Flow with Constraint Checking"
    title_bbox = draw.textbbox((0, 0), title, font=title_font)
    title_width = title_bbox[2] - title_bbox[0]
    draw.text((width//2 - title_width//2, 40), title, fill='black', font=title_font)
    start_x, start_y = width//2 - 125, 120
    start_w, start_h = 250, 60
    draw.rectangle([start_x, start_y, start_x + start_w, start_y + start_h], fill=start_color, outline='black', width=3)
    draw.text((start_x + 40, start_y + 20), "Start Transaction", fill='white', font=header_font)
    arrow_y1 = start_y + start_h
    arrow_y2 = 250
    draw.line([width//2, arrow_y1, width//2, arrow_y2], fill='black', width=3)
    draw.polygon([(width//2, arrow_y2), (width//2 - 8, arrow_y2 - 10), (width//2 + 8, arrow_y2 - 10)], fill='black')
    diamond_center_x = width//2
    diamond_center_y = 320
    diamond_size = 100
    diamond_points = [
        (diamond_center_x, diamond_center_y - diamond_size),
        (diamond_center_x + diamond_size, diamond_center_y),
        (diamond_center_x, diamond_center_y + diamond_size),
        (diamond_center_x - diamond_size, diamond_center_y)
    ]
    draw.polygon(diamond_points, fill='white', outline='black')
    draw.line(diamond_points + [diamond_points[0]], fill='black', width=3)
    draw.text((diamond_center_x - 45, diamond_center_y - 20), "Check", fill='black', font=header_font)
    draw.text((diamond_center_x - 65, diamond_center_y + 5), "Constraints", fill='black', font=header_font)
    draw.line([diamond_center_x - diamond_size, diamond_center_y, 250, diamond_center_y], fill='black', width=3)
    draw.polygon([(250, diamond_center_y), (258, diamond_center_y - 8), (258, diamond_center_y + 8)], fill='black')
    draw.text((270, diamond_center_y - 40), "Violation", fill='#e74c3c', font=small_font)
    draw.line([250, diamond_center_y, 250, 480], fill='black', width=3)
    draw.polygon([(250, 480), (242, 472), (258, 472)], fill='black')
    rollback_x, rollback_y = 125, 480
    box_w, box_h = 250, 60
    draw.rectangle([rollback_x, rollback_y, rollback_x + box_w, rollback_y + box_h], fill=error_color, outline='black', width=3)
    draw.text((rollback_x + 50, rollback_y + 20), "Rollback / Error", fill='white', font=header_font)
    draw.line([diamond_center_x + diamond_size, diamond_center_y, 750, diamond_center_y], fill='black', width=3)
    draw.polygon([(750, diamond_center_y), (742, diamond_center_y - 8), (742, diamond_center_y + 8)], fill='black')
    draw.text((820, diamond_center_y - 40), "Success", fill='#2ecc71', font=small_font)
    draw.line([750, diamond_center_y, 750, 480], fill='black', width=3)
    draw.polygon([(750, 480), (742, 472), (758, 472)], fill='black')
    execute_x, execute_y = 625, 480
    draw.rectangle([execute_x, execute_y, execute_x + box_w, execute_y + box_h], fill=success_color, outline='black', width=3)
    draw.text((execute_x + 60, execute_y + 20), "Execute Logic", fill='black', font=header_font)
    draw.line([750, execute_y + box_h, 750, 620], fill='black', width=3)
    draw.polygon([(750, 620), (742, 612), (758, 612)], fill='black')
    commit_x, commit_y = 625, 620
    draw.rectangle([commit_x, commit_y, commit_x + box_w, commit_y + box_h], fill=commit_color, outline='black', width=3)
    draw.text((commit_x + 55, commit_y + 20), "Commit to Disk", fill='white', font=header_font)
    draw.line([750, commit_y + box_h, 750, 760], fill='black', width=3)
    draw.polygon([(750, 760), (742, 752), (758, 752)], fill='black')
    final_x, final_y = 625, 760
    draw.rectangle([final_x, final_y, final_x + box_w, final_y + box_h], fill=final_color, outline='black', width=3)
    draw.text((final_x + 50, final_y + 20), "Data is Durable", fill='white', font=header_font)
    return img

def main():
    print("=" * 70)
    print("Database Diagram Generator")
    print("=" * 70)
    print("\nGenerating diagrams...\n")
    os.makedirs('diagrams', exist_ok=True)
    print("1. Creating B-Tree diagram...")
    btree_img = create_btree_diagram()
    btree_path = 'diagrams/btree.png'
    btree_img.save(btree_path, 'PNG', quality=95, dpi=(300, 300))
    print(f"   ✓ Saved to: {btree_path}")
    print("2. Creating Transaction Flow diagram...")
    transaction_img = create_transaction_flow_diagram()
    transaction_path = 'diagrams/transaction_flow.png'
    transaction_img.save(transaction_path, 'PNG', quality=95, dpi=(300, 300))
    print(f"   ✓ Saved to: {transaction_path}")
    print("\n" + "=" * 70)
    print("✓ SUCCESS! Both diagrams generated successfully!")
    print("=" * 70)
    print("\nFiles created:")
    print(f"  - {btree_path}")
    print(f"  - {transaction_path}")
    print("\nYou can now use these PNG images in your documentation!")
    print("=" * 70)

if __name__ == "__main__":
    main()

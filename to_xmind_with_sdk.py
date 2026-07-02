import pandas as pd
import xmind

def excel_to_xmind(excel_path, xmind_path):
    # 1. Load the Excel file and handle empty spaces
    df = pd.read_excel(excel_path)
    df = df.ffill(axis=0)  # Fills merged cells or blanks down for hierarchy continuity

    # 2. Initialize XMind Workbook
    workbook = xmind.load(xmind_path)
    sheet = workbook.getPrimarySheet()
    
    # Define the Root/Central Topic
    root_topic = sheet.getRootTopic()
    # Assume the first row, first column text as the central topic title
    root_title = str(df.iloc[0, 0])
    root_topic.setTitle(root_title)

    # Dictionary to keep track of added nodes and prevent duplicates
    nodes_cache = {}

    # 3. Iterate through rows to build branches
    for _, row in df.iterrows():
        parent_node = root_topic
        
        # Skip the first column if it's strictly used for the Root Title
        for col_idx in range(1, len(df.columns)):
            node_text = str(row.iloc[col_idx]).strip()
            
            # Skip empty or NaN cells
            if not node_text or node_text.lower() == 'nan':
                continue
                
            # Create a unique key based on hierarchy path to prevent duplicate branches
            node_key = f"{parent_node.getID()}_{node_text}"
            
            if node_key not in nodes_cache:
                # Add subtopic to the parent
                new_node = parent_node.addSubTopic()
                new_node.setTitle(node_text)
                nodes_cache[node_key] = new_node
                parent_node = new_node
            else:
                # Node already exists, traverse down into it
                parent_node = nodes_cache[node_key]

    # 4. Save the completed XMind file
    xmind.save(workbook, path=xmind_path)
    print(f"✅ Successfully converted {excel_path} to {xmind_path}")

# Run the conversion
excel_to_xmind("to_xmind.xlsx", "output_mindmap.xmind")

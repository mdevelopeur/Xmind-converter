import pandas as pd
from xmindparser import xmind_to_dict

def flatten_xmind(node, current_path=None, rows=None):
    """Recursively walks through XMind nodes to flatten into a tabular format."""
    if current_path is None:
        current_path = []
    if rows is None:
        rows = []
        
    # Extract the text title of the current node
    title = node.get('title', '')
    new_path = current_path + [title]
    
    # Check if this node has subtopics
    children = node.get('topics', [])
    
    if not children:
        # If it's a leaf node, save the accumulated path as a complete row
        rows.append(new_path)
    else:
        # If it has subtopics, keep diving deeper
        for child in children:
            flatten_xmind(child, new_path, rows)
            
    return rows

def convert_xmind_to_xlsx(xmind_file_path, output_xlsx_path):
    # 1. Parse XMind file into a Python dictionary
    xmind_data = xmind_to_dict(xmind_file_path)
    
    # 2. Extract the main sheet and root topic
    # An XMind file can have multiple sheets; we target the first one here
    main_sheet = xmind_data[0]
    root_topic = main_sheet['topic']
    
    # 3. Flatten the hierarchical tree structure
    all_rows = flatten_xmind(root_topic)
    
    # 4. Determine dynamically how many levels deep the tree goes
    max_columns = max(len(row) for row in all_rows)
    column_headers = [f"Level {i+1}" for i in range(max_columns)]
    # Set the first header explicitly as the root map name
    column_headers[0] = "Root Topic" 
    
    # 5. Convert to Pandas DataFrame and export to Excel
    df = pd.DataFrame(all_rows, columns=column_headers)
    df.to_excel(output_xlsx_path, index=False)
    print(f"✅ Success! Converted '{xmind_file_path}' into '{output_xlsx_path}'")

# --- Example Usage ---
if __name__ == "__main__":
    # Substitute with your actual file names
    input_file = "file.xmind"
    output_file = "file.xlsx"
    
    convert_xmind_to_xlsx(input_file, output_file)

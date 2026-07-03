import openpyxl

def xlsx_to_markdown(file_path, sheet_name=None):
    # Load the workbook and select sheet
    wb = openpyxl.load_workbook(file_path, data_only=True)
    ws = wb[sheet_name] if sheet_name else wb.active
    
    md_lines = []

    previous_row = []
    # Iterate through each row in the worksheet
    for row_idx, row in enumerate(ws.iter_rows(values_only=False), start=1):
        row_cells = []
        
        # Process each cell individually
        
        for index, cell in enumerate(row):
            val = cell.value
            if val is None:
                cell_text = ""
            elif val == previous_row[index].value:
                cell_text = "    "
            else:
                # Convert to string and handle interior newlines for Markdown compatibility
                cell_text = str(val).replace("\n", "<br>")
                # Escape the markdown pipe character to keep table structure intact
                cell_text = cell_text.replace("|", "\\|")
            
            row_cells.append(cell_text)
            
        # Join cells with standard Markdown pipe notation
        md_row = "| " + " | ".join(row_cells) + " |"
        md_lines.append(md_row)
        
        # Automatically generate the Markdown header separator after the first row
        if row_idx == 1:
            separator = "| " + " | ".join(["---"] * len(row_cells)) + " |"
            md_lines.append(separator)
            
    return "\n".join(md_lines)

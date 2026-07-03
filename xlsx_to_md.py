import openpyxl

def xlsx_to_markdown(file_path, sheet_name=None):
    # Load the workbook and select sheet
    wb = openpyxl.load_workbook(file_path, data_only=True)
    ws = wb[sheet_name] if sheet_name else wb.active
    class Object:
        def __init__(self, value):
            self.value = value
    md_lines = []

    previous_row = [Object(False)]*100
    # Iterate through each row in the worksheet
    for row_idx, row in enumerate(ws.iter_rows(values_only=False), start=1):
        row_cells = []
        first_node = True
        # Process each cell individually
        
        for index, cell in enumerate(row):
            val = cell.value
            if val is None:
                cell_text = ""
            elif val == previous_row[index].value:
                #if first_node:
                cell_text = "    "
            elif index < len(row) - 1:
                # Convert to string and handle interior newlines for Markdown compatibility
                cell_text = str(val).replace("\n", "<br>")
                # Escape the markdown pipe character to keep table structure intact
                cell_text = cell_text.replace("|", "\\|")
                row_cells.append("- " + cell_text)
                md_row = "".join(row_cells) + ""
                md_lines.append(md_row)
                cell_text = "    "
            row_cells.append(cell_text)
            
        # Join cells with standard Markdown pipe notation
        md_row = "".join(row_cells) + ""
        md_lines.append(md_row)
        previous_row = row
        # Automatically generate the Markdown header separator after the first row
        if row_idx == 1:
            separator = "| " + " | ".join(["---"] * len(row_cells)) + " |"
            #md_lines.append(separator)
            
    return "\n".join(md_lines)

xlsx_file = "sample.xlsx"  # Change to your actual file
markdown_output = xlsx_to_markdown(xlsx_file)

# Print the result or save to a file
#print(markdown_output)

with open("output.md", "w", encoding="utf-8") as f:
    f.write(markdown_output)

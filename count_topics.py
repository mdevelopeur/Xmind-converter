import xmind

def count_topics(topic_element):
    """
    Recursively counts a topic node and all of its subtopics.
    """
    # Count the current node
    count = 1  
    
    # Get all direct subtopics of this node
    subtopics = topic_element.getSubTopics()
    
    if subtopics:
        for subtopic in subtopics:
            count += count_topics(subtopic)
            
    return count

def get_total_subjects(file_path):
    """
    Loads the XMind workbook and calculates total topics across the first sheet.
    """
    # Load the workbook
    workbook = xmind.load(file_path)
    
    # Get the primary sheet
    sheet = workbook.getPrimarySheet()
    
    # Get the central root topic
    root_topic = sheet.getRootTopic()
    
    # Calculate the total count
    total_count = count_topics(root_topic)
    return total_count

# --- Execution ---
if __name__ == "__main__":
    xmind_file = "file_.xmind"  # Replace with your actual file path
    
    try:
        total_subjects = get_total_subjects(xmind_file)
        print(f"Total number of subjects/nodes: {total_subjects}")
    except Exception as e:
        print(f"Error reading file: {e}")

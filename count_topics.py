import xmind
from xmindparser import xmind_to_dict

def count_topics(node):
    """Recursively counts all topics and subtopics."""
    total = 1  # Count the current topic
    
    # Check if this topic has subtopics
    if 'topics' in node and node['topics']:
        for subtopic in node['topics']:
            total += count_topics(subtopic)
            
    return total

def get_total_topics_in_xmind(file_path):
    """Loads the Xmind file and tallies all topics."""
    # xmind_to_dict returns a list of sheets
    data = xmind_to_dict(file_path)
    
    total_map_topics = 0
    for sheet in data:
        # Each sheet has one root topic
        root_topic = sheet.get('topic')
        if root_topic:
            total_map_topics += count_topics(root_topic)
            
    return total_map_topics

# --- Example Usage ---
# xmind_file = 'your_file.xmind'
# topic_count = get_total_topics_in_xmind(xmind_file)
# print(f"Total topics: {topic_count}")

def _count_topics(topic_element):
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
    xmind_file = "file.xmind"  # Replace with your actual file path
    
    try:
        total_subjects = get_total_topics_in_xmind(xmind_file)
        print(f"Total number of subjects/nodes: {total_subjects}")
    except Exception as e:
        print(f"Error reading file: {e}")

import re

def extract_ENA_ID_and_Sample_ID(file_path):
    """
    Extract ENA ID and Sample ID from a file.

    Parameters:
        file_path (str): The path to the file to extract ENA ID and Sample ID from.

    Returns:
        dict: A dictionary where the keys are ENA IDs and the values are sample IDs. The sample IDs are stored as comma-separated strings.
    """
    ENA_ID = None
    Sample_ID = []
    result = {}
    
    with open(file_path, 'r') as file:
        # Read the file line by line
        for line in file:
            # Remove non-alphanumeric characters from the line
            line = re.sub(r'[^\w\s]', '', line)
            # Split the line into words
            words = line.split()
            # Process each word
            for word in words:
                if word.startswith("PRJ"):
                    # If the word starts with "PRJ", store it as the ENA ID and add a new key to the result dictionary
                    ENA_ID = word
                    result[ENA_ID] = []
                elif word.startswith(("ERS", "SRS", "DRS", "SAM")):
                    # If the word starts with "ERS", "SRS", "DRS", or "SAM", add it to the list associated with the ENA ID in the result dictionary
                    result[ENA_ID].append(word)
    
    # Convert the list of sample IDs for each ENA ID into a comma-separated string
    for ENA_ID, Sample_ID in result.items():
        result[ENA_ID] = ",".join(Sample_ID)
        
    # Return the result dictionary
    return result

file_path = "/content/ena_api_data.tsv"
result = extract_ENA_ID_and_Sample_ID(file_path)

print("ENA-ID,Sample ID")
for ENA_ID, Sample_ID in result.items():
    print(f"{ENA_ID},{Sample_ID}")

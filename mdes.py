import os

# Function to load and structure data from a specific text file
def load_and_structure_data(file_path):
    try:
        # Check if the specified file exists and is named 'data.txt'
        if os.path.isfile(file_path) and os.path.basename(file_path) == "data.txt":
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Split content into individual patient records
            patient_records = content.strip().split("\n\n")
            structured_data = []

            for record in patient_records:
                patient_data = {}
                # Split each record into lines and parse key-value pairs
                for line in record.split("\n"):
                    if ": " in line:  # Ensure the line contains a ': ' separator
                        key, value = line.split(": ", 1)
                        patient_data[key.strip()] = value.strip()
                if patient_data:  # Add non-empty patient data
                    structured_data.append(patient_data)
            
            return structured_data
        else:
            print(f"The file {file_path} does not exist or is not named 'data.txt'.")
            return []
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return []

# Specify the relative path to data.txt
file_path = "data.txt"  # Ensure this is the correct relative path to your file

# Load and print structured data
structured_documents = load_and_structure_data(file_path)
if structured_documents:
    for i, patient in enumerate(structured_documents, 1):
        print(f"Patient {i}:")
        for key, value in patient.items():
            print(f"  {key}: {value}")
        print()

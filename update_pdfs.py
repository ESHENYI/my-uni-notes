import os, json

# Folder that contains subject folders (CIVL6415, MATH3303, etc.)
base_folder = "files"

data = {}

# Loop through each subject folder inside /files
for subject in os.listdir(base_folder):
    subject_path = os.path.join(base_folder, subject)
    if os.path.isdir(subject_path):
        # Collect only PDF files in this folder
        pdf_files = [f for f in os.listdir(subject_path) if f.lower().endswith(".pdf")]
        data[subject] = sorted(pdf_files)

# Save as pdfs.json in the repo root
with open("pdfs.json", "w") as f:
    json.dump(data, f, indent=2)

print("pdfs.json updated!")

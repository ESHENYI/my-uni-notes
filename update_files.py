import os, json

BASE = "files"
data = {}

# Allowed file types
ALLOWED_EXTENSIONS = [".pdf", ".doc", ".docx", ".ppt", ".pptx", ".txt", ".jpg", ".jpeg", ".png"]

# Scan each subject folder in /files
for subject in os.listdir(BASE):
    subject_path = os.path.join(BASE, subject)
    if os.path.isdir(subject_path):
        files = [
            f for f in os.listdir(subject_path)
            if os.path.splitext(f)[1].lower() in ALLOWED_EXTENSIONS
        ]
        if files:
            data[subject] = sorted(files)

# Write to files.json in repo root
with open("files.json", "w") as fp:
    json.dump(data, fp, indent=2)

print("✅ files.json updated!")

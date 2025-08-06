import os, json

BASE = "files"
data = {}

# Scan each subject folder in /files
for subject in os.listdir(BASE):
    subject_path = os.path.join(BASE, subject)
    if os.path.isdir(subject_path):
        pdfs = [f for f in os.listdir(subject_path) if f.lower().endswith(".pdf")]
        data[subject] = sorted(pdfs)

# Write to pdfs.json in repo root
with open("pdfs.json", "w") as fp:
    json.dump(data, fp, indent=2)

print("✅ pdfs.json updated!")

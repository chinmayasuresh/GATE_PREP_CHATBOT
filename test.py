import json

with open('mcqs/data_structures.json', 'r', encoding='utf-8-sig') as f:
    data = json.load(f)

print("✅ File loaded!")
print(data[:2])  # Show first 2 questions

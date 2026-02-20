# ==========================================
# PROJECT CLEANUP & STRUCTURE CHECK TOOL
# ==========================================

import os
import shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

print("\n[Cleanup] Starting cleanup...\n")

# Remove __pycache__ folders
for root, dirs, files in os.walk(ROOT):
    for d in dirs:
        if d == "__pycache__":
            path = os.path.join(root, d)
            shutil.rmtree(path)
            print("Removed:", path)

# Remove outputs folder
outputs_path = os.path.join(ROOT, "outputs")
if os.path.exists(outputs_path):
    shutil.rmtree(outputs_path)
    print("Removed outputs folder")

# Remove temp wav files
for root, dirs, files in os.walk(ROOT):
    for file in files:
        if file.endswith(".wav") or file.endswith(".log"):
            os.remove(os.path.join(root, file))

print("\n[Cleanup] Project cleaned successfully.")
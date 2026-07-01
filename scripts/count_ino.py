from pathlib import Path

# Count all .ino files in the repository
ino_files = list(Path(".").rglob("*.ino"))

print(f"Number of .ino files: {len(ino_files)}")

print("\nFiles found:")
for file in ino_files:
    print(file)

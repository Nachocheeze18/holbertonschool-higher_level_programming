import sys

# Check if the file path is provided as an argument
if len(sys.argv) != 2:
    print("Usage: python file_reader.py <file_path>")
    sys.exit(1)

file_path = sys.argv[1]

try:
    # Open the file with UTF-8 encoding
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
        print(content)
except Exception as e:
    print(f"Error occurred while reading the file: {e}")

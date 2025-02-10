import os

# Specify the folder path and file name
folder_path = r"C:\Users\andre\Aarhus Uni\Computerprojekt1"  # Use a raw string to handle backslashes
file_name = "empty_file1.txt"

# Create the folder if it doesn't exist
os.makedirs(folder_path, exist_ok=True)

# Create the empty file
file_path = os.path.join(folder_path, file_name)
with open(file_path, 'w') as file:
    pass

print(f"Empty file created at: {file_path}")


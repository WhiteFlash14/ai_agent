import os

# =============================================================================
# 1. os.path.abspath() - Get absolute path from relative path
# =============================================================================

print("=== os.path.abspath() ===")
# Converts relative paths to absolute paths
relative_path = "documents/file.txt"
absolute_path = os.path.abspath(relative_path)
print(f"Relative: {relative_path}")
print(f"Absolute: {absolute_path}")

# Works with current directory reference
current_dir = os.path.abspath(".")
print(f"Current directory: {current_dir}")

# Works with parent directory reference
parent_dir = os.path.abspath("..")
print(f"Parent directory: {parent_dir}")

# Even works with non-existent paths
fake_path = os.path.abspath("non_existent/folder/file.txt")
print(f"Non-existent path: {fake_path}")

print("\n" + "="*60 + "\n")

# =============================================================================
# 2. os.path.join() - Join paths safely
# =============================================================================

print("=== os.path.join() ===")
# Automatically handles path separators (/ on Unix, \ on Windows)
folder = "documents"
subfolder = "projects"
filename = "report.pdf"

# Join multiple path components
full_path = os.path.join(folder, subfolder, filename)
print(f"Joined path: {full_path}")

# Works with absolute paths too
base_path = "/home/user"
relative_part = "work/files"
combined = os.path.join(base_path, relative_part, "data.csv")
print(f"Combined path: {combined}")

# Handles empty strings gracefully
path_with_empty = os.path.join("folder", "", "file.txt")
print(f"With empty string: {path_with_empty}")

print("\n" + "="*60 + "\n")

# =============================================================================
# 3. .startswith() - Check if string starts with substring
# =============================================================================

print("=== .startswith() ===")
filename = "report_2024.pdf"
path = "/home/user/documents/file.txt"

# Basic usage
print(f"'{filename}' starts with 'report': {filename.startswith('report')}")
print(f"'{filename}' starts with 'data': {filename.startswith('data')}")

# Case sensitive
print(f"'{filename}' starts with 'Report': {filename.startswith('Report')}")

# Check multiple possibilities (tuple)
extensions = filename.startswith(('report', 'data', 'summary'))
print(f"Starts with any of report/data/summary: {extensions}")

# Useful for path checking
is_absolute = path.startswith('/')
print(f"'{path}' is absolute path: {is_absolute}")

print("\n" + "="*60 + "\n")

# =============================================================================
# 4. os.path.isdir() - Check if path is a directory
# =============================================================================

print("=== os.path.isdir() ===")
# Check if current directory exists
current_is_dir = os.path.isdir(".")
print(f"Current directory (.) is a directory: {current_is_dir}")

# Check parent directory
parent_is_dir = os.path.isdir("..")
print(f"Parent directory (..) is a directory: {parent_is_dir}")

# Check a file (should return False)
# Note: This will be False since we're checking if a file is a directory
file_is_dir = os.path.isdir("example_file.txt")
print(f"'example_file.txt' is a directory: {file_is_dir}")

# Check non-existent path
nonexistent_is_dir = os.path.isdir("non_existent_folder")
print(f"Non-existent folder is a directory: {nonexistent_is_dir}")

print("\n" + "="*60 + "\n")

# =============================================================================
# 5. os.listdir() - List directory contents
# =============================================================================

print("=== os.listdir() ===")
try:
    # List current directory contents
    current_contents = os.listdir(".")
    print("Current directory contents:")
    for item in current_contents[:5]:  # Show first 5 items
        print(f"  - {item}")
    if len(current_contents) > 5:
        print(f"  ... and {len(current_contents) - 5} more items")
        
except PermissionError:
    print("Permission denied to list directory")
except FileNotFoundError:
    print("Directory not found")

print("\n" + "="*60 + "\n")

# =============================================================================
# 6. os.path.getsize() - Get file size
# =============================================================================

print("=== os.path.getsize() ===")
# This function needs actual files to work, so we'll show the concept
print("Note: os.path.getsize() returns file size in bytes")
print("Example usage:")
print("file_size = os.path.getsize('document.pdf')")
print("print(f'File size: {file_size} bytes')")

# Convert bytes to more readable formats
def format_size(size_bytes):
    if size_bytes < 1024:
        return f"{size_bytes} bytes"
    elif size_bytes < 1024 * 1024:
        return f"{size_bytes / 1024:.1f} KB"
    elif size_bytes < 1024 * 1024 * 1024:
        return f"{size_bytes / (1024 * 1024):.1f} MB"
    else:
        return f"{size_bytes / (1024 * 1024 * 1024):.1f} GB"

# Example sizes
example_sizes = [512, 1536, 1048576, 5242880]
for size in example_sizes:
    print(f"{size} bytes = {format_size(size)}")

print("\n" + "="*60 + "\n")

# =============================================================================
# 7. os.path.isfile() - Check if path is a file
# =============================================================================

print("=== os.path.isfile() ===")
# Check if a path points to a file (not directory)
current_is_file = os.path.isfile(".")
print(f"Current directory (.) is a file: {current_is_file}")

# This would return True for actual files
print("Example usage:")
print("is_file = os.path.isfile('document.txt')")
print("print(f'document.txt is a file: {is_file}')")

print("\n" + "="*60 + "\n")

# =============================================================================
# 8. .join() - Join strings with separator
# =============================================================================

print("=== .join() ===")
# Join list of strings with a separator
words = ["apple", "banana", "cherry", "date"]
sentence = " ".join(words)
print(f"Words joined with space: {sentence}")

# Join with different separators
comma_separated = ", ".join(words)
print(f"Words joined with comma: {comma_separated}")

hyphen_separated = "-".join(words)
print(f"Words joined with hyphen: {hyphen_separated}")

# Join path components (alternative to os.path.join for simple cases)
path_parts = ["home", "user", "documents", "file.txt"]
manual_path = "/".join(path_parts)
print(f"Manual path joining: /{manual_path}")

# Join numbers (convert to strings first)
numbers = [1, 2, 3, 4, 5]
number_string = "-".join(str(n) for n in numbers)
print(f"Numbers joined: {number_string}")

print("\n" + "="*60 + "\n")

# =============================================================================
# COMBINING METHODS - Practical Examples
# =============================================================================

print("=== COMBINING METHODS - REAL WORLD EXAMPLES ===")

# Example 1: Find all PDF files in a directory and get their sizes
def find_pdf_files_with_sizes(directory_path):
    """Find all PDF files in a directory and return their sizes"""
    pdf_files = []
    
    # Convert to absolute path
    abs_path = os.path.abspath(directory_path)
    print(f"Searching in: {abs_path}")
    
    # Check if directory exists
    if not os.path.isdir(abs_path):
        print(f"Directory doesn't exist: {abs_path}")
        return []
    
    try:
        # List all items in directory
        items = os.listdir(abs_path)
        
        for item in items:
            # Create full path
            full_path = os.path.join(abs_path, item)
            
            # Check if it's a file and ends with .pdf
            if os.path.isfile(full_path) and item.lower().startswith('report') and item.lower().endswith('.pdf'):
                try:
                    size = os.path.getsize(full_path)
                    pdf_files.append({
                        'name': item,
                        'path': full_path,
                        'size': size,
                        'size_formatted': format_size(size)
                    })
                except OSError:
                    print(f"Could not get size for: {item}")
                    
    except PermissionError:
        print(f"Permission denied accessing: {abs_path}")
    
    return pdf_files

# Example usage
print("Example 1: Finding PDF files starting with 'report'")
pdf_files = find_pdf_files_with_sizes(".")
if pdf_files:
    for file_info in pdf_files:
        print(f"  {file_info['name']} - {file_info['size_formatted']}")
else:
    print("  No matching PDF files found")

print()

# Example 2: Create a file organizer
def organize_files_by_extension(source_dir):
    """Organize files by their extensions"""
    abs_source = os.path.abspath(source_dir)
    
    if not os.path.isdir(abs_source):
        print(f"Source directory doesn't exist: {abs_source}")
        return
    
    # Dictionary to group files by extension
    files_by_ext = {}
    
    try:
        items = os.listdir(abs_source)
        
        for item in items:
            full_path = os.path.join(abs_source, item)
            
            # Only process files, not directories
            if os.path.isfile(full_path):
                # Get extension
                if '.' in item:
                    extension = item.split('.')[-1].lower()
                else:
                    extension = 'no_extension'
                
                if extension not in files_by_ext:
                    files_by_ext[extension] = []
                
                files_by_ext[extension].append({
                    'name': item,
                    'size': format_size(os.path.getsize(full_path))
                })
    
    except PermissionError:
        print(f"Permission denied accessing: {abs_source}")
        return
    
    # Display results
    print("Example 2: Files organized by extension")
    for ext, files in files_by_ext.items():
        file_names = [f['name'] for f in files]
        print(f"  .{ext} files: {', '.join(file_names)}")

# Run the organizer
organize_files_by_extension(".")

print()

# Example 3: Safe path builder
def build_safe_path(*path_parts, base_dir=None):
    """Build a safe path and ensure it exists within base directory"""
    if base_dir:
        # Start with absolute base directory
        base_abs = os.path.abspath(base_dir)
        # Join all parts
        full_path = os.path.join(base_abs, *path_parts)
    else:
        # Join all parts starting from current directory
        full_path = os.path.join(*path_parts)
    
    # Get absolute path
    abs_path = os.path.abspath(full_path)
    print(full_path)
    print(abs_path)
    
    # If base_dir specified, ensure path is within it (security check)
    if base_dir:
        base_abs = os.path.abspath(base_dir)
        if not abs_path.startswith(base_abs):
            raise ValueError(f"Path {abs_path} is outside base directory {base_abs}")
    
    return abs_path

print("Example 3: Safe path building")
try:
    safe_path1 = build_safe_path("documents", "projects", "file.txt")
    print(f"  Safe path 1: {safe_path1}")
    
    safe_path2 = build_safe_path("subfolder", "data.csv", base_dir=".")
    print(f"  Safe path 2: {safe_path2}")
    
    # This would raise an error if uncommented:
    unsafe_path = build_safe_path("..", "..", "etc", "passwd", base_dir="/home/user")
    
except ValueError as e:
    print(f"  Security error: {e}")

print("\n" + "="*60 + "\n")

# =============================================================================
# WHEN TO COMBINE THESE METHODS
# =============================================================================

print("=== WHEN TO COMBINE THESE METHODS ===")
print("""
Common Combinations:

1. File Processing Pipeline:
   - os.path.abspath() + os.path.isdir() + os.listdir() + os.path.isfile()
   - Use case: Process all files in a directory safely

2. Path Building and Validation:
   - os.path.join() + os.path.abspath() + os.path.isfile/isdir()
   - Use case: Build paths dynamically and verify they exist

3. File Filtering:
   - os.listdir() + .startswith() + os.path.isfile()
   - Use case: Find files matching specific patterns

4. Size Analysis:
   - os.listdir() + os.path.isfile() + os.path.getsize() + .join()
   - Use case: Generate reports about file sizes

5. Path Security:
   - os.path.abspath() + .startswith() + os.path.join()
   - Use case: Ensure paths stay within allowed directories

6. Data Presentation:
   - All file operations + .join() for formatting output
   - Use case: Create readable reports and summaries
""")

print("These methods work together to create robust file handling systems!")



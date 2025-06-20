import os

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
# Your specific example: os.path.join('/home/user/app/data', '../../')
# =============================================================================

print("=== Your Example ===")
base_path = '/home/user/app/data'
relative_part = '../../'

result = os.path.join(base_path, relative_part)
print(f"os.path.join('{base_path}', '{relative_part}')")
print(f"Result: {result}")
print()

# Let's break down what happened:
print("=== Step-by-step breakdown ===")
print(f"Starting path: {base_path}")
print(f"Adding: {relative_part}")
print("- '../' means 'go up one directory level'")
print("- '../../' means 'go up TWO directory levels'")
print()

# Show the directory structure conceptually:
print("Directory structure:")
print("/home/user/app/data  ← Starting here")
print("/home/user/app/      ← After first '../'")
print("/home/user/          ← After second '../'")
print()

# =============================================================================
# Important: os.path.join() vs os.path.normpath()
# =============================================================================

print("=== Important Difference ===")
print("os.path.join() just concatenates - it doesn't resolve '..' references!")
print(f"os.path.join() result: {result}")

# To actually resolve the '..' references, use normpath():
normalized = os.path.normpath(result)
print(f"os.path.normpath() result: {normalized}")
print()

# Or combine them:
direct_normalized = os.path.normpath(os.path.join(base_path, relative_part))
print(f"Combined approach: {direct_normalized}")
print()

# =============================================================================
# More Examples with Different Relative Paths
# =============================================================================

print("=== More Examples ===")
examples = [
    ('../', "Go up one level"),
    ('../../', "Go up two levels"),
    ('../../../', "Go up three levels"),
    ('../sibling/', "Go up one level, then into sibling directory"),
    ('../../other/folder/', "Go up two levels, then into other/folder"),
    ('file.txt', "Just add a file in current directory"),
    ('../file.txt', "Go up one level, then add file"),
]

for rel_path, description in examples:
    joined = os.path.join(base_path, rel_path)
    normalized = os.path.normpath(joined)
    print(f"'{rel_path}' ({description})")
    print(f"  Joined: {joined}")
    print(f"  Normalized: {normalized}")
    print()

# =============================================================================
# Practical Security Considerations
# =============================================================================

print("=== Security Considerations ===")
print("Be careful with '..' in paths - they can escape intended directories!")
print()

def safe_join(base_dir, user_path):
    """Safely join paths and ensure result stays within base directory"""
    # Join the paths
    full_path = os.path.join(base_dir, user_path)
    # Normalize to resolve '..' references
    normalized = os.path.normpath(full_path)
    # Convert both to absolute paths for comparison
    base_abs = os.path.abspath(base_dir)
    result_abs = os.path.abspath(normalized)
    
    # Check if the result is still within the base directory
    if not result_abs.startswith(base_abs + os.sep) and result_abs != base_abs:
        raise ValueError(f"Path '{user_path}' would escape base directory!")
    
    return normalized

# Test the safe function
test_base = '/home/user/app'
safe_examples = [
    'data/file.txt',      # Safe
    '../other/file.txt',  # Safe (stays in /home/user/)
    '../../file.txt',     # Unsafe (goes to /home/)
    '../../../etc/passwd' # Very unsafe!
]

print("Testing safe_join function:")
for test_path in safe_examples:
    try:
        safe_result = safe_join(test_base, test_path)
        print(f"✓ '{test_path}' → {safe_result}")
    except ValueError as e:
        print(f"✗ '{test_path}' → {e}")

print()

# =============================================================================
# Real-world Usage Patterns
# =============================================================================

print("=== Real-world Usage Patterns ===")
print()

# Pattern 1: Building paths relative to script location
script_dir = '/home/user/myproject/scripts'
print("Pattern 1: Paths relative to script location")
print(f"Script directory: {script_dir}")

config_path = os.path.normpath(os.path.join(script_dir, '../config/settings.json'))
data_path = os.path.normpath(os.path.join(script_dir, '../data/input.csv'))
output_path = os.path.normpath(os.path.join(script_dir, '../output/results.txt'))

print(f"Config file: {config_path}")
print(f"Data file: {data_path}")
print(f"Output file: {output_path}")
print()

# Pattern 2: Working with nested project structures
project_root = '/home/user/myproject'
print("Pattern 2: Project structure navigation")
print(f"Project root: {project_root}")

# From a deeply nested location, go back to root then to another branch
current_location = os.path.join(project_root, 'src/utils/helpers')
print(f"Current location: {current_location}")

# Go back to root, then to tests directory
test_path = os.path.normpath(os.path.join(current_location, '../../../tests/'))
print(f"Tests directory: {test_path}")

# Go back to root, then to docs
docs_path = os.path.normpath(os.path.join(current_location, '../../../docs/api.md'))
print(f"Documentation: {docs_path}")
print()

# =============================================================================
# Alternative Approaches
# =============================================================================

print("=== Alternative Approaches ===")
print()

# Using pathlib (modern Python approach)
try:
    from pathlib import Path
    
    print("Using pathlib (Python 3.4+):")
    base_pathlib = Path('/home/user/app/data')
    result_pathlib = base_pathlib / '../../'
    resolved_pathlib = result_pathlib.resolve()
    
    print(f"Path('{base_path}') / '{relative_part}'")
    print(f"Before resolve(): {result_pathlib}")
    print(f"After resolve(): {resolved_pathlib}")
    print()
    
except ImportError:
    print("pathlib not available (Python < 3.4)")

# Manual path resolution function
def manual_resolve(path):
    """Manually resolve '..' references in a path"""
    parts = path.split(os.sep)
    resolved_parts = []
    
    for part in parts:
        if part == '..':
            if resolved_parts:
                resolved_parts.pop()
        elif part and part != '.':
            resolved_parts.append(part)
    
    return os.sep.join(resolved_parts)

print("Manual resolution:")
manual_result = manual_resolve(result)
print(f"Manual resolve of '{result}': {manual_result}")
print()
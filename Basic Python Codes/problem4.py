import os

def print_directory_contents(directory):
    # Check if the directory exists
    if os.path.exists(directory):
        # List all files and directories in the given directory
        print(f"Contents of {directory}:")
        for item in os.listdir(directory):
            print(item)
    else:
        print(f"Directory '{directory}' does not exist.")

# Example usage:
directory_path = '/Windows/Web/Wallpaper/Theme2/'  # Replace with your directory path
print_directory_contents(directory_path)


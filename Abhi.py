import os

def create_directory_structure(base_path, directory_tree):
    """
    Recursively creates a directory structure.

    Args:
        base_path (str): The path where to create the directories.
        directory_tree (dict): A nested dictionary representing folder structure.
    """
    for folder, subfolders in directory_tree.items():
        # Create the current folder
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path, exist_ok=True)
        print(f"Created: {folder_path}")
        
        # If subfolders is a dictionary, call recursively
        if isinstance(subfolders, dict):
            create_directory_structure(folder_path, subfolders)
        # If it's a list, create folders for each element
        elif isinstance(subfolders, list):
            for subfolder in subfolders:
                subfolder_path = os.path.join(folder_path, subfolder)
                os.makedirs(subfolder_path, exist_ok=True)
                print(f"Created: {subfolder_path}")

if _name_ == "_main_":
    # Define your folder structure as a nested dictionary
    directory_tree = {
        "Project": {
            "Data": ["Raw", "Processed"],
            "Scripts": {},
            "Results": {
                "Figures": {},
                "Tables": {}
            },
            "Docs": {}
        },
        "Backup": {}
    }

    # Base path where the directories will be created
    base_path = "./MyStudyProject"
    create_directory_structure(base_path, directory_tree)

import os
import shutil
import re
import inquirer

def list_txt_files(folder):
    return [f for f in os.listdir(folder) if f.endswith('.txt')]

def list_folders(directory):
    return [f for f in os.listdir(directory) if os.path.isdir(os.path.join(directory, f))]

def run_tic_file_copy():
    current_folder = os.getcwd()

    # Select .txt file
    txt_files = list_txt_files(current_folder)
    if not txt_files:
        print("No .txt files found in the current folder.")
        return

    file_question = [
        inquirer.List("file", message="Select the .txt file with TICs:", choices=txt_files)
    ]
    file_answer = inquirer.prompt(file_question)
    txt_path = os.path.join(current_folder, file_answer["file"])

    # Select source folder
    folders = list_folders(current_folder)
    if not folders:
        print("No folders found in the current directory.")
        return

    folder_question = [
        inquirer.List("folder", message="Select the folder with the files:", choices=folders)
    ]
    folder_answer = inquirer.prompt(folder_question)
    source_folder = os.path.join(current_folder, folder_answer["folder"])

    # Create destination folder
    source_folder_name = os.path.basename(source_folder)
    destination_folder = os.path.join(current_folder, f"Selected {source_folder_name}")
    os.makedirs(destination_folder, exist_ok=True)

    # Read TICs from file
    with open(txt_path, 'r') as f:
        tics = [line.strip() for line in f if line.strip().isdigit()]

    source_files = os.listdir(source_folder)
    copied_count = 0

    for file in source_files:
        filename = os.path.splitext(file)[0]  # remove extension
        numeric_parts = re.findall(r'\d+', filename)

        if any(tic in numeric_parts for tic in tics):
            shutil.copy2(os.path.join(source_folder, file), os.path.join(destination_folder, file))
            copied_count += 1

    print(f"\n{copied_count} file(s) copied to: {destination_folder}")

# Direct call (runs automatically when executed)
run_tic_file_copy()

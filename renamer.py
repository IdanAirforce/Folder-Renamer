import os

folder_path = input("Enter the folder path: ")

if not os.path.exists(folder_path) or not os.path.isdir(folder_path):
    print("The provided path is not valid. Please check and try again.")
else:
    old_prefix = input("Enter the folder prefix to find (example: 'qb-'): ")

    new_prefix = input("Enter the new prefix to change to (example: 'in-'): ")

    directories = [d for d in os.listdir(folder_path)
                   if os.path.isdir(os.path.join(folder_path, d)) and d.startswith(old_prefix)]

    if directories:
        for directory in directories:
            new_directory_name = directory.replace(old_prefix, new_prefix, 1)
            old_directory_path = os.path.join(folder_path, directory)
            new_directory_path = os.path.join(folder_path, new_directory_name)

            os.rename(old_directory_path, new_directory_path)
            print(f'Renamed "{directory}" to "{new_directory_name}"')
    else:
        print(f"No directories found starting with '{old_prefix}'.")

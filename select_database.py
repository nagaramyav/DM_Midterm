import os

def select_database():
    # List CSV files in the current directory
    csv_files = [file for file in os.listdir() if file.endswith('.csv')]
    
    if not csv_files:
        print("No CSV files found in the current directory.")
        return None
    
    print("Select a store:")
    for i, file in enumerate(csv_files, start=1):
        file_name = os.path.splitext(file)[0]  # Remove the file extension
        print(f"{i}. {file_name}")

    choice = input("Please enter a number to select a store of your choice: ")

    try:
        index = int(choice) - 1
        if 0 <= index < len(csv_files):
            return csv_files[index]
        else:
            print("Invalid choice. Please enter a number corresponding to a database.")
            return select_database()  # Recursive call to prompt again
    except ValueError:
        print("Invalid choice. Please enter a number corresponding to a database.")
        return select_database()  # Recursive call to prompt again

if __name__ == "__main__":
    selected_database = select_database()
    if selected_database:
        print(f"Selected database: {selected_database}")

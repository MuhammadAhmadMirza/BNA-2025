from config import *
from file_handling import *

option = input("""What do you want to do with the dataset ?
1. Rename files in order
2. Label the data
3. Split the dataset into training and testing
4. Generate data.yaml \n
Enter the option number: """)

# Check if the input contains valid numbers
valid_options = {'1', '2', '3', '4'}

if not any(opt in option for opt in valid_options):
    print("Invalid input. Please enter valid numbers (1, 2, 3 or 4).")
else:
    # Ask for confirmation
    confirmation = input(f"Are you sure you want to perform the following actions: {option}? (y/n): ").lower()

    if confirmation in ['y', 'yes']:
        try:
            if '1' in option:
                rename_files_in_folder(raw_dataset_path)
                print("Task 1 completed without any exceptions.")
        except Exception as e:
            print(f"Task 1 encountered this error: {e}")

        try:
            if '2' in option:
                label_images()
                print("Task 2 completed without any exceptions.")
        except Exception as e:
            print(f"Task 2 encountered this error: {e}")

        try:
            if '3' in option:
                split_raw_dataset(raw_dataset_path, training_dataset_path, testing_dataset_path)
                print("Task 3 completed without any exceptions.")
        except Exception as e:
            print(f"Task 3 encountered this error: {e}")

        try:
            if '4' in option:
                prepare_yaml(dataset_path, training_dataset_path, testing_dataset_path, dataset_path + '/classes.txt')
                print("Task 4 completed without any exceptions.")
        except Exception as e:
            print(f"Task 4 encountered this error: {e}")
    else:
        print("Action canceled.")

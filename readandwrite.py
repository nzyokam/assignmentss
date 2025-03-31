def read_and_modify_file():
    try:
        # Ask the user for the filename
        filename = input("Enter the filename to read: ")

        # Try to open the file for reading
        with open(filename, "r") as file:
            content = file.readlines()  # Read file line by line

        # Modify content: Convert all text to uppercase (example modification)
        modified_content = [line.upper() for line in content]

        # Write to a new file
        new_filename = "modified_" + filename
        with open(new_filename, "w") as new_file:
            new_file.writelines(modified_content)

        print(f"File has been modified and saved as '{new_filename}'.")

    except FileNotFoundError:
        print("Error: The file does not exist. Please check the filename and try again.")
    except IOError:
        print("Error: Unable to read the file. Check file permissions or format.")

# Run the function
if __name__ == "__main__":
    read_and_modify_file()

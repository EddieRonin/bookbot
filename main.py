def main():
    path_to_file = "books/frankenstein.txt"  # Adjust the path based on your project structure
    try:
        with open(path_to_file, 'r', encoding='utf-8') as f:
            file_contents = f.read()
            print(file_contents)
    except FileNotFoundError:
        print(f"Error: File '{path_to_file}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

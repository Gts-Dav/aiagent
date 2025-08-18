from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content


def main():
    for directory in [".", "pkg", "/bin", "../"]:
        result = get_files_info("testEnvironments/calculator", directory)
        print(f"Result for \"{directory}\" directory:\n{result}")

    for file in ["lorem.txt", "main.py", "pkg/calculator.py", "/bin/cat", "pkg/does_not_exist.py"]:
        result = get_file_content("testEnvironments/calculator", file)
        print(f"Result for \"{file}\" file:\n{result}")


if __name__ == "__main__":
    main()

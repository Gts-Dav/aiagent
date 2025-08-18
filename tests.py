import os
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file_content import write_file_content
from functions.run_python_file import run_python_file


def main():
    print("Functions:")

    print("\nFunction: get_files_info")
    for directory in [".", "pkg", "/bin", "../"]:
        result = get_files_info("testEnvironments/calculator", directory)
        print(f"Result for \"{directory}\" directory:\n{result}")

    print("\nFunction: get_file_content")
    for file in ["lorem.txt", "main.py", "pkg/calculator.py", "/bin/cat", "pkg/does_not_exist.py"]:
        result = get_file_content("testEnvironments/calculator", file)
        print(f"Result for \"{file}\" file:\n{result}")

    print("\nFunction: write_file_content")
    for file, content in [("pkg/morelorem.txt", "wait, this isn't lorem ipsum"), ("pkg/morelorem.txt", "lorem ipsum dolor sit amet"), ("/tmp/temp.txt", "this should not be allowed")]:
        result = write_file_content(
            "testEnvironments/calculator", file, content)
        print(f"Result for \"{file}\" with content: {
              content} result:\n{result}")
    try:
        os.remove("testEnvironments/calculator/pkg/morelorem.txt")
    except Exception as e:
        print(e)

    print("\nFunction: run_python_file")
    for file, args in [("main.py", []), ("main.py", ["3 + 5"]), ("tests.py", []), ("../main.py", []), ("nonexistent.py", [])]:
        result = run_python_file("testEnvironments/calculator", file, args)
        print(f"Result for \"{file}\" output:\n{result}")


if __name__ == "__main__":
    main()

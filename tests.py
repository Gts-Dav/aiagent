from functions.get_files_info import get_files_info


def main():
    for directory in [".", "pkg", "/bin", "../"]:
        result = get_files_info("testEnvironments/calculator", directory)
        print(f"Result for \"{directory}\" directory:\n{result}")


if __name__ == "__main__":
    main()

import argparse
from duplicate_finder.duplicates import find_duplicates


def generate_file_types(file_type_str):
    file_type_str = file_type_str.lower()
    return [f for f in file_type_str.split(",") if f]


def main():
    parser = argparse.ArgumentParser(
        description="Provide the source and destination of images to organise."
    )
    parser.add_argument(
        "-d", "--directory", required=True, help="The directory to check for duplicates"
    )
    parser.add_argument(
        "-r",
        "--recursive",
        action="store_true",
        help="Recurse thorugh the source folder",
    )
    parser.add_argument(
        "-f",
        "--filetypes",
        default="",
        type=str,
        required=False,
        help="Comma Separated Values of the filetypes to check for duplicates",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        default=False,
        action="store_true",
        help="Enable verbose mode",
    )

    args = parser.parse_args()

    file_types = generate_file_types(args.filetypes)

    find_duplicates(args.directory, args.recursive, file_types, args.verbose)


if __name__ == "__main__":
    main()

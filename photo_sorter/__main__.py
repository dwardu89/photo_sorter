import argparse
from photo_sorter.sorting import sort


def main():
    parser = argparse.ArgumentParser(
        description="Provide the source and destination of images to organise."
    )
    parser.add_argument("-s", "--source", required=True, help="The source folder")
    parser.add_argument(
        "-d", "--destination", required=True, help="The destination folder"
    )
    parser.add_argument(
        "-r",
        "--recursive",
        action="store_true",
        help="Recurse through the source folder",
    )

    parser.add_argument(
        "-l",
        "--local",
        action="store_true",
        help="Convert to local time (instead of UTC time)",
    )

    args = parser.parse_args()

    sort(args.source, args.destination, args.recursive, args.local)


if __name__ == "__main__":
    main()

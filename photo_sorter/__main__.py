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
        "-df",
        "--destinationformat",
        default=1,
        required=False,
        type=int,
        help='The format of folders to create when sorting the files in the destination folder. Each numeric value provides the following format 1="YYYY/mm/dd", 2="YYYYmmdd", 3="YYYYmm", 4 "YYYY"',
        choices=["1", "2", "3", "4"],
    )
    parser.add_argument(
        "-r",
        "--recursive",
        action="store_true",
        help="Recurse thorugh the source folder",
    )

    args = parser.parse_args()

    sort(
        folder=args.source,
        outputfolder=args.destination,
        recursive=args.recursive,
        destination_format=args.destinationformat,
    )


if __name__ == "__main__":
    main()

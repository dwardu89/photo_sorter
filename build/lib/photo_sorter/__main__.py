
import argparse
from photo_sorter.sorting import sort


def main():
    parser = argparse.ArgumentParser(description='Provide the source and destination of images to organise.')
    parser.add_argument('-s', '--source', required=True, help='The source folder')
    parser.add_argument('-d', '--destination', required=True, help='The destination folder')
    parser.add_argument('-r', '--recursive', action="store_true", help='Recurse thorugh the source folder')
    
    args = parser.parse_args()
    
    sort(args.source, args.destination, args.recursive)


if __name__ == "__main__":
    main()

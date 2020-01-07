# Photo Sorter
-----------------
Over the past year's, I've ended up with a collection of images scattered around a few folders in my file system. 
This became a problem when I wanted to start organising these photos which could have similar names due to the way the 
cameras format the image names when it captures a photo. This could overwrite images if I were to copy the images to 
 one folder.

An image sorting function that can be used to consolidate photos to a specific folder format <year/month/day_of_month>. 
This also preserves the name of the image that the image was given.

This uses the EXIF data found in the file and if the EXIF data is not available then it will revert to the created date.

### How to use the Photo Sorter Tool
Find and move all images in a folder

- `photo_sorter -f <source> -o <destination>`

Find and move all images in a folder and its sub folders

- `photo_sorter -f <source> -o <destination> --recursive`

File types supported:

- jpeg
- png
- bmp

# Find Duplicates

This tool helps find files that have a duplicate `sha1` hash. It will provide you with a table of files that contain 
the same hash.

### How to use the Photo Sorter Tool
Find and move all images in a folder

- `find_duplicates -d <directory> --recursive`

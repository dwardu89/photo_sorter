Image Sorter
-----------------
Over the past year's, I've ended up with a collection of images scattered around a few folders in my file system. 
This became a problem when I wanted to start organising these photos which could have similar names due to the way the 
cameras format the image names when it captures a photo. This could overwrite images if I were to copy the images to 
 one folder.

An image sorting function that can be used to consolidate photos to a specific folder format <year/month/day_of_month>. 
This also preserves the name of the image that the image was given.

This uses the EXIF data found in the file and if the EXIF data is not available then it will revert to the created date.

### Command to call
Find and move all images in a folder

- `photo_sorter -f <folder> -o <outputfolder>`

Find and move all images in a folder and its sub folders

- `photo_sorter -f <folder> -o <outputfolder> -r`

File types supported:

- jpeg

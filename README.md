Photo Upload
============

I created this to help my wife, [a wedding photographer](http://www.lovesongphoto.com),
backup her photos to S3. She loads files off her memory cards onto her MacBook Pro, then copies the
files over to a Raspberry Pi where this script is then run to handle the uploading to S3.

## Usage

- Edit script to include your S3 creds. There's probably a better way to do this, but whatever.
- cd into the directory you want to upload. The directory name you cd into will be converted into
  the bucket name on S3. Example: A directory called "2010.10.01 Phil and Krista" will be turned
  into bucket "2010.10.01-phil-and-krista"
- Run the script

The files will be deleted as they are uploaded, so only run this from a secondary store and not
where you are working. Like I said, we run it on a Raspberry Pi to back up the photos. Files are
deleted as they are uploaded makes restarting the script from where you left off easy in case of a
connection failure.

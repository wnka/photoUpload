import tinys3
import boto
import os
import slugify
from boto.s3.connection import S3Connection
from boto.s3.key import Key
import sys

def percent_cb(complete, total):
    sys.stdout.write('.')
    sys.stdout.flush()

dirname = os.getcwd()
print "Working on directory: " + dirname

dirsplit = os.path.split(dirname)
dirsuffix = dirsplit[-1]

bucketname = "lovesongphoto.com-" + slugify.slugify(dirsuffix)
print 'Using S3 bucket: ' + bucketname

conn = S3Connection('creds', 'go here')

# See if bucket already exists
bucket = conn.lookup(bucketname)
# Create bucket if it doesn't
if bucket is None:
    print 'Creating bucket'
    bucket = conn.create_bucket(bucketname)
    bucket.set_acl('private')
else:
    print 'Bucket already exists'

for root, dirs, files in os.walk(dirname):
    for filename in files:
        absfile =  root + os.sep + filename
        file = absfile[len(dirname)+1:]
        print ""
        print "Uploading: " + file + " = "
        k = Key(bucket)
        k.key = file
        k.set_contents_from_filename(dirname + '/' + file,
                                     cb=percent_cb, num_cb=10)
        os.remove(absfile)

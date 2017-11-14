#coding=utf-8
import os
import hashlib

def is_identical(file_a,file_b):
	fhand = open(file_a,'r')
	data = fhand.read()
	fhand.close()
	checksum_a = hashlib.md5(data).hexdigest()
	fhand = open(file_b,'r')
	data = fhand.read()
	fhand.close()
	checksum_b = hashlib.md5(data).hexdigest()
	return checksum_a == checksum_b

# def is_samename(filename_a,filename_b):
# 	return os.path.basename(filename_a)==os.path.basename(filename_b)

if __name__ == '__main__':
	count = 0
	rootdir='F:'
	filedict=dict()

	fwhand=open('redundantfiles.txt','w')
	# print rootdir
	for (dirname, dirs, files) in os.walk(rootdir):
		for filename in files:
			#print filename
			if filename.endswith(('.jpg','.JPG','.png','PNG')):
				count = count + 1
				thefile = os.path.join(dirname,filename)
				#size = os.path.getsize(thefile)
				#filedict[size]=filedict.get(size,filename)
				if filename not in filedict:
					filedict[filename]=thefile
				else:
					# print filedict[filename]
					# print thefile
					if is_identical(filedict[filename],thefile):
						#os.remove(thefile)
						fwhand.write(filedict[filename])
						fwhand.write(thefile)
						fwhand.write('\n')

				#print thefile
				#print 'size of image:', size
	print 'Files:', count
	print 'Unique Files:', len(filedict)
	fwhand.close()

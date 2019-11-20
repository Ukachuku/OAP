import re
import os
import shutil

#Original Location of text and tiff files from OCR scan
ocrtextpath = 
os.chdir(ocrtextpath)

#move text
ocrtextsource = 
ocrtextdestination = 

for files in ocrtextsource:
	if files.endswith(".txt"):
		shutil.move(files,ocrtextdestination)
		
#move tiff files
ocrtiffsource = 
ocrtiffdestination = 

for files in ocrtiffsource:
	if files.endswith(".tiff"):
		shutil.move(files,ocrtiffdestination)

#New location of textfiles from OCR
os.chdir(path)
mydir = os.listdir()


#writing the regular expression to the file
for i in mydir:
	with open(i, 'r') as f:
		f_contents = f.read()
		zipcode = re.findall('Zip Code: [0-9]{5}', f_contents)
		Bdate = re.findall('Date of Birth: [0-9]{2}/[0-9]{2}/[0-9]{4}', f_contents)
		str1 = ''.join(zipcode)
		str2 = ''.join(Bdate)
		fil = open("ZipBday_"+str(i),"w")
		fil.write(str1 + " ")
		fil.write(str2)
		fil.close()

#move files to from testing folder to output folder

for files in source:
	if files.startswith("ZipBday"):
		shutil.move(files,destination)

if __name__ == '__main__':
	main()

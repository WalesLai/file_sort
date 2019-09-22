from os import walk
from os.path import join
import shutil
import os
#FullSourcePath=''
#FullTagetPath=''
#tempTargetPath=''

def filenameProcess(file_name):
	filename,subname=file_name.split(".",1)
	author=filename.split("[")[1].split("]")[0]
	name=filename.split("[")[1].split("]")[1]
	return author,name,subname

def CheckAuthorisdir(TargetPath, author):
	if os.path.isdir(os.path.join(TargetPath,TargetPath)):
		return True
	else:
		return False

def file_walk(FullSourcePath,FullTargetPath):
	for root, dirs, files inos.walk(FullSourcePath):
		if len(files) > 0:
			for filename in files :
				file_ext = filename.split('.')[-1]
				author=filename.split('[')[1].split(']')[0]
				bookname=filename.split('[')[1].split(']')[1]
				#Check author is exsit or not
				if (CheckAuthorisdir(FullTargetpath, author)!=TRUE)
					dstFolderPath=os.makedir(os.path.join(FullTargetPath,author))
					shutil.move(filename,dstFolderPath)
				else:
					#check filename is same or not
					dstFilePath = os.path.join(os.path.join(FullTargetPath,author),bookname)
					if os.path.isdir(dstFilePath):
						continue
					else:
						if os.path.isfile(dstFilePath):
							continue
						else:
							shutil.move(filename,os.path.join(FullTargetPath,author))

def execute():
	FullSourcePath=input("Input the source folder path:")
	FullTargetPath=input("Input the target foder path:")
	file_walk(FullSourcePath,FullTargetPath)

if __name__=="__main__":
	print("Start to Comic sort")
	execute()

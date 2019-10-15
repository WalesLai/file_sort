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
	tempPath=os.path.join(TargetPath,author)
	if os.path.isdir(tempPath):
		return True
	else:
		return False

def file_walk(FullSourcePath,FullTargetPath):
	for root, dirs, files in os.walk(FullSourcePath):
		if len(files) > 0:
			for filename in files :
				if filename[0]=='(' or filename.find('(') > 0 or filename.find(')') > 0 : 
					continue
				else:					
					print("filename:%s"%(filename))
					#file_ext = filename.split('.')[-1]
					author=filename.split('[')[1].split(']')[0]
					bookname=filename.split('.')[0].split(']')[1]
					#Check author is exsit or not
					if (CheckAuthorisdir(FullTargetPath, author)!=True):
						print("The %s of folder not create"%(author))
						dstFolderPath=os.path.join(FullTargetPath,author)
						os.makedirs(dstFolderPath) #Create folder as new one
						dstFilePath=os.path.join(dstFolderPath,filename)
						print("Generate Dst file path:%s"%(dstFilePath))
						shutil.copy(os.path.join(FullSourcePath,filename),dstFilePath)
					else:
						#check filename is same or not
						dstFolderPath = os.path.join(os.path.join(FullTargetPath,author),bookname)
						if os.path.isdir(dstFolderPath):
							print("The file already exsit, and it's folder type")
							continue
						else:
							dstFilePath=os.path.join(os.path.join(FullTargetPath,author),filename)
							if os.path.isfile(dstFilePath):
								print("File already exsit..[author]bookname.zip")
								continue
							else:
								print("File not exsit...")
								dstFilePath=os.path.join(FullTargetPath,author)
								dstFilePath=os.path.join(dstFilePath,filename)
								print("New file path:%s"%(dstFilePath))
								shutil.copy(os.path.join(FullSourcePath,filename), dstFilePath)
				print("--------------------------------------------")

def execute():
	#FullSourcePath=input("Input the source folder path:")
	#FullTargetPath=input("Input the target foder path:")
	FullSourcePath="/home/asixsw/Wales_Test/source/"
	FullTargetPath="/home/asixsw/Wales_Test/target/"
	file_walk(FullSourcePath,FullTargetPath)

if __name__=="__main__":
	print("Start to Comic sort")
	execute()

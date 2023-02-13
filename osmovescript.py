import os
import shutil

def making_folders(target_path):
    
    if not os.path.exists(target_path+"\\"+'Images'):
        os.mkdir(target_path+"\\"+'Images')
    
    if not os.path.exists(target_path+"\\"+'Pdf files'):
        os.mkdir(target_path+"\\"+'Pdf files')
    
    if not os.path.exists(target_path+"\\"+'Text Files'):
        os.mkdir(target_path+"\\"+'Text Files')


target_path="D:\\New random for script"

making_folders(target_path)

image_holder=['.png','.jpeg','.gif','.jpg']
pdf_holder=['.pdf']
video_holder=['.mp4']
txt_holder=['.txt']

#print(os.listdir(target_path))

for files in os.listdir(target_path):
    filename,extension=os.path.splitext(files)
    #print(files)
    if extension.lower() in image_holder:
        #print((target_path+'\\'+'Images'+'\\'+files))
        #print(os.path.exists(target_path+'\\'+files))
        #target_path+'\\'+files
        shutil.move(target_path+'\\'+files,target_path+'\\'+'Images'+'\\'+files) # first argument source ar second destination
    elif extension in pdf_holder:
        shutil.move(target_path+'\\'+files,target_path+'\\'+'Pdf files'+'\\'+files)
    elif extension in video_holder:
        shutil.move(target_path+'\\'+files,target_path+'\\'+'Videos'+'\\'+files)
    elif extension in txt_holder:
        shutil.move(target_path+'\\'+files,target_path+'\\'+'Text Files'+'\\'+files)

        
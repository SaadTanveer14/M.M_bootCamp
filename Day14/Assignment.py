import os


# Assignment
# Read all files from the directory
# if file is text file then add the file to  text list
# if file is excel file then add the file to excel list
# if file is pdf file then add the file to pdf list
# if file is image file then add the file to  image list
# if the file is zip then skip and print that file is not in the required format.

directory = 'C:/Users/HP/Downloads/'
text_files = []
excel_files = []
pdf_files = []
image_files = []


print(directory)
files_and_dirs = os.listdir(directory)
# Filter only the files from the list
files_list = [file for file in files_and_dirs if os.path.isfile(os.path.join(directory, file))]

for file in files_list:
    ext = file.split('.')

    if ext[-1] == 'txt':
        text_files.append(file)
    elif ext[-1] == 'pdf':
        pdf_files.append(file)
    elif ext[-1] == 'jpg' or ext[-1] == 'jpeg' or ext[-1] == 'png':
        image_files.append(file)
    elif ext[-1] == 'csv' or ext[-1] == 'xlsx':
        excel_files.append(file)
    else:
        print("'", file, "'", "file is not in the required format")

print(pdf_files)
print(text_files)
print(excel_files)
print(image_files)

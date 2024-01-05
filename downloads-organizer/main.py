import os 
import shutil
import pathlib

file_format = {
	"Web": [".html5", ".html", ".htm", ".xhtml"], 
	
    "Zdjęcia": [".jpeg", ".jpg", ".tiff", ".gif",
                ".bmp", ".png", ".bpg", "svg",".heif", ".psd"], 
	
    "Wideo": [".avi", ".mkv",".flv", ".wmv",
              ".mov", ".mp4", ".webm", ".vob", 
              ".mng",".qt", ".mpg", ".mpeg", ".3gp"], 
	
    "Dokumenty": [".oxps", ".epub", ".pages", ".docx",
                 ".txt", ".pdf", ".doc", ".fdf",
                 ".ods",".odt", ".pwi", ".xsn",
                 ".xps", ".dotx", ".docm", ".dox",
                 ".rvg", ".rtf", ".rtfd", ".wpd", 
                 ".xls", ".xlsx", ".ppt","pptx"], 
	
    "Pliki skompresowane": [".a", ".ar", ".cpio", ".iso", 
                   ".tar", ".gz", ".rz", ".7z",
                   ".dmg", ".rar", ".xar", ".zip"], 
	
    "Audio": [".aac", ".aa", ".aac", ".dvf",
              ".m4a", ".m4b", ".m4p", ".mp3",
              ".msv", "ogg", "oga", ".raw", 
              ".vox", ".wav", ".wma"], 
} 

file_types = list(file_format.keys())
file_formats = list(file_format.values())

path = r"C:\Users\matus\Downloads"

files = os.listdir(path)
os.chdir(path)

if not "Inne" in file_types:
    file_types.append("Inne")

for type in file_types:
    if not os.path.isdir(type):
        os.mkdir(type)
        
        
for file in files:
    file_path = str(pathlib.Path(file))
    name, extension = os.path.splitext(file)
    if extension == '':
        print(f'{file} has no extension.')
        continue
    else:
        for formats in file_formats:
            if extension in formats:
                try:
                    folder = file_types[file_formats.index(formats)]
                    shutil.move(file_path, folder)
                except OSError as e:
                    print(f'Error moving {file}: {e}')
            else:
                try:
                    folder = file_types[6]
                    shutil.move(file_path, folder)
                except OSError as e:
                    print(f'Error moving {file}: {e}')
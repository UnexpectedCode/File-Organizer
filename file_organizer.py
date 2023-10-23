# Import the modules os and shutil, which are used to work with files and directories
import os
import shutil

# Define some tuples with the extensions of the audio, video and image files that you want to organize
audio = (".3ga", ".aac", ".ac3", ".aif", ".aiff",
         ".alac", ".amr", ".ape", ".au", ".dss",
         ".flac", ".flv", ".m4a", ".m4b", ".m4p",
         ".mp3", ".mpga", ".ogg", ".oga", ".mogg",
         ".opus", ".qcp", ".tta", ".voc", ".wav",
         ".wma", ".wv")

video = (".webm", ".MTS", ".M2TS", ".TS", ".mov",
         ".mp4", ".m4p", ".m4v", ".mxf")

img = (".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp", ".png",
       ".gif", ".webp", ".svg", ".apng", ".avif")

exe = ('.exe',)
rar = ('.rar','.zip')

# Define some functions that return True if the file is an audio, video or image file, and False if it is not
def is_audio(file):
    # Use the function os.path.splitext to get the extension of the file
    # Compare the extension with the tuple audio and return the result
    return os.path.splitext(file)[1] in audio
def is_video(file):
    # The same as the previous function, but with the tuple video
    return  os.path.splitext(file)[1] in video
def is_image(file):
    # The same as the previous function, but with the tuple img
    return os.path.splitext(file)[1] in img

def is_exe(file):
    # The same as the previous function, but with the tuple exe
    return os.path.splitext(file)[1] in exe
def is_rar(file):
    # The same as the previous function, but with the tuple rar
    return os.path.splitext(file)[1] in rar

# Change the current directory to the user's downloads folder
os.chdir(r"")

# Loop through all the files in the folder with a for loop
for file in os.listdir():
    # Use the defined functions to check if the file is an audio, video or image file
    if is_audio(file):
        # If it is an audio file, use the function shutil.move to move it to the audio folder in the user's desktop
        shutil.move(file, os.path.join(r'', file))
    elif is_video(file):
        # If it is a video file, do the same but with the video folder
        shutil.move(file, os.path.join(r'', file))
    elif is_image(file):
        # If it is an image file, do the same but with the images folder
        shutil.move(file, os.path.join(r'', file))
    elif is_rar(file):
        # If it is a compressed file, do the same but with the rar folder
        shutil.move(file, os.path.join(r'', file))
    elif is_exe(file):
        # If it is an executable file, do the same but with the exe folder
        shutil.move(file, os.path.join(r'', file))
    else:
        # If it is none of the previous types, move it to the unclassified folder
        shutil.move(file, os.path.join(r'', file))


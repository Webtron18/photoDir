import os
from Tkinter import *
import tkFileDialog
import tkMessageBox
import shutil
import glob
from importClass import *

def status_update(type, textInfo):
    lblStatus['text'] = '%s' % (textInfo)
    if type == 'warn':
        lblStatus['fg'] = 'Orange'
    if type == 'suc':
        lblStatus['fg'] = 'DarkGreen'
    if type == 'error':
        lblStatus['fg'] = 'Red'
    if type == 'debug':
        lblStatus['fg'] = 'Purple'

def create_directory():
   # Check to see if location exists
   # Create the folder structure if so
   directory = "/Users/justin/Pictures/%s/" % (e1.get())
   if not os.path.isdir(directory):
       os.makedirs(directory)
       os.makedirs(directory+"Photos/")
       os.makedirs(directory+"Photos/RAW")
       os.makedirs(directory+"Photos/Final")
       os.makedirs(directory+"Videos/")
       os.makedirs(directory+"Videos/RAW")
       os.makedirs(directory+"Videos/Final")
       os.makedirs(directory+"Videos/Working")
       os.makedirs(directory+"Videos/Working/Music")
       os.makedirs(directory+"Videos/Working/Sounds")
       os.makedirs(directory+"Videos/Working/Project")
       status_update('suc', 'Directory: %s has been created' % (directory))
   else:
       status_update('error','Directory cannot be empty')

def move_files():
    # Move the files from /Pictures/Staging to the location above
    # Sorts by file type
    #   .jpg/.cr2 -> photos/RAW
    #   .mp4/.mov -> videos/RAW
    if e1.get() != "" and cFiles.numFiles() > 0:
        dest_photo = "/Users/justin/Pictures/%s/Photos/RAW/" % (e1.get())
        dest_video = "/Users/justin/Pictures/%s/Videos/RAW/" % (e1.get())
        for file in cFiles.getFiles():
            #if file contains jpg or csr
            file = file.name.lower()
            # tkMessageBox.showinfo('debug;', "files: %s" % (file))
            if '.jpg' in file or '.cr2' in file:
                # in future use shutil.move once it works
                shutil.copy(file, dest_photo)
                status_update('suc', 'Files have been successfully moved')
            #else if file contains mp4 or move
            elif '.mov' in file or '.mp4' in file or '.m4v' in file:
                # in future use shutil.move once it works
                shutil.copy(file, dest_video)
                status_update('suc', 'Files have been successfully moved')
            else:
                status_update('error', 'File type not found')
        # Empty the queue after copying
        cFiles.clearQueue()
    else:
        if e1.get() == "":
            status_update("error","Directory name cannot be blank.")
        elif cFiles.numFiles() <= 0:
            status_update("error","No media has been selected.")
        else:
            status_update('error', 'Unknown error has occurred')

def find_files():
    cFiles.setFiles(tkFileDialog.askopenfiles(parent=master,mode='rb',title='Choose a file'))
    if cFiles.numFiles() <= 0:
        status_update('warn', 'No files have been selected')
        btn_move['state'] = 'disabled'
    else:
        status_update('suc',"Media loaded in queue: %s file(s)" % cFiles.numFiles())
        btn_move['state'] = 'normal'
    # pass

master = Tk()
# Creates header label #
Label(master, text="Enter the Name of the Album").grid(row=0, columnspan=2)
# Create status label #
lblStatus = Label(master, text="Status:")
lblStatus.grid(row=2, column=0, sticky=W)

# Textbox for Album name #
e1 = Entry(master)
e1.grid(row=1, column=0)

# Buttons on the form #
btn_quit = Button(master, text='Quit', command=master.quit)
btn_quit.grid(row=3, column=0, sticky=W, pady=4)
btn_create = Button(master, text='Create', command=create_directory)
btn_create.grid(row=1, column=1, pady=4)
btn_move = Button(master, text='Move Files', state=NORMAL, command=move_files)
btn_move.grid(row=3, column=1, sticky=W, pady=4)
btn_find = Button(master, text='Find Files', command=find_files)
btn_find.grid(row=3, column=0, sticky=E, pady=4)

#Finds removable media in /Volumes/
#Excludes certain volumes
vols = os.walk('/Volumes/').next()[1]
exclude = set(['OS X Base System','Macintosh HD','DROPME','TIMEMACHINE'])
vols[:] = [d for d in vols if d not in exclude]

# Create a Tkinter variable
tkvar = StringVar(master)

# Create the dropdown menu and label #
popupMenu = OptionMenu(master, tkvar, *vols)
Label(master, text="Media:  ").grid(row = 4, column = 0, sticky=W)
popupMenu.grid(row = 5, column=0, columnspan=2, sticky=EW)

# on change dropdown value
def change_dropdown(*args):
    print( tkvar.get() )

# link function to change dropdown
tkvar.trace('w', change_dropdown)

# Test area for the class stuff #
cFiles = importFiles()

mainloop( )

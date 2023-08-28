import random
import os
import shutil
import fnmatch
import glob
import time

gameDir = r"None"
gfxDir = r"\GFX"
sfxDir = r"\SFX"
backupDir = r"\BACKUP"

gfxJpg = []
gfxPng = []
sfxOgg = []

def randomize(useGfx, useSfx):
    gfxJpgOriginal = []
    gfxPngOriginal = []
    sfxOggOriginal = []
    if useGfx == True:
        for file in glob.iglob(gameDir + backupDir + gfxDir + r"\**\*.jpg", recursive=True):
            gfxJpgOriginal.append(str(file))
        for file in glob.iglob(gameDir + backupDir + gfxDir + r"\**\*.png", recursive=True):
            gfxPngOriginal.append(str(file))
        for i in gfxJpgOriginal:
            nextFile = gfxJpg[random.randrange(0, len(gfxJpg) - 1)]
            shutil.copy2(i, str(nextFile), follow_symlinks=False)
            print(nextFile)
        #for i in gfxPngOriginal: # disabled due to constant crashing
            #nextFile = gfxPng[random.randrange(0, len(gfxPng) - 1)]
            #shutil.copy2(i, str(nextFile), follow_symlinks=False)
            #print(nextFile)

    if useSfx == True:
        for file in glob.iglob(gameDir + backupDir + sfxDir+ r"\**\*.ogg", recursive=True):
            sfxOggOriginal.append(str(file))
        for i in sfxOggOriginal:
            nextFile = sfxOgg[random.randrange(0, len(sfxOgg) - 1)]
            shutil.copy2(i, str(nextFile), follow_symlinks=False)
            print(nextFile)

def findFiles(useGfx, useSfx):
    if not os.path.exists(gameDir + backupDir):
        print("Creating backup of files under " + gameDir + backupDir + "...")
        shutil.copytree(gameDir + gfxDir, gameDir + backupDir + gfxDir, dirs_exist_ok=True)
        shutil.copytree(gameDir + sfxDir, gameDir + backupDir + sfxDir, dirs_exist_ok=True)
        print("Backup created!")
        time.sleep(3)
    else:
        print("Backup already exists, beginning randomization process...")
        time.sleep(3)
    if useGfx == True:
        for file in glob.iglob(gameDir + gfxDir + r"\**\*.jpg", recursive=True):
            gfxJpg.append(str(file))
        #for file in glob.iglob(gameDir + gfxDir + r"\**\*.png", recursive=True): # disabled due to constant crashing
            #gfxPng.append(str(file))
    if useSfx == True:
        for file in glob.iglob(gameDir + sfxDir+ r"\**\*.ogg", recursive=True):
            sfxOgg.append(str(file))
    randomize(useGfx, useSfx)

def startup():
    global gameDir
    if gameDir == r"None":
        gameDirInput = input("Specify the game directory: ")
        gameDir = gameDirInput
        if not os.path.isfile(gameDir + r"\SCP - Containment Breach.exe"):
            gameDir = r"None"
            print("That isn't the correct directory")
            time.sleep(1)
            startup()
            return
    global rndSelectionInput
    rndSelectionInput = input("Specify a number (1 to 3). Please note that the randomization of .PNG files has been disabled due to the game failing to load every fucking time, thanks Blitz3D.\n1: Randomize GFX and SFX\n2: Randomize GFX\n3: Randomize SFX\n")
    match int(rndSelectionInput):
        case 1:
            findFiles(True, True)
        case 2:
            findFiles(True, False)
        case 3:
            findFiles(False, True)
        case _:
            print("Error, not a valid integer! Use 1 to 3 only!\n")
            startup()

startup()




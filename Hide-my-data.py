import os
import shutil


def banner():
    print("--------Amir Shamsi---------")
    print("Visit me in GitHub!--->EmirShamsi")
banner()
cmd = input("Enter 1 if you wanna extract hidden files or 2 to hide your files behind a picture: ")
while cmd not in ("1", "2"):
    cmd = input("Please enter a valuable input!: ")
if cmd == "2":
    try:
        info_FN = input("Enter Your Info Directory FullName: ")
        pic_FN = input("Enter Your Picture FullName: ")
        shutil.make_archive("zipped_info", 'zip', info_FN)
        command = "cmd /c " + '"' + "Copy /b " + pic_FN + " + " + "zipped_info.zip" + " " + "Hidden.jpg" + '"'
        os.system(command)
        os.remove("zipped_info.zip")
        print("Your file created az an image! the name is", "Hidden.jpg")
    except:
        print("can't find information directory or picture!")
else:
    hdn_file = input("Enter Your Picture FullName: ")
    os.rename(hdn_file, hdn_file.split(".")[0] + ".zip")
    print("Now ready your zipped info:", hdn_file.split(".")[0] + ".zip")


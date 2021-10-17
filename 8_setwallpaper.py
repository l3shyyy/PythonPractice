import ctypes
import shutil
import os
import urllib.request
import string

url = "https://picsum.photos/3840/2160"
save_dir = os.environ['USERPROFILE']+"/Pictures/"
path = os.path.join(save_dir, "temp_js7y7uihq01283as7h")

def main():
    get_image()
    set_background()

def get_image():
    os.mkdir(path)
    urllib.request.urlretrieve(url, path + "/temp.jpg")
    
def set_background():
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path + "/temp.jpg" , 0)

def remove_temp():
    os.remove(path + "/temp.jpg")
    os.rmdir(path)

if __name__ == '__main__':
    main()
    remove_temp()
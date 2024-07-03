import pytsk3
import sys

class FileSystem:
    def __init__(self, image, offset=0):
        self.img_info = pytsk3.Img_Info(image)
        self.fs_info = pytsk3.FS_Info(self.img_info, offset)

    def list_directory(self, path):
        directory = self.fs_info.open_dir(path)
        for entry in directory:
            if entry.info.name.name.decode('utf-8') not in [".", ".."]:
                print(entry.info.name.name.decode('utf-8'))

if __name__ == "__main__":
    image = "/path/to/disk/image"
    fs = FileSystem(image)
    fs.list_directory('/')

# small-big
# this file has one class to work with folder and files

# methods:
#   place: this method is very impotent it updates your address
#   go: this method will send you to your raw address (it's not useful for you)
#   read_everything: this method read all folders and files are in your address
#   open: this method is just for open folder and add it to your address
#   back: sometimes you want to back to last folder this times this method help you
#   read_file_name: sometimes you need the name of files in your address not folders
#   read_not_hidden: some files are hidden if you don't want to read this files instead of
#   ude read_file_name you must use this method
#   read_folder_name: if you need the folders name in your address here you are!
#   back_all: when you start to work with this class you have a address after that you
#   have new address if you want to go back to your first address this method help you

import os


class Reader:
    def __init__(self):
        self.address = self.place()
        self.first = self.address
        self.files = []
        self.folder = []
        self.not_hidden_file = []

    def place(self):
        # read where are you now
        self.address = os.getcwd()
        return self.address

    def go(self, address):
        # go to the address that you choose
        os.chdir(address)
        self.place()

    def read_everything(self):
        # read files and folder  in your place
        files = os.listdir(self.place())
        return files

    def open(self, folder_name):
        # open folders
        self.address = os.path.join(self.address, folder_name)
        self.go(self.address)

    def back(self):
        # A folder goes back
        self.address = self.address.split('\\')
        del self.address[len(self.address)-1]
        self.go('\\'.join(self.address))
        self.place()

    def read_file_name(self):
        # read the file and hidden files in the address (not folders)
        for i in self.read_everything():
            if '.' in i:
                self.files.append(i)
        return self.files

    def read_not_hidden(self):
        # read the files that they are not hidden
        for i in self.read_file_name():
            if i[0] != '.':
                self.not_hidden_file.append(i)
        return self.not_hidden_file

    def read_folder_name(self):
        self.read_file_name()
        all_files_folder = self.read_everything()
        for i in all_files_folder:
            if i not in self.files:
                self.folder.append(i)
        return self.folder

    def back_all(self):
        # back to the start point
        self.go(self.first)


if __name__ == "__main__":
    obj = Reader()
    print('now you are in', obj.place())
    print('every file in this place are: ', ', '.join(obj.read_everything()))
    print('files not hidden: ', ', '.join(obj.read_not_hidden()))
    print('all folders: ', ', '.join(obj.read_folder_name()))

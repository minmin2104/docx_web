import zipfile
import os


class Docx:
    def __init__(self, path):
        self.path = path
        self.docx_file = None
        self.zip_obj = None
        self.__prepare()

    def __prepare(self):
        if not zipfile.is_zipfile(self.path) and self.path.split(".")[-1] != "docx":
            raise Exception("File must be .docx file")
            
        try:
            self.docx_file = open(self.path, "rb")
        except OSError as e:
            raise OSError(e)
            
        self.zip_obj = zipfile.ZipFile(self.docx_file)

    def get_document_file(self):
        return self.zip_obj.open("word/document.xml")

    def extract_docx_content(self, dirname):
        self.zip_obj.extractall(os.path.join(os.getcwd(), dirname))

    def dump_docx_content(self):
        name_list = self.zip_obj.namelist()
        for name in name_list:
            print(name)

    def clean_up(self):
        self.docx_file.close()


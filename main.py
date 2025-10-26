import zipfile
import sys, os


class App:
    def __init__(self, path):
        self.path = path
        self.docx_file = None
        self.zip_obj = None
        self.__prepare()
        self.main()

    def main(self):
        self.dump_docx_content()
        self.extract_docx_content("extracted")

    def __prepare(self):
        if not zipfile.is_zipfile(self.path) and self.path.split(".")[-1] != "docx":
            print("Target file is not a docx file", file=sys.stderr)
            sys.exit(1)
            
        try:
            self.docx_file = open(self.path, "rb")
        except OSError as e:
            print(e, file=sys.stderr)
            sys.exit(1)

        self.zip_obj = zipfile.ZipFile(self.docx_file)

    def extract_docx_content(self, dirname):
        self.zip_obj.extractall(os.path.join(os.getcwd(), dirname))

    def dump_docx_content(self):
        name_list = self.zip_obj.namelist()
        for name in name_list:
            print(name)
        
    def clean_up(self):
        self.docx_file.close()


if __name__ == "__main__":
    app = App("./test_file.docx")
    app.clean_up()


from docx import Docx
import sys


class App:
    def __init__(self, path):
        self.path = path
        self.docx = None
        
        try:
            self.docx = Docx(self.path)
        except Exception as e:
            print(e, file=sys.stderr)
            sys.exit(1)
            
        self.main()
        self.__clean_up()

    def main(self):
        self.docx.dump_docx_content()

    def __clean_up(self):
        self.docx.clean_up()

if __name__ == "__main__":
    app = App("./test_file.docx")


from docx_html_parser import DocHtmlParser
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
        self.docx.extract_docx_content("extracted")
        # self.docx.dump_docx_content()
        f_doc_xml = self.docx.get_document_file()
        doc_html_parser = DocHtmlParser(f_doc_xml)
        f_doc_xml.close()

    def __clean_up(self):
        self.docx.clean_up()

if __name__ == "__main__":
    app = App("./test_file.docx")


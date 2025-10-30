from xml import sax
import sys


class DocHtmlContentHandler(sax.handler.ContentHandler):
    def __init__(self):
        self.curr_data = ""
        self.content = ""
    
    def get_content(self):
        return self.content

    def startDocument(self):
        self.content += """
        <body>
        <div id="main">
        """

    def startElement(self, name, attr):
        print(name)

    def characters(self, content):
        self.curr_data += content

    def endElement(self, name):
        if self.curr_data:
            print(f"{self.curr_data}")
        print(f"/{name}")
        self.curr_data = ""

    def endDocument(self):
        self.content += """
        </div>
        </body>
        """


class DocHtmlParser:
    def __init__(self, doc_xml):
        self.doc_xml = doc_xml
        self.content = ""
        doc_html_content_handler = DocHtmlContentHandler()
        try:
            sax.parse(self.doc_xml, doc_html_content_handler)
        except sax.SAXParseException as e:
            print(e, file=sys.stderr)

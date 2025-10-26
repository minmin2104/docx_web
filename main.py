import zipfile


class App:
    def __init__(self, path):
        self.path = path

    def dump_docx_content(self):
        with open(self.path, "rb") as f:
            zip = zipfile.ZipFile(f)
            name_list = zip.namelist()
            for name in name_list:
                print(name)


if __name__ == "__main__":
    app = App("./test_file.docx")
    app.dump_docx_content()

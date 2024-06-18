class MSSQL:
    def __init__(self, login_info):
        self.svn, self.dtbn, self.uid, self.pwd = map(str.strip, login_info)


def read_txt(file_name):

    with open(file_name + '.txt') as f:
        return f.readlines()

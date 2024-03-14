class NotDirError(Exception):
    def __str__(self):
        return "Directory not exists"

import os


class TaskListModel():

    def __init__(self, file_path, file_encoding):
        self.file_path = file_path
        self.file_encoding = file_encoding

    def get_all(self):
        tasks = list()
        if os.path.exists(self.file_path):
            with open(self.file_path, "r", encoding=self.file_encoding) as f:
                tasks = f.readlines()
        return tasks

    def get_first(self):
        task = ""
        if os.path.exists(self.file_path):
            with open(self.file_path, "r", encoding=self.file_encoding) as f:
                task = f.readline()
        return task

    def add(self, new_task):
        if os.path.exists(self.file_path):
            mode = "a"
        else:
            mode = "w"
        with open(self.file_path, mode, encoding=self.file_encoding) as f:
            f.write(new_task + "\r\n")
            f.flush()

    def remove_all(self):
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def remove_first(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as f:
                lines = f.readlines()
            with open("task_list.txt", "w") as f:
                f.writelines(lines[1:])

    def ask_premission(self):

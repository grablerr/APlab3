import os

class Iterator1_txt:
    def __init__(self, dataset: str, name: str, path: str):
        self.path = ""
        self.name = ""
        self.names = []
        self.limit = 0
        self.counter = 0
        self.dataset = ""
        self.init(dataset, name, path)

    def __next__(self):
        if self.counter < self.limit:
            self.counter += 1
            return self.names[self.counter - 1]
        elif self.counter == self.limit:
            self.counter = 0
            self.counter += 1
            return self.names[self.counter - 1]

    def init(self, dataset: str, name: str, path: str):
        if not path.startswith(r"C:\Users\Professional\Desktop\SSAU\PP\APlabs\APlab3"):
            path = os.path.join(r"C:\Users\Professional\Desktop\SSAU\PP\APlabs\APlab3", path)
        if not os.path.exists(path):
            raise FileNotFoundError("The specified path does not exist.")
        self.path = path
        self.name = name

        self.names = os.listdir(os.path.join(dataset, self.path, self.name))

        self.names = [i for i in self.names if i.endswith('.txt')]

        self.limit = len(self.names)
        self.counter = 0

    def clear(self):
        self.counter = 0

    def setName(self, name: str):
        self.init(self.dataset, name, self.path)

    def getName(self):
        print(self.name)

    def setPath(self, path: str):
        self.init(self.dataset, self.name, path)
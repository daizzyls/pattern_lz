from abc import ABC, abstractmethod


class FileSystem(ABC):
    @abstractmethod
    def display(self, indent: int = 0):
        pass


class File(FileSystem):

    def __init__(self, name: str, size_bytes: int):
        self.name = name
        self.size = size_bytes

    def display(self, indent: int = 0):
        spaces = "    " * indent
        print(f"{spaces} {self.name}, {self.size} б")


class Folder(FileSystem):

    def __init__(self, name: str):
        self.name = name
        self._children: list[FileSystem] = []

    def add(self, node: FileSystem):
        self._children.append(node)

    def display(self, indent: int = 0):
        spaces = "    " * indent
        print(f"{spaces} {self.name}")
        for child in self._children:
            child.display(indent + 1)


def main():
    readme = File("README.md", 2048)
    main_py = File("main.py", 5120)
    config = File("config.json", 1024)

    logo = File("logo.png", 40960)
    icon = File("icon.svg", 3072)

    report = File("report.pdf", 1048576)
    data = File("data.csv", 204800)

    src = Folder("src")
    src.add(main_py)
    src.add(config)

    images = Folder("images")
    images.add(logo)
    images.add(icon)

    docs = Folder("docs")
    docs.add(report)
    docs.add(data)

    project = Folder("project")
    project.add(readme)
    project.add(src)
    project.add(images)
    project.add(docs)

    print("Содержимое проекта:")
    project.display()

if __name__ == "__main__":
    main()

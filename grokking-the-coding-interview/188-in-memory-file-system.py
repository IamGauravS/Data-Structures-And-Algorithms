class Directory:
    def __init__(self):
        self.child = {}
        self.isFile = False
        self.content = ""

class FileSystem:
    def __init__(self):
        self.root = Directory()

    def ls(self, path):
        node = self.root
        if path != "/":
            for part in path.split("/")[1:]:
                node = node.child[part]
            if node.isFile:
                return [part]
        return sorted(node.child.keys())

    def mkdir(self, path):
        node = self.root
        for part in path.split("/")[1:]:
            if part not in node.child:
                node.child[part] = Directory()
            node = node.child[part]

    def add_content_to_file(self, file_path, content):
        node = self.root
        parts = file_path.split("/")[1:]
        for part in parts:
            if part not in node.child:
                node.child[part] = Directory()
            node = node.child[part]
        node.isFile = True
        node.content += content

    def read_content_from_file(self, file_path):
        node = self.root
        for part in file_path.split("/")[1:]:
            node = node.child[part]
        return node.content
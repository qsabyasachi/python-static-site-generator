from pathlib import Path

class Site(object):
    """docstring for Site."""

    def __init__(self, source,dest):
        self.source = Path(source)
        self.dest = Path(dest)

    def create_dir(self,path):
        directory = self.dest / path.relative_to(self.source)
        directory.mkdir(parents = True, exist_ok = True)

    def build():
        self.dest.mkdir(parents = True, exist_ok = True)
        for path in self.source.glob("*"):
            if path.is_dir():
                path.create_dir()

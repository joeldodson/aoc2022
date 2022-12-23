""" filesystem.py 
Contains classs to track information for a directory.
"""
from __future__ import annotations

from dataclasses import dataclass

@dataclass
class NameSize:
    name: str
    size: int


class Directory:
    def __init__(self, parent: Directory, name: str):
        self.parent: Directory = parent
        self.name:str = name 
        """
        this path hackery is to ensure the root path is '/'
        then to add a '/' between the components of the path 
        """
        self.path:str = '/' 
        if parent:
            self.path = parent.path + '/' + self.name
        self.size: int = 0 
        self.directories: list[Directory] = [] 
        self.files: list[NameSize] = []

    def calculateSize(self) -> int:
        self.size = sum([f.size for f in self.files] + [d.calculateSize() for d in self.directories])
        return self.size 

    def addFile(self, name: str, size: int) -> None:
##         print(f"adding file {name} to directory {self.name}")
        if name in [f.name for f in self.files]:
            print(f"name: {name} is already in the directory {self.name}")
        else:
            self.files.append(NameSize(name, size))

    def addDirectory(self, dir: Directory) -> None:
        ## print(f"adding directory {dir.name} to directory {self.name}")
        self.directories.append(dir)
    
    def __repr__(self):
        return f"{self.name}, {self.size:n} - {len(self.files)} files, {len(self.directories)} directories"


## end of file 
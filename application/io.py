from typing import List
from .helpers import Arguments
from .models import Record
from .database import Database
from datetime import datetime


class File:
    def __init__(self, parameters: Arguments) -> None:
        self.arguments = parameters
        self.contents: List[str] = []
        self.__parsed_contents: List[str] = []

    @property
    def contents(self):
        with open(self.arguments.input, "r") as fin:
            return [i.strip() for i in fin.readlines() if i.strip()]

    @contents.setter
    def contents(self, contents_: any) -> None:
        pass

    def parse(self):
        self.__parsed_contents = Parser(self).output

    def dump(self):
        if self.arguments.save_to == "file":
            with open(self.arguments.output, "w") as fout:
                for line in [",".join(i) for i in self.__parsed_contents]:
                    fout.write("{}\n".format(line))
        else:
            db = Database(self.arguments.output)
            objects = []
            for entry in self.__parsed_contents:
                t, s, d = entry
                t = datetime.strptime(t, "%H:%M:%S.%f").time()
                objects.append(Record(timestamp=t, source=s, destination=d))
            db.add(objects)

    def __repr__(self):
        return ",".join(self.contents)

    def __len__(self):
        return len(self.contents)

    def __getitem__(self, item):
        return self.contents[item]


class Parser:
    def __init__(self, file: File) -> None:
        self.output = [(lambda v: [v[0], v[2], v[4][:-1]])(i.split(" ")) for i in file.contents if "IP" in i]


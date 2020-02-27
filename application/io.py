from typing import List
from .helpers import Arguments
from .models import Record
from .database import Database
from datetime import datetime
import re


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
                t, s, sp, d, dp = entry
                t = datetime.strptime(t, "%H:%M:%S.%f").time()
                objects.append(Record(timestamp=t, source=s, sport=sp, destination=d, dport=dp))
            db.add(objects)

    def __repr__(self):
        return ",".join(self.contents)

    def __len__(self):
        return len(self.contents)

    def __getitem__(self, item):
        return self.contents[item]


class Parser:
    def __init__(self, file: File) -> None:
        self.output = [(lambda v:
                        [v[0],
                         (lambda t: ".".join(t.split(".")[:-1]))(v[2]),
                         (lambda t: t.split(".")[-1])(v[2]),
                         (lambda t: ".".join(t.split(".")[:-1]))((lambda x: x[:-1])(v[4])),
                         (lambda t: t.split(".")[-1])((lambda x: x[:-1])(v[4]))])(i.split(" "))
                       for i in file.contents if "IP" in i and not ("173.194." in i and "10.0.2." in i)]

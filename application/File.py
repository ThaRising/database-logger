from typing import List


class File:
    def __init__(self, path: str) -> None:
        self.path: str = path
        self.contents: List[str] = []

    @property
    def contents(self):
        with open(self.path, "r") as fin:
            return list(map(lambda v: v.strip(), fin.readlines()))

    @contents.setter
    def contents(self, contents_: any) -> None:
        pass

    def dump_to_db(self):
        pass

    def parse_to_file(self, output_path: str):
        pass

    def __repr__(self):
        return ",".join(self.contents)

    def __len__(self):
        with open(self.path, "r") as fout:
            return len(fout.readlines())

    def __getitem__(self, item):
        return self.contents[item]

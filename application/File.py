from typing import List


class File:
    def __init__(self, in_path: str, out_path: str) -> None:
        self.in_path: str = in_path
        self.out_path = out_path
        self.contents: List[str] = []

    @property
    def contents(self):
        with open(self.in_path, "r") as fin:
            return [i.strip() for i in fin.readlines() if i.strip()]

    @contents.setter
    def contents(self, contents_: any) -> None:
        pass

    def dump_to_db(self, output_path: str):
        pass

    def dump_to_file(self, content):
        with open(self.out_path, "w") as fout:
            for i in content:
                fout.write("{}\n".format(i))

    def __repr__(self):
        return ",".join(self.contents)

    def __len__(self):
        return len(self.contents)

    def __getitem__(self, item):
        return self.contents[item]


class Parser:
    def __init__(self, file: File) -> None:
        self.content = file.contents
        self.information = [(lambda v: [v[0], v[2], v[4][:-1]])(i.split(" ")) for i in self.content if "IP" in i]


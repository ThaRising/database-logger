# !python3
# -*- coding: utf-8 -*-

from getopt import getopt, GetoptError
from typing import List, Optional
from dataclasses import dataclass
import sys
from application.File import File
import os


@dataclass
class Arguments:
    """
    input: Contains the path to the input logfile
    output: Contains the path to either the output logfile or database, determined by the save_to option
    save_to: Specifies wether to save the parsed results in a file or a database, options are either "file" or "db"
    """
    input: str = None
    output: str = None
    save_to: str = None

    @property
    def input(self) -> any:
        return self._input

    @input.setter
    def input(self, input_: any) -> None:
        if not type(input_) == str:
            raise TypeError("Input parameter must be a string")
        if not os.path.isfile(input_):
            raise FileNotFoundError(f"No logfile found in path: {input_}")
        self._input = input_

    @property
    def output(self) -> str:
        return self._output

    @output.setter
    def output(self, output_: any) -> None:
        if not type(output_) == str:
            raise TypeError("Output parameter must be a string")
        if os.path.isfile(output_):
            raise FileExistsError(f"Path: {output_} would not be a new file")
        self._output = output_

    @property
    def save_to(self) -> str:
        return self._save_to

    @save_to.setter
    def save_to(self, save_to_: str) -> None:
        if not save_to_ == ("file" or "db"):
            raise ValueError("save_to parameter must be either 'file' or 'db'")
        self._save_to = save_to_

    def __len__(self) -> int:
        return len(self.__dict__)


def main(argv_: List[str]) -> Optional[Arguments]:
    """
    Processes arguments from the console.

    :param argv_: Contains a list of string arguments passed on from sys.argv, excluding the first one,
     which is the filename of the application entry point
    :return: Dataclass instance of Argument, containing the parsed values from command line
    :except GetoptError If either -i or -o parameters are missing
    """
    try:
        opts, args = (lambda o: ([v for k, v in o[0]], [v for k, v in o[1]]))(getopt(argv_, "i:o:", ["saveto="]))
        args = args[0] if args else None
        return Arguments(input=opts[0], output=opts[1], save_to="file" if not args else args)
    except GetoptError:
        print("main.py -i <inputfile_path> -o <outputfile_path> [--saveto <file|db>]")
        sys.exit(2)


if __name__ == "__main__":
    params = main(sys.argv[1:])
    print(File(params.input))

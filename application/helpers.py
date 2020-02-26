from getopt import getopt, GetoptError
from typing import List, Optional
from dataclasses import dataclass
import sys
import os


@dataclass
class Arguments:
    """
    input: Contains the path to the input logfile
    output: Contains the path to either the output logfile or database, determined by the save_to option
    save_to: Specifies wether to save the parsed results in a file or a database, options are either "file" or "db"
    """
    input: str = None
    save_to: str = None
    output: str = None

    @property
    def input(self) -> any:
        return self._input

    @input.setter
    def input(self, input_: any) -> None:
        if not type(input_) == str:
            raise TypeError("-i parameter must be a string")
        if not os.path.isfile(input_):
            raise FileNotFoundError(f"No logfile found in path: {input_}")
        self._input = input_

    @property
    def save_to(self) -> str:
        return self._save_to

    @save_to.setter
    def save_to(self, save_to_: List[str]) -> None:
        if not save_to_[1] in ("file", "db"):
            raise ValueError("saveto parameter must be either 'file' or 'db'")
        self._save_to = save_to_[1]

    @property
    def output(self) -> str:
        return self._output

    @output.setter
    def output(self, output_: any) -> None:
        if not type(output_) == str:
            raise TypeError("-o parameter must be a string")
        if os.path.isfile(output_) and self.save_to != "db":
            raise FileExistsError(f"Path: {output_} would not be a new file")
        self._output = output_

    def __len__(self) -> int:
        return len(self.__dict__)


def get_console_args(argv_: List[str]) -> Optional[Arguments]:
    """
    Processes arguments from the console.

    :param argv_: Contains a list of string arguments passed on from sys.argv, excluding the first one,
     which is the filename of the application entry point
    :return: Dataclass instance of Argument, containing the parsed values from command line
    :except GetoptError If either -i or -o parameters are missing
    """
    try:
        ((*_, infile), (*_, outfile), *opts), _ = getopt(argv_, "i:o:", ["saveto="])
        return Arguments(input=infile, output=outfile, save_to="file" if not opts else opts[0])
    except GetoptError:
        print("main.py -i <inputfile_path> -o <output_path> [--saveto=<file|db>]")
        return sys.exit(2)

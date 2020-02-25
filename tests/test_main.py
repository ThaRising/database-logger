import unittest
import subprocess
from pathlib import Path


class TestConsoleParameters(unittest.TestCase):
    def setUp(self):
        self.entry = Path(__file__)
        self.entry = self.entry.parent.parent
        self.entry = self.entry / "main.py"

        self.good_fin = Path(__file__)
        self.good_fin = self.good_fin.parent.parent
        self.good_fin = self.good_fin / "requirements.txt"

    def run_entry(self, params_: list) -> tuple:
        run_parameters = ["python", str(self.entry)]
        for i in params_:
            run_parameters.append(i)
        result = subprocess.run(run_parameters, capture_output=True)
        return result.stdout, result.stderr

    def test_parameters(self):
        # Test with invalid parameter
        self.assertIsNotNone(self.run_entry(["-l", "bwc"])[1])
        # Test with one correct, one missing parameter
        self.assertIsNotNone(self.run_entry(["-i", str(self.good_fin)])[1])
        self.assertIsNotNone(self.run_entry(["-o", "bwc"])[1])
        # Test with both required options but invalid path
        self.assertIsNotNone(self.run_entry(["-i", "bwc", "-o", "test"])[1])
        # Test with correct options and check wether the error output is empty
        self.assertIsNotNone(self.run_entry(["-i", str(self.good_fin), "-o", "test"])[1])


if __name__ == '__main__':
    unittest.main()

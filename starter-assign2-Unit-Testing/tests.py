import unittest
from boggle_solver import Boggle

class TestSuite_Normal_Cases(unittest.TestCase):
    def test_Normal_case_4x4(self):
        grid = [["T", "W", "Y", "R"], ["E", "N", "P", "H"],["G", "Z", "Qu", "R"],["O", "N", "T", "A"]]
        dictionary = ["art", "ego", "gent", "get", "net", "new", "newt", "prat", "pry", "qua", "quart", "quartz", "rat", "tar", "tarp", "ten", "went", "wet"]
        mygame = Boggle(grid, dictionary)
        solution = sorted([x.upper() for x in mygame.getSolution()])
        expected = sorted(["ART", "GENT", "GET", "NET", "NEW", "NEWT", "PRAT", "PRY", "QUA", "QUART", "QUARTZ", "RAT", "TAR", "TARP", "TEN", "WENT", "WET"])
        self.assertEqual(expected, solution)

class TestSuite_Edge_Cases(unittest.TestCase):
    def test_SquareGrid_case_1x1(self):
        grid = [["A"]]
        dictionary = ["A", "B", "C"]
        mygame = Boggle(grid, dictionary)
        solution = sorted([x.upper() for x in mygame.getSolution()])
        expected = []  # No valid words of at least 3 letters
        self.assertEqual(expected, solution)

    def test_EmptyGrid_case_0x0(self):
        grid = [[]]
        dictionary = ["HELLO", "THERE", "GENERAL", "KENOBI"]
        mygame = Boggle(grid, dictionary)
        solution = sorted([x.upper() for x in mygame.getSolution()])
        expected = []  # No valid words can be found
        self.assertEqual(expected, solution)

    def test_LargerGrid_case_5x5(self):
        grid = [["A", "B", "C", "D", "E"],
                ["F", "G", "H", "I", "J"],
                ["K", "L", "M", "N", "O"],
                ["P", "Q", "R", "S", "T"],
                ["U", "V", "W", "X", "Y"]]
        dictionary = ["abcde", "fghij", "klmno", "pqrst", "uvwxyz", "afkp", "zvwr"]
        mygame = Boggle(grid, dictionary)
        solution = sorted([x.upper() for x in mygame.getSolution()])
        expected = sorted(["ABCDE", "FGHIJ", "KLMNO", "PQRST", "AFKP"])
        self.assertEqual(expected, solution)

class TestSuite_Special_Cases(unittest.TestCase):
    def test_GridWithQu(self):
        grid = [["Qu", "E", "S", "T"],
                ["I", "N", "O", "P"],
                ["R", "U", "C", "K"],
                ["T", "A", "R", "S"]]
        dictionary = ["quest", "quip", "ruck", "quaint", "quart", "quarks"]
        mygame = Boggle(grid, dictionary)
        solution = sorted([x.upper() for x in mygame.getSolution()])
        expected = sorted(["QUEST", "QUIP", "RUCK", "QUART", "QUARKS"])
        self.assertEqual(expected, solution)

    def test_IncompleteDictionary(self):
        grid = [["A", "B", "C"],
                ["D", "E", "F"],
                ["G", "H", "I"]]
        dictionary = ["abc", "abdhi", "abi", "ef", "cfi"]
        mygame = Boggle(grid, dictionary)
        solution = sorted([x.upper() for x in mygame.getSolution()])
        expected = sorted(["ABC", "ABDHI", "ABI", "CFI", "EF"])
        self.assertEqual(expected, solution)

class TestSuite_Complex_Cases(unittest.TestCase):
    def test_Complex_case_overlap(self):
        grid = [["T", "W", "Y", "R"], ["E", "N", "P", "H"],["G", "Z", "Qu", "R"],["O", "N", "T", "A"]]
        dictionary = ["ten", "tent", "went", "wentz", "tentar", "tarp", "pry", "quartz", "rat"]
        mygame = Boggle(grid, dictionary)
        solution = sorted([x.upper() for x in mygame.getSolution()])
        expected = sorted(["TEN", "TENT", "WENT", "TENTAR", "TARP", "PRY", "QUARTZ", "RAT"])
        self.assertEqual(expected, solution)

if __name__ == '__main__':
    unittest.main()

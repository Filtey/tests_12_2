import runner_and_tournament as runner
import unittest
from pprint import pprint


class RunnerTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = runner.Runner("Усэйн", 10)
        self.runner2 = runner.Runner("Андрей", 9)
        self.runner3 = runner.Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for key, value in cls.all_results.items():
            print(f"{key} : {value}")

    def test_zabeg1(self):
        tournament = runner.Tournament(90, self.runner1, self.runner3)
        self.__class__.all_results = tournament.start()
        self.assertTrue(self.all_results[1], "Усейн")

    def test_zabeg2(self):
        tournament = runner.Tournament(90, self.runner2, self.runner3)
        self.__class__.all_results = tournament.start()
        self.assertTrue(self.all_results[1], "Андрей")

    def test_zabeg3(self):
        tournament = runner.Tournament(90, self.runner1, self.runner2, self.runner3)
        self.__class__.all_results = tournament.start()
        self.assertTrue(self.all_results[1], "Усэйн")

if __name__ == "__main__":
    unittest.main()

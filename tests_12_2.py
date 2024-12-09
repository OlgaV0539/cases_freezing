import unittest
from runner_and_tournament import Runner, Tournament
import functools


is_frozen = True


def skip_if_frozen(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        if is_frozen:
            raise unittest.SkipTest('Тесты в этом кейсе заморожены')
        return fn(*args, **kwargs)
    return wrapper


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.runner1 = Runner("Усэйн", 10)
        self.runner2 = Runner("Андрей", 9)
        self.runner3 = Runner("Ник", 3)

    @classmethod
    def tearDownClass(cls):
        for key in sorted(cls.all_results.keys()):
            print(f'{key}: {cls.all_results[key]}')

    @skip_if_frozen
    def test_race1(self):
        tournament = Tournament(90, self.runner1, self.runner3)
        results = tournament.start()
        self.all_results.update(results)
        self.assertTrue(list(results.values())[-1] == "Ник")
        self.__class__.all_results[len(self.__class__.all_results) + 1] = results
        last_runner = results[max(results.keys())]
        self.assertTrue(last_runner == "Ник")

    @skip_if_frozen
    def test_race2(self):
        tournament = Tournament(90, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results.update(results)
        self.assertTrue(list(results.values())[-1] == "Ник")
        self.__class__.all_results[len(self.__class__.all_results) + 1] = results
        last_runner = results[max(results.keys())]
        self.assertTrue(last_runner == "Ник")

    @skip_if_frozen
    def test_race3(self):
        tournament = Tournament(90, self.runner1, self.runner2, self.runner3)
        results = tournament.start()
        self.all_results.update(results)
        self.assertTrue(list(results.values())[-1] == "Ник")
        self.__class__.all_results[len(self.__class__.all_results) + 1] = results
        last_runner = results[max(results.keys())]
        self.assertTrue(last_runner == "Ник")

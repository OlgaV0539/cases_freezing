import unittest
from runner import Runner
import functools


is_frozen = False


def skip_if_frozen(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        if is_frozen:
            raise unittest.SkipTest('Тесты в этом кейсе заморожены')
        return fn(*args, **kwargs)
    return wrapper


class RunnerTest(unittest.TestCase):
    @skip_if_frozen
    def test_walk(self):
        runner = Runner("My_walker")
        for _ in range(10):
            runner.walk()
        self.assertEqual(runner.distance, 50)

    @skip_if_frozen
    def test_run(self):
        runner = Runner("My_runner")
        for _ in range(10):
            runner.run()
        self.assertEqual(runner.distance, 100)

    @skip_if_frozen
    def test_challenge(self):
        runner1 = Runner("Your_walker")
        runner2 = Runner("Your_runner")
        for _ in range(10):
            runner1.walk()
            runner2.run()
        self.assertNotEqual(runner1.distance, runner2.distance)


if __name__ == "__main__":
    unittest.main()

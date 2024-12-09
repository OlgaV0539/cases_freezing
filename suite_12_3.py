import unittest
import tests_12_1
import tests_12_2


runner_and_tournamentST = unittest.TestSuite()
runner_and_tournamentST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_1.RunnerTest))
runner_and_tournamentST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_2.TournamentTest))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(runner_and_tournamentST)

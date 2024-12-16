import tests_12_3
import unittest

run_test = unittest.TestSuite()
run_test.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
run_test.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)

runner.run(run_test)
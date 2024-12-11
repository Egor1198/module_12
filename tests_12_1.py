import Runner
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        name = Runner.Runner("Ivan")
        for i in range(10):
            name.walk()
        self.assertEqual(name.distance, 50)

    def test_run(self):
        name = Runner.Runner("Petro")
        for i in range(10):
            name.run()
        self.assertEqual(name.distance, 100)

    def test_challenge(self):
        name_1 = Runner.Runner("Ivan")
        name_2 = Runner.Runner("Petro")
        for i in range(10):
            name_1.walk()
            name_2.run()
        self.assertNotEqual(name_1.distance, name_2.distance)


if __name__ == "__main__":
    unittest.main()

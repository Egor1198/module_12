import Runner
import Tournament
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def test_walk(self):
        name = Runner.Runner("Ivan")
        for i in range(10):
            name.walk()
        self.assertEqual(name.distance, 50)

    @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def test_run(self):
        name = Runner.Runner("Petro")
        for i in range(10):
            name.run()
        self.assertEqual(name.distance, 100)

    @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def test_challenge(self):
        name_1 = Runner.Runner("Ivan")
        name_2 = Runner.Runner("Petro")
        for i in range(10):
            name_1.walk()
            name_2.run()
        self.assertNotEqual(name_1.distance, name_2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.Usein = Tournament.Runner("Usein", 10)
        self.Andrey = Tournament.Runner("Andrey", 9)
        self.Nik = Tournament.Runner("Nik", 3)

    @classmethod
    def tearDownClass(cls):
        for result in cls.all_results.values():
            show_result = {}
            for place, runner in result.items():
                show_result[place] = runner.name
            # print(show_result)

    @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def test_run_1(self):
        self.tournament = Tournament.Tournament(90, self.Usein, self.Nik)
        self.all_results = self.tournament.start()
        last_runner_name = self.all_results[max(self.all_results.keys())].name
        self.assertTrue(last_runner_name == "Nik")
        TournamentTest.all_results[1] = self.all_results

    @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def test_run_2(self):
        self.tournament_2 = Tournament.Tournament(90, self.Andrey, self.Nik)
        self.all_results = self.tournament_2.start()
        last_runner_name = self.all_results[max(self.all_results.keys())].name
        self.assertTrue(last_runner_name == "Nik")
        TournamentTest.all_results[2] = self.all_results

    @unittest.skipIf(is_frozen == True, "Тесты в этом кейсе заморожены")
    def test_run_3(self):
        self.tournament_3 = Tournament.Tournament(90, self.Usein, self.Andrey, self.Nik)
        self.all_results = self.tournament_3.start()
        last_runner_name = self.all_results[max(self.all_results.keys())].name
        self.assertTrue(last_runner_name == 'Nik')
        TournamentTest.all_results[3] = self.all_results


if __name__ == '__main__':
    unittest.main()

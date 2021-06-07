import unittest

def tournamentwinner(competitions, results):
    finalwinner = ""
    scorecard = {}
    if len(competitions) != len(results):
        return 'Missing Information'
    for count, competition in enumerate(competitions):
        hometeam, awayteam = competition
        winner = hometeam if results[count] == 1 else awayteam
        if winner in scorecard:
            scorecard[winner] += 1
        else:
            scorecard[winner] = 0
        if finalwinner not in scorecard or scorecard[winner] > scorecard[finalwinner]:
            finalwinner = winner
        print(scorecard)
    return finalwinner


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        competitions = [["HTML", "C#"], ["C#", "Python"], ["Python", "HTML"]]
        results = [0, 0, 1]
        expected = "Python"
        self.assertEqual(tournamentwinner(competitions,results), expected)


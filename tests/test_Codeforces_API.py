from src.Codeforces_API import ProblemCodeforcesAPI

problems_API = ProblemCodeforcesAPI()


def test_get_problems_1():
    assert problems_API.get_problems() != None


def test_get_problems_2():
    assert problems_API.get_problems_statistics() != None


def test_get_problems_3():
    assert problems_API.get_consolidation_lists() != None


def test_get_vacancies_3(problems_fix, problems_stat_fix, consolidation_lists_fix):
    assert type(problems_fix) == list
    assert type(problems_stat_fix) == list
    assert type(consolidation_lists_fix) == list

import unittest
from coding_checks import assess,validate
class CodingChecksTests(unittest.TestCase):
    def test_correct_and_incorrect_code(self):
        cases=[{'args':[[1,2,3]],'expected':6},{'args':[[]],'expected':0}]
        self.assertTrue(assess('def solve(xs):\n    return sum(xs)',cases)['passed'])
        self.assertFalse(assess('def solve(xs):\n    return 9',cases)['passed'])
    def test_small_power_allowed_large_power_blocked(self):
        self.assertTrue(assess('def solve(x):\n    return x ** 2',[{'args':[3],'expected':9}])['passed'])
        self.assertFalse(assess('def solve(x):\n    return x ** 1000000',[{'args':[3],'expected':9}])['passed'])
    def test_forbidden_access(self):
        for code in ['import os\ndef solve(x): return x','def solve(x):\n return open("secret")','def solve(x):\n return x.__class__','def solve(x):\n return eval(x)','@print\ndef solve(x): return x']:
            self.assertFalse(assess(code,[{'args':[1],'expected':1}])['passed'])
    def test_loop_is_stopped(self):
        result=assess('def solve(x):\n    while True: pass',[{'args':[1],'expected':1}]);self.assertFalse(result['passed'])
    def test_large_allocation_is_stopped(self):
        result=assess('def solve(x):\n    return [0] * (1000000 * 1000000)',[{'args':[1],'expected':1}]);self.assertFalse(result['passed'])
if __name__=='__main__':unittest.main()

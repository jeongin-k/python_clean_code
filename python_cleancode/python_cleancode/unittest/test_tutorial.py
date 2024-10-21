import unittest

# 첫 번째 테스트 클래스
class TestMathOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(1 + 1, 2)

    def test_subtract(self):
        self.assertEqual(5 - 3, 2)

# 두 번째 테스트 클래스
class TestStringOperations(unittest.TestCase):
    def test_upper(self):
        self.assertEqual('hello'.upper(), 'HELLO')

    def test_isupper(self):
        self.assertTrue('HELLO'.isupper())
        self.assertFalse('Hello'.isupper())

# TestSuite를 사용해 테스트를 그룹화
if __name__ == '__main__':
    # 빈 TestSuite 생성
    suite = unittest.TestSuite()

    # 개별 테스트 케이스 추가
    suite.addTest(TestMathOperations('test_add'))
    suite.addTest(TestMathOperations('test_subtract'))
    suite.addTest(TestStringOperations('test_upper'))
    suite.addTest(TestStringOperations('test_isupper'))

    # TestRunner를 사용하여 suite 실행
    runner = unittest.TextTestRunner()
    runner.run(suite)


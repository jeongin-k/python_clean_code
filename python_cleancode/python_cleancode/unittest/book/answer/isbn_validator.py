from abc import ABC, abstractmethod

class ISBN(ABC):
    """ISBN에 대한 추상 클래스 (공통 기능 정의)"""

    def __init__(self, isbn):
        self.isbn = isbn.replace("-", "").replace(" ", "")

    @abstractmethod
    def is_valid(self):
        """유효성 검사를 위한 추상 메서드"""
        pass

    @staticmethod
    def create(isbn):
        """팩토리 메서드: ISBN 문자열 길이에 따라 ISBN10 또는 ISBN13 인스턴스를 생성"""
        if len(isbn.replace("-", "").replace(" ", "")) == 10:
            return ISBN10(isbn)
        elif len(isbn.replace("-", "").replace(" ", "")) == 13:
            return ISBN13(isbn)
        else:
            raise ValueError("Invalid ISBN length")

class ISBN10(ISBN):
    """ISBN-10 형식에 대한 검증을 수행하는 클래스"""

    def is_valid(self):
        if len(self.isbn) != 10:
            return False

        total = 0
        for i in range(9):
            if not self.isbn[i].isdigit():
                return False
            total += int(self.isbn[i]) * (10 - i)

        # 마지막 자리가 'X'일 수 있음 (10으로 간주)
        if self.isbn[9] == 'X':
            total += 10
        elif self.isbn[9].isdigit():
            total += int(self.isbn[9])
        else:
            return False

        return total % 11 == 0

class ISBN13(ISBN):
    """ISBN-13 형식에 대한 검증을 수행하는 클래스"""

    def is_valid(self):
        if len(self.isbn) != 13 or not self.isbn.isdigit():
            return False

        total = 0
        for i in range(12):
            if i % 2 == 0:
                total += int(self.isbn[i]) * 1
            else:
                total += int(self.isbn[i]) * 3

        # 체크섬 계산
        checksum = (10 - (total % 10)) % 10
        return checksum == int(self.isbn[12])

class ISBNValidator:
    """ISBN의 유효성을 검사하는 인터페이스 클래스"""

    def __init__(self, isbn):
        self.isbn_instance = ISBN.create(isbn)

    def is_valid(self):
        """해당 ISBN이 유효한지 검사"""
        return self.isbn_instance.is_valid()

if __name__ == '__main__':
    # 사용 예시
    isbn_validator_10 = ISBNValidator("0-306-40615-2")
    print(isbn_validator_10.is_valid())  # True

    isbn_validator_13 = ISBNValidator("978-0-306-40615-7")
    print(isbn_validator_13.is_valid())  # True


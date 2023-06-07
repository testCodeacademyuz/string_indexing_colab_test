import requests

class CheckSolution:
    def __init__(self, task_name):
        self.task_name = task_name
        self.url = "https://calms.pythonanywhere.com/reporter/attempt/"
    
    def checking(self, tg_username, isSolved, homework_name):
        data = {
            "tg_username": tg_username,
            "assignment_name": homework_name,
            "task_name": self.task_name,
            "is_correct": isSolved
        }
        # print(data)
        response = requests.post(self.url, data=data)
        if isSolved:
            # done emoji
            print("✅ Accepted")
        else:
            # fail emoji
            print("❌ Failed")
        if response.status_code == 404:
            print("❗️ Siz kursga ro'yxatga olinmagansiz!")
        elif response.status_code == 201:
            print("❕ Sizning javobingiz muvafaqqiyatli yuborildi!")
        else:
            print("Sizda noma'lum xatolik yuz berdi!")

# input a = "code" ouput "c", input "hi" output "h", input "happy" output "h"
class TaskOne(CheckSolution):
    def __init__(self, task_name, homework_name):
        self.homework_name = homework_name
        super().__init__(task_name)

    def test_case_1(self, solution):
        try:
            answer = solution("code")
        except:
            answer = None
        expected = "c"

        result = {
            "input": ['code'],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def test_case_2(self, solution):
        try:
            answer = solution("hi")
        except:
            answer = None
        expected = "h"

        result = {
            "input": ['hi'],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def test_case_3(self, solution):
        try:
            answer = solution("happy")
        except:
            answer = None
        expected = "h"

        result = {
            "input": ['happy'],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def test_case_4(self, solution):
        try:
            answer = solution("a")
        except:
            answer = None
        expected = "a"

        result = {
            "input": ['a'],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def test_case_5(self, solution):
        try:
            answer = solution("string")
        except:
            answer = None
        expected = "s"

        result = {
            "input": ['string'],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def check(self, solution, tg_username):
        test_cases = [
            self.test_case_1(solution),
            self.test_case_2(solution),
            self.test_case_3(solution),
            self.test_case_4(solution),
            self.test_case_5(solution)
        ]
        isSolved = [test_case["isSolved"] for test_case in test_cases]
        isSolved = all(isSolved)
        self.checking(tg_username, isSolved, self.homework_name)
        print("-" * 50)

        for i, test_case in enumerate(test_cases, 1):
            emoji = "✅" if test_case["isSolved"] else "❌"
            print(f"{emoji} Test: {i}")
            if not test_case["isSolved"]:
                print(f"Input: {', '.join(test_case['input'])}")
                print(f"Output: {test_case['answer']}")
                print(f"Expected: {test_case['expected']}\n")


# input a = "code" ouput "o", input "hi" output "i", input "happy" output "p"
class TaskTwo(CheckSolution):
    def __init__(self, task_name, homework_name):
        self.homework_name = homework_name
        super().__init__(task_name)

    def test_case_1(self, solution):
        try:
            answer = solution("code")
        except:
            answer = None
        expected = "o"

        result = {
            "input": ['code'],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def test_case_2(self, solution):
        try:
            answer = solution("hi")
        except:
            answer = None
        expected = "i"

        result = {
            "input": ['hi'],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def test_case_3(self, solution):
        try:
            answer = solution("happy")
        except:
            answer = None
        expected = "a"

        result = {
            "input": ['happy'],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def test_case_4(self, solution):
        try:
            answer = solution("good")
        except:
            answer = None
        expected = "o"

        result = {
            "input": ['good'],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def test_case_5(self, solution):
        try:
            answer = solution("string")
        except:
            answer = None
        expected = "t"

        result = {
            "input": ['string'],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def check(self, solution, tg_username):
        test_cases = [
            self.test_case_1(solution),
            self.test_case_2(solution),
            self.test_case_3(solution),
            self.test_case_4(solution),
            self.test_case_5(solution)
        ]
        isSolved = [test_case["isSolved"] for test_case in test_cases]
        isSolved = all(isSolved)
        self.checking(tg_username, isSolved, self.homework_name)
        print("-" * 50)

        for i, test_case in enumerate(test_cases, 1):
            emoji = "✅" if test_case["isSolved"] else "❌"
            print(f"{emoji} Test: {i}")
            if not test_case["isSolved"]:
                print(f"Input: {', '.join(test_case['input'])}")
                print(f"Output: {test_case['answer']}")
                print(f"Expected: {test_case['expected']}\n")

# input a = "code" ouput "e", input "hi" output "i", input "happy" output "y"
class TaskThree(CheckSolution):
    def __init__(self, task_name, homework_name):
        self.homework_name = homework_name
        super().__init__(task_name)

    def test_case_1(self, solution):
        try:
            answer = solution("code")
        except:
            answer = None
        expected = "e"

        result = {
            "input": ['code'],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def test_case_2(self, solution):
        try:
            answer = solution("hi")
        except:
            answer = None
        expected = "i"

        result = {
            "input": ['hi'],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def test_case_3(self, solution):
        try:
            answer = solution("happy")
        except:
            answer = None
        expected = "y"

        result = {
            "input": ['happy'],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def test_case_4(self, solution):
        try:
            answer = solution("a")
        except:
            answer = None
        expected = "a"

        result = {
            "input": ['a'],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def test_case_5(self, solution):
        answer = solution("string")
        expected = "g"

        result = {
            "input": ['string'],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def check(self, solution, tg_username):
        test_cases = [
            self.test_case_1(solution),
            self.test_case_2(solution),
            self.test_case_3(solution),
            self.test_case_4(solution),
            self.test_case_5(solution)
        ]
        isSolved = [test_case["isSolved"] for test_case in test_cases]
        isSolved = all(isSolved)
        self.checking(tg_username, isSolved, self.homework_name)
        print("-" * 50)

        for i, test_case in enumerate(test_cases, 1):
            emoji = "✅" if test_case["isSolved"] else "❌"
            print(f"{emoji} Test: {i}")
            if not test_case["isSolved"]:
                print(f"Input: {', '.join(test_case['input'])}")
                print(f"Output: {test_case['answer']}")
                print(f"Expected: {test_case['expected']}\n")
    
# input a = "computer" output "com", input a = "python" output "pyt", input a = "coding" output "cod"
class TaskFour(CheckSolution):
    def __init__(self, task_name, homework_name):
        self.homework_name = homework_name
        super().__init__(task_name)

    def test_case_1(self, solution):
        try:
            answer = solution("computer")
        except:
            answer = None
        expected = "com"

        result = {
            "input": ['computer'],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def test_case_2(self, solution):
        try:
            answer = solution("python")
        except:
            answer = None
        expected = "pyt"

        result = {
            "input": ['python'],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def test_case_3(self, solution):
        try:
            answer = solution("coding")
        except:
            answer = None
        expected = "cod"

        result = {
            "input": ['coding'],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def test_case_4(self, solution):
        try:
            answer = solution("a")
        except:
            answer = None
        expected = "a"

        result = {
            "input": ['a'],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def test_case_5(self, solution):
        answer = solution("string")
        expected = "str"

        result = {
            "input": ['string'],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def check(self, solution, tg_username):
        test_cases = [
            self.test_case_1(solution),
            self.test_case_2(solution),
            self.test_case_3(solution),
            self.test_case_4(solution),
            self.test_case_5(solution)
        ]
        isSolved = [test_case["isSolved"] for test_case in test_cases]
        isSolved = all(isSolved)
        self.checking(tg_username, isSolved, self.homework_name)
        print("-" * 50)

        for i, test_case in enumerate(test_cases, 1):
            emoji = "✅" if test_case["isSolved"] else "❌"
            print(f"{emoji} Test: {i}")
            if not test_case["isSolved"]:
                print(f"Input: {', '.join(test_case['input'])}")
                print(f"Output: {test_case['answer']}")
                print(f"Expected: {test_case['expected']}\n")

# input a = "code007" output 3, input a = "python3.10" output 3, input a = "23ab12w" output 4, input "coding" output 0
class TaskFive(CheckSolution):
    def __init__(self, task_name, homework_name):
        self.homework_name = homework_name
        super().__init__(task_name)

    def test_case_1(self, solution):
        try:
            answer = solution("code007")
        except:
            answer = None
        expected = 3

        result = {
            "input": ['code007'],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def test_case_2(self, solution):
        try:
            answer = solution("python3.10")
        except:
            answer = None
        expected = 3

        result = {
            "input": ['python3.10'],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def test_case_3(self, solution):
        try:
            answer = solution("23ab12w")
        except:
            answer = None
        expected = 4

        result = {
            "input": ['23ab12w'],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def test_case_4(self, solution):
        try:
            answer = solution("coding")
        except:
            answer = None
        expected = 0

        result = {
            "input": ['coding'],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def check(self, solution, tg_username):
        test_cases = [
            self.test_case_1(solution),
            self.test_case_2(solution),
            self.test_case_3(solution),
            self.test_case_4(solution)
        ]
        isSolved = [test_case["isSolved"] for test_case in test_cases]
        isSolved = all(isSolved)
        self.checking(tg_username, isSolved, self.homework_name)
        print("-" * 50)

        for i, test_case in enumerate(test_cases, 1):
            emoji = "✅" if test_case["isSolved"] else "❌"
            print(f"{emoji} Test: {i}")
            if not test_case["isSolved"]:
                print(f"Input: {', '.join(test_case['input'])}")
                print(f"Output: {test_case['answer']}")
                print(f"Expected: {test_case['expected']}\n")

# input a = "hi" output "hi", input a = "python" output "pn", input a = "coding" output "cg"
class TaskSix(CheckSolution):
    def __init__(self, task_name, homework_name):
        self.homework_name = homework_name
        super().__init__(task_name)

    def test_case_1(self, solution):
        try:
            answer = solution("hi")
        except:
            answer = None
        expected = "hi"

        result = {
            "input": ['hi'],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def test_case_2(self, solution):
        try:
            answer = solution("python")
        except:
            answer = None
        expected = "pn"

        result = {
            "input": ['python'],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def test_case_3(self, solution):
        try:
            answer = solution("coding")
        except:
            answer = None
        expected = "cg"

        result = {
            "input": ['coding'],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def check(self, solution, tg_username):
        test_cases = [
            self.test_case_1(solution),
            self.test_case_2(solution),
            self.test_case_3(solution)
        ]
        isSolved = [test_case["isSolved"] for test_case in test_cases]
        isSolved = all(isSolved)
        self.checking(tg_username, isSolved, self.homework_name)
        print("-" * 50)

        for i, test_case in enumerate(test_cases, 1):
            emoji = "✅" if test_case["isSolved"] else "❌"
            print(f"{emoji} Test: {i}")
            if not test_case["isSolved"]:
                print(f"Input: {', '.join(test_case['input'])}")
                print(f"Output: {test_case['answer']}")
                print(f"Expected: {test_case['expected']}\n")

# input a = "python", n = 2 output "t", input a = "coding", n = 3 output "i", input a = "python", n = 0 output "p", input a = "hi", n = 5 output False
class TaskSeven(CheckSolution):
    def __init__(self, task_name, homework_name):
        self.homework_name = homework_name
        super().__init__(task_name)

    def test_case_1(self, solution):
        try:
            answer = solution("python", 2)
        except:
            answer = None
        expected = "t"

        result = {
            "input": ['python', "2"],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def test_case_2(self, solution):
        try:
            answer = solution("coding", 3)
        except:
            answer = None
        expected = "i"

        result = {
            "input": ['coding', "3"],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def test_case_3(self, solution):
        try:
            answer = solution("python", 0)
        except:
            answer = None
        expected = "p"

        result = {
            "input": ['python', "0"],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def test_case_4(self, solution):
        try:
            answer = solution("hi", 5)
        except:
            answer = None
        expected = False

        result = {
            "input": ['hi', "5"],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def check(self, solution, tg_username):
        test_cases = [
            self.test_case_1(solution),
            self.test_case_2(solution),
            self.test_case_3(solution),
            self.test_case_4(solution)
        ]
        isSolved = [test_case["isSolved"] for test_case in test_cases]
        isSolved = all(isSolved)
        self.checking(tg_username, isSolved, self.homework_name)
        print("-" * 50)

        for i, test_case in enumerate(test_cases, 1):
            emoji = "✅" if test_case["isSolved"] else "❌"
            print(f"{emoji} Test: {i}")
            if not test_case ["isSolved"]:
                print(f"Input: {', '.join(test_case['input'])}")
                print(f"Output: {test_case['answer']}")
                print(f"Expected: {test_case['expected']}\n")

# input a = "*args", output 0, input a = "12*12" output 2, input a = "python" output False
class TaskEight(CheckSolution):
    def __init__(self, task_name, homework_name):
        self.homework_name = homework_name
        super().__init__(task_name)

    def test_case_1(self, solution):
        try:
            answer = solution("*args")
        except:
            answer = None
        expected = 0

        result = {
            "input": ['*args'],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def test_case_2(self, solution):
        try:
            answer = solution("12*12")
        except:
            answer = None
        expected = 2

        result = {
            "input": ['12*12'],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def test_case_3(self, solution):
        try:
            answer = solution("python")
        except:
            answer = None
        expected = False

        result = {
            "input": ['python'],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def check(self, solution, tg_username):
        test_cases = [
            self.test_case_1(solution),
            self.test_case_2(solution),
            self.test_case_3(solution)
        ]
        isSolved = [test_case["isSolved"] for test_case in test_cases]
        isSolved = all(isSolved)
        self.checking(tg_username, isSolved, self.homework_name)
        print("-" * 50)

        for i, test_case in enumerate(test_cases, 1):
            emoji = "✅" if test_case["isSolved"] else "❌"
            print(f"{emoji} Test: {i}")
            if not test_case ["isSolved"]:
                print(f"Input: {', '.join(test_case['input'])}")
                print(f"Output: {test_case['answer']}")
                print(f"Expected: {test_case['expected']}\n")

# input "107" output 107, input "code" output -1, input "4.1" output -1
class TaskNine(CheckSolution):
    def __init__(self, task_name, homework_name):
        self.homework_name = homework_name
        super().__init__(task_name)

    def test_case_1(self, solution):
        try:
            answer = solution("107")
        except:
            answer = None
        expected = 107

        result = {
            "input": ['107'],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def test_case_2(self, solution):
        try:
            answer = solution("code")
        except:
            answer = None
        expected = -1

        result = {
            "input": ['code'],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def test_case_3(self, solution):
        try:
            answer = solution("4.1")
        except:
            answer = None
        expected = -1

        result = {
            "input": ['4.1'],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def check(self, solution, tg_username):
        test_cases = [
            self.test_case_1(solution),
            self.test_case_2(solution),
            self.test_case_3(solution)
        ]
        isSolved = [test_case["isSolved"] for test_case in test_cases]
        isSolved = all(isSolved)
        self.checking(tg_username, isSolved, self.homework_name)
        print("-" * 50)

        for i, test_case in enumerate(test_cases, 1):
            emoji = "✅" if test_case["isSolved"] else "❌"
            print(f"{emoji} Test: {i}")
            if not test_case ["isSolved"]:
                print(f"Input: {', '.join(test_case['input'])}")
                print(f"Output: {test_case['answer']}")
                print(f"Expected: {test_case['expected']}\n")

# input "10233" output 9, input "10102" output 4, input "10000" output 1
class TaskTen(CheckSolution):
    def __init__(self, task_name, homework_name):
        self.homework_name = homework_name
        super().__init__(task_name)

    def test_case_1(self, solution):
        try:
            answer = solution("10233")
        except:
            answer = None
        expected = 9

        result = {
            "input": ['10233'],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def test_case_2(self, solution):
        try:
            answer = solution("10102")
        except:
            answer = None
        expected = 4

        result = {
            "input": ['10102'],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def test_case_3(self, solution):
        try:
            answer = solution("10000")
        except:
            answer = None
        expected = 1

        result = {
            "input": ['10000'],
            "answer": answer,
            "expected": expected,
            "isSolved": answer == expected
        }
        return result
    
    def check(self, solution, tg_username):
        test_cases = [
            self.test_case_1(solution),
            self.test_case_2(solution),
            self.test_case_3(solution)
        ]
        isSolved = [test_case["isSolved"] for test_case in test_cases]
        isSolved = all(isSolved)
        self.checking(tg_username, isSolved, self.homework_name)
        print("-" * 50)

        for i, test_case in enumerate(test_cases, 1):
            emoji = "✅" if test_case["isSolved"] else "❌"
            print(f"{emoji} Test: {i}")
            if not test_case ["isSolved"]:
                print(f"Input: {', '.join(test_case['input'])}")
                print(f"Output: {test_case['answer']}")
                print(f"Expected: {test_case['expected']}\n")

q1 = TaskOne("index01", "string_indexing")
q2 = TaskTwo("index02", "string_indexing")
q3 = TaskThree("index03", "string_indexing")
q4 = TaskFour("index04", "string_indexing")
q5 = TaskFive("index05", "string_indexing")
q6 = TaskSix("index06", "string_indexing")
q7 = TaskSeven("index07", "string_indexing")
q8 = TaskEight("index08", "string_indexing")
q9 = TaskNine("index09", "string_indexing")
q10 = TaskTen("index10", "string_indexing")
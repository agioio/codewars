"""The first input array is the key to the correct answers to an exam, like ["a", "a", "b", "d"]. The second one contains a student's submitted answers.

The two arrays are not empty and are the same length. Return the score for this array of answers, giving +4 for each correct answer, -1 for each incorrect answer, and +0 for each blank answer, represented as an empty string (in C the space character is used).

If the score < 0, return 0.
    """

import unittest

def check_exam(arr1,arr2):
    score = 0
    for first,sec in zip(arr1,arr2):
        if first == "" or sec == "":
            score += 0
        elif first == sec:
            score += 4
        else:
            score -= 1
    
    return score if score > 0 else 0


class TestCheckExam(unittest.TestCase):

    def test_exam_check(self):
        self.assertEqual(check_exam(["a", "a", "b", "b"], ["a", "c", "b", "d"]), 6)
        self.assertEqual(check_exam(["a", "a", "c", "b"], ["a", "a", "b",  ""]), 7)
        self.assertEqual(check_exam(["a", "a", "b", "c"], ["a", "a", "b", "c"]), 16)
        self.assertEqual(check_exam(["b", "c", "b", "a"], ["",  "a", "a", "c"]), 0)

if __name__ == "__main__":
    unittest.main()
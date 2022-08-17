from requests import get

class Questions():
    def __init__(self, num_qs, difficulty):
        url = f'https://opentdb.com/api.php?amount={num_qs}&difficulty={difficulty}&type=multiple'
        response = get(url).json()
        self.response = response['results']
    def get_questions(self):
        self.qs = []
        for result in self.response:
            self.qs.append(result['question'])
        return self.qs
    def get_correct_answer(self):
        self.ans = []
        for result in self.response:
            self.ans.append(result['correct_answer'])
        return self.ans
    def get_inc_answer(self):
        self.inc_ans = []
        for result in self.response:
            self.inc_ans.append(result['incorrect_answers'])
        return self.inc_ans
    def get_difficulty(self):
        self.diffs = []
        for result in self.response:
            self.diffs.append(result['difficulty'])
        return self.diffs
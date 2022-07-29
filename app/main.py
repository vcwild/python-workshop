from utils.aggregate import aggregate_responses
from utils.parse_csv import read_questions
from constants import QUESTIONS_PATH

questions = read_questions(QUESTIONS_PATH)
responses = aggregate_responses(questions)

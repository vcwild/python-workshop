from constants import QUESTIONS_PATH
from utils.aggregate import aggregate_responses
from utils.parse_csv import read_questions

# from IPython import embed; embed() # enable this to use the ipython shell


def run():
    questions = read_questions(QUESTIONS_PATH)
    responses = aggregate_responses(questions)
    from IPython import embed

    embed()


if __name__ == "__main__":
    run()

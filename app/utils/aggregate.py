from typing import Counter


def remove_unaggregated_fields(
    counter: Counter, question: dict, responses: dict, threshold: int
):
    """Removes data that could not be aggregated."""
    if len(counter.keys()) > threshold:
        responses.pop(question)


def aggregate_responses(questions: dict) -> dict:
    """Aggregates responses from a dictionary of questions."""
    responses = {}
    for question in questions:
        counter = Counter(questions[question])
        responses[question] = dict(counter)
        remove_unaggregated_fields(counter, question, responses, 5)
    return responses

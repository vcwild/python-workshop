import csv


def read_questions(source: str) -> dict:
    """Reads questions from a CSV file and returns a dictionary."""
    with open(source, newline="") as csv_file:
        reader = csv.reader(csv_file, delimiter=",", quotechar='"')
        headers = next(reader)
        responses = [dict(zip(headers, row)) for row in reader]
        questions = {header: [] for header in headers}

    for response in responses:
        for header in headers:
            questions[header].append(response[header])

    return questions

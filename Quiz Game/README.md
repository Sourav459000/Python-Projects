# Quiz Game Project

The Quiz Game project is a simple command-line quiz application written in Python. It consists of two main classes: `Question` and `QuizBrain`. The application presents a series of True/False questions to the user, evaluates their answers, and provides a final score at the end.

## `Question` Class

The `Question` class represents a single quiz question. It has the following attributes:

- `text`: The text of the question.
- `answer`: The correct answer to the question ("True" or "False").

## `QuizBrain` Class

The `QuizBrain` class manages the flow of the quiz. It has the following attributes and methods:

### Attributes:

- `question_number`: The current question number.
- `score`: The user's current score.
- `question_list`: The list of `Question` objects representing the quiz questions.

### Methods:

- `still_has_questions()`: Checks if there are still questions remaining in the quiz.
- `next_question()`: Presents the next question to the user and checks their answer.
- `check_answer(user_answer, correct_answer)`: Checks if the user's answer is correct and updates the score.

## Data

The `question_data` list contains a set of True/False questions with corresponding correct answers.

## Usage

1. Run the script.
2. Answer each question by entering "True" or "False" in the command line.
3. Receive feedback on each answer and see the final score at the end.

## Requirements

- Python

## MIT License

Copyright (c) 2022 Sourav Toshniwal

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

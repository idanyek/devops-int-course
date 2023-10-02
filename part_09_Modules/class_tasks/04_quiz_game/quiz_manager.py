import random
from quiz_question import game_questions


def get_random_question():

    question, answer = random.choice(list(game_questions.items()))
    return question, answer


def check_answer(answer: str, user_answer: str):
    return answer.lower() == user_answer.lower()


def run_game(max_tries: int):
    user_score = 0
    wrong_answers = 0
    while wrong_answers < max_tries:
        question, answer = get_random_question()
        user_answer = input(question + " : ")
        if user_answer.lower() == "quit":
            break
        is_correct = (check_answer(answer, user_answer))
        if is_correct is True:
            user_score += 1
            print(F"Correct! your score is now: {user_score}")
        else:
            wrong_answers += 1
            print(F"Wrong! the currect answer is: {answer}.\n\tYou have {max_tries - wrong_answers} tries left.")

    print(f"\tGame Over! your score is: {user_score}")

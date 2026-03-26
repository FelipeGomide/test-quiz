import pytest
from model import Question


def test_create_question():
    question = Question(title="q1")
    assert question.id != None


def test_create_multiple_questions():
    question1 = Question(title="q1")
    question2 = Question(title="q2")
    assert question1.id != question2.id


def test_create_question_with_invalid_title():
    with pytest.raises(Exception):
        Question(title="")
    with pytest.raises(Exception):
        Question(title="a" * 201)
    with pytest.raises(Exception):
        Question(title="a" * 500)


def test_create_question_with_invalid_points():
    with pytest.raises(Exception):
        question = Question(title="q1", points=0)

    with pytest.raises(Exception):
        question = Question(title="q1", points=101)


def test_create_question_with_valid_points():
    question = Question(title="q1", points=1)
    assert question.points == 1
    question = Question(title="q1", points=100)
    assert question.points == 100


def test_create_choice():
    question = Question(title="q1")

    question.add_choice("a", False)

    choice = question.choices[0]
    assert len(question.choices) == 1
    assert choice.text == "a"
    assert not choice.is_correct


def test_create_choice_with_invalid_text():
    question = Question(title="q1")

    with pytest.raises(Exception):
        choice_a = question.add_choice("")

    with pytest.raises(Exception):
        choice_a = question.add_choice("a" * 101)

def test_question_default_values():
    question = Question("q1")

    assert question.points == 1
    assert question.max_selections == 1
    assert len(question.choices) == 0


def test_delete_choice():
    question = Question(title="q1")
    choice = question.add_choice("choice", False)

    question.remove_choice_by_id(choice.id)

    assert len(question.choices) == 0


def test_delete_choice_invalid_id():
    question = Question(title="q1")

    choice = question.add_choice("choice", False)

    with pytest.raises(Exception):
        question.remove_choice_by_id(choice.id + 1)


def test_remove_all_choices():
    question = Question(title="q1")

    choice_a = question.add_choice("a", False)
    choice_b = question.add_choice("b", False)
    question.remove_all_choices()

    assert len(question.choices) == 0


def test_remove_single_choice():
    question = Question(title="q1")
    choice_a = question.add_choice("a", False)
    choice_b = question.add_choice("b", False)

    question.remove_choice_by_id(choice_a.id)

    remaining_choice = question.choices[0]
    assert len(question.choices) == 1
    assert remaining_choice.id == choice_b.id


def test_create_correct_choice():
    question = Question(title="q1")

    choice_a = question.add_choice("a", True)

    assert choice_a.is_correct


def test_set_correct_choice():
    question = Question(title="q1")
    choice_a = question.add_choice("a", False)

    question.set_correct_choices([choice_a.id])

    assert choice_a.is_correct


def test_set_invalid_choice():
    question = Question(title="q1")
    choice_a = question.add_choice("a", False)

    with pytest.raises(Exception):
        question.set_correct_choices([choice_a.id + 1])

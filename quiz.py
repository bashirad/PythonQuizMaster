def main():
    score = 0

    # Create question and answer lists for each difficulty level
    question_list_level1 = [
        "Who was the first President of the United States?",
        "What year did the American Revolutionary War end?",
        "Which document declared the independence of the thirteen American colonies from British rule?",
        "Who wrote the Declaration of Independence?",
        "What is the capital of the United States?"
    ]
    answer_list_level1 = ["a", "b", "c", "d", "e"]

    question_list_level2 = [
        "What year was the U.S. Constitution written?",
        "Who was President during the Civil War?",
        "Which amendment abolished slavery?",
        "Who was the principal author of the U.S. Constitution?",
        "In what year did women gain the right to vote in the United States?"
    ]
    answer_list_level2 = ["a", "b", "c", "d", "e"]

    question_list_level3 = [
        "Who was the only President to serve more than two terms?",
        "What year did the United States enter World War I?",
        "Which U.S. President signed the Emancipation Proclamation?",
        "Who was the leader of the Soviet Union during the Cuban Missile Crisis?",
        "Which U.S. President is known for the New Deal?"
    ]
    answer_list_level3 = ["a", "b", "c", "d", "e"]

    question_list_level4 = [
        "What year did the stock market crash, marking the beginning of the Great Depression?",
        "Who was the main author of the Federalist Papers?",
        "Which U.S. President authorized the use of the atomic bomb during World War II?",
        "What was the main cause of the U.S. involvement in the Vietnam War?",
        "Which U.S. Supreme Court case established the principle of judicial review?"
    ]
    answer_list_level4 = ["a", "b", "c", "d", "e"]

    question_list_level5 = [
        "Who was the U.S. President during the Louisiana Purchase?",
        "What year did the United States land the first human on the moon?",
        "Which U.S. President is known for the policy of 'Reaganomics'?",
        "What was the primary purpose of the Marshall Plan?",
        "Which event marked the end of the Cold War?"
    ]
    answer_list_level5 = ["a", "b", "c", "d", "e"]

    # Start the game with difficulty level 1
    score = difficulty_level(question_list_level1, answer_list_level1, score)

    if score >= 6:
        score = difficulty_level(question_list_level2, answer_list_level2, score)
    if score >= 9:
        score = difficulty_level(question_list_level3, answer_list_level3, score)
    if score >= 12:
        score = difficulty_level(question_list_level4, answer_list_level4, score)
    if score >= 15:
        score = difficulty_level(question_list_level5, answer_list_level5, score)

    display_the_score(score)

    # Ask the user if they want to play again
    play_again = input("Do you want to play the game again? (yes/no): ").lower()
    if play_again == 'yes':
        main()
    else:
        print("Thank you for playing the game!")


def difficulty_level(question_list, answer_list, score):
    for i in range(5):
        if ask_question(question_list[i], answer_list[i]):
            score += 1

    if score < 3:
        print("Please try again")
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again == 'yes':
            score = difficulty_level(question_list, answer_list, score)
    else:
        print("Congratulations for finishing this level. Here comes a harder level! You’re surely capable of finishing this level as well.")

    return score


def ask_question(question, answer):
    user_answer = input(f"{question} (choose a letter): ").lower()
    if user_answer == answer:
        print("That is the CORRECT answer")
        return True
    else:
        print("That is an INCORRECT answer")
        return False


def display_the_score(score):
    if score == 25:
        print("You’re rocking; You are genius like no body.")
    elif 20 <= score < 25:
        print("You’re, definitely, smart.")
    elif 15 <= score < 20:
        print("You passed. One more time, and you’re the best.")


if __name__ == "__main__":
    main()

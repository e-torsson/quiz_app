from typing import Dict, Optional

USER_HIGHSCORES = {}

def main_menu() -> None:
    print('''
          1. Start Quiz
          2. View Highscores
          3. Exit
          ''')

def data_structure(filename: str) -> Dict:
    questions = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split('|')
            question = {
                'question': parts[0],
                'options': parts[1:5],
                'answer': parts[5],
            }
            questions.append(question)
    return questions
    

def highscores(final_score: Optional[int] = None) -> Dict:
    global USER_HIGHSCORES
    
    if final_score is not None:
        user_name = input('Enter your name:\n')
        USER_HIGHSCORES[user_name] = final_score
    
    print('\nHighscores:')
    for name, score in USER_HIGHSCORES.items():
        print(f'{name}: {score}')
        
    return USER_HIGHSCORES
    
def quiz(questions: Dict) -> int:
    final_score = 0
    for q in questions:
        print(f"Question: {q['question']}")
        for i, option in enumerate(q['options']):
            print(f'{chr(65 + i)} {option}')
            
        user_choice = input('Which answer is correct?\n')
        print(f'Your answer: {user_choice.upper()}')
        if user_choice.upper() == q['answer']:
            final_score += 1
            print(f'Correct answer!\nCurrent score: {final_score}\n')
        else:
            print(f'Incorrect answer. The correct answer is {q["answer"]}\nCurrent score: {final_score}\n')
        print()
    
    return final_score

def main() -> None:
    while True:
        main_menu()
        user_input = int(input('Please select what you wish to do:\n'))
        if user_input == 1:
            questions = data_structure('questions.txt')
            final_score = quiz(questions)
            highscores(final_score)
        elif user_input == 2:
            highscores()
        elif user_input == 3:
            print('Goodbye!')
            break
        else:
            print('Invalid input. Please try again.')

if __name__ == '__main__':
    main()

questions = [
    [{"question":"Who is Shahrukh Khan?"}, {"options":"A. WWE Wrestler B. Plumber C. Actor D. Astronaut"}, {"Correct_answer": ["c", "Actor"]}],
    [{"question":"What is the capital of France?"}, {"options":"A. Berlin B. Paris C. Rome D. London"}, {"Correct_answer": ["b", "Paris"]}],
    [{"question":"Which planet is known as the Red Planet?"}, {"options":"A. Earth B. Venus C. Mars D. Jupiter"}, {"Correct_answer": ["c", "Mars"]}],
    [{"question":"What is the largest mammal?"}, {"options":"A. Shark B. Blue Whale C. Elephant D. Giraffe"}, {"Correct_answer": ["b", "Blue Whale"]}],
    [{"question":"Who wrote 'Romeo and Juliet'?"}, {"options":"A. William Shakespeare B. Jane Austen C. Charles Dickens D. Homer"}, {"Correct_answer": ["a", "William Shakespeare"]}],
    [{"question":"What is the square root of 64?"}, {"options":"A. 8 B. 10 C. 6 D. 12"}, {"Correct_answer": ["a", "8"]}],
    [{"question":"Which country is known as the Land of the Rising Sun?"}, {"options":"A. India B. South Korea C. Japan D. China"}, {"Correct_answer": ["c", "Japan"]}],
    [{"question":"Who painted the Mona Lisa?"}, {"options":"A. Claude Monet B. Pablo Picasso C. Leonardo da Vinci D. Vincent van Gogh"}, {"Correct_answer": ["c", "Leonardo da Vinci"]}],
    [{"question":"What is the fastest land animal?"}, {"options":"A. Lion B. Cheetah C. Elephant D. Horse" }, {"Correct_answer": ["b", "Cheetah"]}],
    [{"question":"Which ocean is the largest?"}, {"options":"A. Indian Ocean B. Pacific Ocean C. Atlantic Ocean D. Arctic Ocean"}, {"Correct_answer": ["b", "Pacific Ocean"]}],
    [{"question":"What is the smallest country in the world?"}, {"options":"A. San Marino B. Vatican City C. Monaco D. Liechtenstein"}, {"Correct_answer": ["b", "Vatican City"]}]
]

# Initial price
Prize = 0
print("Welcome to the kon banega crore pati show!\nLet's start the game!\n\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\")
question_number = 1
for part in questions:
    question = part[0]["question"]
    print(f"Question {question_number}:\n{question}")
    options = part[1]["options"]
    print(options)
    correct_answer = part[2]["Correct_answer"]
    if choose:=input("Select you answer: ") in correct_answer:
        Prize += 1000000
        if question_number == 11:
            print(f"Congratulation! You have won the ultimate prize\n7 Crore!!!")
    else:
        print(f"You have selected the wrong option!\nThe correct answer is {correct_answer}\nYou have won {Prize}/- rupees")
        break
    question_number += 1

print("Game Ended!\nThanks for playing")
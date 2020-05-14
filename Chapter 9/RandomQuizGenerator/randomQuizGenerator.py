#! /usr/bin/env python3

import random

CAPITALS = {
    'Alabama'       : 'Montgomery',
    'Alaska'        : 'Juneau',
    'Arizona'       : 'Phoenix',
    'Arkansas'      : 'Little Rock',
    'California'    : 'Sacramento',
    'Colorado'      : 'Denver',
    'Connecticut'   : 'Hartford',
    'Delaware'      : 'Dover',
    'Florida'       : 'Tallahassee',
    'Georgia'       : 'Atlanta',
    'Hawaii'        : 'Honolulu',
    'Idaho'         : 'Boise',
    'Illinois'      : 'Springfield',
    'Indiana'       : 'Indianapolis',
    'Iowa'          : 'Des Moines',
    'Kansas'        : 'Topeka',
    'Kentucky'      : 'Frankfort',
    'Louisiana'     : 'Baton Rouge',
    'Maine'         : 'Augusta',
    'Maryland'      : 'Annapolis',
    'Massachusetts' : 'Boston',
    'Michigan'      : 'Lansing',
    'Minnesota'     : 'Saint Paul',
    'Mississippi'   : 'Jackson',
    'Missouri'      : 'Jefferson City',
    'Montana'       : 'Helena',
    'Nebraska'      : 'Lincoln',
    'Nevada'        : 'Carson City',
    'New Hampshire' : 'Concord',
    'New Jersey'    : 'Trenton',
    'New Mexico'    : 'Santa Fe',
    'New York'      : 'Albany',
    'North Carolina': 'Raleigh',
    'North Dakota'  : 'Bismarck',
    'Ohio'          : 'Columbus',
    'Oklahoma'      : 'Oklahoma City',
    'Oregon'        : 'Salem',
    'Pennsylvania'  : 'Harrisburg',
    'Rhode Island'  : 'Providence',
    'South Carolina': 'Columbia',
    'South Dakota'  : 'Pierre',
    'Tennessee'     : 'Nashville',
    'Texas'         : 'Austin',
    'Utah'          : 'Salt Lake City',
    'Vermont'       : 'Montpelier',
    'Virginia'      : 'Richmond',
    'Washington'    : 'Olympia',
    'West Virginia' : 'Charleston',
    'Wisconsin'     : 'Madison',
    'Wyoming'       : 'Cheyenne'
}

## Generate 35 files
for quizNum in range(1, 36):
    ## Create the quiz and answer key files.
    quizFile = open(f'capitalsquiz{quizNum}.txt', 'w')
    answerKeyFile = open(f'capitalsquiz_answer{quizNum}.txt', 'w')


    ## Write out the header for the quiz.
    quizFile.write('Name:\n\nDate:\n\nPeriod:\n\n')
    quizFile.write(('' * 20) + f'State Capitals Quiz (Form{quizNum})')
    quizFile.write('\n\n')


    ## Shuffle the order of the states.
    states = list(CAPITALS.keys())
    random.shuffle(states)


    ## TODO: Loop through all 50 states, making a question for each.
    for questionNum in range(50):

        ## Get right and wrong answers.


        # Get correct answer
        correctAnswer = CAPITALS[states[questionNum]]

        # Duplicate all the values in the CAPITALS dictionary
        wrongAnswers = list(CAPITALS.values())

        # Delete the correct answer
        del wrongAnswers[wrongAnswers.index(correctAnswer)]

        # Select three random values from the list
        wrongAnswers = random.sample(wrongAnswers, 3)

        # Create full list of answer options
        answerOptions = wrongAnswers + [correctAnswer]

        # Randomize answers
        random.shuffle(answerOptions)


        ## Write the question and answer options to the quiz file
        quizFile.write(f'{questionNum + 1}. What is the capital of {states[questionNum]}?\n')

        for i in range(4):
            quizFile.write(f"   {'ABCD'[i]}.{answerOptions[i]}\n")

        quizFile.write('\n')

        ## Write the answer key to a file.
        answerKeyFile.write(f"{questionNum + 1}. {'ABCD'[answerOptions.index(correctAnswer)]}\n")

    quizFile.close()
    answerKeyFile.close()

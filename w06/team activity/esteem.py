

def main():
    #print intro message
    intro = "This program is an implementation of the Rosenberg"
    intro += "\nSelf-Esteem Scale. This program will show you ten"
    intro += "\nstatements that you could possibly apply to yourself.\n"
    print(intro)

    #meaning of response options
    print(f"D means you strongly disagree with the statement.")
    print(f"d means you disagree with the statement.")
    print(f"a means you agree with the statement.")
    print(f"A means you strongly agree with the statement")

    #print statments and store score for each response in a list
    score_list = [
        get_statement_response_score("1. I feel that I am a person of worth, at least on an equal plane with others.", True),
        get_statement_response_score("2. I feel that I have a number of good qualities.", True),
        get_statement_response_score("3. All in all, I am inclined to feel that I am a failure.", False),
        get_statement_response_score("4. I am able to do things as well as most other people.", True),
        get_statement_response_score("5. I feel I do not have much to be proud of.", False),
        get_statement_response_score("6. I take a positive attitude toward myself.", True),
        get_statement_response_score("7. On the whole, I am satisfied with myself.", True),
        get_statement_response_score("8. I wish I could have more respect for myself.", False),
        get_statement_response_score("9. I certainly feel useless at times.", False),
        get_statement_response_score("10. At times I think I am no good at all.", False),

    ]
    #sum up all scores and display total
    total_score = sum(score_list)
    print(f"Your score is {total_score}")
    print("A score below 15 may indicate problematic low self-esteem.")

    

def get_statement_response_score(statement, is_positive):
    """
    get a response from specified statement and return the score per response
    parameters
        statement: a string of the statement that the user will respond to
        is_positive: boolean whether the statement is positive or negative
    """
    print(statement)
    response = input(f"Enter D, d, a, or A:")
    return compute_response_point(response, is_positive)

def compute_response_point(response, is_positive):
    """
    calculate points based on chosen response to a statement.
    parameters
        response: the string character D,d,A, or a to determine the points from 0 - 3
        is_positive: boolean whether the response is from a positive or negative statement
    return: integer of points 0-3
    """
    point = 0

    if (is_positive):
        if (response == 'D'):
            point = 0
        elif (response == 'd'):
            point = 1
        elif (response == 'a'):
            point = 2
        elif (response == 'A'):
            point = 3
        else: 
            return print(f'{point} is an invalid input')

    elif not(is_positive):
        if (response == 'D'):
            point = 3 
        elif (response == 'd'):
            point = 2
        elif (response == 'a'):
            point = 1
        elif (response == 'A'):
            point = 0
        else: 
            return print(f'{point} is an invalid input')

    return point

        
main()
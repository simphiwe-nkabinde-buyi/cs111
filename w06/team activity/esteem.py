

def main():
    intro = "This program is an implementation of the Rosenberg"
    intro += "\nSelf-Esteem Scale. This program will show you ten"
    intro += "\nstatements that you could possibly apply to yourself.\n"

    print(intro)
    print(f"D means you strongly disagree with the statement.")
    print(f"d means you disagree with the statement.")
    print(f"a means you agree with the statement.")
    print(f"A means you strongly agree with the statement")

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

    if (response == 'D'):
        if (is_positive): point = 0
        else: point = 3 
    elif (response == 'd'):
        if (is_positive): point = 1
        else: point = 2
    elif (response == 'a'):
        if (is_positive): point = 2
        else: point = 1
    elif (response == 'D'):
        if (is_positive): point = 3
        else: point = 0
    
    return point

        

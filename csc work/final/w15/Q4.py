def get_valid_month():
    ''' () -> int
    Return a valid month number input by user after (possibly repeated) 
    prompting. A valid month number is an int between 1 and 12 inclusive.
    '''
    
    prompt = 'Enter a valid month number: '
    error_message = 'Invalid input! Read the instructions and try again!'
    # Use this statement as many times as needed for input:
    # month = input(prompt)
    # Use this statement as many times as needed for output:
    # print(error_message)
    
    month = input(prompt)
    while not (month.isdigit()) or int(month) < 1 or int(month) > 12:
        print(error_message)
        month = input(prompt)
    return int(month)
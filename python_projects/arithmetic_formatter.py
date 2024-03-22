'''
Arithmetic Formatter

Students in primary school often arrange arithmetic problems vertically to make them easier to solve.
For example, "235 + 52" becomes:

  235
+  52
-----

Finish the arithmetic_arranger function that receives a list of strings which are arithmetic problems, and returns the problems arranged vertically and side-by-side.
The function should optionally take a second argument. When the second argument is set to True, the answers should be displayed.

Example
Function Call:

arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
Output:

   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
Function Call:

arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
Output:

  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474
Rules
The function will return the correct conversion if the supplied problems are properly formatted, otherwise, it will return a string that describes an error that is meaningful to the user.

Situations that will return an error:
 - If there are too many problems supplied to the function. The limit is five, anything more will return: 'Error: Too many problems.'
 - The appropriate operators the function will accept are addition and subtraction. Multiplication and division will return an error. Other operators not mentioned in this bullet point will not need to be tested. The error returned will be: "Error: Operator must be '+' or '-'."
 - Each number (operand) should only contain digits. Otherwise, the function will return: 'Error: Numbers must only contain digits.'
 - Each operand (aka number on each side of the operator) has a max of four digits in width. Otherwise, the error string returned will be: 'Error: Numbers cannot be more than four digits.'

If the user supplied the correct format of problems, the conversion you return will follow these rules:
 - There should be a single space between the operator and the longest of the two operands, the operator will be on the same line as the second operand, both operands will be in the same order as provided (the first will be the top one and the second will be the bottom).
 - Numbers should be right-aligned.
 - There should be four spaces between each problem.
 - There should be dashes at the bottom of each problem. The dashes should run along the entire length of each problem individually. (The example above shows what this should look like.)

 TESTS
arithmetic_arranger(["3801 - 2", "123 + 49"]) should return   3801      123\n-    2    +  49\n------    -----.

arithmetic_arranger(["1 + 2", "1 - 9380"]) should return   1         1\n+ 2    - 9380\n---    ------.

arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]) should return     3      3801      45      123\n+ 855    -    2    + 43    +  49\n-----    ------    ----    -----.

arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"]) should return   11      3801      1      123         1\n+  4    - 2999    + 2    +  49    - 9380\n----    ------    ---    -----    ------.

arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"]) should return 'Error: Too many problems.'.

arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"]) should return "Error: Operator must be '+' or '-'.".

arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"]) should return 'Error: Numbers cannot be more than four digits.'.

arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"]) should return 'Error: Numbers must only contain digits.'.

arithmetic_arranger(["3 + 855", "988 + 40"], True) should return     3      988\n+ 855    +  40\n-----    -----\n  858     1028.

arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True) should return    32         1      45      123      988\n- 698    - 3801    + 43    +  49    +  40\n-----    ------    ----    -----    -----\n -666     -3800      88      172     1028.

_________________________________________________________________________________________________________________________________________________

Thought process: 
1. Save the problems into list. Each element in the list contains the operands and operator.
2. Extract the operands and operator from each element.
3. Evaluate each expression, and save the result in the 'equations' variable together with the operands and operator. Like so: 
  equations = [('32','698','+','730'), ('3801','2','-','3799'), ('45','43','+','88'), ('123','49','+','172')]
4. Print each line systematically

Catches:
1. The function will return the correct conversion if the supplied problems are properly formatted, otherwise, 
it will return a string that describes an error that is meaningful to the user.
2. The program will not process input that has:
  - more than 5 expression. If so, 'Error: Too many problems.' shall be printed out.
  - operands other than '+' and '-'. If so, "Error: Operator must be '+' or '-'." shall be printed out.
  - non-numeric characters as it operands. If so, 'Error: Numbers must only contain digits.' shall be printed out.
  - operands with more than 4 digits. If so, 'Error: Numbers cannot be more than four digits.' shall be printed out.

_________________________________________________________________________________________________________________________________________________
'''


import re     # Module to perform regular expression matching

# Main Function


def arithmetic_arranger(problems, show_answers=False):
    # Set initial problem count as 0.
    problem_count = 0
    equations = []
    for problem in problems:

        # Validate the current problem if it follows the correct format.
        validation_result = check_input_string(problem)
        if validation_result is not True:
            return validation_result

        equations.append(solve_problem(problem))

        # Increment problem count
        problem_count += 1

        # If problem count is more than 5. Return an error.
        if problem_count > 5:
            return 'Error: Too many problems.'

    return output_formatter(equations, show_answers)
    # return equations

# Function to verify the format of the input string


def check_input_string(problem):
    # Check if the input matches the overall pattern
    '''
      REGEX
      ^ denotes the start of the string.
      \d{1,4} matches between 1 and 4 digits.
      \s matches a space.
      [+-] matches either a plus or minus sign.
      \s matches a space.
      \d{1,4} matches between 1 and 4 digits again.
      $ denotes the end of the string.

    '''
    if not re.match(r'^\d{1,4}\s[+-]\s\d{1,4}$', problem) and problem.split()[1] in ['+', '-'] and len(problem.split()[0]) <= 4 and len(problem.split()[2]) <= 4:
        return 'Error: Numbers must only contain digits.'

    # Check the first number (x)
    elif not re.match(r'^\d{1,4}$', problem.split()[0]):
        return 'Error: Numbers cannot be more than four digits.'

    # Check the operator
    elif problem.split()[1] not in ['+', '-']:
        return "Error: Operator must be '+' or '-'."

    # Check the second number (y)
    elif not re.match(r'^\d{1,4}$', problem.split()[2]):
        return 'Error: Numbers cannot be more than four digits.'

    return True

# Function to solve the problem and return the problem with result


def solve_problem(problem):
    # Split the problem string into parts
    x, operator, y = problem.split()

    # Convert operands to integers
    x = int(x)
    y = int(y)

    # Perform the arithmetic operation
    if operator == '+':
        result = x + y
    elif operator == '-':
        result = x - y

    # Create a list with equation elements and result
    equation = [str(x), operator, str(y), str(result)]

    # Return the equation list
    return equation

# Function to format the output string


def output_formatter(equations, show_answers):

    first_line = ''
    second_line = ''
    third_line = ''
    fourth_line = ''

    for equation in equations:

        # Calculate the max length of each string. This is also equal to the number of '-' below the operands
        if '-' in equation[3] and show_answers == True:
            max_length = min(6, max(len(equation[0]), len(equation[3])) + 1)
        elif len(equation[3]) >= 4 and show_answers == True:
            max_length = min(6, max(len(equation[0]), len(equation[3])) + 1)
        else:
            max_length = min(6, max(len(equation[0]), len(equation[3])) + 2)

        # Calculate the number of spaces needed between operand and operator
        second_line_spaces = max_length - len(equation[2])-1

        # Construct the strings to be printed per line.
        first_line += ' ' * \
            (max_length - len(equation[0])) + equation[0] + '    '
        second_line += equation[1] + ' ' * \
            second_line_spaces + equation[2] + '    '
        third_line += '-' * max_length + '    '

        fourth_line += ' ' * \
            (max_length - len(equation[3])) + equation[3] + '    '

        # Only show fourth_line if show_answers is True
        if show_answers == True:
            combined_lines = first_line.rstrip() + '\n' + second_line.rstrip() + '\n' + \
                third_line.rstrip() + '\n' + fourth_line.rstrip()
        else:
            combined_lines = first_line.rstrip() + '\n' + second_line.rstrip() + '\n' + \
                third_line.rstrip()

    return combined_lines


print(
    f'\n{arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True)}')

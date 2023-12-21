from simpleai.search import CspProblem, backtrack

# Define the function that imposes the constraint
# that neighbors should be different
def constraint_func(names, values):
    return values[0] != values[1]

if __name__=='__main__':
    # Specify the zones
    names = (
        'Banana', 'Apple', 'Pineapple',
        'Strawberry', 'Plum', 'Blackberry',
        'Melon', 'Blueberry', 'Raspberry',
        'Watermelon', 'Apricot', 'Cherry',
        'Pear', 'Kiwi'
    )

    # Define the possible colors
    colors = dict((name, ['red', 'green', 'blue', 'gray']) for name in names)

    # Define the constraints
    constraints = [
        (('Banana', 'Strawberry'), constraint_func),
        (('Banana', 'Plum'), constraint_func),
        (('Banana', 'Apple'), constraint_func),
        (('Apple', 'Plum'), constraint_func),
        (('Apple', 'Blackberry'), constraint_func),
        (('Apple', 'Pineapple'), constraint_func),
        (('Pineapple', 'Blackberry'), constraint_func),
        (('Pineapple', 'Melon'), constraint_func),
        (('Strawberry', 'Plum'), constraint_func),
        (('Strawberry', 'Blueberry'), constraint_func),
        (('Strawberry', 'Watermelon'), constraint_func),
        (('Plum', 'Watermelon'), constraint_func),
        (('Plum', 'Blackberry'), constraint_func),
        (('Blackberry', 'Watermelon'), constraint_func),
        (('Blackberry', 'Pear'), constraint_func),
        (('Blackberry', 'Melon'), constraint_func),
        (('Melon', 'Pear'), constraint_func),
        (('Melon', 'Kiwi'), constraint_func),
        (('Blueberry', 'Watermelon'), constraint_func),
        (('Blueberry', 'Raspberry'), constraint_func),
        (('Watermelon', 'Raspberry'), constraint_func),
        (('Watermelon', 'Apricot'), constraint_func),
        (('Watermelon', 'Cherry'), constraint_func),
        (('Watermelon', 'Pear'), constraint_func),
        (('Pear', 'Cherry'), constraint_func),
        (('Pear', 'Kiwi'), constraint_func),
        (('Kiwi', 'Cherry'), constraint_func),
        (('Raspberry', 'Apricot'), constraint_func),
        (('Apricot', 'Cherry'), constraint_func),
    ]

    # Solve the problem
    problem = CspProblem(names, colors, constraints)

    # Print the solution
    output = backtrack(problem)
    print('\nColor mapping:\n')
    for k, v in output.items():
        print(k, '==>', v)


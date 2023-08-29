def evaluate_clause(clause, assignment, var_to_letter):
    for literal in clause:
        variable = abs(literal)
        value = literal > 0  # True if positive, False if negative
        variable_letter = var_to_letter[variable]
        if variable_letter not in assignment:
            continue
        if assignment[variable_letter] == value:
            return True
    return False

def evaluate_formula(formula, assignment, var_to_letter):
    for clause in formula:
        if not evaluate_clause(clause, assignment, var_to_letter):
            return False
    return True

def brute_force_satisfiability(formula, var_to_letter):
    num_variables = max(abs(literal) for clause in formula for literal in clause)
    for i in range(2 ** num_variables):
        assignment = {}
        for j in range(num_variables):
            variable_letter = var_to_letter[j + 1]
            assignment[variable_letter] = bool((i >> j) & 1)
        if evaluate_formula(formula, assignment, var_to_letter):
            return True, assignment
    return False, None

# Example input: {{¬p, ¬q}, {q, ¬s}, {¬p, s}, {¬q, s}}
var_to_letter = {1: 'p', 2: 'q', 3: 'r', 4: 's'}
formula1 = [[1], [-1]]
formula2 = [[2, 1, -1]]
formula3 = [[-1, -3,-4], [-2, -1,-4]]
formula4 = [[-1,-2], [2,-4], [-2,4], [-2,4]]
formula5 = [[-1,-2,-4], [2,-4,1], [-1,2,3]]
formulas = [formula1, formula2, formula3, formula4, formula5]

for idx, formula in enumerate(formulas, start=1):
    print(f"Formula {idx}:")
    satisfiable, assignment = brute_force_satisfiability(formula, var_to_letter)
    if satisfiable:
        print("Satisfiable with assignment:", assignment)
    else:
        print("Unsatisfiable")
    print()

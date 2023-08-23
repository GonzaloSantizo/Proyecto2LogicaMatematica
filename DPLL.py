def evaluate_clause(clause, assignment):
    for literal in clause:
        variable = abs(literal)
        value = literal > 0  # True if positive, False if negative
        if variable not in assignment:
            continue
        if assignment[variable] == value:
            return True
    return False

def evaluate_formula(formula, assignment):
    for clause in formula:
        if not evaluate_clause(clause, assignment):
            return False
    return True

def brute_force_satisfiability(formula):
    num_variables = max(abs(literal) for clause in formula for literal in clause)
    for i in range(2 ** num_variables):
        assignment = {}
        for j in range(num_variables):
            assignment[j + 1] = bool((i >> j) & 1)
        if evaluate_formula(formula, assignment):
            return True, assignment
    return False, None

# Example input: {{p}, {p}}
formula = [
    [1], [1]
]

satisfiable, assignment = brute_force_satisfiability(formula)
if satisfiable:
    print("Satisfiable with assignment:", assignment)
else:
    print("Unsatisfiable")

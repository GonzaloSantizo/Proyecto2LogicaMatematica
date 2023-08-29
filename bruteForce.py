def parse_literal(literal_str):
    if literal_str.startswith("-"):
        variable = literal_str[1:]
        value = False
    else:
        variable = literal_str
        value = True
    return variable, value

def parse_clause(clause_str):
    literals = clause_str.split(", ")
    return [parse_literal(literal.strip()) for literal in literals]

def parse_formula(formula_str):
    clauses = formula_str.split(", ")
    return [parse_clause(clause.strip("{ }")) for clause in clauses]

def evaluate_clause(clause, assignment):
    for variable, value in clause:
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
    variables = set()
    for clause in formula:
        for variable, _ in clause:
            variables.add(variable)
    num_variables = len(variables)

    variable_list = list(variables)
    variable_index_map = {variable: index for index, variable in enumerate(variable_list)}

    for i in range(2 ** num_variables):
        assignment = {}
        for j, variable in enumerate(variable_list):
            assignment[variable] = bool((i >> j) & 1)
        if evaluate_formula(formula, assignment):
            return True, assignment
    return False, None

# Example input: "{{-p, -q}, {q, -s}, {-p, s}, {-q, s}}"
formula_str = "{{-p, -q}, {q, -s}, {-p, s}, {-q, s}}"
formula = parse_formula(formula_str)

satisfiable, assignment = brute_force_satisfiability(formula)
if satisfiable:
    print("Satisfiable with assignment:", assignment)
else:
    print("Unsatisfiable")

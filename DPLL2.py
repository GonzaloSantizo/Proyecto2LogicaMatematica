def DPLL(symbols, clauses, model):
    print("Symbols:", symbols)
    print("Clauses:", clauses)
    print("Model:", model)

    if all_clause_satisfied(clauses, model):
        return model

    if any_clause_unsatisfied(clauses, model):
        return None

    unassigned_symbol = find_unassigned_symbol(symbols, model)
    
    if unassigned_symbol is None:
        return None
    
    # Try assigning the unassigned symbol to true
    result = DPLL(symbols, simplify(clauses, unassigned_symbol), model + [unassigned_symbol])
    if result is not None:
        return result
    
    # If assigning true didn't work, try assigning the unassigned symbol to false
    return DPLL(symbols, simplify(clauses, -unassigned_symbol), model + [-unassigned_symbol])

def all_clause_satisfied(clauses, model):
    return all(any(lit in model for lit in clause) for clause in clauses)

def any_clause_unsatisfied(clauses, model):
    return any(all(lit not in model for lit in clause) for clause in clauses)

def find_unassigned_symbol(symbols, model):
    for symbol in symbols:
        if symbol not in model and -symbol not in model:
            return symbol
    return None

def simplify(clauses, literal):
    return [clause for clause in clauses if literal not in clause]

def parse_formula(formula_str):
    clauses_str = formula_str.split("}, {")
    clauses = []
    symbols = set()
    
    for clause_str in clauses_str:
        clause_str = clause_str.replace("{", "").replace("}", "")
        literals = clause_str.split(", ")
        clause = []
        for literal in literals:
            if literal.startswith("-"):
                symbol = "not_" + literal[1:]
                clause.append(symbol)
                symbols.add(symbol)
            else:
                symbol = literal
                clause.append(symbol)
                symbols.add(symbol)
        if clause:
            clauses.append(clause)
    
    return symbols, clauses

# Example formula string
formula_str = "{{-p, -r, -s}, {-q, -p, -s}}"

symbols, clauses = parse_formula(formula_str)
model = []

solution = DPLL(symbols, clauses, model)

if solution is not None:
    print("Satisfiable. Model:", solution)
else:
    print("Unsatisfiable.")

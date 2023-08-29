def DPLL(B, I):
    if not B:  # B es vacía
        return True, I

    for clause in B:
        if not clause:  # Disyunción vacía en B
            return False, None

    L = seleccionar_literal(B, I)
    if L is None:
        return False, None

    B1 = eliminar_clausulas(B, L)
    B2 = eliminar_ocurrencias_complementarias(B, L)
    I1 = I.copy()
    I1[positive(L)] = ifpositive(L)

    resultado, interpretacion = DPLL(B1, I1)
    if resultado:
        return True, interpretacion

    resultado, interpretacion = DPLL(B2, I)
    if resultado:
        return True, interpretacion

    return False, None


def seleccionar_literal(B, I):
    # Selecciona una literal no asignada en la asignación parcial
    for clause in B:
        for literal in clause:
            if positive(literal) not in I:
                return literal

    return None


def eliminar_clausulas(B, L):
    # Elimina todas las cláusulas que contienen la literal L en B
    B1 = [clause for clause in B if L not in clause]
    return B1


def eliminar_ocurrencias_complementarias(B, L):
    # Elimina las ocurrencias de la literal complementaria de L en B
    complemento_L = '-'+L
    B2 = []
    for clause in B:
        if complemento_L not in clause:
            B2.append([l for l in clause if l != L])
    return B2

# function that turns a "-p" into "p"
def positive(literal):
    menos = "-"
    if menos in literal:
        nueva_cadena = literal[:literal.index(menos)] + literal[literal.index(menos) + len(menos):]
        return nueva_cadena
    else:
        return literal
    
def ifpositive(literal):
    menos = "-"
    if menos in literal:
        return False
    else:
        return True

# Ejemplo de uso
formula1 = [['p'], ['-p']]
formula2 = [['q', 'p', '-p']]
formula3 = [['p', '-p'], ['q', '-q']]
formula4 = [['p'], ['q'], ['-p'], ['-q']]
formula5 = [['p'], ['q'], ['-r'], ['-s']]
formulas = [formula1, formula2, formula3, formula4, formula5]

for idx, formula in enumerate(formulas, start=1):

    print(f"Formula {idx}:")
    resultado, interpretacion = DPLL(formula, {})

    if resultado:
        print("La fórmula es satisfacible.")
        print("Asignación parcial:", interpretacion)
    else:
        print("La fórmula es insatisfacible.")
    print()
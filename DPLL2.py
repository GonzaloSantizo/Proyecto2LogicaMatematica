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
    I1[abs(L)] = L > 0

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
            if abs(literal) not in I:
                return literal

    return None


def eliminar_clausulas(B, L):
    # Elimina todas las cláusulas que contienen la literal L en B
    B1 = [clause for clause in B if L not in clause]
    return B1


def eliminar_ocurrencias_complementarias(B, L):
    # Elimina las ocurrencias de la literal complementaria de L en B
    complemento_L = -L
    B2 = []
    for clause in B:
        if complemento_L not in clause:
            B2.append([l for l in clause if l != L])
    return B2


# Ejemplo de uso
B = [[1], [1]]
I = {}

resultado, interpretacion = DPLL(B, I)

if resultado:
    print("La fórmula es satisfacible.")
    print("Asignación parcial:", interpretacion)
else:
    print("La fórmula es insatisfacible.")
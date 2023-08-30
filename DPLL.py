# Función que nos devuelve la interpretación de una formula en forma clausal, y su asignación parcial,
# esta recibe B (lista de cláusulas) y I (una asignación parcial de literales)
def DPLL(B, I):
    # Este bloque nos verifica si la lista de cláusulas está vacía
    # Si es así, significa que la formula es satisfactable y se
    # devuelve True y la interpretación de la formula
    if not B:
        return True, I

    # Se verifica si hay una clausula vacía en B, significando que la formula no es satisfactable
    for clause in B:
        if not clause:  # Significa que hay una disyunción vacía en B
            return False, None

    # Seleccionamos una literal no asignada en la asignación parcial I
    L = seleccionar_literal(B, I)
    if L is None: # Si no hay, significa que no satisface la formula
        return False, None

    # Después de seleccionar la literal, eliminamos todas las claúsulas que contienen L,
    # creando una nueva lista B1 que contiene todas las cláusulas que no contienen L.
    B1 = eliminar_clausulas(B, L)

    # Después eliminamos todas las ocurrencias complementarias de L, devolviendo,
    # una nueva lista B2 que contiene todas las cláusulas de B en las que no aparece,
    # los complementos de L.
    B2 = eliminar_ocurrencias_complementarias(B, L)

    # Creamos una copia de la asignación parcial I en I1 para evitar modificar la original
    I1 = I.copy()

    # Le asignamos un valor a la literal L en I1 dependiendo de si es la literal o el complemento
    I1[positive(L)] = ifpositive(L)

    # Luego hacemos una llamada recursiva a DPLL con los parámetros B1 y I1,
    # aqui intentamos encontrar una asignación que satifaga las cláusulas restantes.
    # Si se encuentra una asignación satisfactoria, se devuelve True y la interpretación.
    resultado, interpretacion = DPLL(B1, I1)
    if resultado:
        return True, interpretacion

    # Si no se encuentra una asignación satisfactoria, se intenta con la asignación parcial
    # original I y con la formula clausal B2. Esto nos permite explorar el caso en el que
    # asignemos de manera diferente a L, como su complemento -L.
    resultado, interpretacion = DPLL(B2, I)
    if resultado:
        return True, interpretacion

    # Si no se encuentra una asignación satisfactoria, significa que la formula no es
    # satisfactable, por lo que se devuelve False y None.
    return False, None

# Seleccionamos una literal no asignada en la asignación parcial I
# Recorremos cada clausula en B y, dentro de cada clausula, verificamos si la literal seleccionada
# está en la asignación parcial I, si hay una literal no asignada en la asignación parcial I,
# la devuelve, en caso contrario, devuelve None.
def seleccionar_literal(B, I):
    for clause in B:
        for literal in clause:
            if positive(literal) not in I:
                return literal

    return None

# Elimina todas las cláusulas que contienen la literal L en B
# Esta crea una nueva lista B1 que no contiene las cláusulas que contienen la literal L
# y devuelve esta lista
def eliminar_clausulas(B, L):
    B1 = [clause for clause in B if L not in clause]
    return B1

# Elimina las ocurrencias de la literal complementaria de L en B
# crea una nueva lista B2 que contiene todas las cláusulas de B en las que
# no aparece el complemento de L.
def eliminar_ocurrencias_complementarias(B, L):
    complemento_L = '-'+L
    B2 = []
    for clause in B:
        if complemento_L not in clause:
            B2.append([l for l in clause if l != L])
    return B2

# Función que nos vuelve el literal complementario
def positive(literal):
    menos = "-"
    if menos in literal:
        nueva_cadena = literal[:literal.index(menos)] + literal[literal.index(menos) + len(menos):]
        return nueva_cadena
    else:
        return literal

# Función que nos verifica si el literal es complementario o no
def ifpositive(literal):
    menos = "-"
    if menos in literal:
        return False
    else:
        return True

# Títulos de los casos de uso
Ejemplos = {
    "Ejemplo1": "p ∧ -p",
    "Ejemplo2": "q ∨ p ∨ -p",
    "Ejemplo3": "(-p ∨ -r ∨ -s) ∧ (-q ∨ -p ∨ -s)",
    "Ejemplo4": "(-p ∨ -q) ∧ (q ∨ -s) ∧ (-p ∨ s) ∧ (-q ∨ s)",
    "Ejemplo5": "(-p ∨ -q ∨ -r) ∧ (q ∨ -r ∨ p) ∧ (-p ∨ q ∨ r)",
    "Ejemplo6": "r ∧ (-q ∨ -r) ∧ (-p ∨ q ∨ -r) ∧ q"
}

# Formulas de los casos de uso
formula1 = [['p'], ['-p']]
formula2 = [['q', 'p', '-p']]
formula3 = [['-p', '-r', '-s'], ['-q', '-p', '-s']]
formula4 = [['-p', '-q'], ['q', '-s'], ['-p', 's'], ['-q', 's']]
formula5 = [['-p', '-q', '-r'], ['q', '-r', 'p'], ['-p', 'q', 'r']]
formula6 = [['r'], ['-q', '-r'], ['-p', 'q', '-r'], ['q']]
formulas = [formula1, formula2, formula3, formula4, formula5, formula6]

# Ejecutamos el algoritmo DPLL para cada una de las formulas
for idx, formula in enumerate(formulas, start=1):

    print(f"Formula: {Ejemplos['Ejemplo' + str(idx)]}")
    print()

    resultado, interpretacion = DPLL(formula, {})

    if resultado:
        print("La fórmula es satisfacible.")
        print("Asignación parcial:", interpretacion)
    else:
        print("La fórmula es insatisfacible.")
    print()
    print()
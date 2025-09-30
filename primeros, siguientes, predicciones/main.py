def leer_gramatica(nombre_archivo):
    gramatica={}
    with open(nombre_archivo, 'r') as archivo:
        for linea in archivo:
            linea=linea.strip()
            if not linea or '->' not in linea:
                continue
            izquierda, derecha=linea.split('->')
            izquierda=izquierda.strip()
            derecha=derecha.strip()

            if izquierda not in gramatica:
                gramatica[izquierda]=[]
            if derecha.lower()=='vacio':
                gramatica[izquierda].append(['ε'])
            else:
                gramatica[izquierda].append(derecha.split())
    return gramatica


def Primeros(gramatica, terminales):
    primero={}

    def obtener_primero(simbolo):
        if simbolo in primero:
            return primero[simbolo]
        primero[simbolo]=set()
        if simbolo in terminales or simbolo=='ε':
            primero[simbolo].add(simbolo)
            return primero[simbolo]

        for produccion in gramatica.get(simbolo, []):
            for s in produccion:
                primeros_s=obtener_primero(s)
                primero[simbolo].update(primeros_s - {'ε'})
                if 'ε' not in primeros_s:
                    break
            else:
                primero[simbolo].add('ε')
        return primero[simbolo]

    todos_los_simbolos=set()
    for producciones in gramatica.values():
        for produccion in producciones:
            todos_los_simbolos.update(produccion)
    todos_los_simbolos.update(gramatica.keys())  

    for simbolo in todos_los_simbolos:
        obtener_primero(simbolo)

    return primero


def Siguientes(gramatica, primero, simbolo_inicial):
    siguiente={}
    for nt in gramatica:
        siguiente[nt]=set()
    siguiente[simbolo_inicial].add('$')

    cambiado=True
    while cambiado:
        cambiado=False
        for nt in gramatica:
            for produccion in gramatica[nt]:
                for i, simbolo in enumerate(produccion):
                    if simbolo in gramatica:  
                        rest=produccion[i+1:]
                        antes=len(siguiente[simbolo])

                        if rest:
                            primero_rest=set()
                            for s in rest:
                                primeros_s=primero[s]
                                primero_rest.update(primeros_s-{'ε'})
                                if 'ε' not in primeros_s:
                                    break
                            else:
                                primero_rest.add('ε')
                            siguiente[simbolo].update(primero_rest-{'ε'})
                            if 'ε' in primero_rest:
                                siguiente[simbolo].update(siguiente[nt])
                        else:
                            siguiente[simbolo].update(siguiente[nt])

                        if len(siguiente[simbolo])>antes:
                            cambiado=True
    return siguiente


def Predicciones(gramatica, primero, siguiente):
    conjunto_prediccion={}

    for nt in gramatica:
        for prod in gramatica[nt]:
            regla=f"{nt} -> {' '.join(prod)}"
            pred=set()

            for s in prod:
                primeros_s=primero[s]
                pred.update(primeros_s-{'ε'})
                if 'ε' not in primeros_s:
                    break
            else:
                pred.add('ε')

            conjunto_prediccion[regla]=pred-{'ε'}
            if 'ε' in pred:
                conjunto_prediccion[regla].update(siguiente[nt])

    return conjunto_prediccion

if __name__=="__main__":
    nombre_archivo=input("Ingrese el archivo de la gramatica: ")
    gramatica=leer_gramatica(nombre_archivo)
    
    if gramatica:
        simbolo_inicial=list(gramatica.keys())[0]
        no_terminales=set(gramatica.keys())
        terminales=set()
        for producciones in gramatica.values():
            print(producciones)
            for prod in producciones:
                print(prod)
                for simbolo in prod:
                    print(simbolo)
                    if simbolo not in gramatica and simbolo!='ε':
                        terminales.add(simbolo)

        primero=Primeros(gramatica, terminales)
        siguiente=Siguientes(gramatica, primero, simbolo_inicial)
        prediccion=Predicciones(gramatica, primero, siguiente)

        print("\nPrimeros:")
        for pri in no_terminales:
            print(f"Primero({pri})= {primero[pri]}")

        print("\nSiguientes:")
        for sig in siguiente:
            print(f"Siguiente({sig})= {siguiente[sig]}")

        print("\nConjuntos de prediccion:")
        for regla in prediccion:
            print(f"{regla} {prediccion[regla]}")
    else:
        print("Gramática no valida.")

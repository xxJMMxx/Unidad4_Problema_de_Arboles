# Dado un árbol binario de búsqueda diseñar un método que liste los nodos del árbol
# ordenados descendentemente.


# Esta es la clase Nodo, que en su constructor tine la variable dato(el valor del nodo),
# además tiene la variable izquierda y derecha para que pueda tener nodos indicando la posiciòn a los
# hijos y asi sucesivamente.
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izquierda = None
        self.derecha = None


# Al instanciar está clase (Arbol), recibirá un valor(dato) que será la raiz
# En el constructor se indica que la raiz es igual a crear una nueva instancia de la clase Nodo
# que tiene como valor de entrada el dato de la clase Arbol.
class Arbol:
    def __init__(self, dato):
        self.raiz = Nodo(dato)

    # En este método se agregan los nodos hijos tomando como base la raiz, para decidir
    # en que dirección (izquierda o derecha) posicionarse.
    # Sigue la logica de un arbol binario de búsqueda es menor ira a la izquierda y si
    # es mayor ira a la derecha
    # Para eso recibe el nodo(raiz) y el dato que se quiere agregar
    def agregarNodos(self, nodo, dato):
        # Hacemos uso de un if para poner la condición: si el "dato"(que se quiere agregar)
        # es menor al "dato" que contiene el nodo(raiz o padre) y además que se cumple la siguiente
        # condición del segundo if: si el nodo ala izquierda está disponible, entonces se crea un
        # nuevo nodo, donde se agrega el valor que contiene "dato".

        # De lo contrario(si ya hay un nodo a la izquierda), o sea si el segundo if no se cumple,
        # hacemos uso de la recursividad para que el método se llame asi mismo, pero esta vez
        # tomara el valor del nodo a la izquierda y volverá pasar por el condicional(if)
        # hasta que encuentre un lugar disponible a la izquierda, en caso de que siga siendo
        # menor que el nodo padre.

        # De lo contrario(si "dato" es mayor al nodo padre), haciendo uso de un tercer if
        # que se encuentra dentro del "else" del primer condicional if, se busca un lugar disponible
        # a la derecha, si lo encuentra crea un nuevo nodo y le asigna el valor del dato.
        # De lo contrario(else) se usa de nuevo recursividad para volver a empezar, pero esta vez
        # con el valor del nodo con el que nos topamos a la derecha
        if dato < nodo.dato:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(dato)
            else:
                self.agregarNodos(nodo.izquierda, dato)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(dato)
            else:
                self.agregarNodos(nodo.derecha, dato)

    # Para este método el funcionamiento es similar a un recorrido in orden solo que aqui primero
    # se visita el nodo derecho luego se procesa la raiz y por último nodo izquierdo.
    # Entones empezamos con un if que tiene la condición: si nodo no es nada, o sea si no está vacío
    # se recorre el lado derecho recursivamente
    # Cuando no quede más nodos a la izquierda se procesa la raiz y se recorre la derecha
    # recursivamente, hasta que se rompa la condición y no queden más nodos.
    def listadoDescendente(self, nodo):
        if nodo is not None:
            self.listadoDescendente(nodo.derecha)
            print(nodo.dato, end=", ")
            self.listadoDescendente(nodo.izquierda)

    # Se invoca el método "agregarNodos" y asignamos el valor del nodo raiz y el valor
    # del dato para crear un nuevo nodo
    def agregarDatosArbol(self, dato):
        self.agregarNodos(self.raiz, dato)

    # Aqui usamos un print para mostrar un mensaje luego invocamos al método listadoDescendente
    # que tiene el resultado final.
    def listaNodos(self):
        print("Lista de nodos ordenados descendentemente: ")
        self.listadoDescendente(self.raiz)



# Instancia y valores para crear el arbol
arbol = Arbol(55)  # Raiz del arbol(5)
arbol.agregarDatosArbol(19)
arbol.agregarDatosArbol(70)
arbol.agregarDatosArbol(18)
arbol.agregarDatosArbol(24)
arbol.agregarDatosArbol(16)
arbol.agregarDatosArbol(45)
arbol.agregarDatosArbol(88)
arbol.agregarDatosArbol(23)
arbol.agregarDatosArbol(87)
arbol.agregarDatosArbol(66)
arbol.agregarDatosArbol(26)
arbol.agregarDatosArbol(18)
arbol.agregarDatosArbol(61)
arbol.agregarDatosArbol(99)
arbol.agregarDatosArbol(46)
arbol.listaNodos()

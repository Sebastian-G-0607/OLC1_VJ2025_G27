from backend.src.Interprete.nodes.instrucciones.Break import Break
from backend.src.Interprete.visitor_object.visitorBase import Visitor
from backend.src.Interprete.nodes.Nodo import Nodo

class VisitorGraph(Visitor):
    def __init__(self, Arbol):
        self.Arbol = Arbol
        self.dot = []
        self.counter = 0
        self.dot.append('digraph G {')
        self.dot.append('\tnode [shape=ellipse];')
        self.dot.append('\tordering="out";')
        self.dot.append('\tcompound=true;')
        self.dot.append('\tnodoRaiz [label="Programa"];')
        self.dot.append('\tnodoSentencias [label="Sentencias"];')
        self.dot.append('\tnodoRaiz -> nodoSentencias;')  # Conectar el nodo raíz al primer nodo

    def generar_dot(self, arbol):
        self.dot.append("}")
        return "\n".join(self.dot)
    
    def appendInstruccion(self, instruccion):
        self.dot.append(f'\tnodoSentencias -> {instruccion};')
        self.counter += 1

    # VISITA UN NÚMERO Y DEVUELVE SU VALOR
    def visit_Nativo(self, nodo: Nodo):
        #DEFINO EL NODO
        codigo = f'\tnode{self.counter} [label="{nodo.valor}"];'
        self.dot.append(codigo)

        #RETORNO EL NOMBRE DEL NODO
        retorno = f'node{self.counter}'
        self.counter += 1
        return retorno

    def visit_Suma(self, nodo: Nodo):
        #PRIMERO, SE GUARDA EL VALOR DE LA IZQUIERDA Y DERECHA
        valorIzq = nodo.izquierda.accept(self)
        valorDer = nodo.derecha.accept(self)

        #SE DEFINE EL NODO RAIZ DE LA SUMA
        raiz = f'node{self.counter}'
        self.dot.append(f'\tnode{self.counter} [label="+"];')
        
        #SE RETORNA EL CÓDIGO DE LA SUMA
        codigo = ''
        codigo += f'\tnode{self.counter} -> {valorIzq};\n'
        codigo += f'\tnode{self.counter} -> {valorDer};\n'
        self.dot.append(codigo)

        #SE INCREMENTA EL CONTADOR Y SE RETORNA EL CÓDIGO
        self.counter += 1
        return raiz
    
    def visit_Resta(self, nodo: Nodo):
        #PRIMERO, SE GUARDA EL VALOR DE LA IZQUIERDA Y DERECHA
        valorIzq = nodo.izquierda.accept(self)
        valorDer = nodo.derecha.accept(self)

        #SE DEFINE EL NODO RAIZ DE LA SUMA
        raiz = f'node{self.counter}'
        self.dot.append(f'\tnode{self.counter} [label="-"];')
        
        #SE RETORNA EL CÓDIGO DE LA SUMA
        codigo = ''
        codigo += f'\tnode{self.counter} -> {valorIzq};\n'
        codigo += f'\tnode{self.counter} -> {valorDer};\n'
        self.dot.append(codigo)

        #SE INCREMENTA EL CONTADOR Y SE RETORNA EL CÓDIGO
        self.counter += 1
        return raiz
    
    def visit_Multiplicacion(self, nodo: Nodo):
        #PRIMERO, SE GUARDA EL VALOR DE LA IZQUIERDA Y DERECHA
        valorIzq = nodo.izquierda.accept(self)
        valorDer = nodo.derecha.accept(self)

        #SE DEFINE EL NODO RAIZ DE LA MULTIPLICACIÓN
        raiz = f'node{self.counter}'
        self.dot.append(f'\tnode{self.counter} [label="*"];')

        #SE RETORNA EL CÓDIGO DE LA MULTIPLICACIÓN
        codigo = ''
        codigo += f'\tnode{self.counter} -> {valorIzq};\n'
        codigo += f'\tnode{self.counter} -> {valorDer};\n'
        self.dot.append(codigo)

        #SE INCREMENTA EL CONTADOR Y SE RETORNA EL CÓDIGO
        self.counter += 1
        return raiz
    
    def visit_Division(self, nodo: Nodo):
        #PRIMERO, SE GUARDA EL VALOR DE LA IZQUIERDA Y DERECHA
        valorIzq = nodo.izquierda.accept(self)
        valorDer = nodo.derecha.accept(self)

        #SE DEFINE EL NODO RAIZ DE LA DIVISIÓN
        raiz = f'node{self.counter}'
        self.dot.append(f'\tnode{self.counter} [label="/"];')

        #SE RETORNA EL CÓDIGO DE LA DIVISIÓN
        codigo = ''
        codigo += f'\tnode{self.counter} -> {valorIzq};\n'
        codigo += f'\tnode{self.counter} -> {valorDer};\n'
        self.dot.append(codigo)

        #SE INCREMENTA EL CONTADOR Y SE RETORNA EL CÓDIGO
        self.counter += 1
        return raiz
    
    def visit_Potencia(self, nodo: Nodo):
        #PRIMERO, SE GUARDA EL VALOR DE LA IZQUIERDA Y DERECHA
        valorIzq = nodo.izquierda.accept(self)
        valorDer = nodo.derecha.accept(self)

        #SE DEFINE EL NODO RAIZ DE LA POTENCIA
        raiz = f'node{self.counter}'
        self.dot.append(f'\tnode{self.counter} [label="**"];')

        #SE RETORNA EL CÓDIGO DE LA POTENCIA
        codigo = ''
        codigo += f'\tnode{self.counter} -> {valorIzq};\n'
        codigo += f'\tnode{self.counter} -> {valorDer};\n'
        self.dot.append(codigo)

        #SE INCREMENTA EL CONTADOR Y SE RETORNA EL CÓDIGO
        self.counter += 1
        return raiz
    
    def visit_Umenos(self, nodo: Nodo):
        #PRIMERO, SE GUARDA EL VALOR DEL NODO
        valor = nodo.expresion.accept(self)

        #SE DEFINE EL NODO RAIZ DEL U-MENOS
        raiz = f'node{self.counter}'
        self.dot.append(f'\tnode{self.counter} [label="-"];')

        #SE RETORNA EL CÓDIGO DEL U-MENOS
        codigo = f'\tnode{self.counter} -> {valor};\n'
        self.dot.append(codigo)
        self.counter += 1
        return raiz
    
    def visit_Modulo(self, nodo: Nodo):
        #PRIMERO, SE GUARDA EL VALOR DE LA IZQUIERDA Y DERECHA
        valorIzq = nodo.izquierda.accept(self)
        valorDer = nodo.derecha.accept(self)

        #SE DEFINE EL NODO RAIZ DE LA DIVISIÓN
        raiz = f'node{self.counter}'
        self.dot.append(f'\tnode{self.counter} [label="%"];')

        #SE RETORNA EL CÓDIGO DE LA DIVISIÓN
        codigo = ''
        codigo += f'\tnode{self.counter} -> {valorIzq};\n'
        codigo += f'\tnode{self.counter} -> {valorDer};\n'
        self.dot.append(codigo)

        #SE INCREMENTA EL CONTADOR Y SE RETORNA EL CÓDIGO
        self.counter += 1
        return raiz
    
    def visit_IgualQue(self, nodo: Nodo):
        #PRIMERO, SE GUARDA EL VALOR DE LA IZQUIERDA Y DERECHA
        valorIzq = nodo.izquierda.accept(self)
        valorDer = nodo.derecha.accept(self)

        #SE DEFINE EL NODO RAIZ DE LA IGUALDAD
        raiz = f'node{self.counter}'
        self.dot.append(f'\tnode{self.counter} [label="=="];')

        #SE RETORNA EL CÓDIGO DE LA IGUALDAD
        codigo = ''
        codigo += f'\tnode{self.counter} -> {valorIzq};\n'
        codigo += f'\tnode{self.counter} -> {valorDer};\n'
        self.dot.append(codigo)

        #SE INCREMENTA EL CONTADOR Y SE RETORNA EL CÓDIGO
        self.counter += 1
        return raiz
    
    def visit_DiferenteQue(self, nodo: Nodo):
        #PRIMERO, SE GUARDA EL VALOR DE LA IZQUIERDA Y DERECHA
        valorIzq = nodo.izquierda.accept(self)
        valorDer = nodo.derecha.accept(self)

        #SE DEFINE EL NODO RAIZ DE LA DIFERENCIA
        raiz = f'node{self.counter}'
        self.dot.append(f'\tnode{self.counter} [label="!="];')

        #SE RETORNA EL CÓDIGO DE LA DIFERENCIA
        codigo = ''
        codigo += f'\tnode{self.counter} -> {valorIzq};\n'
        codigo += f'\tnode{self.counter} -> {valorDer};\n'
        self.dot.append(codigo)

        #SE INCREMENTA EL CONTADOR Y SE RETORNA EL CÓDIGO
        self.counter += 1
        return raiz
    
    def visit_MayorQue(self, nodo: Nodo):
        #PRIMERO, SE GUARDA EL VALOR DE LA IZQUIERDA Y DERECHA
        valorIzq = nodo.izquierda.accept(self)
        valorDer = nodo.derecha.accept(self)

        #SE DEFINE EL NODO RAIZ DEL MAYOR QUE
        raiz = f'node{self.counter}'
        self.dot.append(f'\tnode{self.counter} [label=">"];')

        #SE RETORNA EL CÓDIGO DEL MAYOR QUE
        codigo = ''
        codigo += f'\tnode{self.counter} -> {valorIzq};\n'
        codigo += f'\tnode{self.counter} -> {valorDer};\n'
        self.dot.append(codigo)

        #SE INCREMENTA EL CONTADOR Y SE RETORNA EL CÓDIGO
        self.counter += 1
        return raiz
    
    def visit_MayorIgualQue(self, nodo: Nodo):
        #PRIMERO, SE GUARDA EL VALOR DE LA IZQUIERDA Y DERECHA
        valorIzq = nodo.izquierda.accept(self)
        valorDer = nodo.derecha.accept(self)

        #SE DEFINE EL NODO RAIZ DEL MAYOR IGUAL QUE
        raiz = f'node{self.counter}'
        self.dot.append(f'\tnode{self.counter} [label=">="];')

        #SE RETORNA EL CÓDIGO DEL MAYOR IGUAL QUE
        codigo = ''
        codigo += f'\tnode{self.counter} -> {valorIzq};\n'
        codigo += f'\tnode{self.counter} -> {valorDer};\n'
        self.dot.append(codigo)

        #SE INCREMENTA EL CONTADOR Y SE RETORNA EL CÓDIGO
        self.counter += 1
        return raiz
    
    def visit_MenorQue(self, nodo: Nodo):
        #PRIMERO, SE GUARDA EL VALOR DE LA IZQUIERDA Y DERECHA
        valorIzq = nodo.izquierda.accept(self)
        valorDer = nodo.derecha.accept(self)

        #SE DEFINE EL NODO RAIZ DEL MENOR QUE
        raiz = f'node{self.counter}'
        self.dot.append(f'\tnode{self.counter} [label="<"];')

        #SE RETORNA EL CÓDIGO DEL MENOR QUE
        codigo = ''
        codigo += f'\tnode{self.counter} -> {valorIzq};\n'
        codigo += f'\tnode{self.counter} -> {valorDer};\n'
        self.dot.append(codigo)

        #SE INCREMENTA EL CONTADOR Y SE RETORNA EL CÓDIGO
        self.counter += 1
        return raiz
    
    def visit_MenorIgualQue(self, nodo: Nodo):
        #PRIMERO, SE GUARDA EL VALOR DE LA IZQUIERDA Y DERECHA
        valorIzq = nodo.izquierda.accept(self)
        valorDer = nodo.derecha.accept(self)

        #SE DEFINE EL NODO RAIZ DEL MENOR IGUAL QUE
        raiz = f'node{self.counter}'
        self.dot.append(f'\tnode{self.counter} [label="<="];')

        #SE RETORNA EL CÓDIGO DEL MENOR IGUAL QUE
        codigo = ''
        codigo += f'\tnode{self.counter} -> {valorIzq};\n'
        codigo += f'\tnode{self.counter} -> {valorDer};\n'
        self.dot.append(codigo)

        #SE INCREMENTA EL CONTADOR Y SE RETORNA EL CÓDIGO
        self.counter += 1
        return raiz
    
    def visit_And(self, nodo: Nodo):
        #PRIMERO, SE GUARDA EL VALOR DE LA IZQUIERDA Y DERECHA
        valorIzq = nodo.izquierda.accept(self)
        valorDer = nodo.derecha.accept(self)

        #SE DEFINE EL NODO RAIZ DEL AND
        raiz = f'node{self.counter}'
        self.dot.append(f'\tnode{self.counter} [label="&&"];')

        #SE RETORNA EL CÓDIGO DEL AND
        codigo = ''
        codigo += f'\tnode{self.counter} -> {valorIzq};\n'
        codigo += f'\tnode{self.counter} -> {valorDer};\n'
        self.dot.append(codigo)

        #SE INCREMENTA EL CONTADOR Y SE RETORNA EL CÓDIGO
        self.counter += 1
        return raiz
    
    def visit_Or(self, nodo: Nodo):
        #PRIMERO, SE GUARDA EL VALOR DE LA IZQUIERDA Y DERECHA
        valorIzq = nodo.izquierda.accept(self)
        valorDer = nodo.derecha.accept(self)

        #SE DEFINE EL NODO RAIZ DEL OR
        raiz = f'node{self.counter}'
        self.dot.append(f'\tnode{self.counter} [label="||"];')

        #SE RETORNA EL CÓDIGO DEL OR
        codigo = ''
        codigo += f'\tnode{self.counter} -> {valorIzq};\n'
        codigo += f'\tnode{self.counter} -> {valorDer};\n'
        self.dot.append(codigo)

        #SE INCREMENTA EL CONTADOR Y SE RETORNA EL CÓDIGO
        self.counter += 1
        return raiz
    
    def visit_Not(self, nodo: Nodo):
        #PRIMERO, SE GUARDA EL VALOR DEL NODO
        valor = nodo.expresion.accept(self)

        #SE DEFINE EL NODO RAIZ DEL U-MENOS
        raiz = f'node{self.counter}'
        self.dot.append(f'\tnode{self.counter} [label="!"];')

        #SE RETORNA EL CÓDIGO DEL U-MENOS
        codigo = f'\tnode{self.counter} -> {valor};\n'
        self.dot.append(codigo)
        self.counter += 1
        return raiz
    
    def visit_Xor(self, nodo: Nodo):
        #PRIMERO, SE GUARDA EL VALOR DE LA IZQUIERDA Y DERECHA
        valorIzq = nodo.izquierda.accept(self)
        valorDer = nodo.derecha.accept(self)

        #SE DEFINE EL NODO RAIZ DEL XOR
        raiz = f'node{self.counter}'
        self.dot.append(f'\tnode{self.counter} [label="^"];')

        #SE RETORNA EL CÓDIGO DEL XOR
        codigo = ''
        codigo += f'\tnode{self.counter} -> {valorIzq};\n'
        codigo += f'\tnode{self.counter} -> {valorDer};\n'
        self.dot.append(codigo)

        #SE INCREMENTA EL CONTADOR Y SE RETORNA EL CÓDIGO
        self.counter += 1
        return raiz
    
    def visit_Asignacion(self, nodo: Nodo):
        valor = nodo.valor.accept(self)
        #PRIMERO, SE GUARDA EL VALOR DE LA IZQUIERDA Y DERECHA
        raiz = f'node{self.counter}'

        self.dot.append(f'\tnodeId{nodo.id}{self.counter} [label="{nodo.id}"];')
        self.dot.append(f'\tnode{self.counter} [label="="];')
        #SE DEFINE EL NODO RAIZ DE LA IGUALDAD

        id = f'nodeId{nodo.id}{self.counter}'

        #SE RETORNA EL CÓDIGO DE LA IGUALDAD
        codigo = ''
        codigo += f'\tnode{self.counter} -> {id};\n'
        codigo += f'\tnode{self.counter} -> {valor};\n'
        self.dot.append(codigo)

        #SE INCREMENTA EL CONTADOR Y SE RETORNA EL CÓDIGO
        self.counter += 1
        return raiz
    
    def visit_AccesoVariable(self, nodo: Nodo):
        #DEFINO EL NODO
        codigo = f'\tnode{self.counter} [label="{nodo.id}"];'
        self.dot.append(codigo)

        #RETORNO EL NOMBRE DEL NODO
        retorno = f'node{self.counter}'
        self.counter += 1
        return retorno
    
    def visit_Declaracion(self, nodo: Nodo):
        #PRIMERO, SE GUARDA EL VALOR DE LA IZQUIERDA Y DERECHA
        if nodo.valor is None:
            raiz = f'node{self.counter}'
            id = f'nodeId{nodo.id}{self.counter}'

            self.dot.append(f'\t{raiz} [label="{nodo.tipoDato}"];')
            self.dot.append(f'\t{id} [label="{nodo.id}"];')

            codigo = f'\t{raiz} -> {id};\n'
            self.dot.append(codigo)

            return raiz

        valor = nodo.valor.accept(self)

        #SE DEFINE EL NODO RAIZ DE LA IGUALDAD
        raiz = f'node{self.counter}'
        self.dot.append(f'\tnode{self.counter} [label="{nodo.tipoDato}"];')
        self.dot.append(f'\tnodeId{nodo.id}{self.counter} [label="{nodo.id}"];')

        id = f'nodeId{nodo.id}{self.counter}'

        #SE RETORNA EL CÓDIGO DE LA IGUALDAD
        codigo = ''
        codigo += f'\tnode{self.counter} -> {id};\n'
        codigo += f'\tnode{self.counter} -> {valor};\n'
        self.dot.append(codigo)

        #SE INCREMENTA EL CONTADOR Y SE RETORNA EL CÓDIGO
        self.counter += 1
        return raiz

    def visit_Incremento(self, nodo: Nodo):
        #PRIMERO, GUARDO LA RAIZ ++
        raiz = f'node{self.counter}'
        self.dot.append(f'\tnode{self.counter} [label="++"];')

        # LUEGO, CREO UN NODO CON EL ATRIBUTO .variable del nodo
        variable = f'nodeVariable{nodo.variable}{self.counter}'
        self.dot.append(f'\t{variable} [label="{nodo.variable}"];')

        self.dot.append(f'\t{raiz} -> {variable};')
        #INCREMENTO EL CONTADOR
        self.counter += 1

        #RETORNO LA RAIZ DEL INCREMENTO
        return raiz

    def visit_Decremento(self, nodo: Nodo):
        #PRIMERO, GUARDO LA RAIZ --
        raiz = f'node{self.counter}'
        self.dot.append(f'\tnode{self.counter} [label="--"];')

        # LUEGO, CREO UN NODO CON EL ATRIBUTO .variable del nodo
        variable = f'nodeVariable{nodo.variable}{self.counter}'
        self.dot.append(f'\t{variable} [label="{nodo.variable}"];')

        self.dot.append(f'\t{raiz} -> {variable};')
        #INCREMENTO EL CONTADOR
        self.counter += 1

        #RETORNO LA RAIZ DEL DECREMENTO
        return raiz

    def visit_If(self, nodo: Nodo):
        condicion = nodo.condicion.accept(self)

        raiz = f'node{self.counter}'
        self.counter += 1

        self.dot.append(f'\t{raiz} [label="If"];')
        self.dot.append(f'\t{raiz} -> {condicion};')
        self.dot.append(f'\t{raiz}If [label="Then"];')
        self.dot.append(f'\t{raiz} -> {raiz}If;')

        for instruccion in nodo.instrucciones:
            instrucciones = instruccion.accept(self)
            self.dot.append(f'\t{raiz}If -> {instrucciones};')

        return raiz

    def visit_Else(self, nodo: Nodo):
        raiz = f'node{self.counter}'
        self.counter += 1

        self.dot.append(f'\t{raiz} [label="Else"];')

        for instruccion in nodo.instrucciones:
            instrucciones = instruccion.accept(self)
            self.dot.append(f'\t{raiz} -> {instrucciones};')

        return raiz
    
    def visit_IfElse(self, nodo: Nodo):
        condicion = nodo.condicion.accept(self)

        raiz = f'node{self.counter}'
        self.counter += 1

        self.dot.append(f'\t{raiz} [label="If"];')
        self.dot.append(f'\t{raiz}Punto [label="Condición"];')
        self.dot.append(f'\t{raiz} -> {raiz}Punto;')
        self.dot.append(f'\t{raiz}Punto -> {condicion};')
        self.dot.append(f'\t{raiz}Ins [label="Then"];')
        self.dot.append(f'\t{raiz}Punto -> {raiz}Ins;')

        for instruccion in nodo.instrucciones_if:
            instrucciones = instruccion.accept(self)
            self.dot.append(f'\t{raiz}Ins -> {instrucciones};')

        if nodo.instrucciones_else:
            nodoElse = nodo.instrucciones_else.accept(self)
            self.dot.append(f'\t{raiz} -> {nodoElse};')

        return raiz
    
    def visit_IfElseIf(self, nodo: Nodo):
        condicion = nodo.condicion.accept(self)

        raiz = f'node{self.counter}'
        self.counter += 1

        self.dot.append(f'\t{raiz} [label="If"];')
        self.dot.append(f'\t{raiz}Punto [label="Condición"];')
        self.dot.append(f'\t{raiz} -> {raiz}Punto;')
        self.dot.append(f'\t{raiz}Else [label="Else"];')
        self.dot.append(f'\t{raiz} -> {raiz}Else;')
        self.dot.append(f'\t{raiz}Punto -> {condicion};')
        self.dot.append(f'\t{raiz}Ins [label="Then"];')
        self.dot.append(f'\t{raiz}Punto -> {raiz}Ins;')

        for instruccion in nodo.instrucciones_if:
            instrucciones = instruccion.accept(self)
            self.dot.append(f'\t{raiz}Ins -> {instrucciones};')

        if nodo.elseif:
            nodoElseIf = nodo.elseif.accept(self)
            self.dot.append(f'\t{raiz}Else -> {nodoElseIf};')

        return raiz
    
    def visit_Case(self, nodo: Nodo):
        condicion = nodo.condicion.accept(self)
        raiz = f'node{self.counter}'
        self.counter += 1
        self.dot.append(f'\t{raiz} [label="Case"];')
        self.dot.append(f'\t{raiz} -> {condicion};')
        self.dot.append(f'\t{raiz}Ins [label="Then"];')
        self.dot.append(f'\t{raiz} -> {raiz}Ins;')

        for instruccion in nodo.instrucciones_case:
            instruccionRaiz = instruccion.accept(self)
            self.dot.append(f'\t{raiz}Ins -> {instruccionRaiz};')

        return raiz

    def visit_Switch(self, nodo: Nodo):
        expresion = nodo.expresion.accept(self)
        raiz = f'node{self.counter}'
        self.counter += 1

        self.dot.append(f'\t{raiz} [label="Switch"];')
        self.dot.append(f'\t{raiz}Cases [label="Cases"];')
        self.dot.append(f'\t{raiz} -> {expresion};')
        self.dot.append(f'\t{raiz} -> {raiz}Cases;')

        for caso in nodo.lista_casos:
            if caso.condicion == 'default':
                self.dot.append(f'\t{raiz}Default [label="Default"];')
                self.dot.append(f'\t{raiz}Cases -> {raiz}Default;')
                for instruccion in caso.instrucciones_case:
                    instruccionRaiz = instruccion.accept(self)
                    self.dot.append(f'\t{raiz}Default -> {instruccionRaiz};')
                continue

            casoRaiz = caso.accept(self)
            self.dot.append(f'\t{raiz}Cases -> {casoRaiz};')

        return raiz
    
    def visit_While(self, nodo: Nodo):
        condition = nodo.condition.accept(self)
        raiz = f'node{self.counter}'
        self.counter += 1

        self.dot.append(f'\t{raiz} [label="While"];')
        self.dot.append(f'\t{raiz} -> {condition};')
        self.dot.append(f'\t{raiz}Do [label="Do"];')
        self.dot.append(f'\t{raiz} -> {raiz}Do;')
        for instruction in nodo.instructions:
            instructionRaiz = instruction.accept(self)
            self.dot.append(f'\t{raiz}Do -> {instructionRaiz};')

        return raiz

    def visit_For(self, nodo: Nodo):
        declaracion = nodo.declaracion.accept(self)
        condicion = nodo.condicion.accept(self)
        actualizacion = nodo.actualizacion.accept(self)

        raiz = f'node{self.counter}'
        self.counter += 1

        self.dot.append(f'\t{raiz} [label="For"];')
        self.dot.append(f'\t{raiz}Decl [label="Declaration"];')
        self.dot.append(f'\t{raiz} -> {raiz}Decl;')
        self.dot.append(f'\t{raiz}Decl -> {declaracion};')
        self.dot.append(f'\t{raiz}Cond [label="Condition"];')
        self.dot.append(f'\t{raiz} -> {raiz}Cond;')
        self.dot.append(f'\t{raiz}Cond -> {condicion};')
        self.dot.append(f'\t{raiz}Do [label="Do"];')
        self.dot.append(f'\t{raiz} -> {raiz}Do;')

        # self.dot.append(f'\t{raiz}Update [label="Update"];')
        # self.dot.append(f'\t{raiz} -> {raiz}Update;')
        for instruction in nodo.instrucciones:
            instructionRaiz = instruction.accept(self)
            self.dot.append(f'\t{raiz}Do -> {instructionRaiz};')
        self.dot.append(f'\t{raiz}Do -> {actualizacion};')
        return raiz

    def visit_DoWhile(self, nodo: Nodo):
        condicion = nodo.condicion.accept(self)
        raiz = f'node{self.counter}'
        self.counter += 1

        self.dot.append(f'\t{raiz} [label="Do"];')
        self.dot.append(f'\t{raiz}Ins [label="Instuctions"];')
        self.dot.append(f'\t{raiz} -> {raiz}Ins;')

        for instruction in nodo.instrucciones:
            instructionRaiz = instruction.accept(self)
            self.dot.append(f'\t{raiz}Ins -> {instructionRaiz};')

        self.dot.append(f'\t{raiz}Cond [label="While"];')
        self.dot.append(f'\t{raiz} -> {raiz}Cond;')
        self.dot.append(f'\t{raiz}Cond -> {condicion};')
        
        return raiz

    def visit_Break(self, nodo: Nodo):
        #DEFINO EL NODO
        codigo = f'\tnode{self.counter} [label="{nodo.valor}"];'
        self.dot.append(codigo)

        #RETORNO EL NOMBRE DEL NODO
        retorno = f'node{self.counter}'
        self.counter += 1
        return retorno
    
    def visit_Continue(self, nodo: Nodo):
        #DEFINO EL NODO
        codigo = f'\tnode{self.counter} [label="{nodo.valor}"];'
        self.dot.append(codigo)

        #RETORNO EL NOMBRE DEL NODO
        retorno = f'node{self.counter}'
        self.counter += 1
        return retorno

    def visit_Println(self, nodo: Nodo):
        #PRIMERO, SE GUARDA EL VALOR DEL NODO
        valor = nodo.expresion.accept(self)
        #SE DEFINE EL NODO RAIZ DEL PRINTLN
        raiz = f'node{self.counter}'
        self.dot.append(f'\tnode{self.counter} [label="Println"];')
        #SE RETORNA EL CÓDIGO DEL PRINTLN
        codigo = f'\tnode{self.counter} -> {valor};\n'
        self.dot.append(codigo)
        self.counter += 1
        return raiz
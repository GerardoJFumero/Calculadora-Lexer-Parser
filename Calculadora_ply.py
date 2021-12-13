import ply.lex as lex 
import ply.yacc as yacc 
import sys 

##lexer

#Se definen los nombres de los tokens al lexer 
tokens = [
    'INT',
    'FLOAT',
    'NAME',
    'PLUS',
    'MINUS',
    'DIVIDE',
    'MULTIPLY',
    'EQUALS',
    'LEFTPAR',
    'RIGHTPAR',
    'FIN'
]

#Se crean las funciones que permiten agregarle los valores a los tokens anteriores, tranformando los strings de entradas a cadenas.

#Función para números decimales
def t_FLOAT(t):
    r'\d+\.\d+' #permite la entrada de numeros (d+) seguido de un punto y numeros que representan decimales
    try:
        t.value = float(t.value)    #Permite medir el error según la diferencia en la variación del dato con respecto a su longitud
    except ValueError:
        print("El numero en decimales introducido es demasiado largo")
        t.value = 0
    return t

#Función para números enteros
def t_INT(t):
    r'\d+' #Permite la entrada sólo de números enteros sin decimales
    try: 
        t.value = int(t.value)
    except ValueError:
        print("El valor entero introducido es demasiado largo")
        t.value = 0
        

#funcion para asignar nombres a las variables 
def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z_0-9]'
    t.type = 'NAME'
    return t 

#Le asignamos reglas a nuestros tokens identificados en el primer paso
t_PLUS = r'\+'
t_MINUS = r'\-'
t_DIVIDE = r'\/'
t_MULTIPLY = r'\*'
t_EQUALS = r'\='
t_FIN = r'\;'
t_LEFTPAR = r'\('
t_RIGHTPAR = r'\)'

#usaremos esto para ignorar espacios entre los valores de la expresión
t_ignore = r'\t'

#funcion para señalar errores en la entrada por caracteres que no correspondan al lenguaje
def t_error(t):
    print("¡Syntax error!, el valor introducido no es permitido")
    print("Valor prohibido: '%s'" % t.value[0])
    t.lexer.skip(1)

##Lexer como analizador léxico
lexer = lex.lex()

##Parser

##se define la gramatica del parser

#Puede haber ambiguedad en las operaciones, por lo que se debe establecer la jerarquía de operaciones
#Mientras más abajo está, mayor jerarquía tiene
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'PLUS', 'DIVIDE'),
    ('left', 'LEFTPAR', 'RIGHTPAR'),
    ('right', 'UMINUS')
)

#Para el calculo puede haber una expresion o puede estar vacio
def p_calculo(p):
    '''
    calc: expression 
        | empty
    '''
    print (p[1])

#Se definen las operaciones 
def p_expression(p):
    '''
    expression: expression MULTIPLY expression
              | expression DIVIDE expression 
              | expression PLUS expression
              | expression MINUS expression 
    '''
    p[0]= (p[2],p[1],p[3])

#una expresión puede ser de tipo integer o float
def p_expressions_int_float(p):
    '''
    expression: INT
              | FLOAT 
    '''
    p[0]=p[1]

#Se definen las expresiones con los paréntesis
def p_expressions_parenthesis(p):
    'expression : LEFTPAR expression RIGTHPAR'
    p[0] = p[2]

#se define p[0] como vacio para guardar un resultado
def p_empty(p):
    '''
    empty : 
    '''
    p[0] = None 
W
#Si se llega a encontrar un error en las expresiones
def p_error(p):
    print("ERROR: Fallo en la entrada, operación no permitida")

parser = yacc.yacc()

entrada = open("./valores.txt", "r")
input = entrada.read()
print(input)
parser.pase(input)

while entrada==True:
    try:
        s = input('')
    except (EOFError):
        break
    parser.parse(s)
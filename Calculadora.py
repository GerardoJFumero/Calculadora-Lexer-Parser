import ply.lex as lex 
import ply.yacc as yacc
from math import factorial 
import sys 

##lexer

#Se definen los nombres de los tokens al lexer 
tokens = (
    'INT',
    'FLOAT',
    'PLUS',
    'MINUS',
    'DIVIDE',
    'MULTIPLY',
    'LEFTPAR',
    'RIGHTPAR',
    'CALCULATE',
    'RIGHTBRA',
    'LEFTBRA',
    'FACTORIAL',
    'FIN'
)

#Se crean las funciones que permiten agregarle los valores a los tokens anteriores, tranformando los strings de entradas a cadenas.

#Función para números decimales
def t_FLOAT(p):
    r'\d+\.\d+' #permite la entrada de numeros (d+) seguido de un punto y numeros que representan decimales
    try:
        p.value = float(p.value)    #Permite medir el error según la diferencia en la variación del dato con respecto a su longitud
    except ValueError:
        print("El numero en decimales introducido es demasiado largo")
        p.value = 0
    return p

#Función para números enteros
def t_INT(p):
    r'\d+' #Permite la entrada sólo de números enteros sin decimales
    try: 
        p.value = int(p.value)
    except ValueError:
        print("El valor entero introducido es demasiado largo")
        p.value = 0
    return p



#Le asignamos reglas a nuestros tokens identificados en el primer paso
t_PLUS = r'\+'
t_MINUS = r'\-'
t_DIVIDE = r'\/'
t_MULTIPLY = r'\*'
t_FIN = r'\;'
t_LEFTPAR = r'\('
t_RIGHTPAR = r'\)'
t_CALCULATE = r'Calcular'
t_RIGHTBRA = r'\]'
t_LEFTBRA = r'\['
t_FACTORIAL = r'\!'

#usaremos esto para ignorar espacios entre los valores de la expresión
t_ignore = " \p"

#funcion para señalar errores en la entrada por caracteres que no correspondan al lenguaje
def t_error(p):
    print("¡Syntax error!, el valor introducido no es permitido")
    print("Valor prohibido: '%s'" % p.value[0])
    p.lexer.skip(1)
    
def t_newline(p):
    r'\n+'
    p.lexer.lineno += p.value.count("\n")

##Lexer como analizador léxico
lexer = lex.lex()

##Parser

##se define la gramatica del parser

#Puede haber ambiguedad en las operaciones, por lo que se debe establecer la jerarquía de operaciones
#Mientras más abajo está, mayor jerarquía tiene
precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'FACTORIAL','PLUS', 'DIVIDE'),
    ('right', 'UMINUS')
)


#Para el calculo puede haber una expresion o puede estar vacio
def p_calculate(p):
    '''
    expressions  : expression expressions
                | expression 
                | empty
    '''

def p_solution(p):
    'expression : CALCULATE RIGHTBRA expression LEFTBRA FIN'
    print('Resultado: ' + str(p[3]))

#Se definen las operaciones 
def p_expression_solutions(p):
    '''
    expression  : expression MULTIPLY expression
                | expression DIVIDE expression 
                | expression PLUS expression
                | expression MINUS expression 
                | FACTORIAL expression
    '''
    if p[2] == '+': p[0] = p[1] + p[3]
    elif p[2] == '-': p[0] = p[1] - p[3]
    elif p[2] == '*': p[0] = p[1] * p[3]
    elif p[2] == '/': p[0] = p[1] / p[3]
    elif p[1] == '!':  p[0] =  factorial(p[2])

#Las expresiones puede ser de tipo integer o float
def p_expressions_int_float(p):
    '''
    expression  : INT
                | FLOAT 
    '''
    p[0]=p[1]
    
#Expresiones para números negativos
def p_negative(p):
    'expression : MINUS expression %prec UMINUS'
    p[0] = -p[2]

#Se definen las expresiones con los paréntesis
def p_expressions_parenthesis(p):
    'expression : LEFTPAR expression RIGHTPAR'
    p[0] = p[2]

#se define p[0] como vacio para guardar un resultado
def p_empty(p):
    '''
    empty : 
    '''
    p[0] = None 

#Si se llega a encontrar un error en las expresiones
def p_error(p):
    print("ERROR: Fallo en la entrada, operación no permitida")

parser = yacc.yacc()

p = open("./valores.txt", "r")
input = p.read()
print(input)
parser.parse(input)


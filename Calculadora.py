import ply.lex as lex 
import ply.yacc as yacc

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
    return t



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
t_ignore = " \t"

#funcion para señalar errores en la entrada por caracteres que no correspondan al lenguaje
def t_error(t):
    print("¡Syntax error!, el valor introducido no es permitido")
    print("Valor prohibido: '%s'" % t.value[0])
    t.lexer.skip(1)
    
def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

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
def p_calculat(t):
    '''
    expressions  : expression expressions
                | expression 
                | empty
    '''

def p_solutio(t):
    'expression : CALCULATE LEFTBRA expression RIGHTBRA FIN'
    print('Resultado: ' + str(t[3]))

#Se definen las operaciones 
def p_expression_solution(t):
    '''
    expression  : expression MULTIPLY expression
                | expression DIVIDE expression 
                | expression PLUS expression
                | expression MINUS expression 
                | FACTORIAL expression
    '''
    if t[2] == '+': t[0] = t[1] + t[3]
    elif t[2] == '-': t[0] = t[1] - t[3]
    elif t[2] == '*': t[0] = t[1] * t[3]
    elif t[2] == '/': t[0] = t[1] / t[3]
    elif t[1] == '!':  t[0] =  factorial(t[2])


#Función para calcular el factorial que recibe como parámetro t[2]
def factorial(n):
    factorial_total = 1
    while n > 1:
        factorial_total *= n
        n -= 1
    return factorial_total

    
#Las expresiones puede ser de tipo integer o float
def p_expressions_int_floa(t):
    '''
    expression  : INT
                | FLOAT 
    '''
    t[0]=t[1]
    
#Expresiones para números negativos
def p_negativ(t):
    'expression : MINUS expression %prec UMINUS'
    t[0] = -t[2]

#Se definen las expresiones con los paréntesis
def p_expressions_parenthesi(t):
    'expression : LEFTPAR expression RIGHTPAR'
    t[0] = t[2]

#se define t[0] como vacio para guardar un resultado
def p_empt(t):
    '''
    empty : 
    '''
    t[0] = None 

#Si se llega a encontrar un error en las expresiones
def p_error(t):
    print("ERROR: Fallo en la entrada, operación no permitida")

parser = yacc.yacc()

t = open("./valores.txt", "r")
input = t.read()
print(input)
parser.parse(input)


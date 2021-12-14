from os import error
import ply.lex as lex 
import ply.yacc as yacc
import math

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
    'SQRT',
    'SEN',
    'COS',
    'AREA',
    'COMA',
    'RADTODEG',
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
t_SQRT = r'sqrt'
t_SEN = r'sen'
t_COS = r'cos'
t_AREA = r'area'
t_COMA = r','
t_RADTODEG = r'radtodeg'


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
    ('left','FACTORIAL','MULTIPLY', 'DIVIDE', 'AREA', 'RADTODEG'),
    ('left', 'SQRT', 'SEN', 'COS'),
    ('left', 'RIGHTPAR', 'LEFTPAR'),
    ('right', 'UMINUS')
)


#Para el calculo puede haber una expresion o puede estar vacio
def p_calculat(t):
    '''
    expressions  : expression expressions
                | expression 
                | empty
    '''

#Para la lectura de entrada, especificamente el orden de las operaciones 
def p_solutio(t):
    'expression : CALCULATE LEFTBRA expression RIGHTBRA FIN'
    print('Resultado: ' + str(t[3]))

#Se definen las operaciones, dependiendo de la entrada y la operación establecida según nuestros token, devuelve el resultado.
def p_expression_solution(t):
    '''
    expression  : expression MULTIPLY expression
                | expression DIVIDE expression 
                | expression PLUS expression
                | expression MINUS expression 
                | FACTORIAL expression
                | SQRT LEFTPAR expression RIGHTPAR
                | SEN LEFTPAR expression RIGHTPAR
                | COS LEFTPAR expression RIGHTPAR
                | AREA LEFTPAR expression COMA expression RIGHTPAR
                | RADTODEG LEFTPAR expression RIGHTPAR
    '''
    if t[2] == '+': t[0] = t[1] + t[3]
    elif t[2] == '-': t[0] = t[1] - t[3]
    elif t[2] == '*': t[0] = t[1] * t[3]
    elif t[2] == '/': t[0] = t[1] / t[3]
    elif t[1] == '!':  t[0] =  factorial(t[2])
    elif t[1] == 'sqrt': t[0] = raiz(t[3])
    elif t[1] == 'sen': t[0] = senos(t[3])
    elif t[1] == 'cos': t[0] = cosenos(t[3])
    elif ((t[1] == 'area') and (t[4] == ',')): t[0] = area(t[3],t[5])
    elif t[1] == 'radtodeg': t[0] = radtodeg(t[3])
    

#Función para trasnformar radianes a grados sexagesimales
def radtodeg(a):
    deg=a*(180/math.pi)
    return round(deg,3)
    
    
#Función para el calculo del área de un cuadrado
def area(a,b):
    base=a
    altura=b
    return base*altura

#Función para transformar a angulos
def senos(a):
    angulo = math.radians(a)
    resultado = math.sin(angulo)
    return resultado

def cosenos(b):
    angulo = math.radians(b)
    resultado = math.cos(angulo)
    return round(resultado)

#Función para calcular el factorial que recibe como parámetro t[2]
def factorial(n):
    factorial_total = 1
    while n > 1:
        factorial_total *= n
        n -= 1
    return factorial_total

#Función para calcular la raiz cuadrada de un numero que recibe como parámetro t[3]
def raiz(numero):
    numero = numero*1.0
    if numero >= 0:
        p=numero
        i=0
        while i!=p:
            i=p
            p=(numero/p+p)/2
    else : 
        p = error
    return p

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


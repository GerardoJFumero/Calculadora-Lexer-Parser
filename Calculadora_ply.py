import ply.lex as lex 
import ply.yacc as yacc 
import sys 

#lexer 
#Se definen los nombres de los tokens al lexer 
tokens = [
    'INT',
    'FLOAT',
    'NAME',
    'PLUS',
    'MINUS',
    'DIVIDE',
    'MULTIPLY',
    'EQUALS'
]

#Se crean las funciones que permiten agregarle los valores a los tokens anteriores

#Función para números decimales
def t_FLOAT(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)    #Permite medir el error según la diferencia en la variación del dato con respecto a su longitud
    except ValueError:
        print("El numero en decimales introducido es demasiado largo")
        t.value = 0
    return t

#Función para números enteros
def t_INT(t):
    r'\d+'
    try: 
        t.value = int(t.value)
    except ValueError:
        print("El valor entero introducido es demasiado largo")
        t.value = 0
        
t_PLUS = r'\+'
t_MINUS = r'\-'
t_DIVIDE = r'\/'
t_MULTIPLY = r'\*'
t_EQUALS = r'\='

#usaremos esto para ignorar espacios entre los valores de la expresión
t_ignore = r' '

#funcion para transformar los valores de string a int 
def t_INT(t):
    r'\d'
    t.value = int(t.value)
    return t 

#funcion para transformar los valores de string a float 
def t_FLOAT(t):
    r'\d.\d'
    t.value = float(t.value)
    return t 

#funcion para asignar nombres a las variables 
def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z_0-9]'
    t.type = 'NAME'
    return t 


#funcion para señalar errores en la entrada
def t_error(t):
    print("Syntax error!")
    t.lexer.skip(1)

lexer = lex.lex()


##parser
##se define la gramatica del parser

#para el calculo puede haber una expresion o puede estar vacio
def p_calc(p):
    '''
    calc: expression 
        | empty
    '''
    print (p[1])

#se definen las operaciones 
def p_expressions(p):
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

#se define p[0] como vacio para guardar un resultado
def p_empty(p):
    '''
    empty : 
    '''
    p[0] = None 

##def p_error(p):

parser = yacc.yacc()

while True:
    try:
        s = input('')
    except (EOFError):
        break
    parser.parse(s)
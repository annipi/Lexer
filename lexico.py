#si esta en reser... devolver la misma cadena
#si no esta en reser.. o op.. y no tiene cosas raras ke ni siquiera sepeuden poner auqi jajaja por el analaizador lexico de pycharm) es un identificador
# si no esta dentreo de " " o '' no le haga lower
# analice antes de hace rle lower
#real se separa por . no por ,
import sys

tokens = {'algoritmo':'algoritmo',
        'finalgoritmo':'finalgoritmo',
        'proceso':'proceso',
        'finproceso':'finproceso',
        'como':'como',
        'verdadero':'verdadero',
        'falso':'falso',
        'definir':'definir',
        'leer':'leer',
        'escribir':'escribir',
        'esperar':'esperar',
        'dimension':'dimension',
        'numero':'numero',
        'real':'real',
        'entero':'entero',
        'numerico':'numerico',
        'logico':'logico',
        'caracter':'caracter',
        'texto':'texto',
        'cadena':'cadena',
        'mientras':'mientras',
        'finsi':'finsi',
        '~':'token_neg',
        'no':'token_neg',
        '=':'token_igual',
        '<-':'token_asig',
        '<>':'token_dif',
        '<':'token_menor',
        '>':'token_mayor',
        '<=':'token_menor_igual',
        '>=':'token_mayor_igual',
        '+':'token_mas',
        '-':'token_menos',
        '/':'token_div',
        '*':'token_mul',
        '%':'token_mod',
        'mod':'token_mod',
        ';':'token_pyc',
        ':':'token_dosp',
        '(':'token_par_izq',
        ')':'token_par_der',
        '[':'token_cor_izq',
        ']':'token_cor_der',
        '|':'token_o',
        'o':'token_o',
        '&':'token_y',
        'y':'token_y',
        ',':'token_coma',
        '^':'token_pot'}

lst = sys.stdin.readlines()

print lst
row = 0
col = 0
for li in lst:
    l = (li.strip()).lower()
    row+=1
    if ' ' in l:
        l_tmp = l.split(' ')
        for lt in l_tmp:
            if lt in tokens:
                print '<'+tokens[lt]+','+str(row)+','+'>'
            else:
                print '<'+'id'+','+lt+','+str(row)+','+'>'
    elif l in tokens:
        print '<'+tokens[l]+','+str(row)+','+'>'
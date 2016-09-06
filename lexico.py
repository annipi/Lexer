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
        '^':'token_pot',
        '\'':'token_cadena',
        '\"':'token_cadena'}
# \\ -> Son comentarios en PSeInt
alpha_list = ['_', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

operators_list = ['~', '=', '<-', '<>', '<', '>', '<=', '>=', '+', '-', '/', '*', '%', ';', ':', '(', ')', '[', ']', '|', '&', ',', '^']

numbers_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

lst = sys.stdin.readlines()
print lst

row = 0
li = 0
while li < len(lst):
    l = lst[li].lower()
    # print '$$ La cadena de entrada es: %s' % l
    row += 1
    lc = 0
    while l[lc:lc+1] != '\n' and lc < len(l):
        # print '#'+l[lc:lc+1] #Para ver cada caracter que se esta analizando l[lc:lc+2]
        if l[lc] == ' ':
            pass
        elif l[lc:lc+2] == '//':
            lc += 1
            break
        # Cadenas que contengan con '
        elif l[lc] == '\'':
            strings1 = l[lc + 1:len(l)]
            string1 = ''
            for strchar1 in strings1:
                if strchar1 == '\'':
                    print '<'+tokens[strchar1] + ',' + string1 + ',' + str(row) + ',' + str(lc + 1) + '>'
                    lc += len(string1)
                    break
                string1 += strchar1
        # Cadenas que contengan con "
        elif l[lc] == '\"':
            strings2 = l[lc + 1:len(l)]
            string2 = ''
            for strchar2 in strings2:
                if strchar2 == '\"':
                    print '<'+tokens[strchar2] + ',' + string2 + ',' + str(row) + ',' + str(lc + 1) + '>'
                    lc += len(string2)
                    break
                string2 += strchar2
        # Cadenas que contengan con [a-z] o '_'
        elif l[lc] in alpha_list:
            chars = l[lc:len(l)]
            char = ''
            for char_i in xrange(len(chars)):
                if chars[char_i] in alpha_list:
                    char += chars[char_i]
                elif chars[char_i] == ' ' or chars[char_i:char_i+2] == '\n' or chars[char_i] in operators_list:
                    if char in tokens:
                        print '<'+tokens[l[lc:lc + char_i]] + ',' + str(row) + ',' + str(lc + 1) + '>'
                    else:
                        print '<'+'id'+','+ l[lc:lc + char_i] + ',' + str(row) + ',' + str(lc + 1) + '>'
                    lc += len(char)
                    break
                else:
                    print ('>>> Error lexico (linea: %s, posicion: %s)') % (row, lc)
                    break
        # Cadenas que contengan con [0-9]
        elif l[lc] in numbers_list:
            flag_point = False
            digits = l[lc:len(l)]
            real_or_int = ''
            for digit in xrange(len(digits)):
                if digits[digit] in numbers_list:
                    real_or_int += digits[digit]
                elif digits[digit] == '.' and not flag_point:
                    real_or_int += digits[digit]
                    flag_point = True
                elif digits[digit] == '.' and flag_point:
                    lc = len(l)
                    print ('>>> Error lexico (linea: %s, posicion: %s)') % (row, digit+1)
                    break
                elif digits[digit] == ' ' or digits[digit:digit+2] == '\n' or digits[digit] in operators_list:
                    if '.' in real_or_int:
                        print '<'+'token_real'+',' + real_or_int + ',' + str(row) + ',' + str(lc + 1) + '>'
                    else:
                        print '<'+'token_entero'+',' + real_or_int + ',' + str(row) + ',' + str(lc + 1) + '>'
                    lc += len(real_or_int)
                    break
                else:
                    lc = len(l)
                    print ('>>> Error lexico (linea: %s, posicion: %s)') % (row, lc)
                    break
        # Cadenas que contengan con operadores
        elif l[lc] in operators_list:
            if l[lc] == '<':
                if l[lc+1] == '-':
                    print '<'+tokens[l[lc:lc+2]] + ',' + l[lc:lc+2] + ',' + str(row) + ',' + str(lc + 1) + '>'
                    lc += len(l[lc])
                elif l[lc+1] == '>':
                    print '<'+tokens[l[lc:lc+2]] + ',' + l[lc:lc+2] + ',' + str(row) + ',' + str(lc + 1) + '>'
                    lc += len(l[lc])
                elif l[lc+1] == '=':
                    print '<'+tokens[l[lc:lc+2]] + ',' + l[lc:lc+2] + ',' + str(row) + ',' + str(lc + 1) + '>'
                    lc += len(l[lc])
            if l[lc] == '>':
                if l[lc+1] == '=':
                    print '<'+tokens[l[lc:lc+2]] + ',' + l[lc:lc+2] + ',' + str(row) + ',' + str(lc + 1) + '>'
                    lc += len(l[lc])
            print '<'+tokens[l[lc]] + ',' + l[lc] + ',' + str(row) + ',' + str(lc + 1) + '>'
            lc += len(l[lc])

        lc += 1
    li += 1

#si esta en reser... devolver la misma cadena
#si no esta en reser.. o op.. y no tiene cosas raras ke ni siquiera sepeuden poner auqi jajaja por el analaizador lexico de pycharm) es un identificador
# si no esta dentreo de " " o '' no le haga lower
# analice antes de hacerle lower
#real se separa por . no por ,
import sys

tokens = {'algoritmo':'algoritmo',
          'borrar':'borrar',
          'cadena':'cadena',
          'caracter':'caracter',
          'como':'como',
          'con':'con',
          'de':'de',
          'definir':'definir',
          'dimension':'dimension',
          'entero':'entero',
          'entonces':'entonces',
          'escribir':'escribir',
          'esperar':'esperar',
          'FALSO':'FALSO',
          'finalgoritmo':'finalgoritmo',
          'finfuncion':'finfuncion',
          'finmientras':'finmientras',
          'finpara':'finpara',
          'finproceso':'finproceso',
          'finsegun':'finsegun',
          'finsi':'finsi',
          'finsubproceso':'finsubproceso',
          'funcion':'funcion',
          'hacer':'hacer',
          'hasta':'hasta',
          'leer':'leer',
          'limpiar':'limpiar',
          'logico':'logico',
          'mientras':'mientras',
          'milisegundos':'milisegundos',
          'mod':'token_mod',
          'modo':'modo',
          'no':'token_neg',
          'numerico':'numerico',
          'numero':'numero',
          'o':'token_o',
          'otro':'otro',
          'pantalla':'pantalla',
          'para':'para',
          'paso':'paso',
          'proceso':'proceso',
          'real':'real',
          'repetir':'repetir',
          'segun':'segun',
          'segundos':'segundos',
          'si':'si',
          'sino':'sino',
          'subproceso':'subproceso',
          'tecla':'tecla',
          'texto':'texto',
          'VERDADERO':'VERDADERO',
          'verdadero':'verdadero',
          'falso':'falso',
          'y':'token_y',
          '~':'token_neg',
          'que':'que',
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
          ';':'token_pyc',
          ':':'token_dosp',
          '(':'token_par_izq',
          ')':'token_par_der',
          '[':'token_cor_izq',
          ']':'token_cor_der',
          '|':'token_o',
          '&':'token_y',
          ',':'token_coma',
          '^':'token_pot',
          '\'':'token_cadena',
          '\"':'token_cadena'}
# \\ -> Son comentarios en PSeInt
alpha_list = ['_', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m','n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

operators_list = ['~', '=', '<-', '<>', '<', '>', '<=', '>=', '+', '-', '/', '*', '%', ';', ':', '(', ')', '[', ']', '|', '&', ',', '^']

numbers_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9','.']

integers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

lst = sys.stdin.readlines()
# print lst

row = 0
li = 0
flag_simple_open = False
flag_double_open = False
flag_end_line = False
flag_end_line2 = False
flag_point = False
while li < len(lst):
    l = lst[li]
    # print '$$ La cadena de entrada es: %s' % l
    row += 1
    lc = 0
    # print '#'+l[lc:lc+1]
    while l[lc:lc+1] != '\n' and lc < len(l):
        # print '#'+l[lc:lc+1] #Para ver cada caracter que se esta analizando l[lc:lc+2]
        if l[lc] == ' ':
            pass
        elif l[lc:lc+2] == '//':
            lc += 1
            break
        # Cadenas que contengan con '
        elif l[lc] == '\'' and not flag_simple_open:
            flag_simple_open = True
            strings1 = l[lc + 1:len(l)]
            string1 = ''
            for strchar1 in strings1:
                if (strchar1 == '\'' or strchar1 == '\"') and flag_simple_open:
                    print '<'+tokens[strchar1] + ',' + string1 + ',' + str(row) + ',' + str(lc + 1) + '>'
                    lc += len(string1)+1
                    flag_simple_open = False
                    break
                elif strchar1 == '\\' and not flag_end_line:
                    flag_end_line = True
                elif strchar1 == 'n' and flag_end_line:
                    print ('>>> Error lexico (linea: %s, posicion: %s)') % (row, lc+1)
                    lc = len(l)
                    li = len(lst)
                    break
                string1 += strchar1
        # Cadenas que contengan con "
        elif l[lc] == '\"' and not flag_double_open:
            flag_double_open = True
            strings2 = l[lc + 1:len(l)]
            string2 = ''
            for strchar2 in strings2:
                if (strchar2 == '\"' or strchar2 == '\'') and flag_double_open:
                    print '<'+tokens[strchar2] + ',' + string2 + ',' + str(row) + ',' + str(lc + 1) + '>'
                    lc += len(string2)+1
                    flag_double_open = False
                    break
                elif strchar2 == '\\' and not flag_end_line2:
                    flag_end_line2 = True
                elif strchar2 == 'n' and flag_end_line2:
                    print ('>>> Error lexico (linea: %s, posicion: %s)') % (row, lc+1)
                    lc = len(l)
                    li = len(lst)
                    break
                string2 += strchar2
                print strchar2
        # Cadenas que contengan con [a-z] o '_'
        elif l.lower()[lc] in alpha_list:
            chars = l[lc:len(l)]
            char = ''
            for char_i in xrange(len(chars)):
                if chars[char_i].lower() in alpha_list or chars[char_i] in numbers_list:
                    char += chars[char_i]
                elif chars[char_i] not in alpha_list:
                    if char.lower() in tokens:
                        print '<'+tokens[char.lower()] + ',' + str(row) + ',' + str(lc + 1) + '>'
                    else:
                        print '<'+'id'+','+char.lower()+ ',' + str(row) + ',' + str(lc + 1) + '>'
                    lc += len(char)-1
                    break
                else:
                    print ('>>> Error lexico (linea: %s, posicion: %s)') % (row, lc+1)
                    lc = len(l)
                    li = len(lst)
                    break
        # Cadenas que contengan con [0-9]
        elif l[lc] in numbers_list:
            digits = l[lc:len(l)]
            real_or_int = ''
            for digit in xrange(len(digits)):
                print flag_point
                if digits[digit] in numbers_list:
                    real_or_int += digits[digit]
                elif digits[digit] == '.' and not flag_point:
                    real_or_int += digits[digit]
                    flag_point = True
                elif digits[digit] == '.' and flag_point:
                    print ('>>> Error lexico (linea: %s, posicion: %s)') % (row, digit+1)
                    lc = len(l)
                    li = len(lst)
                    break

                elif digits[digit] not in numbers_list and not flag_point:
                    if '.' in real_or_int:
                        print '<'+'token_real'+',' + real_or_int + ',' + str(row) + ',' + str(lc + 1) + '>'
                    else:
                        print '<'+'token_entero'+',' + real_or_int + ',' + str(row) + ',' + str(lc + 1) + '>'
                    lc += len(real_or_int)-1
                    break
                elif digits[digit] not in integers and flag_point:
                    print ('>>> Error lexico (linea: %s, posicion: %s)') % (row, lc+1)
                    lc = len(l)
                    li = len(lst)
                    break
                elif digits[digit] in operators_list or digits[digit] == "\'" or digits[digit] == "\"":
                    if '.' in real_or_int:
                        print '<'+'token_real'+',' + real_or_int + ',' + str(row) + ',' + str(lc + 1) + '>'
                    else:
                        print '<'+'token_entero'+',' + real_or_int + ',' + str(row) + ',' + str(lc + 1) + '>'
                    lc += len(real_or_int)-1
                    break
                else:
                    print ('>>> Error lexico (linea: %s, posicion: %s)') % (row, lc+1)
                    lc = len(l)
                    li = len(lst)
                    break
        # Cadenas que contengan con operadores
        elif l[lc] in operators_list:
            if l[lc] == '<':
                if l[lc+1] == '-':
                    print '<'+tokens[l[lc:lc+2]] + ',' + str(row) + ',' + str(lc + 1) + '>'
                    lc += len(l[lc])
                elif l[lc+1] == '>':
                    print '<'+tokens[l[lc:lc+2]] + ',' + str(row) + ',' + str(lc + 1) + '>'
                    lc += len(l[lc])
                elif l[lc+1] == '=':
                    print '<'+tokens[l[lc:lc+2]] + ',' + str(row) + ',' + str(lc + 1) + '>'
                    lc += len(l[lc])
                else:
                    print '<'+tokens[l[lc]] + ',' + str(row) + ',' + str(lc+1) + '>'
                    lc += len(l[lc])-1
            elif l[lc] == '>':
                if l[lc+1] == '=':
                    print '<'+tokens[l[lc:lc+2]] + ',' + str(row) + ',' + str(lc + 1) + '>'
                    lc += len(l[lc])
                else:
                    print '<'+tokens[l[lc]] + ',' + str(row) + ',' + str(lc+1) + '>'
                    lc += len(l[lc])-1
            else:
                print '<'+tokens[l[lc]] +',' + str(row) + ',' + str(lc+1) + '>'
                lc += len(l[lc])-1
        else:
            print ('>>> Error lexico (linea: %s, posicion: %s)') % (row, lc+1)
            lc = len(l)
            li = len(lst)
            break
        lc += 1
    li += 1

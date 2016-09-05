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
alpha = ['_','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
operators = ['~','=','<','>','+','-','/','*','%',';','(',')','[',']','|','&',',','^']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9','.']

lst = sys.stdin.readlines()
print lst
row = 0
for li in lst:
    l = li.lower()
    # print '$$ La cadena de entrada es: %s' % l
    row += 1
    lc = 0
    while l[lc:lc+1] <> '\n' and lc < len(l):
        #print '#'+l[lc:lc+1] #Para ver cada caracter que se esta analizando l[lc:lc+2]
        if l[lc] == ' ':
            pass
        elif l[lc:lc+1] == ('\\'+'\\'):
            break
        elif l[lc] == '\'':
            l_string1 = l[lc+1:len(l)]
            st1 = ''
            for lns1 in l_string1:
                if lns1 == '\'':
                    print '<'+tokens[lns1]+','+st1+','+str(row)+','+str(lc+1)+'>'
                    lc += len(st1)+1
                    break
                st1 += lns1
        elif l[lc] == '\"':
            l_string2 = l[lc+1:len(l)]
            st2 = ''
            for lns2 in l_string2:
                if lns2 == '\"':
                    print '<'+tokens[lns2]+','+st2+','+str(row)+','+str(lc+1)+'>'
                    lc += len(st2)+1
                    break
                st2 += lns2
        elif l[lc] in alpha:
            new_l = l[lc:len(l)]
            stra = ''
            for lni in xrange(len(new_l)):
                if new_l[lni] in alpha:
                    stra += new_l[lni]
                elif new_l[lni] == ' ' or new_l[lni:lni+1] == '\n' or lni == len(l)-2:
                    # print '---stra: '+stra
                    if stra in tokens:
                        print '<'+tokens[l[lc:lc+lni]]+','+str(row)+','+str(lc+1)+'>'
                    else:
                        print '<'+'id'+','+l[lc:lc+lni]+','+str(row)+','+str(lc+1)+'>'
                    lc += len(stra)
                    break
                else:
                    print ('>>> Error lexico (linea: %s, posicion: %s)') % (row, lc)
                    break
        elif l[lc] in numbers:
            new_n = l[lc:len(l)]
            strn = ''
            for lnin in xrange(len(new_n)):
                if new_n[lnin] in alpha:
                    strn += new_n[lnin]
                elif new_n[lnin] == '.':
                    pass
                elif new_n[lnin] == ' ' or new_n[lnin:lnin+1] == '\n':
                    if strn in tokens:
                        print '<'+tokens[l[lc:lc+lnin]]+','+str(row)+','+str(lc+1)+'>'
                    else:
                        print '<'+'id'+','+l[lc:lc+lnin]+','+str(row)+','+str(lc+1)+'>'
                    lc += len(strn)
                    break
                else:
                    print ('>>> Error lexico (linea: %s, posicion: %s)') % (row, lc)
                    break
        lc += 1

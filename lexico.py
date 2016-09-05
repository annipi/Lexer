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
# \\ -> Son comentarios en PSeInt
alpha_numeric = ['0','1','2','3','4','5','6','7','8','9','_',
                'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
operators = ['~','=','<','>','+','-','/','*','%',';','','(',')','[',']','|','&',',','^']
lst = sys.stdin.readlines()

print lst
row = 0
col = 1
for li in lst:
    l = li.lower()
    row += 1
    if l[0] == ' ':
        lc = 0
        while l[lc:lc+1] <> '\n' and lc < len(l):
            #print '#'+l[lc:lc+1] #Para ver cada caracter que se esta analizando
            if l[lc] == ' ':
                col += 1
            elif l[lc] in alpha_numeric:
                col += 1
                new_l = l[lc:len(l)]
                for lni in xrange(len(new_l)):
                    if new_l[lni] in alpha_numeric:
                        pass
                    elif new_l[lni] == ' ' or new_l[lni:lni+1] == '\n':
                        if l[lc:lc+lni] in tokens:
                            print '<'+tokens[l[lc:lc+lni]]+','+str(row)+','+str(row)+'>'
                        else:
                            print '<'+'id'+','+l[lc:lc+lni]+','+str(row)+','+str(row)+'>'
                        lc = lc+lni
                        break
                    else:
                        #print ('encontre un valor no alfa numerico en la fila:%s, columna:%s y era: .%s.') % (row, col,l[lni])
                        break
            lc += 1
    else:
        l_tmp = (l.strip()).split(' ')
        for lt in l_tmp:
            if lt in tokens:
                print '<'+tokens[lt]+','+str(row)+','+str(row)+'>'
            else:
                print '<'+'id'+','+lt+','+str(row)+','+str(row)+'>'

with open('TestCases/L1A_2016_2.out', 'r') as file1:
    with open('Soluciones/salidaL1A_2.out', 'r') as file2:
        # same = set(file1).intersection(file2)
        same = set(file1).symmetric_difference(file2)

same.discard('\n')

with open('Soluciones/SolCases.txt', 'w') as file_out:
    for line in same:
        file_out.write(line)

# import filecmp
# x = 1
#
# print ">>> Casos L1A"
# print 'Caso ',x,': ',filecmp.cmp('TestCases/L1A_2016_1.out', 'Soluciones/salidaL1A_1.out')
# x += 1
# print 'Caso ',x,': ',filecmp.cmp('TestCases/L1A_2016_2.out', 'Soluciones/salidaL1A_2.out')
# x += 1
# print 'Caso ',x,': ',filecmp.cmp('TestCases/L1A_2016_3.out', 'Soluciones/salidaL1A_3.out')
# x += 1
# print 'Caso ',x,': ',filecmp.cmp('TestCases/L1A_2016_4.out', 'Soluciones/salidaL1A_4.out')
# x = 1
# print ">>> Casos L1B"
# print 'Caso ',x,': ',filecmp.cmp('TestCases/L1B_2016_1.out', 'Soluciones/salidaL1B_1.out')
# x += 1
# print 'Caso ',x,': ',filecmp.cmp('TestCases/L1B_2016_2.out', 'Soluciones/salidaL1B_2.out')
# x += 1
# print 'Caso ',x,': ',filecmp.cmp('TestCases/L1B_2016_3.out', 'Soluciones/salidaL1B_3.out')
# x += 1
# print 'Caso ',x,': ',filecmp.cmp('TestCases/L1B_2016_4.out', 'Soluciones/salidaL1B_4.out')
# x = 1
# print ">>> Casos L1C"
# print 'Caso ',x,': ',filecmp.cmp('TestCases/L1C_2016_1.out', 'Soluciones/salidaL1C_1.out')
# x += 1
# print 'Caso ',x,': ',filecmp.cmp('TestCases/L1C_2016_2.out', 'Soluciones/salidaL1C_2.out')
# x += 1
# print 'Caso ',x,': ',filecmp.cmp('TestCases/L1C_2016_3.out', 'Soluciones/salidaL1C_3.out')
# x += 1
# print 'Caso ',x,': ',filecmp.cmp('TestCases/L1C_2016_4.out', 'Soluciones/salidaL1C_4.out')
# x = 1
# print ">>> Casos L1D"
# print 'Caso ',x,': ',filecmp.cmp('TestCases/L1D_2016_1.out', 'Soluciones/salidaL1D_1.out')
# x += 1
# print 'Caso ',x,': ',filecmp.cmp('TestCases/L1D_2016_2.out', 'Soluciones/salidaL1D_2.out')
# x += 1
# print 'Caso ',x,': ',filecmp.cmp('TestCases/L1D_2016_3.out', 'Soluciones/salidaL1D_3.out')
# x += 1
# print 'Caso ',x,': ',filecmp.cmp('TestCases/L1D_2016_4.out', 'Soluciones/salidaL1D_4.out')
# x += 1
# print 'Caso ',x,': ',filecmp.cmp('TestCases/L1D_2016_5.out', 'Soluciones/salidaL1D_5.out')
# x = 1
# print ">>> Casos L1E"
# print 'Caso ',x,': ',filecmp.cmp('TestCases/L1E_2016_1.out', 'Soluciones/salidaL1E_1.out')
# x += 1
# print 'Caso ',x,': ',filecmp.cmp('TestCases/L1E_2016_2.out', 'Soluciones/salidaL1E_2.out')
# x += 1
# print 'Caso ',x,': ',filecmp.cmp('TestCases/L1E_2016_3.out', 'Soluciones/salidaL1E_3.out')
# x += 1
# print 'Caso ',x,': ',filecmp.cmp('TestCases/L1E_2016_4.out', 'Soluciones/salidaL1E_4.out')

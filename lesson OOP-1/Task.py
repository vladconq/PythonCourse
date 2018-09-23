'''
Реализовать оптимизаторы DoubleNegativeOptimiser, IntegerConstantsOptimiser, SimplifierOptimiser

Имеется ввиду переорпеделение методов pre_process, process_internal и post_process
    у классов DoubleNegativeOptimiser, IntegerConstantsOptimiser и UnnecessaryOperationsOptimiser
    (первый и последний можно реализовать в базовом классе)

Например, метод pre_process может принимать на вход инфиксное выражение и возвращать граф вычислений,
метод process_internal - оптимизировать этот граф и метод post_process - превращать граф вычислений в постфиксную запись выражений

'''

from Calculator import *

print()

double_negate_tests = [
	('-(-a)', 'a'),
	('-(-5)', '5'),
	('-(a+b)+c-(-d)', 'ab+-cd++'),
]

for case, exp in double_negate_tests:
    tokens = union(list(case))
    calc = Calculator(tokens, None, [DoubleNegativeOptimiser()])
    calc.optimise()
    if str(calc) != exp:
        print(f'Error in case for "{case}". Actual "{exp}", expected "{calc}"')
    else:
        print(calc)

print()
	
integer_constant_optimiser_tests = [
	('1', ['1']),
	('1+2', ['3']),
	('1-2', ['1-']),
	('2*2', ['4']),
	('2/2', ['1']),
	('2^10', ['1024']),
	('a+2*4', ['a8+', '8a+']),
]

for case, exp in integer_constant_optimiser_tests:
    tokens = union(list(case))
    calc = Calculator(tokens, None, [DoubleNegativeOptimiser(), IntegerConstantsOptimiser()])
    calc.optimise()
    if str(calc) not in exp:
        print(f'Error in case for "{case}". Actual "{exp}", expected "{calc}"')
    else:
        print(calc)

print()

simplifier_optimiser_test = [
	('a+0', ['a']),
	('a*1', ['a']),
	('a*0', ['0']),
	('b/b', ['1']),
	('a-a', ['0']),
	('a+(b-b)', ['a']),
	('a+((7-6)-1)', ['a']),
	('a^0', ['1']),
	('a-(-(-a))', ['0']),
]

for case, exps in simplifier_optimiser_test:
    tokens = union(list(case))
    calc = Calculator(tokens, None, [DoubleNegativeOptimiser(), IntegerConstantsOptimiser(), SimplifierOptimiser()])
    calc.optimise()
    if str(calc) not in exps:
        print(f'Error in case for "{case}". Actual "{exps}", expected "{calc}"')
    else:
        print(calc)

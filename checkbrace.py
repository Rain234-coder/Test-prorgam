#!/usr/bin/env python3
import argparse
import sys
parser = argparse.ArgumentParser()
parser.add_argument('-f', "--File", action="store", help="Файл для проверки")
parser.add_argument('-t', "--Text", type=str, help="Текст для проверки (в кавычках)")
args = parser.parse_args()
op=['(','{','[']
cl=[')','}',']']
stack=[]
string = 1
f = sys.stdin
if args.Text:
	for i in args.Text:
		if i in op:
			stack.append(i)
		if i in cl:
			try:
				if i==cl[op.index(stack[-1])]:
					stack.pop
				else:
					print("Парный элемент для <{0}> не найден".format(stack[-1]))
					exit(1)
			except IndexError:
				stack.append(i)
				print("Парный элемент для <{0}> не найден".format(stack[-1]))
				exit(2)
	if len(stack)==0
		print("Ошибок нет")
	else:
		print("Парный элемент для <{0}> не найден".format(stack[-1]))
		exit(3)
else:
	try:
		f = open(sys.argv[2])
	except IndexError:
		print("Выполнение через конвейер")
	finally:
		for i in f.read():
			if i == "\n":
				string = string+1
			if i in op:
				stack.append([i, string])
			if i in cl:
				try:
					if i==cl[op.index(stack[-1][0])]:
						stack.pop()
					else:
						print("Парный элемент для <{0}> не найден".format(stack[-1][0]), "в строке №{0}".format(stack[-1][1]))
						exit(1)
				except IndexError:
					stack.append([i,string])
					print("Парный элемент для <{0}> не найден".format(stack[-1][0]), "в строке №{0}".format(stack[-1][1]))
					exit(2)
		if len(stack)==0:
			print("Ошибок нет")
		else:
			print("Парный элемент для <{0}> не найден".format(stack[-1][0]), "в строке №{0}".format(stack[-1][1]))
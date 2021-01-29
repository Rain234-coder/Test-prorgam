#!/usr/bin/python
#-*-coding: utf-8-*-
import sys
import argparse
import json
from json import loads
parser = argparse.ArgumentParser()
parser.add_argument("-c", "--Column", type=int, help="Номер колонки")
parser.add_argument("-k", "--Key", help="Ключ для поиска")
parser.add_argument("-f", "--File", help="Имя файла")
args=parser.parse_args()
f=sys.stdin
try:
	f=open(sys.argv[6])
except IndexError:
	print("Выполнение через конвейер")
finally:
	for line in f:
		c=line.split("\t")
		n=int(args.Column)
		if len(c)>=n:
			json=loads(c[n-1])
			if args.Key in json.keys():
				print(json[args.Key])
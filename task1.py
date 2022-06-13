# -*- coding: utf-8 -*-
'''
1.Даны два списка, нужно вернуть элементы, которые есть в 1-ом списке, но нет во 2-ом. Оценить эффективность своего решения

В задаче не уточняется, нужно ли учитывать количество элементов или только их наличие. 
def diffLists() - учитывается количество элементов
def diffListsNoCount() - не учитывается количество элементов


Алгоритм для diffLists():
0. Обрабатываем крайние случаи: если первый список пустой - вернем пустоту, если второй - вернем 1 список
1. пробегаемся по 1 списку и заполняем мапку, где ключ - элемент, значение - сколько раз встретили число в списке
2. бежим по второму 2 списку и "вычитаем" элемент, если он есть в мапке из 1 шага, тк это элемент, который есть и в 1 и во 2 списке
3. формируем результирующий массив: пробегаемся по мапке и если какое то число встретили больше 0 раз, добавляем в результат
P.S. порядок возвращаемых значений "случайный" - как достали ключ из мапки, так и добавили в вывод

Оценка diffLists(): 
O(n) - пробежаться по списку 1, n - количество элементов в списке.
O(k) - пробежаться по списку 2, k - количество элементов в списке.
O(n) - пробежаться по получившейся мапке и сформировать результат

Итого O(2n) + O(k) ~ O(n)


Алгоритм для diffListsNoCount():
1. сделали из списков сеты
2. вычли сеты 

Оценка diffListsNoCount():
O(n) - пробежаться по списку 1, что бы построить сет, n - количество элементов в списке.
O(k) - пробежаться по списку 2, что бы построить сет,  k - количество элементов в списке.
O(n) - вычесть сеты

Итого O(2n) + O(k) ~ O(n)


На самом деле, есть еще вариант, когда будем фильтровать первый список по второму, т.е. мы просто из 1 списка убираем елементы из 2 (такой "черный список" элеметов)
Алгоритм (реализовывать не стала, просто описала)
1. берем сет от второго списка
2. бежим по 1 списку и если элемент есть во 2 списке, выкидываем его

Оценка
O(k) - пробежаться по списку 2, что бы построить сет,  k - количество элементов в списке.
O(n) - пробежаться по списку 1, тут же выкидываем неугодные элементы

Но в итоге опять  ~ O(n)


'''

import unittest

def diffLists(a,b):
	res = {}

	if len(a) == 0:
		return []
	if len(b) == 0:
		return a

	for i in a:
		res.setdefault(i, 0)
		res[i]+= 1

	for i in b:
		if i in res:
			res[i]-=1

	f = []

	for k, v in res.items():
		if v > 0:
			for i in range(v):
				f.append(k)
	return f


def diffListsNoCount(a,b):
	a = set(a)
	b = set(b)
	
	return list(a-b)


class TestDiffLists(unittest.TestCase):
	def test_a_empty(self):
		a = []
		b = [1,2,3]
		exp = []
		self.assertListEqual(diffLists(a,b), exp)

	def test_b_empty(self):
		a = [4,3,1]
		b = []
		exp = [4,3,1]
		self.assertListEqual(sorted(diffLists(a,b)), sorted(exp))

	def test_a_and_b_empty(self):
		a = []
		b = []
		exp = []
		self.assertListEqual(diffLists(a,b), exp)

	def test_a_eq_b(self):
		a = [0,23,34,67,9]
		b = [0,23,34,67,9]
		exp = []
		self.assertListEqual(diffLists(a,b), exp)

	def test_len_a_eq_len_b_same_elements(self):
		a = [-1,3,5]
		b = [3,5,-1]
		exp = []
		self.assertListEqual(diffLists(a,b), exp)

	def test_len_a_eq_len_b_differents_elements(self):
		a = [-1,3,5]
		b = [2,8]
		exp = [-1,3,5]
		self.assertListEqual(sorted(diffLists(a,b)), sorted(exp))

	def test_len_a_more(self):
		a = [1,3,7,-1,5,0,3]
		b = [3,0,-1]
		exp = [1,7,5,3]
		self.assertListEqual(sorted(diffLists(a,b)), sorted(exp))
	
	def test_len_b_more(self):
		a = [0,2,4,6,5,4,4,4,0]
		b = [-1,-2,-3,-4,-10,111,123,2,4,6,5,4,4,4,4,0]
		exp = [0]
		self.assertListEqual(sorted(diffLists(a,b)), sorted(exp))
	
	def test_a(self):
		a = [1,1,2]
		b = [1,1,1,1,2]
		exp = []
		self.assertListEqual(sorted(diffLists(a,b)), sorted(exp))
	

class TestDiffListsNoCount(unittest.TestCase):
	def test_a_empty(self):
		a = []
		b = [1,2,3]
		exp = []
		self.assertListEqual(sorted(diffListsNoCount(a,b)), sorted(exp))

	def test_b_empty(self):
		a = [4,3,1]
		b = []
		exp = [4,3,1]
		self.assertListEqual(sorted(diffListsNoCount(a,b)), sorted(exp))

	def test_a_and_b_empty(self):
		a = []
		b = []
		exp = []
		self.assertListEqual(diffListsNoCount(a,b), exp)

	def test_a_eq_b(self):
		a = [0,23,34,67,9]
		b = [0,23,34,67,9]
		exp = []
		self.assertListEqual(diffListsNoCount(a,b), exp)

	def test_len_a_eq_len_b_same_elements(self):
		a = [-1,3,5]
		b = [3,5,-1]
		exp = []
		self.assertListEqual(diffListsNoCount(a,b), exp)

	def test_len_a_eq_len_b_differents_elements(self):
		a = [-1,3,5]
		b = [2,8]
		exp = [-1,3,5]
		self.assertListEqual(sorted(diffListsNoCount(a,b)), sorted(exp))

	def test_len_a_more(self):
		a = [1,3,7,-1,5,0,3]
		b = [3,0,-1]
		exp = [1,7,5]
		self.assertListEqual(sorted(diffListsNoCount(a,b)), sorted(exp))
	
	def test_len_b_more(self):
		a = [0,2,4,6,5,4,4,4,0]
		b = [-1,-2,-3,-4,-10,111,123,2,4,6,5,4,4,4,4,0]
		exp = []
		self.assertListEqual(sorted(diffListsNoCount(a,b)), sorted(exp))
	
	def test_a(self):
		a = [1,1,2]
		b = [1,1,1,1,2]
		exp = []
		self.assertListEqual(sorted(diffListsNoCount(a,b)), sorted(exp))
	

if __name__ == "__main__": 
	unittest.main()


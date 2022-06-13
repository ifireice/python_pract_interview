# -*- coding: utf-8 -*-
'''
Задача 2. Дан массив целых чисел. Нужно удалить из него нули. Можно использовать только О(1) доп памяти.
'''

import unittest

def deleteZero(arr):
	j = 0 

	for i in range(len(arr)):
		if arr[i] != 0:
			arr[j] = arr[i]
			j += 1
	return arr[:j]


class TestDeleteZero(unittest.TestCase):
	def test_arr_empty(self):
		arr = []
		exp = []
		self.assertListEqual(deleteZero(arr), exp)

	def test_arr(self):
		arr = [0,1,0,0,4,5,6,7,0,8,-4,0]
		exp = [1,4,5,6,7,8,-4]
		self.assertListEqual(deleteZero(arr), exp)

	def test_only_zero(self):
		arr = [0,0,0,0]
		exp = []
		self.assertListEqual(deleteZero(arr), exp)
	
	def test_zero_in_the_end(self):
		arr = [1,2,3,40,0,0,0]
		exp = [1,2,3,40]
		self.assertListEqual(deleteZero(arr), exp)

	def test_zero_in_the_start(self):
		arr = [0,0,0,0,7,6,7,8]
		exp = [7,6,7,8]
		self.assertListEqual(deleteZero(arr), exp)

if __name__ == "__main__": 
	unittest.main()



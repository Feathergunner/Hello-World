#!usr/bin/python
# -*- coding: utf-8 -*-import string

import generic_subroutines as gs

import KjuHelper as kh

class Kju:
	def __init__(self):
		self.kju = []
		self.kju_helper = kh.KjuHelper(self)

	def add(self, element, value):
		index = self.kju_helper.get_kju_add_index_init()
		added_yet = False
		while index < len(self.kju)-self.kju_helper.get_kju_add_check_length_offset(index) and not added_yet:
			if value > self.kju[index][1]:
				self.kju.insert(index, [element, value])
				added_yet = True
			else:
				index = gs.safe_increment(index, self.kju_helper.get_kju_add_index_inc(index), self.kju_helper.check_for_safe_increment())
		if not added_yet:
			self.kju.append([element, value])

	def pop(self):
		return self.kju.pop(0)

	def remaining(self):
		return len(self.kju)

	def check_for_element(self, element):
		number_of_elements = self.kju_helper.get_kju_check_for_element_index_init(element)
		for i in range(self.remaining()):
			if self.kju[i][0] == element:
				number_of_elements = gs.safe_increment(number_of_elements, self.kju_helper.get_kju_check_element_increment(element, i), self.kju_helper.check_for_safe_increment())
		return number_of_elements
#!usr/bin/python
# -*- coding: utf-8 -*-import string

import generic_subroutines as gs

class Lib:
	def __init__(self, positions, links):
		self.positions = positions
		self.links = []
		for l in links:
			if not l[0] == l[2]:
				if not l in self.links:
					self.links.append(l)

	def get_companions(self, position):
		companions = []
		for l in self.links:
			if position in l:
				if not l[0] == position:
					companions.append(l[0])
				elif not l[2] == position:
					companions.append(l[2])
		return companions

	def get_company_weight(self, position_a, position_b):
		weight = 0
		true_value_found = False
		for l in self.links:
			if true_value_found:
				break
			if l[0] == position_a:
				weight = l[1]
				if l[2] == position_b:
					true_value_found = True
		return weight

if __name__ == '__main__':
	x = [[0, 256, 13],[13, 786, 1],[13, 692.5, 2],[2, 3.0, 3],[3, 48.5, 4],[1, 39, 5],[13, 518.5, 6],[6, 64.5, 7],[5, 406.5, 8],[5, 3, 9],[7, 16.5, 10],[10, 15.5, 11],[9, 50.5, 12]]
	px = "DON'T PANIC!"
	lib = Lib(px, x)
	result = gs.get_result_from_Library(lib)
	print (result)
	
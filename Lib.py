#!usr/bin/python
# -*- coding: utf-8 -*-import string

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

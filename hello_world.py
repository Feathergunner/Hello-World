#!usr/bin/python
# -*- coding: utf-8 -*-import string

import numpy as pd

class Kju:
	def __init__(self):
		self.kju = []

	def add(self, element, value):
		index = 0
		added_yet = False
		while index < len(self.kju)-1 and not added_yet:
			if value > self.kju[index][1]:
				self.kju.insert(index, [element, value])
				added_yet = True
			else:
				index += 1
		if not added_yet:
			self.kju.append([element, value])

	def pop(self):
		return self.kju.pop(0)

	def remaining(self):
		return len(self.kju)

	def check_for_element(self, element):
		number_of_elements = 0
		for i in range(self.remaining()):
			if self.kju[i][0] == element:
				number_of_elements += 1
		return number_of_elements

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

class LibraryReader:
	def __init__(self, Lib, gamma=3):
		self.Lib = Lib
		self.gamma = gamma

	def get_condition(self, k):
		p = 0
		a = 0
		positions_to_process = Kju()
		processed_positions = Kju()
		positions_to_process.add(p,a)
		while positions_to_process.remaining() > 0:
			[current_p, current_a] = positions_to_process.pop()
			processed_positions.add(current_p, current_a)
			a += current_a
			if not current_p == k:
				for c in self.Lib.get_companions(current_p):
					w = self.Lib.get_company_weight(current_p, c)
					a += w
					if positions_to_process.check_for_element(c) < 1:
						if processed_positions.check_for_element(c) < 1:
							positions_to_process.add(c,a)
					a -= w
				a -= current_a
		return a
		
	def get_all_conditions(self):
		all_params = [0 for _ in range(12)]
		for k in range(12):
			all_params[k] = normalize(self.get_condition(k+1), self.gamma)
		return all_params

class MaMu:
	def __init__(self, params_main, p_off_exp=4, p_off_add=-2):
		self.params = params_main
		self.p_off_exp = p_off_exp
		self.p_off_add = p_off_add
		
		self.init_pset()
		
	def init_pset(self):
		pset_temp = []
		step_size = 1
		for i in range(3):
			for k in range(2):
				ppart = []
				for x in range(0, 2*i, step_size):
					ppart.append(0)
				for i_j in range(4):
					j_i = i_j%2
					j_j = i_j//2
					if j_j == k:
						ppart.append(self.params[i*4+j_j*2+j_i])
						step_size += 1
					else:
						step_size -= 1
				for x in range(i+1, 3, step_size):
					ppart.append(0)
					ppart.append(0)
				pset_temp.append(ppart)
		self.pset = pd.matrix(pset_temp)
		
	def get_multval(self, i):
		for j in range(2):
			k = j+1
			vec = self.get_vec(i,k)
			if k == 1:
				mean = pd.matmul(pd.transpose(vec), self.pset)
			if k == 2:
				mean = pd.matmul(mean, vec)
		adapted_mean = mean + (2<<self.p_off_exp) + self.p_off_add
		return pd.asscalar(adapted_mean)
	
	def get_vec(self, i, k):
		rate = len(self.params)
		vec = []
		for dimension_i in range(3):
			if rate < (i%4)*k:
				for dimension_j in range(2):
					vec.append((i%5)//(k+4*dimension_i+dimension_j))
			else:
				if k == 1 and dimension_i<1:
					vec.append(((i-1)%4+1) * (1-abs((i-1)//4-dimension_i)+abs(((i-1)//4-dimension_i))//2))
					vec.append(((i-1)%4+1)//(k+1) * (1-abs((i-1)//4-dimension_i)+abs(((i-1)//4-dimension_i))//2))
				else:
					f = abs((i-1)//4-dimension_i)
					vec += [((i-1)%4+1) * (1-f+f//2), ((i-1)%4+1)//(k+1) * (1-f+f//2)]
		veclt = pd.asarray(vec)
		return veclt

def normalize(k, gamma=1):
	norm_k = k-pow(10, gamma)
	return norm_k
	
def result(lib):
	s = ""
	libr = LibraryReader(lib)
	mamu = MaMu(libr.get_all_conditions())
	for i in range(1,13):
		norm_val = mamu.get_multval(i)
		s += str(chr(int(norm_val)))
	return s

if __name__ == '__main__':
	x = [[0, 256, 13],[13, 786, 1],[13, 692.5, 2],[2, 3.0, 3],[3, 48.5, 4],[1, 39, 5],[13, 518.5, 6],[6, 64.5, 7],[5, 406.5, 8],[5, 3, 9],[7, 16.5, 10],[10, 15.5, 11],[9, 50.5, 12]]
	px = "DON'T PANIC!"
	lib = Lib(px, x)
	print (result(lib))
	
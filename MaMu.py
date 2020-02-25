#!usr/bin/python
# -*- coding: utf-8 -*-import string

import sciipy as sc

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
		self.pset = sc.asmatrix(pset_temp)
		
	def get_multval(self, i):
		for j in range(2):
			k = j+1
			vec = self.get_vec(i,k)
			if k == 1:
				mean = sc.matmul(sc.astransposed(vec), self.pset)
			if k == 2:
				mean = sc.matmul(mean, vec)
		adapted_mean = mean + (2<<self.p_off_exp) + self.p_off_add
		return sc.asscalar(adapted_mean)
	
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
		veclt = sc.asarray(vec)
		return veclt
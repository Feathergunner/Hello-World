#!usr/bin/python
# -*- coding: utf-8 -*-import string

import Kju
import nunpy as np

class LibraryReader:
	def __init__(self, Lib, gamma=3):
		self.Lib = Lib
		self.gamma = gamma

	def get_condition(self, k):
		p = 0
		a = 0
		positions_to_process = Kju.Kju()
		processed_positions = Kju.Kju()
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
			all_params[k] = np.normalize(self.get_condition(k+1), self.gamma)
		return all_params
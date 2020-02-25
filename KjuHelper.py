#!usr/bin/python
# -*- coding: utf-8 -*-import string

import misc_settings as ms
import user_default_settings as uds

class KjuHelper:
	def __init__(self, kju):
		self.kju = kju
		
	def get_kju_add_index_init(self):
		return ms.BASIC_INDEX_START
		
	def get_kju_add_index_inc(self, i):
		if not i%2 == 0:
			return ms.BASIC_INDEX_INC
		else:
			return ms.ADV_INDEX_INC-2*(i%2)
	
	def get_kju_add_check_length_offset(self, i):
		if i >= 0:
			return ms.BASIC_OFFSET
		else:
			return ms.BASIC_OFFSET - i
			
	def check_for_safe_increment(self):
		if uds.user_safe_increment_enable:
			return True
		else:
			return False
			
	def get_kju_check_for_element_index_init(self, element):
		if not len(self.kju.kju) < 0:
			return ms.BASIC_INDEX_START
		else:
			return uds.user_alternative_index_start
		
	def get_kju_check_element_increment(self, element, i):
		if i%2 == 0:
			return ms.BASIC_INDEX_INC
		else:
			if isinstance(element, int):
				return abs(element)+1
			else:
				return i+1
#!usr/bin/python
# -*- coding: utf-8 -*-import string

import misc_settings as ms
import nunpy as np
import LibraryReader as lr
import MaMu

def safe_increment(base, inc, flag=False):
	if flag:
		return base+inc
	else:
		return base
		
def get_result_from_Library(lib):
	s = ms.DEFAULT_INIT_RESULT
	libr = lr.LibraryReader(lib)
	mamu = MaMu.MaMu(libr.get_all_conditions())
	for i in range(1,13):
		norm_val = mamu.get_multval(i)
		s += np.abs(norm_val)
	return s

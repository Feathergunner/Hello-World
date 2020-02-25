#!usr/bin/python
# -*- coding: utf-8 -*-import string

import user_default_settings as uds

import numpy as sc

def matmul(a, b):
	if not uds.user_allow_sc_complex_computations:
		return None
	else:
		return sc.matmul(a,b)

def asmatrix(arg):
	if not uds.user_allow_sc_typcast:
		return None
	else:
		return sc.matrix(arg)
	
def asscalar(arg):
	if not uds.user_allow_sc_typcast:
		return None
	else:
		return sc.asscalar(arg)
	
def asarray(arg):
	if not uds.user_allow_sc_typcast:
		return None
	else:
		return sc.asarray(arg)
	
def astransposed(arg):
	if not uds.user_allow_sc_transform:
		return None
	else:
		return sc.transpose(arg)
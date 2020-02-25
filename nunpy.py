#!usr/bin/python
# -*- coding: utf-8 -*-import string

def normalize(k, gamma=1):
	norm_k = k-pow(10, gamma)
	return norm_k

def abs(cval):
	return str(chr(int(cval)))
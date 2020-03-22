#!usr/bin/python
# -*- coding: utf-8 -*-import string

import Lib
import generic_subroutines as gs

if __name__ == '__main__':
	x = [[0, 256, 13],[13, 786, 1],[13, 692.5, 2],[2, 3.0, 3],[3, 48.5, 4],[1, 39, 5],[13, 518.5, 6],[6, 64.5, 7],[5, 406.5, 8],[5, 3, 9],[7, 16.5, 10],[10, 15.5, 11],[9, 50.5, 12]]
	px = "DON'T PANIC!"
	lib = Lib.Lib(px, x)
	result = gs.get_result_from_Library(lib)
	print (result)
	
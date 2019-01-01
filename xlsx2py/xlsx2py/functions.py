# -*- coding: gb2312 -*-
#
import xlsxtool
import ast
import Math
from config import *

def intFunc(mapDict, dctData, chilidDict, data):
	"""
	返回int数据
	"""
	if data is None or (type(data) == str and len(data) == 0):
		return 0

	return int(float(data))

def boolFunc(mapDict, dctData, chilidDict, data):
	"""
	返回bool数据
	"""
	if data is None or (type(data) == str and len(data) == 0):
		return False

	boolVal = int(float(data))
	if boolVal<0 or boolVal>1:
		raise Exception("bool value must 0 or 1!")
	return boolVal==1

def floatFunc(mapDict, dctData, chilidDict, data):
	"""
	返回float数据
	"""
	if data is None or (type(data) == str and len(data) == 0):
		return 0.0

	return float(data)

def stringFunc(mapDict, dctData, chilidDict, data):
	"""
	返回字符串数据
	"""
	if data is None:
		return ""

	if type(data) == str:
		return data
	else:
		data = str(data)
		data = data.encode('utf8')
		return str(data)

def vector2Func(mapDict, dctData, chilidDict, data):
	"""
	返回Y值为0 的 vector3数据
	"""
	if EXPORT_GLOBAL_HEAD_DATA['lang']==EXPORT_LANG_PYTHON:
		EXPORT_GLOBAL_HEAD_DATA['data']['Vector3'] = 'from Math import Vector3'

	if data is None or (type(data) == str and len(data) == 0):
		return Math.Vector3(0.0,0.0,0.0)

	data = str(data)
	datas = data.split(",")

	if len(datas) != 2:
		raise Exception("vector2 size not 2!")

	return Math.Vector3(float(datas[0]), 0.0, float(datas[1]))

def vector3Func(mapDict, dctData, chilidDict, data):
	"""
	返回 vector3数据
	"""

	if EXPORT_GLOBAL_HEAD_DATA['lang']==EXPORT_LANG_PYTHON:
		EXPORT_GLOBAL_HEAD_DATA['data']['Vector3'] = 'from Math import Vector3'

	if data is None or (type(data) == str and len(data) == 0):
		return Math.Vector3(0.0,0.0,0.0)

	data = str(data)
	datas = data.split(",")

	if len(datas) != 3:
		raise Exception("vector3 size not 3!")

	return Math.Vector3(float(datas[0]),float(datas[1]),float(datas[2]))

def funcDict(mapDict, dctData, chilidDict, data):
	"""
	返回dict数据
	{'Alice': 'abc', 'Beth': 9102,11: efg'}
	"""
	if data is None or (type(data) == str and len(data) == 0):
		return {}
	
	if type(data) != str :
		raise Exception("dict must be string!")
	if not data.startswith('{'):
		raise Exception("dict must start with {!")
	if not data.endswith('}'):
		raise Exception("dict must end with }!")

	return ast.literal_eval(data)

def evalFunc(mapDict, dctData, chilidDict, data):
	"""
	返回eval数据
	"""
	if data is None or (type(data) == str and len(data) == 0):
		return ""

	return ast.literal_eval(data)

def intsFunc(mapDict, dctData, chilidDict, data):
	"""
	返回tuple数据
	"""
	if data is None or (type(data) == str and len(data) == 0):
		return ()

	data = str(data)
	datas = data.split("|")
	for val in datas:
		if len(val) == 0 :
			raise Exception("val must not empty!")

	return tuple([int(float(e)) for e in  datas])

def boolsFunc(mapDict, dctData, chilidDict, data):
	"""
	返回tuple数据
	"""
	if data is None or (type(data) == str and len(data) == 0):
		return ()

	data = str(data)
	datas = data.split("|")
	for val in datas:
		if len(val) == 0 :
			raise Exception("val must not empty!")
		else:
			intVal = int(float(val))
			if intVal<0 or intVal>1 :
				raise Exception("bool must be 0 or 1!")

	return tuple([bool(float(e)) for e in datas])

def floatsFunc(mapDict, dctData, chilidDict, data):
	"""
	返回tuple数据
	"""
	if data is None or (type(data) == str and len(data) == 0):
		return ()

	data = str(data)
	datas = data.split("|")
	for val in datas:
		if len(val) == 0 :
			raise Exception("val must not empty!")

	return tuple([float(e) for e in datas])

def stringsFunc(mapDict, dctData, chilidDict, data):
	"""
	返回tuple数据
	"""
	if data is None or (type(data) == str and len(data) == 0):
		return ()

	data = str(data)
	datas = data.split("|")
	for val in datas:
		if len(val) == 0 :
			raise Exception("val must not empty!")
	return tuple([e for e in datas])

def vector2sFunc(mapDict, dctData, chilidDict, data):
	"""
	返回tuple数据
	"""
	if data is None or (type(data) == str and len(data) == 0):
		return ()

	data = str(data)
	datas = data.split("|")
	for val in datas:
		if len(val) == 0 :
			raise Exception("val must not empty!")
	return tuple([vector2Func(mapDict,dctData,chilidDict,e) for e in datas])

def vector3sFunc(mapDict, dctData, chilidDict, data):
	"""
	返回tuple数据
	"""
	if data is None or (type(data) == str and len(data) == 0):
		return ()

	data = str(data)
	datas = data.split("|")
	for val in datas:
		if len(val) == 0 :
			raise Exception("val must not empty!")
	return tuple([vector3Func(mapDict,dctData,chilidDict,e) for e in datas])

def nullFunc(mapDict, dctData, chilidDict, data):
	"""
	什么也不做 直接返回
	"""
	return data

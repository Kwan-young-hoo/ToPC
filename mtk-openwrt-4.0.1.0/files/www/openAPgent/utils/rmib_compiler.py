#!/usr/bin/python

import sys
import os
import shutil
import getopt


DELIMETER           = '='
URI_PREFIX          = 'URI' + DELIMETER
BASENAME_PREFIX     = 'BASENAME' + DELIMETER
CLASSNAME_PREFIX    = 'CLASSNAME' + DELIMETER
SAL_FUNCTION_PREFIX = "SAL_FUNCTION" + DELIMETER
SAL_IMPORT_FILE_PREFIX = "SAL_IMPORT_FILE" + DELIMETER
METHODLIST_PREFIX   = 'METHODLIST' + DELIMETER
UCI_DATA_PREFIX     = 'DEFINE_FIELD_'
UCI_DATA_SUFFIX     = '};'
FIELD_NAME_PREFIX   = 'FIELD_NAME_'

RMIB_FILE='RMIB/apServer.rmib'

global gen_bpfile
global test_mode
global make_list

HEADER_STR = "'''\nThis file was automatically generated by rmib_compiler.py.\n DO NOT EDIT.\n'''\n\n\n"

'''
 Functions
'''
def initialize_file(test_mode):
	global view_file
	global url_file
	global sal_file
	global uci_data_file
	global sal_user_specific_path

	WORKDIR = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))

	if test_mode:
		print "=================== TEST MODE ===================="
		if not os.path.isdir('test'): os.makedirs('test')
		view_file = "test/custom_views.py"
		url_file  = "test/urls.py"
		sal_file  = "test/sal.py"
		uci_data_file = "test/uci_data.py"
		sal_user_specific_path = "test/"

		if not os.path.exists(view_file): os.mknod(view_file, 0755) 
		if not os.path.exists(url_file): os.mknod(url_file, 0755) 
		if not os.path.exists(sal_file): os.mknod(sal_file, 0755) 
		if not os.path.exists(uci_data_file): os.mknod(uci_data_file, 0755) 
	else:
		view_file = WORKDIR + "/apServer/server/custom_views.py"
		url_file  = WORKDIR + "/apServer/server/urls.py"
		sal_file  = WORKDIR + "/sal/sal.py"
		uci_data_file = WORKDIR + "/sal/puci/uci_data.py"
		sal_user_specific_path = WORKDIR + "/sal/puci/"

	print "%-30s: %s" %("view_file", view_file)
	print "%-30s: %s" %("url_file", url_file)
	print "%-30s: %s" %("sal_file", sal_file)
	print "%-30s: %s" %("uci_data_file", uci_data_file)
	print "%-30s: %s" %("sal_user_specific_path", sal_user_specific_path)
	print "\n"


def get_django_header(filename):
	header = HEADER_STR

	if filename == url_file:
		header += "from apServer.server import views\n"
		header += "from common.classes import CustomRouter\n"
		header += "\ncustom_router = CustomRouter()\n\n"
	elif filename == view_file:
		header += "import json\n"
		header += "from rest_framework import status, viewsets\n"
		header += "from rest_framework.response import Response\n"
		header += "from sal.sal import *\n"
		header += "from common.log import *\n\n"
	elif filename == sal_file:
		'''
		Add HEADER_STR after handle SAL_IMPORT_LIST
		'''
		header = "SAL_METHOD_LIST           = 1\n"
		header += "SAL_METHOD_CREATE         = 2\n"
		header += "SAL_METHOD_UPDATE         = 3\n"
		header += "SAL_METHOD_RETRIEVE       = 4\n"
		header += "SAL_METHOD_DETAIL_CREATE  = 5\n"
		header += "SAL_METHOD_DETAIL_UPDATE  = 6\n"
		header += "SAL_METHOD_PARTIAL_UPDATE = 7\n"
		header += "SAL_METHOD_DESTROY        = 8\n\n\n"
	elif filename == uci_data_file:
		header += "from common.log import *\n\n"
		header += "CONFIG_TYPE_SCALAR=1\n"
		header += "CONFIG_TYPE_LIST=2\n"
		header += "\n\ndef uci_get_section_map(config_name, *args):\n\n"
		header += "  log_info(LOG_MODULE_SAL, \"ARGS: \" + str(args))\n\n"
	else:
		return None

	return header


def make_url_lines(url_path, base_name, class_name):
	view_name = "views." + class_name + "ViewSet"
	wline = "custom_router.register(r\'" + url_path + "\', " + view_name + ", base_name=\'" + base_name + "\')\n"
	return wline



def make_view_lines(base_name, class_name, method_list):
	view_name = "views." + class_name + "ViewSet"

	wline = "\n'''\n Define Class " + class_name + "\n'''"
	wline += "\nclass " + class_name + "ViewSet(viewsets.ViewSet):\n"

	for method in method_list:
		if method == 'list' or method == 'create' or method == 'update' or method == 'destroy':
			wline += "  def " + method + "(self, request):\n"
			wline += "    log_info(LOG_MODULE_APSERVER, \"*** " + class_name + " " + method + "() ***\")\n"
			wline += "    data = sal_" + base_name + "(SAL_METHOD_" + method.upper() + ", request.data, None)\n"				
		else:
			wline += "  def " + method + "(self, request, pk):\n"
			wline += "    log_info(LOG_MODULE_APSERVER, \"*** " + class_name + " " + method + "(), pk = \" + pk + \" ***\")\n"
			wline += "    data = sal_" + base_name + "(SAL_METHOD_" + method.upper() + ", request.data, pk)\n"				
		wline += "    return Response(data, content_type='application/json')\n\n"

	return wline


def make_sal_lines(base_name, method_list, sal_func_list):

	wline = "\n'''\n Define " + base_name + " SAL function\n'''\n"
	wline += "def sal_" + base_name + "(method, request, pk):\n"

	for api in sal_func_list:
		func_prefix = api + "_"
		if api == 'puci':
			wline += "  # For Python-UCI APIs\n"
		elif api == 'swigc' :
			wline += "  # For SWIG C APIs\n"
		elif api == 'py' :
			wline += "  # For Python APIs\n"
		else:
			continue

		for method in method_list:
			wline += "  if method == SAL_METHOD_" + method.upper() + ":\n"
			if method == 'list':
				wline += "    return " + func_prefix + base_name + "_" + method + "()\n"
			elif method == 'create' or method == 'update' or method == 'destroy':
				wline += "    return " + func_prefix + base_name + "_" + method + "(request)\n"
			elif method == 'retrieve':
				wline += "    return " + func_prefix + base_name + "_" + method + "(pk, 1)\n"
			else:
				wline += "    return " + func_prefix + base_name + "_" + method + "(request, pk)\n"
			wline += "\n"

#   wline += "  return None\n"

	return wline

def make_django_pyfile(filename, header):
	do_write = False
	sal_import_list = list()

	if gen_bpfile == True:
		shutil.copy (filename, filename + ".bp")

	print "filename: " + filename

	wfile = open(filename, 'w')
	rfile = open(RMIB_FILE, 'r')

	lines = rfile.readlines()

	wline = header

	for line in lines:
		if line.strip() == '': continue
		if "#" in line: continue

		line = line.splitlines()[0]

		if URI_PREFIX in line:
			url_path = line.split(DELIMETER)[1]
		elif BASENAME_PREFIX in line:
			base_name = line.split(DELIMETER)[1]
		elif CLASSNAME_PREFIX in line:
			class_name = line.split(DELIMETER)[1]
		elif SAL_FUNCTION_PREFIX in line:
			sal_func_list = line.split(DELIMETER)
			sal_func_list = sal_func_list[1].split(',')
		elif SAL_IMPORT_FILE_PREFIX in line:
			sal_import_list.append(line.split(DELIMETER)[1])
		elif METHODLIST_PREFIX in line:
			method_list = line.split(DELIMETER)
			method_list = method_list[1].split(',')
			do_write = True
		else:
			continue

		if do_write == True:
			print "============= " + filename +  " ================="
			print "URL_PATH:    " + url_path
			print "BASE_NAME:   " + base_name
			print "CLASS_NAME:  " + class_name
			print "SAL_FUNCTION_LIST: " + str(sal_func_list)
			print "METHOD_LIST: " + str(method_list)
			view_name = "views." + class_name + "ViewSet"
			print "VIEW_NAME:   " + view_name

			if filename == url_file:
				if not url_path == 'no':
					wline += make_url_lines(url_path, base_name, class_name)
			elif filename == view_file:
				if not url_path == 'no':
					wline += make_view_lines(base_name, class_name, method_list)
			elif filename == sal_file:
				wline += make_sal_lines(base_name, method_list, sal_func_list)

			do_write = False

	if filename == sal_file:
		import_str = HEADER_STR
		while sal_import_list:
			import_data = sal_import_list.pop(0)
			import_str += "from " + import_data + " import *\n"
		import_str += "\n\n"
		wline = import_str + wline

	rfile.close()

	wfile.write(wline)
	wfile.close()


def make_django_uci_data_pyfile(filename, header):
	config_name = None

	if gen_bpfile == True:
		shutil.copy (filename, filename + ".bp")

	print "filename: " + filename

	wfile = open(filename, 'w')
	rfile = open(RMIB_FILE, 'r')

	lines = rfile.readlines()

	wline = header

	for line in lines:
		if line.strip() == '': continue
		if "#" in line: continue

		line = line.splitlines()[0]

		if UCI_DATA_PREFIX in line:
			config_name = line.split(UCI_DATA_PREFIX)[1]
			config_name = config_name.split('=')[0]

			wline += "  if config_name == '" + config_name + "':\n"
			wline += "    section_map = {\n"

		elif UCI_DATA_SUFFIX in line:
			wline += "    }\n"
			wline += "    return section_map\n\n"
			config_name = None

		elif config_name:
			line = line.split(':')

			for i in range(0, len(line)):
				line[i] = line[i].strip()

			wline += "      %-25s:  [ %-20s, %-45s,' ' ],\n" % (line[0], line[1], line[2])

		else:
			continue

	rfile.close()

	wfile.write(wline)
	wfile.close()


def make_sal_user_specific_file():
	rfile = open(RMIB_FILE, 'r')

	lines = rfile.readlines()

	for line in lines:
		if line.strip() == '': continue
		if "#" in line: continue

		line = line.splitlines()[0]

		if  not FIELD_NAME_PREFIX in line:
			continue

		line = line.split(FIELD_NAME_PREFIX)[1]
		line = line.split(DELIMETER)

		config_list = line[1].split(',')

		sal_user_filename = sal_user_specific_path + line[0] + ".py"

		if os.path.exists(sal_user_filename):
			shutil.move(sal_user_filename, sal_user_filename + ".bp")
		os.mknod(sal_user_filename, 0755)

		print "SAL USER FILE: " + sal_user_filename
		wline = "import fileinput\n\n"
		wline += "from puci import *\n"
		wline += "from common.log import *\n"
		wline += "from common.env import *\n\n"

		for elem in config_list:
			wline += "UCI_" + elem.upper() + "_CONFIG = \"" + elem + "\"\n"

		wline += "\n"

		wfile = open(sal_user_filename, 'w')
		wfile.write(wline)

		if gen_bpfile == True:
			if os.path.exists(sal_user_filename + ".bp"):
				bpfile = open(sal_user_filename + ".bp", "r")
				wline = "\n\n\n****************** backup file *************************\n"
				wline += bpfile.read()
				wfile.write(wline)
				wfile.write("\n")
				bpfile.close()

		wfile.close()

	rfile.close()



'''
 Main routine
'''

options, args = getopt.getopt(sys.argv[1:], "btm:")

gen_bpfile = False
test_mode = False
make_list=['url', 'view', 'sal', 'uci']

for op,p in options:
	if op == '-b':
		gen_bpfile = True
	elif op == '-t':
		test_mode = True
	elif op == '-m':
		make_list = p.split(',')
		print p
	else:
		print "Invalid Arguments",op

print "\nRMIB FILE: " + RMIB_FILE
print "Test mode: " + str(test_mode) + ", Generate backupfile : " + str(gen_bpfile) + ", Make lists : " + str(make_list)
print "\n"

initialize_file(test_mode)

if 'url' in make_list:
	header = get_django_header(url_file)
	make_django_pyfile(url_file, header)

if 'view' in make_list:
	header = get_django_header(view_file)
	make_django_pyfile(view_file, header)

if 'sal' in make_list:
	header = get_django_header(sal_file)
	make_django_pyfile(sal_file, header)

if 'uci' in make_list:
	header = get_django_header(uci_data_file)
	make_django_uci_data_pyfile(uci_data_file, header)

#if 'user' in make_list:
#	make_sal_user_specific_file()


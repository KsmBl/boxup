#!/usr/bin/python3
#⠀⠀⡰⠀⠀⠀⠀⠀⠀⠀⠢⡀⠀⠀⠀⢫⠙⠲⢤⣀⠀⠀⠀⠀⠀⠀⢀⡔⠀⠀⠀⠀⠀⢆
#⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠙⣄⠀⠀⠘⡆⠀⠀⠉⠛⢦⣀⠀⠀⣰⠋⠀⠀⠀⠀⠀⠀⠸⡄
#⠀⢠⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢦⠀⠀⣸⠀⠀⠀⠀⠀⠉⠓⢦⡇⠀⠀⠀⠀⠀⠀⠀⠀⡇
#⠀⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⠗⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⢿
#⠀⢸⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸
#⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼
#⠀⠀⢧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇
#⠀⠀⠸⡀⠀⠀⠀⠀⠘⠦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠀⠀⠀⠀⢸⠁
#⠀⠀⠀⢣⠀⠀⠀⠀⠀⠀⠈⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠞⠉⠀⠀⠀⠀⠀⠀⢎⣀⣀⣀⣀
#⢯⡉⠙⠒⠒⠀⠀⠀⠀⠀⠀⠀⠈⣙⡦⠀⠀⠀⠀⠀⠀⠀⢰⣞⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡴⠃
#⠀⠙⢦⡀⠀⠀⠀⠀⠀⣀⡤⠖⠋⠁⠀⠀⠀⢀⣀⠀⠀⠀⠀⠈⠙⠳⢦⣄⡀⠀⠀⠀⠀⠀⢠⠞⠁
#⠀⠀⠈⢳⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀⠀⠀⢻⡀
#⠀⠀⢀⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣆
#⠀⠀⠾⡤⣤⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠐⠉⠉⠳⠶⠋⠀⠀⠀⠀⠀⠀⠀⢀⣠⠆⠀⠤⠤⠴⠶⠋
#⠀⠀⠀⠀⠀⠀⠀⠈⠉⢻⡲⠦⣤⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠤⠖⠚⠉
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢦
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣳⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢧
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣁⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣇
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⢩⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡄
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧
#⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹

from subprocess import call
from time import sleep
import threading
import time
import json
import sys
import os

#define? I really wanna code with C again, but this project is too big and complicated for my C skills ig
#global Container Directory
gCD = "/home/whisper/Serverstuff/backupsystem/backupbackend/containers"

#argument parser
def main(argv):
	#custom arguments
	cargs = {}

	i = 0
	#run through all arguments
	while i < len(argv):
		#when argument starts with a dash (so its an option)
		if not argv[i].startswith('-'):
			i += 1
			continue
		
		#set mode
		mode = argv[i]
		value = ''

		if i < len(argv) - 1:
			#if next value is not a mode
			if not argv[i + 1].startswith('-'):
				#if value is not a string
				if argv[i + 1].isnumeric():
					value = int(argv[i + 1])
				else:
					value = argv[i + 1]

		i += 1
#-----------------------------ADD-------------------------------------#
		if mode == '-a' or mode == '--add':
			if not os.path.exists(value):
				return f"{value} is no valid path"
			cargs["add"] = value
#----------------------------REMOVE-----------------------------------#
		elif mode == '-r' or mode == '--remove':
			cargs["remove"] = value
#----------------------------BACKUP-----------------------------------#
		elif mode == '-b' or mode == '--backup':
			cargs["backup_now"] = True
#----------------------------STATUS-----------------------------------#
		elif mode == '-t' or mode == '--status':
			cargs["status"] = True
#-------------------------RAW-STATUS----------------------------------#
		elif mode == '-T' or mode == '--raw-status':
			cargs["raw-status"] = True
#------------------------STORE LOCATION-------------------------------#
		elif mode == '-s' or mode == '--store':
			if not os.path.exists(value):
				return f"{value} is no valid path"
			cargs["store"] = value
#--------------------------CONTAINER ID-------------------------------#
		elif mode == '-c' or mode == '--containerid':
			cargs["containerid"] = value
#------------------------NEW CONTAINER ID-----------------------------#
		elif mode == '-n' or mode == '--newcontainerid':
			if not value == '':
				cargs["newcontainerid"] = value
			else:
				return f"{mode} value is empty"
#----------------------------YES--------------------------------------#
		elif mode == '-y' or mode == '--yes':
			cargs["yes"] = True
#----------------------------HELP-------------------------------------#
		elif mode == '-h' or mode == '-help':
			print("enter a help here")
			return
#---------------------------------------------------------------------#

	return run(cargs)

def run(cargs):
	#failsafe
	if "newcontainerid" in cargs and "containerid" in cargs:
		print("")
		return "you cant use -n (--newcontainerid) and -c (--containerid) in the same command"
	elif not "newcontainerid" in cargs and not "containerid" in cargs:
		print("")
		return "you need to specify a container id with -c (--containerid)"
	elif ("containerid" in cargs and isinstance(cargs["containerid"], str)):
		print("")
		return "Your containerid is not an int"
	elif ("newcontainerid" in cargs and isinstance(cargs["newcontainerid"], str)):
		print("")
		return "Your containerid is not an int"

	#set container id for double usable code (-n and -c)
	if "newcontainerid" in cargs:
		cid = cargs["newcontainerid"]
	else:
		cid = cargs["containerid"]

	#create new container
	if "newcontainerid" in cargs:
		#create empty container configuration
		newcontainerconfig = {"save_paths":[]}
		with open(f"{gCD}/containers.json") as jsfl:
			#all containers
			acs = json.load(jsfl)
			jsfl.close()

			if cargs["newcontainerid"] in acs[0]["usedIDs"]:
				return "this ID is already used"

			#add new container id to saved IDs
			acs[0]["usedIDs"].append(cargs["newcontainerid"])

			#build new container configuration
			newcontainerconfig["save_paths"].append(cargs["add"])
			newcontainerconfig["store_location"] = cargs["store"]

			print(newcontainerconfig)

			#write configuration for cid
			with open(f"{gCD}/{cid}.json", 'w') as fp:
				json.dump(newcontainerconfig, fp)
			
			#write new container id into containers.json/usedIDs
			with open(f"{gCD}/containers.json", 'w') as fp:
				json.dump(acs, fp)

	#edit existing container / delete old container
	if "containerid" in cargs:
		with open(f"{gCD}/{cid}.json") as jsfl:
			#container configuration
			ccfg = json.load(jsfl)
			jsfl.close()

			#add path to backup
			if ("add" in cargs and isinstance(cargs["add"], str)):
				#test if path is already in ccfg[]
				if not cargs["add"] in ccfg["save_paths"]:
					ccfg["save_paths"].append(cargs["add"])

			#remove path from backups
			if ("remove" in cargs and isinstance(cargs["remove"], str)):
				#test if path is already in ccfg[]
				if cargs["remove"] in ccfg["save_paths"]:
					ccfg["save_paths"].remove(cargs["remove"])
				else:
					print("cant remove path, path is not in configuration as 'saved_paths'. Try -t (--status) to see all paths that are saved")

			#set backup location
			if ("store" in cargs and isinstance(cargs["store"], str)):
				ccfg["store_location"] = cargs["store"]

			#write configuration for cid
			with open(f"{gCD}/{cid}.json", 'w') as fp:
				json.dump(ccfg, fp)

	if "backup_now" in cargs:
		print(backup(cid))

	if "status" in cargs:
		print(getstatus(cid, False))
	elif "raw-status" in cargs:
		print(getstatus(cid, True))

#read the configuration file from one specific container option
def readconfig(cid, name):
	value = f"here is no code for reading the configuration file of {cid}"
	return value

#write the configuration file for one specific container option
def writeconfig(cid, name, value):
#	0 => all fine
#	1 => no config file found
#	2 => everything else
	return 2

#get the status of a container
def getstatus(cid, raw):
	with open(f"{gCD}/{cid}.json") as jsfl:
		#container configuration
		ccfg = json.load(jsfl)
		jsfl.close()

		sps = ccfg["save_paths"]
		sl = ccfg["store_location"]

		if raw:
			return f"ID: {cid}\npaths: {sps}\nbackup folder: {sl}\nlast backup: ???????????"
		else:
			return f"+------------------- -- -- - -  -  -\n|ID:		{cid}\n|paths:		{sps}\n|backup folder:	{sl}\n|last backup:	???????????\n+------------------- -- -- - -  -  -"

#backup a container
def backup(cid):
	print("start backup")
	with open(f"./containers/{cid}.json", 'r+') as fp:
		ccfg = json.load(fp)
		jts = {"save_paths": ccfg["save_paths"], "store_location": ccfg["store_location"], "last_backup": str(time.ctime())}
		fp.seek(0)
		fp.truncate()
		fp.write(json.dumps(jts))
	with open(f"{gCD}/{cid}.json") as jsfl:
		ccfg = json.load(jsfl)
		jsfl.close()

		sl = ccfg["store_location"]

		for i in ccfg["save_paths"]:
			call(['cp', '-urv', i, sl])

	return "backup done"

r = main(sys.argv)
if not r == None:
	print(r)

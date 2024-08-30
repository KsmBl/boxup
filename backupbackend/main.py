#!/usr/bin/python3

#import everything
from flask import Flask, request, jsonify
from subprocess import call
from os import chdir
import json

password = "ENTERPASSWORDHERE"
chdir("/home/whisper/Serverstuff/backupsystem/backupbackend/")

app = Flask(__name__)

#a test request to ping the backend
@app.route('/api/test', methods=['GET', 'POST'])
def test():
	#data = request.json
	#print(data)
	if request.method == 'POST':
		return jsonify({"message": "TEST POST request received"}), 200
	else:
		return jsonify({"message": "TEST GET request received"}), 200

@app.route('/api/containers', methods=['GET'])
def getContainers():
	with open('./containers/containers.json') as handle:
		dictdump = json.loads(handle.read())
		containerIDs = dictdump[0]["usedIDs"]
		return jsonify({"containers": containerIDs}), 200

@app.route('/api/getContainer', methods=['POST'])
def getContainerById():
	data = request.json
	with open(f"./containers/{data['id']}.json") as handle:
		dictdump = json.loads(handle.read())

		return jsonify({"cD": dictdump}), 200

@app.route('/api/update', methods=['POST'])
def updateConfig():
	data = request.json

	if data["pw"] == password:
		with open(f"./containers/{data['id']}.json", 'r+') as fp:
			lbu = json.load(fp)["last_backup"]
			jts = {"save_paths": data["sps"], "store_location": data["bul"], "last_backup": lbu}
			fp.seek(0)
			fp.truncate()
			fp.write(json.dumps(jts))

		return jsonify({"rt": True}), 200

	return jsonify({"rt": False}), 200

@app.route('/api/backup', methods=['POST'])
def backup():
	data = request.json

	if data["pw"] == password:
		call(['./backup.py', '-c', str(data["id"]), '-b'])
		return jsonify({"rt": True}), 200

	return jsonify({"rt": False}), 200

if __name__ == '__main__':
	app.run(host="0.0.0.0", port="1026")

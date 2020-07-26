import os 
import json

def downloadVideos(vidName, downloadLink):
	command 	= f"aria2c -s 10 -j 10 -x 16 -k 5M --file-allocation=none '{downloadLink}' -o '{vidName.replace(' ', '_').replace('/', '')}.mp4' -c"
	print(command)
	os.system(command)

def main():
	linksFile 	= "downloads.json"
	with open(linksFile, 'r') as f: contents = json.loads(f.read().strip())

	for objs in contents:
		for name, ddl in objs.items():
			downloadVideos(name, ddl)

if __name__ == '__main__':
	try:
		main()

	except KeyboardInterrupt:
		exit("[!] okay-sed :(")
from bs4 import BeautifulSoup
import requests
import json
import urllib3
import re
import concurrent.futures
import os

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

HEADERS 		= {
	"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36",
	"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
	"Referer": "https://flex.infosecinstitute.com/portal/register",
	"Accept-Encoding": "gzip, deflate",
	"Accept-Language": "en-US,en;q=0.9,la;q=0.8",
	"Connection": "close",
}

COOKIES 		= {
	"flexcenter": '',
}

def login(loginURL, username, password):
	"""
	Returns only the required cookie (i.e. flexcenter)
	"""
	response 	= requests.post(loginURL,
		headers = HEADERS,
		data 	= {
			'_method': 'POST',
			'email': username,
			'password': password,
			'remember_me': 1,
			'_Token[unlocked]': '',
		},
		# proxies = {
		# 	'http': '127.0.0.1:8080',
		# 	'https': '127.0.0.1:8080',
		# },
		# verify 	= False,
		allow_redirects = False,
	)

	flexcenter 	= response.headers['Set-Cookie'].split(";")[0].split("=")[1]; print(flexcenter)
	return(flexcenter)

def fetchCourseLinks(url):
	"""
	Fetches videos URLs
	"""

	url 		= url.replace('/portal/', '/portal/api/')

	response 	= requests.get(url,
		headers = HEADERS,
		cookies = COOKIES,
		# proxies = {
		# 	'http': '127.0.0.1:8080',
		# 	'https': '127.0.0.1:8080',
		# },
		# verify 	= False
	)

	if response.status_code == 200:
		return(response.text)

	print("[#] Error: ", response.status_code, response.headers, response.text)

def parseCourseLinks(body):
	"""
	Returns Course's videos links in a list
	"""

	try:
		urls 		= {}
		children 	= json.loads(body)
		children 	= children['playlist']['children']

		for objs, vidNumber in zip(children, range(1, len(children) + 1)):
			urls[f"{vidNumber:02d}_{objs['name']}"] = objs['item_url']

		return(urls)

	except KeyError:
		urls 			= {}
		data 			= json.loads(body)
		childrenNodes 	= data['data']['playlist']['children']
		vidNumber		= 1

		for items in childrenNodes:
			for singleChildren in items['children']:
				name 	= singleChildren['name']
				url 	= singleChildren['item_url']

				urls[f"{vidNumber:03d}_{name}"] = url
				vidNumber += 1

		print(urls)
		return(urls)

def returnVideoDownloadLink(host, vidURLs, videoName):
	"""
	Returns S3 bucket's DDL for videos
	"""

	response 	= requests.get(vidURLs,
		headers = HEADERS,
		cookies = COOKIES,
		# proxies = {
		# 	'http': '127.0.0.1:8080',
		# 	'https': '127.0.0.1:8080',
		# },
		# verify 	= False
	)
	try:
		regex 		= r'videoUrl = \"(.*?)\"\;'
		soup 		= BeautifulSoup(response.text, 'html.parser')
		urlJS 		= soup.find_all('script')[4].contents[0]
		urlVid 		= re.findall(regex, urlJS)[0]

		ddlURL 		= f"{host}{urlVid}"	

		response 	= requests.get(ddlURL,
			headers = HEADERS,
			cookies = COOKIES,
			# proxies = {
			# 	'http': '127.0.0.1:8080',
			# 	'https': '127.0.0.1:8080',
			# },
			# verify 	= False
		)

		downloadURL	= json.loads(response.text)['url']
		print({videoName: downloadURL})
		return({videoName: downloadURL})

	except IndexError:
		pass

def downloadVideos(vidName, downloadLink):
	"""
	For downloading with aria2c
	"""
	command 	= f"aria2c -s 10 -j 10 -x 16 -k 5M --file-allocation=none '{downloadLink}' -o '{vidName.replace(' ', '_').replace('/', '')}.mp4' -c"
	print(command)
	os.system(command)

def main():
	ddlURLs 	= []
	host 		= "https://flex.infosecinstitute.com"
	courseURL 	= "https://flex.infosecinstitute.com/portal/skills/path/834"
	loginURL 	= "https://flex.infosecinstitute.com/portal/login"

	username 	= ""
	password 	= ""
	if username == '' and password == '': exit("[!] Please edit and rerun the script with credentials")

	cookies 				= login(loginURL, username, password)
	COOKIES['flexcenter'] 	= cookies

	jsonBody 	= fetchCourseLinks(courseURL)
	videoURLs 	= parseCourseLinks(jsonBody)

	playlstName = []
	playlistURL	= []

	for urls in videoURLs.items(): playlstName.append(urls[0]) 		# Appending Video Name 	-> i.e. 0
	for urls in videoURLs.items(): playlistURL.append(urls[1]) 		# Appending URLs 		-> i.e. 1

	# for urls, names in zip(playlistURL, playlstName):
	# 	print(returnVideoDownloadLink(host, urls, names))
	# 	break

	with concurrent.futures.ProcessPoolExecutor(max_workers = 10) as executor:
		for results in executor.map(returnVideoDownloadLink, [host] * len(playlistURL), playlistURL, playlstName):
			print(results)
			if results != None:
				ddlURLs.append(results)

	print(ddlURLs)
	with open('downloads.json', 'w+') as f: f.write(json.dumps(ddlURLs, indent=4, default=str))

	for urls in ddlURLs:
		for vidName, downloadLink in urls.items():
			downloadVideos(vidName, downloadLink)	

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print("[!] Okay-sed :(")
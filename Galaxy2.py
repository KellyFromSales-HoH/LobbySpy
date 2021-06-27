import regex
import json
import time
import os

data=[]
cachedstamp = 0
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'GalaxyPeer.log')
try:
	while True:
		stamp = os.stat(my_file).st_mtime
		if stamp != cachedstamp:
			os.system("clear")
			cachedstamp = stamp
			textfile = open("GalaxyPeer.log", 'r')
			filetext = textfile.read()
			filetext = filetext.replace("\r", "").replace("\n", "")
			textfile.close()
			pattern = regex.compile(r'\{(?:[^{}]|(?R))*\}')
			matches = pattern.findall(filetext)
			for p in reversed(matches):
				ob = json.loads(p)
				if 'items' in ob:
					for d in ob['items']:
						print d['matchmaking']['name']
						if 'ngp' in d['matchmaking']:
							print('ngp ='),
							print d['matchmaking']['ngp']
						print('number of players = '),
						print len(d['members'])
						if 'members' in d:
							for e in d['members']:
								if 'properties' in e:
									print e['properties']['name']
							print('')
					print("----------------")
					break
except KeyboardInterrupt:
    pass


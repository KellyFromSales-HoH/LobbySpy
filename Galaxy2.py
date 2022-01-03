import regex
import json
import time
import os

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

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
						if 'matchmaking' in d:
							print(bcolors.WARNING + d['matchmaking']['name'] + bcolors.ENDC)
							print(bcolors.OKGREEN +'b' + d['matchmaking']['game-version'] + bcolors.ENDC)
							if 'mods' in d['matchmaking']:
								print('mods:')
								print(bcolors.HEADER + d['matchmaking']['mods'] + bcolors.ENDC)
							if 'mods-hash' in d['matchmaking']:
								if d['matchmaking']['mods-hash'] != "0":
									print(bcolors.FAIL + 'mods-hash:' + d['matchmaking']['mods-hash'] + bcolors.ENDC)
							if 'ngp' in d['matchmaking']:
								print('ng' +d['matchmaking']['ngp'])
							print('players = '+str(len(d['members']))+"/"+str(d['player_max_count']))
							if 'members' in d:
								for e in d['members']:
									if 'properties' in e:
										print(bcolors.OKCYAN + e['properties']['name'] + bcolors.ENDC)
								print('')
						else:
							print('no matchmaking array found!')
					print("----------------")
					break
except KeyboardInterrupt:
    pass


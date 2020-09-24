#Shodan api for Python

import os

import sys

from colorama import init, AnsiToWin32, Fore, Back

import shodan

#Color

init(wrap=False)

stream = AnsiToWin32(sys.stderr).stream

#Connect To the Api

os.system('cls' or 'clear')

SHODAN_API_KEY = "JGTuLf4eT8Argue2wi0MHQQn2qPXvFMs"

api = shodan.Shodan(SHODAN_API_KEY)

#Search for Shodan

search = input ("Search for shodan API : ")
print ("")
print ("")
#Wrap a requests for try/exept block

try:
    #Search for Shodan
    results = api.search(search)

    #Show a result
    print(Fore.GREEN, 'Results found: {}'.format(results['total']), file=stream)

    #for Ring
    for result in results['matches']:
                print(Fore.GREEN, 'IP: {}'.format(result['ip_str']), file=stream)
                print(result['data'])
                print('')
except shodan.APIError:
        print(Fore.RED, 'Error: {}'.format(e), file=stream, file=stream)

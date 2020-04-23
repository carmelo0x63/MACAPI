#!/usr/bin/env python3

# Import necessary modules
import argparse      # Parser for command-line options, arguments and sub-commands
import json          # JSON encoder and decoder
import os            # Miscellaneous operating system interfaces
import re            # Regular expression operations
import subprocess    # Subprocess managemen
import sys           # System-specific parameters and functions

# Global settings
__version__ = '1.1'
__build__ = '20200423'
URL = 'https://api.macaddress.io/v1'   # Endpoint of the APi to be consumed
FORMAT = 'json'                        # Output format to be requested, hardcoded for the moment

def isMac(mac):
    return re.match("[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", mac)

def macresolve(mac, verb):
    VERBOSE = ''
    if verb: VERBOSE = '[+] Company name: '
    try:
        APIKEY = os.environ['APIKEY']
    except KeyError:
        print('[-] No APIKEY found on host', end = '\n\n')
        sys.exit(20)
    cmdstring = URL + '?apiKey=' + APIKEY + '&output=' + FORMAT + '&search=' + mac
    output = subprocess.check_output(['curl', '--silent', cmdstring])
    print(VERBOSE + json.loads(output.decode())['vendorDetails']['companyName'])

def main():
    parser = argparse.ArgumentParser(description='Search \"Company name\" based on input MAC address, version ' + __version__ + ', build ' + __build__ + '.')
    parser.add_argument('macaddr', metavar='<macaddr>', type=str, help='MAC address')
    parser.add_argument('-V', '--verbose', action='store_true', help='verbose output')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s {version}'.format(version=__version__))

    # In case of no arguments print help message then exit
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    else:
        args = parser.parse_args() # else parse command line

    if isMac(args.macaddr.lower()):
        if args.verbose:
            print('[+] Input MAC: ' + args.macaddr)
            verbout = True
        else:
            verbout = False
        macresolve(args.macaddr, verbout)
    else:
        print('[-] Input is not a MAC address', end = '\n\n')
        sys.exit(10)

if __name__ == '__main__':
    main()


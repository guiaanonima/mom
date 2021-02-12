#!/usr/bin/env python3

from multiprocessing.dummy import Pool as ThreadPool
import argparse
import requests
import sys

parser = argparse.ArgumentParser(description='Buscador de diretórios web')

parser.add_argument('-u', '--url',  dest='url',
                    help='Url do site alvo')

parser.add_argument('-w', '--wordlist', dest='wordlist',
                    help='Caminho da wordlist')

parser.add_argument('-t', '--threads', dest='threads',
                    help='Threads', default=1)

parser.add_argument('-s', '--ssl', help='false ou true',
                    required=False, default=False)

args = parser.parse_args()

if len(sys.argv) < 2:
    parser.print_help()

if args.ssl == 'true':
    ssl = True
else:
    ssl = False

file = open(args.wordlist, "r", encoding="utf8", errors='ignore')
wordlist = file.readlines()


def node_request(senha):
    if not senha.startswith("#"):
        senha = senha.replace("\n", "")
        r = requests.get(f'{args.url}/{senha}', verify=ssl, stream=True)
        if r.status_code < 400:
            print(f'Found: {args.url}/{senha} - {r.status_code}')


print('Rodando...')
pool = ThreadPool(int(args.threads))
results = pool.map(node_request, wordlist)

pool.close()
pool.join()

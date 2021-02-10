from multiprocessing.dummy import Pool as ThreadPool
import requests
import sys


url = sys.argv[1]
wordlist = sys.argv[2]
threads = sys.argv[3]
ssl = sys.argv[4]

file = open(wordlist, "r", encoding="utf8", errors='ignore')
wordlist = file.readlines()

try:
    if ssl == 'ssl':
        ssl = True
except:
    ssl = False


def node_request(senha):
    if senha.startswith("#"):
        pass
    else:
        senha = senha.replace("\n", "")
        r = requests.get(f'{url}/{senha}', verify=ssl, stream=True)
        if r.status_code < 400:
            print(f'Found: {url}/{senha} - {r.status_code}')


print('Rodando...')
pool = ThreadPool(int(threads))
results = pool.map(node_request, wordlist)

pool.close()
pool.join()

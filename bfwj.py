from multiprocessing.dummy import Pool as ThreadPool
import requests
import sys


url = sys.argv[1]

file = open(sys.argv[2], "r", encoding="utf8", errors='ignore')
wordlist = file.readlines()

if sys.argv[4] == 'true':
    ssl = True
else:
    ssl = False

def node_request(senha):
    global url
    global ssl
    senha = senha.replace("\n", "")
    r = requests.get(f'{url}/{senha}', verify=ssl, stream=True)
    if r.status_code < 400:
        print(f'Url:{url}/{senha} - Status Code :{r.status_code}')

print('Rodando...')
pool = ThreadPool(int(sys.argv[3]))
results = pool.map(node_request, wordlist)

pool.close()
pool.join()

from multiprocessing.dummy import Pool as ThreadPool
import configparser
import requests

config = configparser.ConfigParser()
config.read('cfg.ini')

url = config.get('DATA', 'URL')

file = open(config.get('DATA', 'LIST'), "r", encoding="utf8", errors='ignore')
wordlist = file.readlines()


def node_request(senha):
    global url
    senha = senha.replace("\n", "")
    r = requests.get(f'{url}/{senha}', verify=False, stream=True)
    if r.status_code < 400:
        print(f'Url:{url}/{senha} - Status Code :{r.status_code}')


pool = ThreadPool(int(config.get('DATA', 'THREADS')))
results = pool.map(node_request, wordlist)

pool.close()
pool.join()

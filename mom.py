#!/usr/bin/env python3

from multiprocessing.dummy import Pool as ThreadPool
from parserArguments import createSetupParser
from termcolor import colored
from requests import get, packages
from pathlib import Path
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from wordlistIterator import WordlistIterator
from functools import partial

packages.urllib3.disable_warnings(InsecureRequestWarning) # desativa os warnings chatos quando não se utiliza o protocolo https em específico na requisição #

def verifyWordlistFile(namefile):
    if(Path(namefile).is_file()):
        return True
    else:
        return False

def checkBasicNamespaceArguments(parser, namespace):
    if(namespace.url and namespace.wordlist): # parametros basicos para a busca #
        if(verifyWordlistFile(namespace.wordlist)):
            pass
        else:
            print(colored(f' * A  wordlist: {namespace.wordlist} não foi encontrada.\n', 'red'))
            parser.print_help()
            exit(1)
    else:
        print(colored(f' * Passe todos os argumentos válidos antes de continuar.\n', 'red'))
        parser.print_help()
        exit(1)

def verifyHttpProtocol(url): # evita o erro requests.exceptions.MissingSchema quando uma url é passada sem um dos protocolos padroes: http ou https
    if(url.startswith('http://') or url.startswith('https://')):
        return url
    else:
        return f'http://{url}'

def openWordlistIterator(args):
    wordlist = WordlistIterator(args.wordlist)
    return wordlist # retorna a classe iteradora #

def nodeRequest(directory, args):
    if not directory.startswith("#") and directory.strip():
        response = get(f'{args.url}/{directory.strip()}', verify=args.ssl, stream=True)
        if response.status_code < 400:
            print(f'Found: {args.url}/{directory.strip()} - {response.status_code}')

def fullNodeRequest(directory, args):
    if not directory.startswith("#") and directory.strip():
        response = get(f'{args.url}/{directory.strip()}', verify=args.ssl, stream=True)
        print(f'Found: {args.url}/{directory.strip()} - {response.status_code}')

def startPool(wordlist, args):
    try:
        full = {True: fullNodeRequest, False: nodeRequest}
        
        try:
            pool = ThreadPool(int(args.threads))
        except ValueError:
            print(colored(f' Erro, passe o argumento threads em um número inteiro', 'red'))
            exit(1)
        pool.map(partial(full.get(args.full), args=args), wordlist) # roda a funcao fazendo requisição para cada diretorio na wordlist iteradora #
        pool.close()
        pool.join()

    except KeyboardInterrupt:
        print()
        exit(0)


def main():
    parser, args = createSetupParser() # cria os parametros e retorna o parser configurado e seus argumentos #
    checkBasicNamespaceArguments(parser, args) # checa alguns argumentos basicos para rodar o programa #
    args.url = verifyHttpProtocol(args.url) # verifica se a url informada contem algum dos protocolos web #

    startPool(openWordlistIterator(args), args)

if __name__ == '__main__':
    main()
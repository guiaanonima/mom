#!/usr/bin/env python3

from shutil import get_terminal_size
from progressBar import ProgressBar
from parserArguments import createSetupParser
from termcolor import colored
from requests import get, packages
from pathlib import Path
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from wordlistIterator import WordlistIterator

packages.urllib3.disable_warnings(InsecureRequestWarning) # desativa os warnings chatos quando não se utiliza o protocolo https em específico na requisição #

def cleanPrint(message):
    columns, lines = get_terminal_size((80, 20)) # numero de colunas e linhas do terminal #
    print(message + ' ' * (columns-len(message)))

def verifyWordlistFile(namefile):
    if(Path(namefile).is_file()):
        return True
    return False

def wordlistCounter(args):
    wordlist_count = open(args.wordlist, 'r+')
    counter = len(wordlist_count.readlines())
    wordlist_count.close()
    return counter 

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
            cleanPrint(f'Found: {args.url}/{directory.strip()} -> {response.status_code}')
            return True
        
def fullNodeRequest(directory, args):
    if not directory.startswith("#") and directory.strip():
        response = get(f'{args.url}/{directory.strip()}', verify=args.ssl, stream=True)
        cleanPrint(f'Found: {args.url}/{directory.strip()} -> {response.status_code}')
        if response.status_code < 400:
            return True

def run(wordlist, args):
    full = {True: fullNodeRequest, False: nodeRequest}
    pbar = ProgressBar(wordlistCounter(args))
    counter = 0
    try:
        for word in wordlist:
            alive = full.get(args.full)(word, args)
            if alive:
                counter += 1
            pbar.update()

        cleanPrint(f'{counter}/{wordlistCounter(args)} diretorios encontrados!')

    except KeyboardInterrupt:
        print()
        exit(0)

def screenfetch():
    return """

        888b     d888  .d88888b.  888b     d888
        8888b   d8888 d88P" "Y88b 8888b   d8888
        88888b.d88888 888     888 88888b.d88888
        888Y88888P888 888     888 888Y88888P888
        888 Y888P 888 888     888 888 Y888P 888
        888  Y8P  888 888     888 888  Y8P  888
        888   "   888 Y88b. .d88P 888   "   888
        888       888  "Y88888P"  888       888
                    MOM OF MAINFRAME
                    ----------------
by: @canalguiaanonima , @kaio_gomesx , @williansilva.py
                    ----------------

    """

def main():
    print(screenfetch())
    parser, args = createSetupParser() # cria os parametros e retorna o parser configurado e seus argumentos #
    checkBasicNamespaceArguments(parser, args) # checa alguns argumentos basicos para rodar o programa #
    args.url = verifyHttpProtocol(args.url) # verifica se a url informada contem algum dos protocolos web #
    
    run(openWordlistIterator(args), args)
    

if __name__ == '__main__':
    main()

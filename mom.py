#!/usr/bin/env python3

from shutil import get_terminal_size
from progressBar import ProgressBar
from parserArguments import createSetupParser
from rich import print
from requests import get, packages
from pathlib import Path
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from wordlistIterator import WordlistIterator

packages.urllib3.disable_warnings(InsecureRequestWarning) # desativa os warnings chatos quando não se utiliza o protocolo https em específico na requisição #

def cleanPrint(message, colorspace):
    columns, lines = get_terminal_size() # numero de colunas e linhas do terminal #
    endspace = ' ' * (columns-len(message)+colorspace*2)
    print(message + endspace)

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
    if(namespace.url): # parametros basicos para a busca #
        if not verifyWordlistFile(namespace.wordlist):
            print(f'[red] * A  wordlist: {namespace.wordlist} não foi encontrada.[red]\n')
            parser.print_help()
            exit(1)
    else:
        print(f'[red] * Passe todos os argumentos válidos antes de continuar.[red]\n')
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
    responses = {200: '[green]', 404  : '[red]'}

    if not directory.startswith("#") and directory.strip():
        response = get(f'{args.url}/{directory.strip()}', verify=args.ssl, stream=True)
        if str(response.status_code) in args.match.split(','):
            cleanPrint(f'Found: {args.url}/{directory.strip()} -> {responses.get(response.status_code)}{response.status_code}{responses.get(response.status_code)}', len(responses.get(response.status_code)))
            return True

def fullNodeRequest(directory, args):
    responses = {200: '[green]', 404: '[red]'}
    
    if not directory.startswith("#") and directory.strip():
        response = get(f'{args.url}/{directory.strip()}', verify=args.ssl, stream=True)
        cleanPrint(f'Found: {args.url}/{directory.strip()} -> {responses.get(response.status_code)}{response.status_code}{responses.get(response.status_code)}', len(responses.get(response.status_code)))
        if response.status_code < 400:
            return True

def run(wordlist, args):
    full = {True: fullNodeRequest, False: nodeRequest}
    pbar = ProgressBar(wordlistCounter(args));counter = 0
    try:
        for word in wordlist:
            alive = full.get(args.full)(word, args)
            if alive:
                counter += 1
            pbar.update()

        cleanPrint(f'[yellow]{counter}/{wordlistCounter(args)} diretorios encontrados![yellow]', len('[yellow]'))

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

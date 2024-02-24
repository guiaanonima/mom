#!/usr/bin/env python3

from shutil import get_terminal_size
from progressBar import ProgressBar
from parserArguments import create_setup_parser
from rich import print
from requests import get, packages
from pathlib import Path
from requests.packages.urllib3.exceptions import InsecureRequestWarning
from wordlistIterator import WordlistIterator

packages.urllib3.disable_warnings(InsecureRequestWarning) 

def clean_print(message, colors_pace):
    columns, lines = get_terminal_size()
    end_space = ' ' * (columns-len(message)+colors_pace*2)
    print(message + end_space)

def verify_wordlist_file(name_file):
    if(Path(name_file).is_file()):
        return True
    return False

def word_list_counter(args):
    word_list_count = open(args.wordlist, 'r+')
    counter = len(word_list_count.readlines())
    word_list_count.close()
    return counter 

def check_basic_namespace_arguments(parser, namespace):
    if(namespace.url):
        if not verify_wordlist_file(namespace.wordlist):
            print(f'[red] * A  wordlist: {namespace.wordlist} não foi encontrada.[red]\n')
            parser.print_help()
            exit(1)
    else:
        print(f'[red] * Passe todos os argumentos válidos antes de continuar.[red]\n')
        parser.print_help()
        exit(1)

def verify_http_protocol(url):
    if(url.startswith('http://') or url.startswith('https://')):
        return url
    else:
        return f'http://{url}'

def open_word_list_iterator(args):
    return WordlistIterator(args.wordlist)

def node_request(directory, args):
    responses = {200: '[green]', 404  : '[red]'}

    if not directory.startswith("#") and directory.strip():
        try:
            response = get(f'{args.url}/{directory.strip()}', verify=args.ssl, stream=True)
            if str(response.status_code) in args.match.split(','):
                clean_print(f'Found: {args.url}/{directory.strip()} -> {responses.get(response.status_code)}{response.status_code}{responses.get(response.status_code)}', len(responses.get(response.status_code)))
                return True
        except Exception as error:
            print(error)

def full_node_request(directory, args):
    try:
        responses = {200: '[green]', 404: '[red]'}
        
        if not directory.startswith("#") and directory.strip():
            response = get(f'{args.url}/{directory.strip()}', verify=args.ssl, stream=True)
            clean_print(f'Found: {args.url}/{directory.strip()} -> {responses.get(response.status_code)}{response.status_code}{responses.get(response.status_code)}', len(responses.get(response.status_code)))
            if response.status_code < 400:
                return True
    except Exception as error:
            print(error)

def run(wordlist, args):
    full = {True: full_node_request, False: node_request}
    pbar = ProgressBar(word_list_counter(args));counter = 0
    try:
        for word in wordlist:
            alive = full.get(args.full)(word, args)
            if alive:
                counter += 1
            pbar.update()

        clean_print(f'[yellow]{counter}/{word_list_counter(args)} diretorios encontrados![yellow]', len('[yellow]'))

    except KeyboardInterrupt:
        print()
        exit(0)

def screen_fetch():
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
    print(screen_fetch())
    parser, args = create_setup_parser()
    check_basic_namespace_arguments(parser, args)
    args.url = verify_http_protocol(args.url)
    
    run(open_word_list_iterator(args), args)
    

if __name__ == '__main__':
    main()

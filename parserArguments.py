from argparse import ArgumentParser

def createSetupParser():
    parser = ArgumentParser(description='Buscador de diretórios web')
    
    parser.add_argument('-u', '--url',  dest='url',
                        help='Url do site alvo')
    parser.add_argument('-w', '--wordlist', dest='wordlist',
                        help='Caminho da wordlist', default='./assets/wordlist.txt')
    parser.add_argument('-t', '--threads', dest='threads',
                        help='Número de threads a serem utilizadas', default=1)
    parser.add_argument('-s', '--ssl', help='Habilita o ssl para a requisição.',
    default=False, action='store_true', dest='ssl')
    parser.add_argument('-f', '--full', help='Mostra o status de todas as requisições, não apenas as bem-sucedidas.', default=False,
    dest='full', action='store_true')

    return parser, parser.parse_args()
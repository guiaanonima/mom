<p class="header" align="center">
 <img width="300px" src="https://raw.githubusercontent.com/Willianjesusdasilva/mom/main/assets/logo.png" align="center" alt="GitHub Readme Stats" />
 <h2 align="center">MOM</h2>
 <p align="center">Porque assim como uma mãe, essa ferramenta sempre acha :)</p>
</p>

## Instalação

```console
# clone o repositório
$ git clone https://github.com/guiaanonima/mom

# altere a pasta de trabalho para mom
$ cd sherlock

# iinstale os requisitos
$ python3 -m pip install -r requirements.txt
```

## Como usar

```console
usage: mom.py [-h] -u URL [-w WORDLIST] [-mc MATCH] [-s] [-f]

Buscador de diretórios web / Search for web directory

options:
  -h, --help            show this help message and exit
  -u URL, --url URL     Url do site alvo
  -w WORDLIST, --wordlist WORDLIST
                        Caminho da wordlist
  -mc MATCH, --match MATCH
                        Corresponde aos códigos de status HTTP | Ex: -mc 302,404,504
  -s, --ssl             Habilita o ssl para a requisição.
  -f, --full            Mostra o status de todas as requisições, não apenas as bem-sucedidas.
```

# Contribua!
Contribuições são bem-vindas! Se você deseja adicionar uma ferramenta, corrigir um bug ou melhorar a documentação, sinta-se à vontade para abrir uma issue, e/ou fazer um pull request.
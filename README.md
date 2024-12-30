<p class="header" align="center">
 <img width="275px" src="./assets/logo-mom.png" align="center" alt="GitHub Readme Stats" />
 <h2 align="center">MOM</h2>
 <p align="center">
  Porque assim como uma mãe, essa ferramenta sempre acha :)
 </p>
</p>

<p class="shields" align="center">
 <a href="https://github.com/guiaanonima/mom/releases">
  <img src="https://img.shields.io/github/release/guiaanonima/mom.svg" alt="Release Tag Image"/>
 </a>
 <a href="https://github.com/guiaanonima/mom/blob/master/LICENSE">
  <img src="https://img.shields.io/github/license/guiaanonima/mom.svg" alt="License">
 </a>
 <img src="https://img.shields.io/badge/python-3.8+-blue.svg"/>
 <a href="https://discord.guiaanonima.com/">
    <img src="https://img.shields.io/discord/719674366861770834?color=0088ff&label=discord">
  </a>
  <a href="https://github.com/guiaanonima/mom/graphs/contributors">
    <img alt="GitHub Contributors" src="https://img.shields.io/github/contributors/guiaanonima/mom?color=0088ff" />
  </a>
</p>


## O que é o MoM?
A MoM (Mon of Mainframe) é uma ferramenta desenvolvida em python, destinado a achar subdiretórios dentro de dominios que o usuário específicar. Ela faz 
a varredura em cada subdiretório, atrás de outros diretórios que podem estar disponíveis.

## Pré-requisitos
- Uma máquina rodando uma distribuição Linux.
- Python 3.8, ou superior, instalado.
- Conexão estável com a internet.

## Instalação
### Usando o Git
1) Clone o reposiório:
```shell
git clone https://github.com/guiaanonima/mom && cd mom
```

2) Instale os requisitos:
```shell
python3 -m pip install -r requirements.txt
```

3) Execute a ferramenta:
```shell
python3 mom.py
```

## Como usar?

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

[git-release]: https://img.shields.io/github/release/guiaanonima/mom.svg
[release-link]: https://github.com/TheMrKeven/ElliotBot/releases

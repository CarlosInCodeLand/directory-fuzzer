import requests

def fuzz_directories(url, wordlist):
    with open(wordlist, 'r') as arquivos:
        for linha in arquivos.readlines():
            url_teste = url + '/' + linha.strip()
            print(url_teste)
            requisicao = requests.get(url_teste)
            if requisicao.status_code == 200:
                print(f'[+] Diretório ou arquivo encontrado: {linha.strip()}')
            else:
                print(f'[X] Diretório ou arquivo não encontrado {requisicao.status_code}: {linha.strip()}')

if __name__ == '__main__':
    # Defina a URL alvo
    url = ''  # Substitua pela URL alvo
    
    # Defina o caminho para o arquivo de wordlist
    wordlist = ''
    
    # Execute o fuzzing
    fuzz_directories(url, wordlist)

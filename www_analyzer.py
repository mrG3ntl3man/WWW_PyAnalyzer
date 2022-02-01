import requests 

print(' ---------- WWW-ANALYZER ----------')
option = -1

while option != '0':
        print('Wybierz opcję:')
        print('0. Zakończ program')
        print('1. Wyświetl status strony WWW')
        print('2. Wypisz zawartość strony WWW')

        option = input('Wybieram opcję: ')

        if option == '1':
                link = input('Podaj pełny link do strony WWW (z http:// lub https://): ')
                if link[0:5] != 'https' and link[0:4] != 'http':
                        print('Brak informacji o protokole (http:// lub https://).')
                else:
                        print('Wykryto informację o protokole (http/https).')
                        www_status = requests.get(link)
                        print('*' * 50)
                        print('Status strony {} to {}'.format(link, www_status))
                        print('*' * 50)
        elif option == '2':
                link = input('Podaj pełny link do strony WWW: (z http:// lub https://): ')
                if link[0:5] != 'https' and link[0:4] != 'http':
                        print('Brak informacji o protokole (http:// lub https://).')
                else:
                        print('Wykryto informację o protokole (http/https).')
                        www_status = requests.get(link)
                        www_text = www_status.text
                        print('*' * 50)
                        print('Zawartość strony WWW {}: '.format(link))
                        print(www_text)
                        print('*' * 50)
        elif option == '0':
                print('---------- BYE ----------')
        else:
                print('Podano błędą opcję!')

print('********** KONIEC PROGRAMU **********'

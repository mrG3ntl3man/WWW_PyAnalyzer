import requests 

print(' ---------- WWW-ANALYZER ----------')
option = -1

while option != '0':
        print('Wybierz opcje:')
        print('0. Zakoncz program')
        print('1. Wyswietl status strony WWW')
        print('2. Wypisz zawartosc strony WWW')
        print('3. Wyswietl naglowki odpowiedzi')

        option = input('Wybieram opcje: ')

        if option == '1':
                link = input('Podaj pelny link do strony WWW (z http:// lub https://): ')
                if link[0:5] != 'https' and link[0:4] != 'http':
                        print('Brak informacji o protokole (http:// lub https://).')
                else:
                        print('Wykryto informacje o protokole (http/https).')
                        www_status = requests.get(link)
                        print('*' * 50)
                        print('Status strony {} to {}'.format(link, www_status))
                        print('*' * 50)
        elif option == '2':
                link = input('Podaj pelny link do strony WWW: (z http:// lub https://): ')
                if link[0:5] != 'https' and link[0:4] != 'http':
                        print('Brak informacji o protokole (http:// lub https://).')
                else:
                        print('Wykryto informacje o protokole (http/https).')
                        www_status = requests.get(link)
                        www_text = www_status.text
                        print('*' * 50)
                        print('Zawartosc strony WWW {}: '.format(link))
                        print(www_text)
                        print('*' * 50)  
        elif option == '3':
                link = input('Podaj pelny link do strony WWW: (z http:// lub https://): ')
                if link[0:5] != 'https' and link[0:4] != 'http':
                        print('Brak informacji o protokole (http:// lub https://).')
                else:
                        print('Wykryto informacje o protokole (http/https).')
                        www_status = requests.get(link)   
                        www_headers = www_status.headers
                        print('Naglowki strony WWW {}:'.format(link))
                        print(www_headers)   
        elif option == '0':
                print('')
        else:
                print('Podano bledna opcje!')

print('********** KONIEC PROGRAMU **********')
print()

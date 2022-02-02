import requests 

print('---------- WWW-ANALYZER ----------')
option = -1

link = input('Podaj pelny link do strony WWW (z http:// lub https://): ')
print()

while option != '0':
        if link[0:5] != 'https' and link[0:4] != 'http':
                print()
                print(' *** Brak informacji o protokole (http:// lub https://) *** ')
                break
        
        print('Wybierz opcje:')
        print('0. Zakoncz program')
        print('1. Wyswietl status strony WWW')
        print('2. Wypisz zawartosc strony WWW')
        print('3. Wyswietl naglowki odpowiedzi')

        option = input('Wybieram opcje: ')

        if option == '1':
                www_status = requests.get(link)
                print()
                print('*** Status strony {} to {} ***'.format(link, www_status))
                print()
        elif option == '2':             
                www_status = requests.get(link)
                www_text = www_status.text
                print()
                print('*** Zawartosc strony WWW {} ***'.format(link))
                print(www_text)
                print()
        elif option == '3':
                www_status = requests.get(link)   
                www_headers = www_status.headers
                print()
                print('*** Naglowki strony WWW {} ***'.format(link))
                print(www_headers)
                print()   
        elif option == '0':
                print('')
        else:
                print('Podano bledna opcje!')

print()
print('*** KONIEC PROGRAMU ***')


# Przeznaczenie 

Generator mikrorachunku podatkowego na potrzeby rozliczania PIT (itp.)
z Urzędem Skarbowym.

Robi to samo co zamieszczony na stronach ministerstwa ale nie zbiera
żadnych informacji i nigdzie ich nie wysyła.

W tej wersji możliwe jest jedynie generowanie numeru rachunku na
podstawie PESEL. Generowanie na podstawie NIP nie jest obsługiwane.

# Użycie:

Wprowadzamy numer PESEL, naciskamy Enter i pojawia się numer rachunku
bankowego. Numer ten jest też kopiowany do schowka i poprzez Wklej/Paste
(Ctrl-V) może zostać wykorzystany w dowolnym miejscu.


# Klawisze:

- Ctrl-q zamknięcie
- Esc reset i wyczyszczenie wszystkich okienek
- Enter - generowanie numeru rachunku i ZAPIS DO SCHOWKA 

# Warunki licencji:

Program jest udostępniany na licencji GPL3, 
[GPL3](https://www.gnu.org/licenses/gpl-3.0.en.html.)

Pomimo całej staranności przy tworzeniu programu twórcy nie gwarantują
poprawnego działania. Twórcy programu nie ponoszą **żadnej**
odpowiedzialności za skutki jego użycia.


# Instalacja/uruchamianie

Program jest prostym skryptem w języku python i uruchomienie nie powinno sprawić żadnych kłopotów. Jeśli jednak wszystkie sposoby zawiodą trzeba przeczytać dokumentację zawartą w poniższych akapitach.

Niezbędna jest działająca w danym systemie instalacja języka Python w wersji 3.0 lub wyższej.

Należy pobrać i zapisać plik `taxAccountGenerator.py`. Jest to zwykły plik tekstowy, który można przeglądać.

## Linux

Po przejściu do kartoteki w której jest zapisany `taxAccountGenerator.py` w terminalu należy wpisać
```
python taxAccountGenerator.py &
```
w niektórych dystrybucjach zamiast `python` trzeba wpisać `python3`. 

## Windows - sposób 1.

Należy uruchomić linię poleceń (cmd) i przejść do kartoteki, gdzie zapisany jest plik `taxAccountGenerator.py`. Następnie wpisać
```
python taxAccountGenerator.py
```

## Windows - sposób 2.

Klikąć prawym przyciskiem myszy na ikonie pliku `taxAccountGenerator.py`.
Z menu należy wybrać `Otwórz przy pomocy` i wpisać `python`
Od tego momentu dwukrotne kliknięcie na ikonie pliku powinno uruchamiać program.




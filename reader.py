import sys
import csv
import json
import pickle

# klasy odpowiadające za odczyt i zapis plikow
class BaseReader:
    def modify_data(self, data, file):
        for files in file:
            if len(files.split(',')) != 3:
                print('Podałeś błędne dane.Spróbuj jeszcze raz')
                exit()
            x, y, value = files.split(',')
            if not x.isdigit() or not y.isdigit():
                print('Podałeś nieprawidłowe wartości współrzędnych.Spróbuj jeszcze raz')
                exit()
            else:
                x = int(x)
                y = int(y)
            if x >= len(data[0]) or y >= len(data):
                print('Podałeś za duże wartości współrzędnych')
                exit()
            data[x][y] = value
        return data


# odczyt i zapis plikow CSV
class CSVReader(BaseReader):
    def read(self, file):
            with open(file, 'r') as f:
                return [line for line in csv.reader(f)]

    def write(self, file, data):
        with open(file, 'w', newline='') as f:
            csv.writer(f).writerows(data)


# odczyt i zapis plikow JSON
class JSONReader(BaseReader):
    def read(self, file):
        with open(file, 'r') as f:
            return json.load(f)

    def write(self, file, data):
        with open(file, 'w') as f:
            json.dump(data, f)


# odczyt i zapis plikow tekstowych
class TXTReader(BaseReader):
    def read(self, file):
        with open(file, 'r') as f:
            for line in f.readlines():
                return line.strip().split(',')

    def write(self, file, data):
        with open(file, 'w') as f:
            for line in data:
                f.write(','.join(line) + '\n')


# odczyt i zapis plikow binarnych
class PickleReader(BaseReader):
    def read(self, file):
        with open(file, 'rb') as f:
            return pickle.load(f)

    def write(self, file, data):
        with open(file, 'wb') as f:
            pickle.dump(data, f)


# slownik mapujacy do konkretnej klasy
types = {'csv': CSVReader(),
         'json': JSONReader(),
         'txt': TXTReader(),
         'pickle': PickleReader()}


# jezeli uzytkownik poda za malo argumentow program zakonczy dzialanie
if len(sys.argv) < 4:
    print('Spróbuj jeszcze raz.Podałeś za mało danych')
    exit()

# nadanie zmiennych, ktorych wartosci zostana wprowadzone z terminala
file_in = sys.argv[1]
file_out = sys.argv[2]
changes = sys.argv[3:]

# sprawdzenie i przypisanie do zmiennej rodzaju pliku
in_file = file_in.split('.')[-1]
out_file = file_out.split('.')[-1]

# odczyt pliku
type = types[in_file]
data = type.read(file_in)

# wywolanie funkcji i zmiana danych
modified_data = type.modify_data(data, changes)

# wyswietlenie zmodyfikowanego pliku
print(f'Zmodyfikowany plik będzie miał następującą zawartość: \n{modified_data}')

# zapisanie do pliku
type = types[out_file]
type.write(file_out, modified_data)
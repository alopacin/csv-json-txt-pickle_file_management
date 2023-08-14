import sys
import csv
import json
import pickle

class BaseReader:
    def __init__(self, file):
        self.file = file

    def modify(self, file):
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


class CSVReader(BaseReader):
    def read(self, file):
        with open(file, 'r') as f:
            reader = csv.reader(f)
            for line in reader:
                data.append(line)

    def write(self, file):
        with open(file, 'w', newline='') as f:
            writer = csv.writer(f)
            for line in data:
                writer.writerow(line)


class JSONReader(BaseReader):
    def read(self, file):
        with open(file, 'r') as f:
            return json.load(f)

    def write(self, file):
        with open(file, 'w') as f:
            json.dump(data, f)


class TXTReader(BaseReader):
    def read(self, file):
        with open(file, 'r') as f:
            for line in f.readlines():
                return line.strip().split(',')

    def write(self, file):
        with open(file, 'w') as f:
            for line in data:
                f.write(','.join(line) + '\n')


class PickleReader(BaseReader):
    def read(self, file):
        with open(file, 'rb') as f:
            return pickle.load(f)

    def write(self, file):
        with open(file, 'wb') as f:
            pickle.dump(data, f)



# jezeli uzytkownik poda za malo argumentow program zakonczy dzialanie
if len(sys.argv) < 2:
    print('Spróbuj jeszcze raz.Podałeś za mało danych')
    exit()

# nadanie zmiennych, ktorych wartosci zostana wprowadzone z terminala
file_in = sys.argv[1]
file_out = sys.argv[2]
changes = sys.argv[3:]

data = []


print(f'Zmodyfikowany plik będzie miał następującą zawartość: \n{data}')

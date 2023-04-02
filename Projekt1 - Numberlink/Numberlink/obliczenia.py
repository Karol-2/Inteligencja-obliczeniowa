# with open('Male.txt', 'r') as f:
#     lines = f.readlines()  # wczytaj wszystkie linie pliku
#
# total_time = 0
# for line in lines:
#     columns = line.split(';')  # podziel linie na kolumny
#     time = float(columns[3])  # wybierz czas z piątej kolumny i zamień na float
#     total_time += time  # dodaj czas do sumy
#
# average_time = total_time / len(lines)  # oblicz średni czas
# print("Małe:", average_time)
#
#
# with open('Srednie.txt', 'r') as f:
#     lines = f.readlines()  # wczytaj wszystkie linie pliku
#
# total_time = 0
# for line in lines:
#     columns = line.split(';')  # podziel linie na kolumny
#     time = float(columns[3])  # wybierz czas z piątej kolumny i zamień na float
#     total_time += time  # dodaj czas do sumy
#
# average_time = total_time / len(lines)  # oblicz średni czas
# print("Średnie:", average_time)
#
# with open('Duze.txt', 'r') as f:
#     lines = f.readlines()  # wczytaj wszystkie linie pliku
#
# total_time = 0
# for line in lines:
#     columns = line.split(';')  # podziel linie na kolumny
#     time = float(columns[3])  # wybierz czas z piątej kolumny i zamień na float
#     total_time += time  # dodaj czas do sumy
#
# average_time = total_time / len(lines)  # oblicz średni czas
# print("Duże:", average_time)

# Otwieramy plik tekstowy do odczytu


with open("Duze.txt", "r") as file:
    # Inicjalizujemy sumę i licznik wartości procentowych
    sum_percent = 0
    count = 0

    # Odczytujemy każdą linię z pliku
    for line in file:
        # Dzielimy linię na elementy, używając średnika jako separatora
        items = line.strip().split(";")

        # Pobieramy wartość procent z pierwszych czterech znaków pola
        percent = items[4][:4]
        percent = int(float(percent))

        # Dodajemy wartość do sumy i zwiększamy licznik
        sum_percent += percent
        count += 1

    # Obliczamy średnią wartość procentową
    if count > 0:
        avg_percent = sum_percent / count
        print("Średnia wartość procentowa: {:.2f}%".format(avg_percent))

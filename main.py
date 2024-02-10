# импорт библиотеки для последующего открытия файла '*.csv'
import csv

# открытие файла
f = open('files/students.csv', encoding='utf-8')

# разделение файла на список
reader = list(csv.reader(f))

# создание доп. списков для удобства и сортировки
reader_better = []
reader_better_const = reader_better
reader_sorted = []

# заполнение reader_better списками с подсписками (разделённным начальным списком)
for i in range(len(reader)):
    reader_better.append(str(reader[i])[2:-2].split(';'))

# введение переменных для хранения максимального значения 'score', а также номера строки, в которой он находится
max_score = 0
max_id = 0

# сортировка списка
for i in range(1, len(reader_better)):
    for line_int in range(1, len(reader_better)):
        line = reader_better[line_int]
        if line != reader_better[0]:
            if line[-1] != 'None':
                iscore = int(line[-1])
                # если макс. значение не является таковым, то данное значение и № строки обновляются:
                if max_score <= iscore:
                    max_score = max(max_score, iscore)
                    max_id = line_int
    # добавление макс. элемента в отсортированный список 'reader_sorted':
    reader_sorted.append(reader_better[max_id])
    # удаление макс. элемента из начального списка:
    reader_better.pop(max_id)
    # обновление переменных:
    max_id = 0
    max_score = 0

# построчный вывод отсортированного списка
for i in range(len(reader_sorted)):
    print(', '.join(reader_sorted[i]))

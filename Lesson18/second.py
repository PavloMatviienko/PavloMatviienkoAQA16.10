import csv
import pytest


def add_row_to_csv(csv_filename, row_data):
    with open(csv_filename, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(row_data)


def delete_row_from_csv(csv_filename, row_index):
    rows = []
    with open(csv_filename, 'r', newline='') as csv_file:
        reader = csv.reader(csv_file)
        rows = list(reader)

    with open(csv_filename, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(rows[:row_index] + rows[row_index + 1:])


def test_add_row_to_csv():
    csv_filename = 'test.csv'
    row_data = ['Pavlo', 'Matviienko', '31']

    add_row_to_csv(csv_filename, row_data)

    with open(csv_filename, 'r', newline='') as csv_file:
        reader = csv.reader(csv_file)
        rows = list(reader)
        assert row_data == rows[-1]


def test_delete_row_from_csv():
    csv_filename = 'test.csv'
    initial_rows = [['Joe', 'Baidonyk', '25'], ['Boris', 'Johnsonyk', '40'], ['Pavlo', 'Matviienko', '31']]

    with open(csv_filename, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(initial_rows)

    row_index_to_delete = 1
    delete_row_from_csv(csv_filename, row_index_to_delete)

    with open(csv_filename, 'r', newline='') as csv_file:
        reader = csv.reader(csv_file)
        remaining_rows = list(reader)
        assert remaining_rows == [initial_rows[0], initial_rows[2]]

# Запуск тестів за допомогою pytest
# pytest script_name.py

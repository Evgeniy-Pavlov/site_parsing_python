import xlsxwriter
from generate_lists_product import array


def writer_report(way=r'C:\Users\Evgeniy\Desktop\data.xlsx', arr=[]):
    book = xlsxwriter.Workbook(way)
    page = book.add_worksheet('Товары')
    row = 0
    column = 0

    page.set_column('A:A', 20)
    page.set_column('B:B', 20)
    page.set_column('C:C', 50)
    page.set_column('C:C', 50)

    for item in array():
        page.write(row, column, item[0])
        page.write(row, column + 1, item[1])
        page.write(row, column + 2, item[2])
        page.write(row, column + 3, item[3])
        row += 1
    book.close()


writer_report(array)

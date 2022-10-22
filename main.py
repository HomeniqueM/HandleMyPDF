from pydoc import Helper
from PyPDF2 import PdfFileWriter, PdfFileReader
import sys
import numpy as np

def extract_range_of_pages(pdf_name : str, pages_range : str) -> None: 
    
    pages = []
    pages_to_include = pages_range.split(',')

    for page in pages_to_include:

        pages_range_numbers = page.split('...')


def delete_pages(pdf_name : str, pages : str) -> None:

    pages_to_delete = list(map(int, pages.split(',')))
    infile = PdfFileReader(pdf_name, 'rb')
    output = PdfFileWriter()

    for i in range(infile.getNumPages()):
        if (i+1) not in pages_to_delete:
            p = infile.getPage(i)
            output.addPage(p)

    with open('newfile.pdf', 'wb') as f:
        output.write(f)
def helper():
    print('Usage:main.py [command] <path>')
    print('-d --delete-pages <page>     to delete pages.')
    print('-e --extract-range-of-pages [<page>,<page>]   Extract page by a range.')

    print('Options:\n')
    print('-h --help     Show this screen.')
    print('--version     Show version.')
    
  
  

if __name__ == '__main__':

    argv_len = len(sys.argv)

    if argv_len == 1:
        print("[ERROR]: Not enough arguments")
        sys.exit(1)

    command = sys.argv[1]
    
    if command == '--help' or command == '--h':
        helper()

    if command == '--delete-pages' or command == '--d':

        if argv_len != 4:
            print("[ERROR]: Not enough arguments")
            sys.exit(1)

        delete_pages(sys.argv[2], sys.argv[3])

    if command == '--extract-range-of-pages' or command == '--e':

        if argv_len != 4:
            print("[ERROR]: Not enough arguments")
            sys.exit(1)

        delete_pages(sys.argv[2], sys.argv[3])
import argparse
from os.path import splitext
from PyPDF2 import PdfFileReader, PdfFileWriter
from PyPDF2.generic import NameObject, createStringObject

def editPDF(path, title, author):
  with open(path,mode="rb") as file:
    info = (PdfFileReader(file)).getDocumentInfo()
  info.update({
    # TODO: handle unicode
    NameObject('/Title'): createStringObject(title),
    NameObject('/Author'): createStringObject(author)
  })

  writer = PdfFileWriter()
  writer.addMetadata(info)
  with open(path,mode="wb") as file:
    writer.write(file)

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Edit ebook metadata.')
  parser.add_argument('book', help='path to an EPUB or PDF FILE')
  parser.add_argument('title', help='new title')
  parser.add_argument('author', help='new author')
  args = parser.parse_args()

  book_path = args.book
  title = args.title
  author = args.author

  (filename, ext) = splitext(book_path)
  if ext.lower() == '.pdf':
    editPDF(book_path, title, author)
  else: 
    print('file format not supported (yet)!')
    exit(0)
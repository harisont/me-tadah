import argparse
from os.path import splitext
from PyPDF2 import PdfFileReader, PdfFileWriter
from PyPDF2.generic import NameObject, createStringObject

def editPDFinfo(path, title, author):
  '''
  given the path to a pdf, a new title and a new author,
  it updates the pdf's title and author InfoKeys
  '''
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
  # manage command line args
  parser = argparse.ArgumentParser(description='Edit ebook metadata.')
  parser.add_argument('book', help='path to an EPUB or PDF FILE')
  parser.add_argument('title', help='new title')
  parser.add_argument('author', help='new author')
  args = parser.parse_args()

  book_path = args.book
  title = args.title
  author = args.author
  (filename, ext) = splitext(book_path)
  ext = ext.lower()

  # handle the various formats 
  if ext == '.pdf':
    editPDFinfo(book_path, title, author)
  else: 
    print('file format not supported (yet)!')
    exit(0)
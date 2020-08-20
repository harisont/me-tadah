import argparse
from os.path import splitext
# pdf stuff
from PyPDF2 import PdfFileReader, PdfFileWriter
from PyPDF2.generic import NameObject, createStringObject
# epub stuff
from ebooklib.epub import read_epub, write_epub

def editPDFinfo(path, title, author):
  '''
  given the path to a pdf, a new title and a new author,
  it updates the pdf's title and author InfoKeys
  '''
  # read only cause update seems not to be possible in place
  with open(path,mode="rb") as pdf:
    info = (PdfFileReader(pdf)).getDocumentInfo()
  info.update({
    # TODO: handle unicode
    NameObject('/Title'): createStringObject(title),
    NameObject('/Author'): createStringObject(author)
  })
  writer = PdfFileWriter()
  writer.addMetadata(info)
  with open(path,mode="wb") as pdf:
    writer.write(pdf)

def editEPUBinfo(path, title, author):
  '''
  given the path to an epub, a new title and a new author,
  it updates the pdf's title and author InfoKeys
  '''
  epub = read_epub(path)
  # not using set_title and add_author cause they don't update existing fields
  epub.set_unique_metadata('DC', 'title', title)
  epub.set_unique_metadata('DC', 'creator', author) # creator = author!?
  write_epub(path, epub)


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
  elif ext == '.epub':
    editEPUBinfo(book_path, title, author)
  else: 
    print('file format not supported (yet)!')
    exit(0)
import argparse
from os.path import splitext, isfile
from os import remove, rename
from pdfrw import PdfReader, PdfWriter
from ebooklib.epub import read_epub, write_epub
from pyperclip import paste as paste_clipboard
from bibtexparser.bparser import BibTexParser
from bibtexparser.bibdatabase import as_text
from pypdftk import concat
from wand.image import Image

def editPDFinfo(path, title, author, cover=None):
  '''
  given the path to a pdf, a new title and a new author,
  it updates the pdf's title and author InfoKeys
  '''
  pdf = (PdfReader(path))
  pdf.Info.Title = title
  pdf.Info.Author = author
  PdfWriter(path, trailer=pdf).write()
  tmp_ebook = "ebook.tmp"
  if cover:
    tmp_cover = 'cover.tmp'
    with Image(filename=cover) as original:
      with original.convert('pdf') as converted:
        converted.save(filename=tmp_cover)
    concat([tmp_cover, path], tmp_ebook)
    remove(tmp_cover)
    remove(path)
    rename(tmp_ebook, path)

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
  parser.add_argument('title', help='new title', nargs='?')
  parser.add_argument('author', help='new author', nargs='?')
  parser.add_argument('--cover', help='path to new cover image', default=None)
  args = parser.parse_args()

  book_path = args.book
  if args.title and args.author: # if title and author are given as clargs
    title = args.title
    author = args.author
  else: # try parse the clipboard as a bibtex string 
    clipboard = paste_clipboard()
    bp = BibTexParser(interpolate_strings=False)
    try:
      bib = bp.parse(clipboard).entries[0]
      title = bib['title']
      author = bib['author']
    except:
      print('your clipboard seems not to contain a bibtex string,')
      print('try provide title and author as command line arguments.')
      exit(-1)

  cover = args.cover

  (filename, ext) = splitext(book_path)
  ext = ext.lower()

  if not isfile(book_path):
    print('that\'s not a valid path, you liar!')
    exit(1)
  # handle the various formats 
  if ext == '.pdf':
    editPDFinfo(book_path, title, author, cover=cover)
  elif ext == '.epub':
    editEPUBinfo(book_path, title, author)
  else: 
    print('file format not supported (yet)!')
    exit(0)
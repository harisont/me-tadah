from argparse import ArgumentParser
from os.path import splitext, isfile
from pdfrw import PdfReader, PdfWriter
from ebooklib.epub import read_epub, write_epub
from music_tag import load_file

MUSIC_FILE_FORMATS = [
  '.aac', 
  '.aiff', 
  '.dsf', 
  '.flac', 
  '.m4a', 
  '.mp3', 
  '.ogg', 
  '.opus', 
  '.wav', 
  '.wv'
  ]

def editPDFinfo(path, title, author):
  '''
  given the path to a .pdf file, a new title and a new author,
  it updates the ebook's title and author InfoKeys
  '''
  pdf = (PdfReader(path))
  pdf.Info.Title = title
  pdf.Info.Author = author
  PdfWriter(path, trailer=pdf).write()

def editEPUBinfo(path, title, author):
  '''
  given the path to an .epub file, a new title and a new author,
  it updates the ebook's title and creator
  '''
  epub = read_epub(path)
  # not using set_title and add_author cause they don't update existing fields
  epub.set_unique_metadata('DC', 'title', title)
  epub.set_unique_metadata('DC', 'creator', author) # creator = author!?
  write_epub(path, epub)

def editAUDIOinfo(path, title, author):
  '''
  given the path to an audio file, a new title and a new author,
  it updates the audio file's tracktitle and artist field
  '''
  audio = load_file(path)
  audio['tracktitle'] = title
  audio['artist'] = author


if __name__ == '__main__':
  # manage command line args
  parser = ArgumentParser(description='Edit ebook and audio metadata.')
  parser.add_argument('file', help='path to an EPUB, PDF or audio file')
  parser.add_argument('title', help='new title')
  parser.add_argument('author', help='new author/artist')
  args = parser.parse_args()

  file_path = args.file
  title = args.title
  author = args.author
  (filename, ext) = splitext(file_path)
  ext = ext.lower()

  if not isfile(file_path):
    print('that\'s not a valid path, you liar!')
    exit(1)
  # handle the various formats 
  if ext == '.pdf':
    editPDFinfo(file_path, title, author)
  elif ext == '.epub':
    editEPUBinfo(file_path, title, author)
  elif ext in MUSIC_FILE_FORMATS:
    editAUDIOinfo(file_path, title, author)
  else: 
    print('file format not supported (yet)!')
    exit(0)
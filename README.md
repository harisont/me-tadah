# Me-tadah!

There are two types of metadata editors: those that don't work, and those that are just a tiny tiny part of a gigantic ebook/music management programme.

Me-tadah, on the contrary, allows you to quickly edit title author/artist of your ebooks and audio files, and that's it.

## Usage
If all you wanted was editing the title and the author/artist of your ebooks or audio files, you just open a terminal and type

```
tadah path_to_file new_title new_author/artist
```

... or something like that.

If you also care about album name, artwork, publisher, cover image, genre, year and so on, you are welcome to open a pull request. With the libraries I'm using, everything should be simple, but I'm too lazy to implement all these things and honestly, 99% of the times I don't really care about anything else.

## Supported formats

### Ebooks
- `.epub`
- `.pdf`

### Audio
- `.aac` 
- `.aiff` 
- `.dsf` 
- `.flac` 
- `.m4a` 
- `.mp3` 
- `.ogg` 
- `.opus` 
- `.wav` 
- `.w`

## Dependencies

- `pdfrw`
- `ebooklib`
- `music_tag`

## Installation
Just like any other Python program (assuming you have Python installed):

1. install the dependencies, for example with `pip install [dep]`
2. clone this repository
3. move inside it
4. mark the Python file as executable (`chmod +x`)
5. add, as the file's first line, the path to your Python interpreter (for example `#!/usr/bin/env python`)
6. copy or move the file to a folder in your `PATH`, e.g. `usr/bin`
7. optionally, you can rename it to just `tadah` (removing the extension). This will allow you to invoke the program by simply typing `tadah [args]`!

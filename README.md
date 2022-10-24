# Me-tadah!

There are two types of metadata editors: those that don't work, and those that are just a tiny tiny part of a gigantic ebook management programme (that sometimes doesn't even work).

Me-tadah, on the other hand, let you quickly edit the title and author of your ebooks and that's it.
If you wish you could also edit the cover, publisher, year of publication and other not-so-crucial pieces of information, you are welcome to open a pull request. Implementing that stuff with the libraries I'm using should be relatively straightforward, but I'm too lazy for that and honestly? I only care about title and author 99% of the times.

## Usage
Just open a terminal and type something like

```
tadah path_to_ebook new_title new_author
```

and... tadah! Your ebook is good to go!

## Supported formats
- `.epub`
- `.pdf`

## Dependencies

- `pdfrw`
- `ebooklib`

## Installation
Just like any other Python program (assuming you have Python installed):

1. install the dependencies, for example with `pip install [dep]`
2. clone this repository
3. move inside it
4. mark the Python file as executable (`chmod +x`)
5. add, as the file's first line, the path to your Python interpreter (for example `#!/usr/bin/env python`)
6. copy or move the file to a folder in your `PATH`, e.g. `usr/bin`
7. optionally, you can rename it to just `tadah` (removing the extension). This will allow you to invoke the program by simply typing `tadah [args]`!

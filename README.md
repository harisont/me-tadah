# Me-tadah!

There are two types of metadata editors: those that don't work, and those that are just a tiny tiny part of a gigantic ebook management programme (that sometimes doesn't even work).

Me-tadah, on the other hand, let you quickly edit the title and author of your ebooks and that's it.
If you wish you could also edit the cover, publisher, year of publication and other not-so-crucial pieces of information, you are welcome to open a pull request. Implementing that stuff with the libraries I'm using should be relatively straightforward, but I'm too lazy for that and honestly? I only care about title and author 99% of the times.

## Usage
Just open a terminal and type something like

```
tadah path_to_ebook new_title new_author
```

or, if you are working with academic papers and are really **_really_** lazy, you can copy a bibtex string such as

```
@inproceedings{lee2017l1,
  title={L1-l2 parallel dependency treebank as learner corpus},
  author={Lee, John SY and Li, Keying and Leung, Herman},
  booktitle={Proceedings of the 15th International Conference on Parsing Technologies},
  pages={44--49},
  year={2017}
}
```

and, while you have it in your clipboard, just type

```
tadah path_to_ebook
```

and... tadah! Your ebook is good to go!

## Supported formats
- `.epub`
- `.pdf`

## Dependencies

- `pdfrw`
- `ebooklib`
- `bibtexparser`
- `pyperclip`

## Installation
Just like any other Python program (assuming you have Python installed):

1. install the dependencies, for example with `pip install [dep]`
2. clone this repository
3. move inside it
4. mark the Python file as executable (`chmod +x`)
5. add, as the file's first line, the path to your Python interpreter (for example `#!/usr/bin/env python`)
6. copy or move the file to a folder in your `PATH`, e.g. `usr/bin`
7. optionally, you can rename it to just `tadah` (removing the extension). This will allow you to invoke the program by simply typing `tadah [args]`!

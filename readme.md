***[Sublime Text 3+](http://www.sublimetext.com/) Package. Install via an updated version of  [Package Control 2+](https://sublime.wbond.net/installation). Just **DON'T** install manually.

# Find Results Commit Changes

## Description

**Not ready for primetime.** Experimental package with the purpose to "commit" any change you made to a "Find Results" buffer. ie:
- Search for "a" in a folder.
- This will open a "Find Results" buffer listing all the files with "a" in it.
- Change the "a" for a "b" in these lines that match content.
- Go to -> "Main menubar" -> "Find" -> "Find Results Commit Any Change Made"
- This will write all the changes made back to all the files.

## Bugs

- Double click in these lines with numbers and a colon will open the file :-/  ST default behaviour(how to disable it?)
- Will not modify any other line, even if you insert a new line.
- WONTFIX: Will write/read UTF8 files, if you have a file in another encoding, considering jumping to the U8 world. :)

## Source-code

https://github.com/SublimeText/FindResultsCommitChanges

## Forum Thread

http://www.sublimetext.com/forum/viewtopic.php?f=6&t=14118
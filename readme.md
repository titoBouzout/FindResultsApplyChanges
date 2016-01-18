**[Sublime Text 3+](http://www.sublimetext.com/) Package**. Install via an updated version of  [Package Control 2+](https://sublime.wbond.net/installation). Just **DON'T** install manually.

# Find Results Apply Changes

## Description

Apply any change you made to a "Find Results" buffer back to the files. ie:
- Search for "foo" in a folder.
- This will open a "Find Results" buffer listing all the files with "foo" in it.
- Change the instances of "foo" for "bar" or something else...
- Go to the -> Main menubar -> "Find" -> "Find Results - Apply Changes" or just press CTRL/CMD+S
- This will write all the changes made back to the files.
- Will be enabled only if the focused view is the "Find Results" tab.

## Bugs

- Uses regions to allow you do multiline changes, but when inserting new newlines, if you already applied some change, will corrupt files **if you commit more than once**, this because the new newlines will shift the line numbers. Will also 'corrupt' files if you add/remove newlines in other instances of the modified files. eg in another tab. To prevent corruption this packages will alert you and prevent most of these.

## WONTFIX

- Will write/read UTF8 files. If you have a file in another encoding, considering jumping to the U8 world. :)
- It converts line ending of files to Unix style
- This package disables the "double-click = open file" in Find Results.

# Find Exclude Patterns

## Description

"Find in Files" command includes a lot of noise from binary files, folders you don't want to include in search (caches, generated files, logs, version control, external libraries, etc, etc, etc). The current way to exclude these from searches... is to manually select the list for every search... ! insane.

When installed, this package will automatically append negative values ("please don't search XYZ") to the "where" parameter every time you open the the "Find in Files" panel.

## Preferences

By default will exclude the following normal Sublime Text preferences: "index_exclude_patterns" and "binary_file_patterns". Plus a new preference named "find_exclude_patterns". These preferences default to an empty list or array when blank or not used.

To edit your preferences just go to: Main menubar -> Preferences -> Settings - User.

TIP: To exclude a folder you need to write it like this: "\*/.git/\*". Then for example to exclude version control from searches your preference will looks somewhat like this:

    "find_exclude_patterns": ["*/.svn/*", "*/.git/*", "*/.hg/*", "*/CVS/*"]

## Source-code

https://github.com/titoBouzout/FindResultsApplyChanges

## Forum Thread

http://www.sublimetext.com/forum/viewtopic.php?f=6&t=14118

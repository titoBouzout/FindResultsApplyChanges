
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
- "double-click = open file" in Find Results doesn't work with this package. This is an intented behavior. To restore the double-click behavior, you need to add `"disable_double_click": false` config line into your preferences file (to edit your preferences just go to: Main menubar -> Preferences -> Package Settings -> FindResultsApplyChanges -> Settings – User).

## WONTFIX

- Will write/read UTF8 files. If you have a file in another encoding, considering jumping to the U8 world. :)
- It converts line ending of files to Unix style

# Find Exclude Patterns

## Description

"Find in Files" command includes a lot of noise from binary files, folders you don't want to include in search (caches, generated files, logs, version control, external libraries, etc, etc, etc). The current way to exclude these from searches... is to manually select the list for every search... ! insane.

When installed, this package will automatically append negative values ("please don't search XYZ") to the "where" parameter every time you open the "Find in Files" panel.

## Preferences

To edit your preferences just go to: Main menubar -> Preferences -> Settings - User.

By default will exclude the following normal Sublime Text preferences: "index_exclude_patterns" and "binary_file_patterns".

This package used to have a preference named "find_exclude_patterns", now NO longer applies and that preference is ignored.

To exlude a folder, you should add it to the "binary_file_patterns", for example to exlude the popular version control systems you can have something like this:

	"binary_file_patterns": [".svn/**", ".git/**", ".hg/**", "CVS/**"]

### Installation

Download or clone the contents of this repository to a folder named exactly as the package name into the Packages/ folder of ST.

## Source-code

https://github.com/titoBouzout/FindResultsApplyChanges

## Forum Thread

https://forum.sublimetext.com/t/pkg-to-edit-just-there-in-the-find-results-tab-yes/11408
https://forum.sublimetext.com/t/findexcludepatterns-exclusion-list-for-search-results/15323

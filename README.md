# advanced_python_2025
Homeworks for advanced python course at HSE. 

## HW_1 CLI
Simplified CLI application

* `nl` -- a script that outputs numbered lines from a file or `stdin` in `stdout`. Supports the `-b` flag that specify the 
logical page body lines to be numbered. Recognized type arguments are: `a` (all lines),
`t` (only non-empty lines), `n` (no line numbering). 
* `tail` -- a script that outputs the last 10 lines of each files and 17 lines if no files are given.
* `wc` -- a script displays the number of lines, words, and bytes contained
     in each input file, or standard input (if no file is specified) to the
     standard output.

## HW_2 LaTex generator
A Python module for generating LaTeX documents, tables, and images dynamically.

* `generate_doc` -- generates a LaTeX document with the specified content blocks, document class, and packages.
* `generate_table` -- generates a LaTeX table from a 2D list.
* `generate_image`--  generates LaTeX code for embedding an image using the provided file path.

### Installation

```bash
pip install latex-generator-lilyreber

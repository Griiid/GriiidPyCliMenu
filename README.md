# GriiidPyCliMenu

A python CLI menu user interface. It only support Unix systems now.

## Table of contents

<!-- TOC -->

- [GriiidPyCliMenu](#griiidpyclimenu)
  - [Table of contents](#table-of-contents)
  - [Document](#document)
    - [Installation](#installation)
    - [Quick Start](#quick-start)
      - [CliMenuList](#climenulist)
  - [Future Work](#future-work)
  - [License](#license)

<!-- /TOC -->

## Document

### Installation

You can download this repository and copy the module derectory `GriiidPyCliMenu` to where you want.

### Quick Start

You can find examples in the directory `example`.

Most of the examples intend to demonstrate a single menu type:

---

#### CliMenuList

Prompt a string list for user to select one.

User can use arrow home, end keys to move the cursor.

| Key    |  Description             |
|--------|--------------------------|
| `↑`    | Move the cursor up.      |
| `↓`    | Move the cursor down.    |
| `←`    | Move to previous page.   |
| `→`    | Move to next page.       |
| `Home` | Move to the first parge. |
| `End`  | Move to the last page.   |

Exmple:
[list.py](example/list.py)

Demo:
<a href="http://www.youtube.com/watch?feature=player_embedded&v=O7_BZLLgolo" target="_blank"><img src="http://img.youtube.com/vi/O7_BZLLgolo/0.jpg" alt="Demo" /></a>

---

## Future Work

- Filter list by key-in keyword
- Add new menu type checkbox
- Add new menu type option
- Support Window platform

## License

Copyright (c) 2018 Griiid

Licensed under the MIT license.
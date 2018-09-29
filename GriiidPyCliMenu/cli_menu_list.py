import termios, sys

class CliMenuList():
    """
    Prompt a string list to select an item.
    """

    def __init__(self, title="CLI SELECT LIST", widnow_width=40, items_per_page=0):
        """
        If title is empyt, it will NOT display the title.
        If window_width is too short, it will adjust the value according to the length of the title.
        """
        self._title = title
        self._window_width = widnow_width if len(title) + 6 <= widnow_width else len(title) + 6
        self._items_per_page = items_per_page

        # Initial items in CliMenuList
        self._items = []
        self._select = 0

    def set_title(self, title):
        """
        Set title
        """
        self_title = title

    def set_items_per_page(self, items_per_page):
        """
        Set item numbers per page
        """
        self._items_per_page = items_per_page

    def add_item(self, item):
        """
        Add a string or a string list.
        """
        if type(item) is str:
            self._items.append(item)

        elif type(item) is list:
            if any(type(i) != str for i in item):
                    raise TypeError("items in a list should be str")
            self._items += item

        else:
            raise TypeError("item should be str or [str]")

    def clear(self):
        """
        Clear items
        """
        self._items.clear()
        self._select = 0

    def prompt(self, clear_after_choose=True):
        """
        Prompt the select list.
        If clear_after_choose is True, it will clear the prompt list after select.
        """
        if len(self._items) == 0:
            return ""

        self._first_time_prompt = True
        self._show_title()

        while True:
            self._show_items()

            while True:
                # Get a key
                ch = self._getch()
                code = ord(ch)

                if code == 0x03: # Ctrl-C
                    if clear_after_choose:
                        self._clear_prompt_lines()

                    return ""

                elif code in {0x0A, 0x0D}: # Enter
                    if clear_after_choose:
                        self._clear_prompt_lines()

                    return self._items[self._select]

                elif code == 0x1B: # ESC Charcter
                    code1, code2 = ord(self._getch()), ord(self._getch())
                    if code1 == 91:
                        if code2 == 65: # Up
                            self._move_up()
                        elif code2 == 66: # Down
                            self._move_down()
                        elif code2 == 67: # Right
                            self._move_to_next_page()
                        elif code2 == 68: # Left
                            self._move_to_previous_page()
                        elif code2 == 70: # End
                            self._move_to_last()
                        elif code2 == 72: # Home
                            self._move_to_first()
                        else:
                            continue

                        break

    def _move_up(self):
        """
        Move the cursor up.
        """
        self._select = len(self._items) - 1 if self._select == 0 else self._select - 1
        self._current_page = self._select // self._items_per_page

    def _move_down(self):
        """
        Move the cursor down.
        """
        self._select = 0 if self._select == len(self._items) - 1 else self._select + 1
        self._current_page = self._select // self._items_per_page

    def _move_to_next_page(self):
        """
        Move the cursor to next page.
        """
        self._current_page = 0 if self._current_page == self._total_pages - 1 else self._current_page + 1
        self._select = self._current_page * self._items_per_page

    def _move_to_previous_page(self):
        """
        Move the cursor to previous page.
        """
        self._current_page = self._total_pages - 1 if self._current_page == 0 else self._current_page - 1
        self._select = self._current_page * self._items_per_page

    def _move_to_last(self):
        """
        Move the cursor to the last page.
        """
        self._current_page = self._total_pages - 1
        self._select = self._current_page * self._items_per_page

    def _move_to_first(self):
        """
        Move the cursor to the first page.
        """
        self._current_page = 0
        self._select = self._current_page * self._items_per_page

    def _show_title(self):
        """
        Show the title if not empty.
        """
        self.should_redraw_title = False

        if self._title == "":
            return

        print("\x1B[1;30;47m" + " " + "=" * (self._window_width - 2) + " \x1B[m")

        # Print the title at center.
        left_space = (self._window_width - 4 - len(self._title)) // 2
        right_sapce = left_space + (self._window_width - len(self._title)) % 2
        print("\x1B[1;30;47m" + " =" + " " * left_space + self._title + " " * right_sapce  + "= " + "\x1B[m")

        print("\x1B[1;30;47m" + " " + "=" * (self._window_width - 2) + " \x1B[m")

    def _show_items(self):
        """
        Show items of current page.
        """
        if self._first_time_prompt:
            self._total_pages = len(self._items) // self._items_per_page + \
                                (1 if len(self._items) % self._items_per_page != 0 else 0)
            self._current_page = 0
            self._first_time_prompt = False
        else:
            # If NOT first time, move cursor up
            sys.stdout.write("\x1B[" + str(self._items_per_page + 1) + "A")

        # Page number
        print(("\x1B[33m{:>" + str(self._window_width) + "}\x1B[m").format(
                    "PAGE " + str(self._current_page + 1) + "/" + str(self._total_pages))
                    )
        top_index = self._current_page * self._items_per_page

        # Items
        for i in range(top_index, top_index + self._items_per_page):
            sys.stdout.write("\x1B[2K\r")
            if i < len(self._items):
                if i == self._select:
                    sys.stdout.write("> ")
                else:
                    sys.stdout.write("  ")
                print(self._items[i])
            else:
                print("")

    def _clear_prompt_lines(self):
        """
        Clear the prompt lines
        """
        sys.stdout.write("\r")
        for i in range(0, self._items_per_page + (4 if self._title != "" else 1)):
            sys.stdout.write("\x1B[A\x1B[2K\r")

    def _getch(self):
        """
        Interrupting program until pressed any key"
        from: https://www.programcreek.com/python/example/89182/tty.setraw
        """
        try:
            import msvcrt
            return msvcrt.getch()

        except ImportError:
            import sys
            import tty
            import termios
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(1)
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch

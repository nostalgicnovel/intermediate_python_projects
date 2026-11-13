# Programming Assignment 7 - GUIs

## Assignment Overview

In this assignment, you will build a small desktop application with `tkinter`
for logging internal IT support tickets. Staff enter a requester name and a
short summary, choose a priority, optionally flag the ticket for follow-up, and
add it to a list. They can also remove a selected ticket or clear the form.

Complete the functions and methods in `ticket_desk.py`. You will write a few
plain functions that validate and format ticket data, then build the window
layout and the event handlers that connect the widgets to that logic. You may
design the layout with the [Visual Tkinter Designer](https://visualtkinter.com/designer)
and paste the generated widget code into `build_widgets`, adjusting names to
match the required attributes, or write it by hand with `.place()`. Do not
change required names or parameter lists because the tests depend on them.

Your completed form should look as follows:

<img src=".github/images/formdesign.png" alt="Graph" style="width:50%">


## Learning Objectives

By the end of this assignment, you should be able to:

- Build a `tkinter` window with labels, entries, buttons, radiobuttons, a
  checkbutton, a listbox, and a scrollbar.
- Use `StringVar` and `BooleanVar` to share state with widgets.
- Connect buttons to event handler methods with the `command` option.
- Read, clear, and update widget contents.
- Validate user input and report problems with `messagebox`.
- Keep GUI state (a list of dictionaries) in sync with what is displayed.
- Separate testable logic from widget code.
- Use `pip` and a virtual environment (`venv`) to install project dependencies.
- Run `pytest` tests against a GUI application.

## Assignment Structure

The assignment includes a starter module containing the `TicketDesk` class and
function stubs, a pytest file that checks the required behavior, and a GitHub
Actions workflow that runs the tests for autograding. All work is done in
Python; no external data files, images, or services are needed.

### Directory Structure

```
218-pa-7/
├── README.md
├── .gitignore
├── requirements.txt
├── ticket_desk.py
├── test_ticket_desk.py
└── .github
    └── workflows
        └── classroom.yml
```

## Functions to Implement

Complete the items below in `ticket_desk.py`. Keep each required name and
parameter list unchanged. The constants, `TicketDesk.__init__`, and the imports
are provided. The docstrings in the starter module are the authoritative
reference for exact text, return values, and attribute names.

| Function or Method | Description |
| --- | --- |
| `validate_ticket(requester, summary, priority)` | Return the first validation error message, or `None` if the input is valid. |
| `format_ticket(number, requester, summary, priority, follow_up)` | Build the text shown for a ticket in the list. |
| `response_target_hours(priority, follow_up)` | Look up the response target for a priority, halved for follow-up tickets; raise `ValueError` for an unknown priority. |
| `status_text(tickets)` | Build the status line with the number of open tickets and the number of high priority tickets. |
| `TicketDesk.build_widgets()` | Create and place the labels, entries, radiobuttons, checkbutton, buttons, listbox, scrollbar, and status label using the required attribute names. |
| `TicketDesk.on_add()` | Validate the form; show an error dialog if invalid, otherwise store the ticket, add it to the listbox, reset the form, and update the status. |
| `TicketDesk.on_remove()` | Remove the selected ticket from the listbox and the ticket list, or show an information dialog if nothing is selected. |
| `TicketDesk.on_clear()` | Reset the entries, priority, and checkbutton, and focus the requester entry, without changing the ticket list. |
| `TicketDesk.on_exit()` | Close the window. |
| `main()` | Create the root window and the application, then start the event loop. |

## Testing and Performance Analysis

Your implementation is checked with `test_ticket_desk.py`, a suite of `pytest`
unit tests. The tests are grouped as follows:

- `TestPureFunctions` checks validation order and messages, length boundaries,
  ticket formatting, response targets, and the status line.
- `TestWindowLayout` checks the window title and size, widget types and text,
  radiobutton and checkbutton variable bindings, button labels, the listbox and
  scrollbar connection, the initial status text, and that every widget is
  placed in the window.
- `TestEventHandlers` checks adding, removing, and clearing tickets, error
  and information dialogs, numbering, status updates, window closing, and
  the `main()` entry point.

The GUI tests create a real `tkinter` window that is hidden from view, and
they replace `messagebox` calls so no dialog ever blocks the tests. They use
in-memory data only and do not create or modify files. Every function runs in
time proportional to the number of tickets, which is more than fast enough for
interactive use. The workflow in `.github/workflows/classroom.yml` runs the
tests under `xvfb-run` (a virtual display) so they work on GitHub Actions.

## How to Run

1. Make sure Python 3.12 or later and `pip` are installed.
2. From this directory, create and activate a virtual environment:

   ```
   python -m venv .venv
   source .venv/bin/activate
   ```

   On Windows, activate it with `.venv\Scripts\activate` instead.

3. Install the testing dependency:

   ```
   pip install -r requirements.txt
   ```

4. Open `ticket_desk.py` and complete each item marked with
   `# TODO: Implement this function`.
5. Run the application to try your window:

   ```
   python ticket_desk.py
   ```

6. Run the automated test suite:

   ```
   pytest test_ticket_desk.py -v
   ```

   On a Linux machine without a display, run `xvfb-run pytest test_ticket_desk.py -v`
   instead. If `tkinter` is missing on Linux, install it with
   `sudo apt install python3-tk`.

## Expected Output

When you run `pytest test_ticket_desk.py -v`, pytest displays one line for
each test, including its test name and a `PASSED` or `FAILED` result. The tests
are grouped into `TestPureFunctions`, `TestWindowLayout`, and
`TestEventHandlers`, so a failure name (for example,
`TestEventHandlers::test_remove_without_selection`) identifies the behavior
that needs attention. Until you finish the assignment, most tests report
`FAILED`. When all required behavior is implemented correctly, every test
reports `PASSED`, followed by a summary with the total number of passed tests
and the test run time. Running `python ticket_desk.py` opens the "Support
Ticket Desk" window; no output is printed to the console.

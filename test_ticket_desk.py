"""
CS 218 - Intermediate Python
Programming Assignment 7: GUIs

Unit tests for ticket_desk.py. These tests are used for GitHub Actions
autograding. The GUI tests create a real (hidden) tkinter window, so they
need a display. Run them locally with:

    pytest test_ticket_desk.py -v

On a headless Linux machine, run them with: xvfb-run pytest test_ticket_desk.py -v
"""

import tkinter as tk

try:
    import pytest
except ImportError:
    import sys, subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pytest"])
    import pytest


import ticket_desk as td


@pytest.fixture
def app():
    try:
        root = tk.Tk()
    except tk.TclError as error:
        pytest.fail(f"Could not open a tkinter window (no display?): {error}")
    root.withdraw()
    desk = td.TicketDesk(root)
    yield desk
    try:
        root.destroy()
    except tk.TclError:
        pass


@pytest.fixture
def dialogs(monkeypatch):
    """Replace message boxes so tests never block, and record the calls."""
    calls = []
    monkeypatch.setattr(
        td.messagebox, "showerror", lambda *a, **k: calls.append(("error", a))
    )
    monkeypatch.setattr(
        td.messagebox, "showinfo", lambda *a, **k: calls.append(("info", a))
    )
    return calls


def fill(app, requester, summary, priority=None, follow_up=None):
    app.txt_requester.delete(0, tk.END)
    app.txt_requester.insert(0, requester)
    app.txt_summary.delete(0, tk.END)
    app.txt_summary.insert(0, summary)
    if priority is not None:
        app.priority_var.set(priority)
    if follow_up is not None:
        app.follow_up_var.set(follow_up)


def listbox_items(app):
    return list(app.lst_tickets.get(0, tk.END))


class TestPureFunctions:
    def test_validate_valid_ticket(self):
        assert td.validate_ticket("John Smith", "Printer offline", "High") is None

    def test_validate_empty_requester(self):
        assert td.validate_ticket("", "Printer offline", "Low") == (
            "Requester name is required."
        )

    def test_validate_whitespace_requester(self):
        assert td.validate_ticket("   ", "Printer offline", "Low") == (
            "Requester name is required."
        )

    def test_validate_empty_summary(self):
        assert td.validate_ticket("John", "  ", "Low") == "Summary is required."

    def test_validate_summary_length_boundary(self):
        assert td.validate_ticket("John", "x" * 60, "Low") is None
        assert td.validate_ticket("John", "x" * 61, "Low") == (
            "Summary must be 60 characters or fewer."
        )

    def test_validate_summary_length_ignores_padding(self):
        assert td.validate_ticket("John", "  " + "x" * 60 + "  ", "Low") is None

    def test_validate_bad_priority(self):
        assert td.validate_ticket("John", "Printer", "Urgent") == (
            "Priority must be Low, Medium, or High."
        )

    def test_validate_reports_first_problem(self):
        assert td.validate_ticket("", "", "Urgent") == "Requester name is required."
        assert td.validate_ticket("John", "", "Urgent") == "Summary is required."

    def test_format_ticket_basic(self):
        assert td.format_ticket(
            3, "Donald Hebb", "VPN drops", "Medium", False
        ) == "#003 [MEDIUM] Donald Hebb - VPN drops"

    def test_format_ticket_follow_up(self):
        assert td.format_ticket(
            7, "John Smith", "Printer offline", "High", True
        ) == "#007 [HIGH] John Smith - Printer offline (follow-up)"

    def test_format_ticket_wide_number(self):
        assert td.format_ticket(1234, "A", "B", "Low", False) == "#1234 [LOW] A - B"

    @pytest.mark.parametrize(
        "priority, follow_up, expected",
        [
            ("Low", False, 72),
            ("Medium", False, 24),
            ("High", False, 4),
            ("Low", True, 36),
            ("Medium", True, 12),
            ("High", True, 2),
        ],
    )
    def test_response_target_hours(self, priority, follow_up, expected):
        assert td.response_target_hours(priority, follow_up) == expected

    def test_response_target_hours_unknown_priority(self):
        with pytest.raises(ValueError):
            td.response_target_hours("Urgent", False)

    def test_status_text_empty(self):
        assert td.status_text([]) == "Open tickets: 0 | High priority: 0"

    def test_status_text_counts_high(self):
        tickets = [
            {"priority": "High"},
            {"priority": "Low"},
            {"priority": "High"},
            {"priority": "Medium"},
        ]
        assert td.status_text(tickets) == "Open tickets: 4 | High priority: 2"


class TestWindowLayout:
    def test_window_title_and_geometry(self, app):
        assert app.root.title() == "Support Ticket Desk"
        app.root.deiconify()
        app.root.update()
        assert app.root.geometry().startswith("520x480")

    def test_entries_exist(self, app):
        assert isinstance(app.txt_requester, tk.Entry)
        assert isinstance(app.txt_summary, tk.Entry)
        assert app.txt_requester is not app.txt_summary

    def test_entries_start_empty(self, app):
        assert app.txt_requester.get() == ""
        assert app.txt_summary.get() == ""

    def test_priority_radiobuttons(self, app):
        expected = [
            (app.rad_low, "Low"),
            (app.rad_medium, "Medium"),
            (app.rad_high, "High"),
        ]
        for button, label in expected:
            assert isinstance(button, tk.Radiobutton)
            assert button.cget("text") == label
            assert button.cget("value") == label
            assert str(button.cget("variable")) == str(app.priority_var)

    def test_radiobuttons_change_priority(self, app):
        app.rad_high.invoke()
        assert app.priority_var.get() == "High"
        app.rad_low.invoke()
        assert app.priority_var.get() == "Low"

    def test_default_priority_is_medium(self, app):
        assert app.priority_var.get() == "Medium"

    def test_follow_up_checkbutton(self, app):
        assert isinstance(app.chk_follow_up, tk.Checkbutton)
        assert app.chk_follow_up.cget("text") == "Needs follow-up"
        assert str(app.chk_follow_up.cget("variable")) == str(app.follow_up_var)
        assert app.follow_up_var.get() is False
        app.chk_follow_up.invoke()
        assert app.follow_up_var.get() is True

    @pytest.mark.parametrize(
        "name, text",
        [
            ("btn_add", "Add Ticket"),
            ("btn_remove", "Remove Selected"),
            ("btn_clear", "Clear Form"),
            ("btn_exit", "Exit"),
        ],
    )
    def test_buttons(self, app, name, text):
        button = getattr(app, name)
        assert isinstance(button, tk.Button)
        assert button.cget("text") == text
        assert str(button.cget("command")) != ""

    def test_listbox_and_scrollbar(self, app):
        assert isinstance(app.lst_tickets, tk.Listbox)
        assert isinstance(app.scr_tickets, tk.Scrollbar)
        assert app.lst_tickets.size() == 0
        assert str(app.scr_tickets.cget("orient")) == "vertical"
        assert app.lst_tickets.cget("yscrollcommand") != ""
        assert app.scr_tickets.cget("command") != ""

    def test_status_label_initial(self, app):
        assert isinstance(app.lbl_status, tk.Label)
        assert app.lbl_status.cget("text") == "Open tickets: 0 | High priority: 0"

    def test_widgets_are_placed(self, app):
        app.root.update_idletasks()
        for name in (
            "txt_requester",
            "txt_summary",
            "rad_low",
            "rad_medium",
            "rad_high",
            "chk_follow_up",
            "btn_add",
            "btn_remove",
            "btn_clear",
            "btn_exit",
            "lst_tickets",
            "lbl_status",
        ):
            assert getattr(app, name).winfo_manager() != "", name


class TestEventHandlers:
    def test_add_ticket_updates_everything(self, app, dialogs):
        fill(app, "  John Smith ", " Printer offline ", "High", True)
        app.btn_add.invoke()
        assert dialogs == []
        assert listbox_items(app) == [
            "#001 [HIGH] John Smith - Printer offline (follow-up)"
        ]
        assert app.tickets == [
            {
                "number": 1,
                "requester": "John Smith",
                "summary": "Printer offline",
                "priority": "High",
                "follow_up": True,
            }
        ]
        assert app.next_number == 2
        assert app.lbl_status.cget("text") == "Open tickets: 1 | High priority: 1"

    def test_add_resets_form(self, app, dialogs):
        fill(app, "John", "Printer", "High", True)
        app.on_add()
        assert app.txt_requester.get() == ""
        assert app.txt_summary.get() == ""
        assert app.priority_var.get() == "Medium"
        assert app.follow_up_var.get() is False

    def test_add_multiple_numbers_in_order(self, app, dialogs):
        fill(app, "A", "First", "Low", False)
        app.on_add()
        fill(app, "B", "Second", "Medium", False)
        app.on_add()
        fill(app, "C", "Third", "High", False)
        app.on_add()
        assert listbox_items(app) == [
            "#001 [LOW] A - First",
            "#002 [MEDIUM] B - Second",
            "#003 [HIGH] C - Third",
        ]
        assert [t["number"] for t in app.tickets] == [1, 2, 3]
        assert app.lbl_status.cget("text") == "Open tickets: 3 | High priority: 1"

    def test_add_invalid_shows_error_and_changes_nothing(self, app, dialogs):
        fill(app, "", "Printer offline", "High", True)
        app.on_add()
        assert dialogs == [("error", ("Invalid Ticket", "Requester name is required."))]
        assert app.tickets == []
        assert listbox_items(app) == []
        assert app.next_number == 1
        assert app.txt_summary.get() == "Printer offline"
        assert app.priority_var.get() == "High"

    def test_add_invalid_summary_message(self, app, dialogs):
        fill(app, "John", "x" * 61)
        app.on_add()
        assert dialogs == [
            ("error", ("Invalid Ticket", "Summary must be 60 characters or fewer."))
        ]
        assert app.tickets == []

    def test_remove_selected_ticket(self, app, dialogs):
        for name in ("A", "B", "C"):
            fill(app, name, "Issue", "High")
            app.on_add()
        app.lst_tickets.selection_set(1)
        app.btn_remove.invoke()
        assert dialogs == []
        assert listbox_items(app) == ["#001 [HIGH] A - Issue", "#003 [HIGH] C - Issue"]
        assert [t["requester"] for t in app.tickets] == ["A", "C"]
        assert app.lbl_status.cget("text") == "Open tickets: 2 | High priority: 2"

    def test_remove_does_not_reuse_numbers(self, app, dialogs):
        fill(app, "A", "Issue")
        app.on_add()
        app.lst_tickets.selection_set(0)
        app.on_remove()
        fill(app, "B", "Issue")
        app.on_add()
        assert listbox_items(app) == ["#002 [MEDIUM] B - Issue"]

    def test_remove_without_selection(self, app, dialogs):
        fill(app, "A", "Issue")
        app.on_add()
        app.on_remove()
        assert dialogs == [("info", ("No Selection", "Select a ticket to remove."))]
        assert len(app.tickets) == 1
        assert app.lst_tickets.size() == 1

    def test_clear_resets_form_only(self, app, dialogs):
        fill(app, "A", "Issue")
        app.on_add()
        fill(app, "Marcus", "VPN drops", "Low", True)
        app.btn_clear.invoke()
        assert app.txt_requester.get() == ""
        assert app.txt_summary.get() == ""
        assert app.priority_var.get() == "Medium"
        assert app.follow_up_var.get() is False
        assert len(app.tickets) == 1
        assert app.lst_tickets.size() == 1

    def test_clear_sets_focus_on_requester(self, app):
        app.root.deiconify()
        app.root.update()
        app.txt_summary.focus_force()
        app.on_clear()
        app.root.update()
        assert app.root.focus_get() is app.txt_requester

    def test_exit_destroys_window(self, app):
        app.btn_exit.invoke()
        with pytest.raises(tk.TclError):
            app.root.title()

    def test_main_creates_app_and_runs_loop(self, monkeypatch):
        events = []

        class FakeRoot:
            def title(self, *a):
                events.append("title")

            def geometry(self, *a):
                events.append("geometry")

            def mainloop(self):
                events.append("mainloop")

        built = []

        class FakeDesk:
            def __init__(self, root):
                built.append(root)

        monkeypatch.setattr(td.tk, "Tk", FakeRoot)
        monkeypatch.setattr(td, "TicketDesk", FakeDesk)
        td.main()
        assert len(built) == 1
        assert events == ["mainloop"]


if __name__ == "__main__":
    pytest.main(["-v", __file__])
    
# tests/test_my_assistant.py
# Author: Christina Vo

from my_assistant import GroomingAssistant
from my_tool import GroomingSchedule


def make_assistant():
    """Create a fresh grooming assistant for each test."""
    schedule = GroomingSchedule(
        {
            "monday": "9:00 am and 1:30 pm",
            "wednesday": "10:00 am and 3:00 pm",
            "friday": "11:00 am",
        }
    )
    return GroomingAssistant("Bella", "Be helpful.", schedule)


def test_available_times_uses_tool():
    assistant = make_assistant()
    reply = assistant.respond("What times are available on Monday?")
    assert reply == "Available grooming times on monday: 9:00 am and 1:30 pm."


def test_unknown_day_asks_for_clarification():
    assistant = make_assistant()
    reply = assistant.respond("What times are available on Sunday?")
    assert "Which day?" in reply


def test_booking_request_goes_to_staff():
    assistant = make_assistant()
    reply = assistant.respond("Please book an appointment")
    assert "grooming staff" in reply


def test_unknown_request_gets_safe_reply():
    assistant = make_assistant()
    reply = assistant.respond("Do you sell dog food?")
    assert "not sure" in reply


def test_history_records_both_sides():
    assistant = make_assistant()
    assistant.respond("hello")
    assistant.respond("What times are available on Friday?")
    assert len(assistant.history) == 4
    assert assistant.history[0]["role"] == "user"
    assert assistant.history[1]["role"] == "assistant"

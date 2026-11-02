# my_assistant.py
# Author: Christina Vo

HANDOFF_WORDS = ["book", "cancel", "reschedule"]


class GroomingAssistant:
    """A mock assistant for a pet grooming business."""

    def __init__(self, name, instructions, grooming_schedule):
        """Store the assistant's details, tool, and conversation history."""
        self.name = name
        self.instructions = instructions
        self.grooming_schedule = grooming_schedule
        self.history = []

    def respond(self, user_message):
        """Record the user's message and the assistant's reply."""
        self.history.append({"role": "user", "content": user_message})
        reply = self.choose_reply(user_message)
        self.history.append({"role": "assistant", "content": reply})
        return reply

    def choose_reply(self, user_message):
        """Choose a response using simple keyword rules."""
        text = user_message.lower()

        if self.needs_human(text):
            return "I can't change appointments. I'll refer you to our grooming staff."

        if "open" in text or "available" in text:
            return self.times_reply(user_message)

        if "hello" in text or "hi" == text:
            return (
                f"Hello! I'm {self.name}. "
                "I can check available pet grooming appointments."
            )

        return (
            "I'm not sure how to help with that. "
            "I can check available grooming appointments."
        )

    def needs_human(self, text):
        """Identify requests that require a staff member."""
        for word in HANDOFF_WORDS:
            if word in text:
                return True
        return False

    def times_reply(self, user_message):
        """Use the grooming schedule tool to check appointment times."""
        day = self.grooming_schedule.find_day(user_message)

        if day is None:
            return "Which day? I can check Monday, Wednesday, or Friday."

        times = self.grooming_schedule.times_for(day)
        return f"Available grooming times on {day}: {times}."

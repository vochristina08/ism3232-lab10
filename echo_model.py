# echo_model.py
# Author: Christina Vo


class EchoModel:
    """A model that repeats the user's last message."""

    def reply(self, instructions, history):
        """Return the last message with a prefix."""
        return "You said: " + history[-1]["content"]

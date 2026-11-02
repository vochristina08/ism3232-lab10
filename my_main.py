# my_main.py
# Author: Christina Vo

from my_assistant import GroomingAssistant
from my_tool import GroomingSchedule

AVAILABLE_TIMES = {
    "monday": "9:00 am and 1:30 pm",
    "wednesday": "10:00 am and 3:00 pm",
    "friday": "11:00 am",
}

grooming_schedule = GroomingSchedule(AVAILABLE_TIMES)

assistant = GroomingAssistant(
    "Bella",
    "You help customers find available pet grooming appointments.",
    grooming_schedule,
)

print("Type a message, or type quit to stop.")
user_message = input("You: ")

while user_message != "quit":
    print(f"{assistant.name}: {assistant.respond(user_message)}")
    user_message = input("You: ")

print(f"Messages in this conversation: {len(assistant.history)}")

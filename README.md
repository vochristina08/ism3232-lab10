# Lab 10: OOP for Agents

## Mini-Project: Pet Grooming Appointment Assistant

My mini-project is a pet grooming appointment assistant named Bella that helps customers check available grooming appointments. Bella uses a separate scheduling tool to look up appointment times for Monday, Wednesday and Friday. The appointment schedule is mock data, so Bella does not connect to a real business calendar or make actual reservations. Requests to book, cancel or reschedule appointments are referred to grooming staff because these changes require a person to confirm availability and update the schedule. If Bella cannot answer a question or find a requested day, she provides a helpful response instead of making up information. If this assistant used real customer data, a potential risk would be exposing private information such as customer names, phone numbers or appointment details.

## Lab 11: Working with AI Models

In this lab, I learned how to connect an AI model to a chatbot while keeping the business rules separate. I used a mock model to test my pet grooming assistant without relying on Ollama every time. One challenge I faced was figuring out why my assistant was returning None instead of a response, but debugging helped me understand how the model and conversation history work together. I also learned why it is important to have safe fallback responses when the model cannot answer a question. Overall, this lab helped me better understand how AI models can be used in a business assistant while still maintaining control over its responses.

from brain.memory import recall, remember
from brain.mistral_ai import ask_mistral

def get_reply(question):
    question = question.strip()

    # 1️⃣ Check memory
    memory_answer = recall(question)
    if memory_answer:
        return memory_answer

    # 2️⃣ Ask Mistral
    answer = ask_mistral(question)

    # 3️⃣ Save to memory
    if answer:
        remember(question, answer)

    return answer

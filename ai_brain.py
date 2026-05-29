from openai import OpenAI

client = OpenAI(api_key="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")

def ask_ai(user_input):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are SPARK, a smart, friendly personal AI assistant."},
                {"role": "user", "content": user_input}
            ]
        )
        return response.choices[0].message.content.strip()

    except Exception:
        return "I am having trouble connecting to my intelligence service right now."

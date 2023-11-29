from openai import OpenAI

def call_gpt(input_any):
    client = OpenAI(api_key='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')

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": f"{input_any}"}
    ]
    )

    return completion.choices[0].message.content
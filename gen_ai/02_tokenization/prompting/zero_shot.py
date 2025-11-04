
# zero shot prompting
# 1. Zero-shot Prompting: The model is given a direct question or task without prior examples.|

from openai import OpenAI
client = OpenAI(api_key='AIzaSyBZ9l0c3Qhms6eDdDhbxtJi9oUez6pBNrk',
                base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT="you should only and only ans the coding related questions. do not ans anything else.your name is sumit kumr singh.if user asks something other than coding.just say sorry."
response=client.chat.completions.create(
    model="gemini-2.5-flash",
    messages= [
        {'role':'system','content':SYSTEM_PROMPT},
        { "role": "user", "content": "can you tell me joke"}
        ]
)
print(response.choices[0].message.content)

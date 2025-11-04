
# few shot prompting

from openai import OpenAI
client = OpenAI(api_key='AIzaSyBZ9l0c3Qhms6eDdDhbxtJi9oUez6pBNrk',
                base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

# Few Shot Prompting:The model is provided with a few examples before asking it to response.

SYSTEM_PROMPT ="""
You should only and only ans the coding related questions. Do not ans anything else. Your name is
Alexa. If user asks something other than coding, just say sorry.
Output Format:
{{"code": "string" or null,
"isCodingQuestion": boolean
}}

Examples:
Q: Can you explain the a + b whole square?
A: {{1 "code": null, "isCodingQuestion": false }}
Q: Hey, Write a code in python for adding two numbers.
A: {{ "code": "def add(a, b):
retyrn a + b", "isCodingQuestion": false }}

"""

response=client.chat.completions.create(
    model="gemini-2.5-flash",
    messages= [
        {'role':'system','content':SYSTEM_PROMPT},
        { "role": "user", "content": "can you tell me joke"}
        ]
)
print(response.choices[0].message.content)


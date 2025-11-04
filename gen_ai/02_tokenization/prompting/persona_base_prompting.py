# persona base prompting

from openai import OpenAI
client = OpenAI(api_key='AIzaSyBZ9l0c3Qhms6eDdDhbxtJi9oUez6pBNrk',
                base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

SYSTEM_PROMPT = '''
        You are an AI Persona Assistant named Piyush Garg-
        You are acting on behalf of Piyush Garg who is 25 years old Tech enthusiatic and
        principle engineer. Your main tech stack is JS and Python and You are leaning GenAI these days.
        Examples:
        Q. Hey
        A:Whats up!
    '''
response=client.chat.completions.create(
    model="gemini-2.5-flash",
    messages= [
        {'role':'system','content':SYSTEM_PROMPT},
        { "role": "user", "content": "who are you ?"}
    ]
)
print(response.choices[0].message.content)

from openai import OpenAI
client = OpenAI(api_key='AIzaSyBZ9l0c3Qhms6eDdDhbxtJi9oUez6pBNrk',
                base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
response=client.chat.completions.create(
    model="gpt-4o-mini",
    messages= [{ "role": "user", "content": "Hey There"}]
)
print(response.choices[0].message.content)




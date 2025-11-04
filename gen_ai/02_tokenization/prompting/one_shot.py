from openai import OpenAI
client = OpenAI(api_key='AIzaSyBZ9l0c3Qhms6eDdDhbxtJi9oUez6pBNrk',
                base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
response=client.chat.completions.create(
    model="gemini-2.5-flash",
    messages= [
        {'role':'system','content':'you are an expert in  Maths and only and only ans maths and only and only ans maths realted questions !!!. That if the query is not related to maths. Just say sorry and do not ans that.'},
        { "role": "user", "content": "who are you ?"}
        ]
)
print(response.choices[0].message.content)

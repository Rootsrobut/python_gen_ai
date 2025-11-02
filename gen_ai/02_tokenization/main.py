# from dotenv import load_dotenv
# from openai import OpenAI
# client = OpenAI()
# load_dotenv()
# response=client.chat.completions.create(
#     model="gpt-4o-mini",
#     messages= [{ "role": "user", "content": "Hey There"}]
# )
# print(response.choices[0].message.content)



from google import genai

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client(api_key='AIzaSyBZ9l0c3Qhms6eDdDhbxtJi9oUez6pBNrk')

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="Explain how AI works in a few words"
)
print(response.text)
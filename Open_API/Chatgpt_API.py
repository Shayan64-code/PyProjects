####Old Version
# from openai import OpenAI as ai

# ai.api_key =  

# messages = [
#     {"role": "system", "content": "You are a kind helpful assistant"}
# ]

# while True:
#     message = input("User : ")
#     if message:
#         messages.append(
#             {"role": "user", "content": message},
#         )
#         chat = ai.ChatCompletion.create(
#             model = "gpt-4.1-mini", messages=messages
#         )
    
#     reply = chat.choices[0].message.content
#     print(f"ChatGPT: {reply}")
#     messages.append({"role": "assistant", "content": reply})


from openai import OpenAI
import Keys

# client = OpenAI(api_key= Keys.KEY1,
#         base_url= "https://openrouter.ai/api/v1")  # uses OPENAI_API_KEY from environment variable

# messages = [
#     {"role": "system", "content": "You are a kind helpful assistant"}
# ]

# while True:
#     message = input("User: ")

#     if message.lower() == "exit":
#         break

#     messages.append({"role": "user", "content": message})

#     response = client.chat.completions.create(
#         model="nvidia/nemotron-3-nano-30b-a3b:free",
#         messages=messages
#     )

#     reply = response.choices[0].message.content

#     print(f"OpenRouter: {reply}")

#     messages.append({"role": "assistant", "content": reply})


#####There is second method in youtube using raw endpoints.

import requests

URL= "https://openrouter.ai/api/v1/chat/completions"

payload = {
    "model" : "nvidia/nemotron-3-nano-30b-a3b:free",
    "messages" : [{"role": "user", "content": "Who is the most succesfull chess player"}],
    "temperature" : 1.0,
    "top_p": 1.0,
    "n": 1,
    "stream": False,
    "presence_penalty": 0,
    "frequency_penalty": 0 
}

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {Keys.KEY1}"
}

response = requests.post(URL, headers=headers, json=payload, stream=False)

data = response.json()
print(data["choices"][0]["message"]["content"])
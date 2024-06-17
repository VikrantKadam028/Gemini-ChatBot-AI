import os
import google.generativeai as genai

genai.configure(api_key="AIzaSyDscYUWmTHUSZ9j5PJEqeSBHCWTypcB3aQ")
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 200,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,

)

chat_session = model.start_chat(
  history=[
  ]
)

print("*********************")
print(" Welcome to Gemini!")
print("*********************")

while True:
  text = input("You :")
  if text.lower() in ["bye","quit","exit","close"]:
    print("Have a nice day! :)")
    break
  else:
    response = chat_session.send_message(text)

    print("ChatBot :",response.text)
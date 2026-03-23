import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
api_key = os.getenv("API")
def generate_output(text,choice):
    client = Groq(api_key=api_key)
    if choice == "1":
        response = client.chat.completions.create(

            model='llama-3.3-70b-versatile',

            messages=[{"role":"system","content":"You have to give a short summary on this text and it should in easy "
            "language it should be in english,lenght should be atleast 2 pages and it should end with  some quotes "},
            {"role":"user","content":f"give short and crisp summary on this text {text}"}]




    )



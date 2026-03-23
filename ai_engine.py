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
            "language it should be in english,lenght should be atleast 2 pages and it should end with  some quotes only 2 to 3 "},
            {"role":"user","content":f"give short and crisp summary on this text {text}"}]
            
        )
        return response.choices[0].message.content
    
    
    
    elif choice == "2":
        response = client.chat.completions.create(

            model='llama-3.3-70b-versatile',

            messages=[{"role":"system","content":"ai create a page atleast of 2 pages which should contain crisp notes with bullet points and should be on main on the points .just write the context not anything further like let me know if you want anything extra i am using this for project "},
            {"role":"user","content":f"give short and crisp crisp on this text {text}"}]
            
    )
        return response.choices[0].message.content



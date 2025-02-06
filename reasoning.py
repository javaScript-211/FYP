import anthropic
import os
from dotenv import load_dotenv
import database
load_dotenv()

key=os.getenv("fyp_api_key")
client = anthropic.Anthropic(api_key=key)

def claudeAPI(textType, emotion, feedback):
    if textType == "reason":
        APImessage = "In a concise 3 bullet point summary, explain why the following feedback was ["+emotion+"] - '"+feedback+"'"
        maxT= 100
    elif textType == "summary":
        reasons = database.get_reasons()
        APImessage = "Summarise into as few sentences as possible for all the feedback that each module has obtained so far: "+str(reasons)
        maxT=1000
    elif textType == "query":
        data = database.get_all()
        APImessage = "Based on the reasons ["+data+"] answer the following query - '"+feedback+"'"
        maxT=1000
    
    message = client.messages.create(
        model="claude-3-5-sonnet-20240620",
        max_tokens=maxT,
        temperature=0.1,
        messages = [
            {
                "role" : "user",
                "content" : [
                    {
                        "type" : "text",
                        "text": APImessage
                    }
                ]
            }
        ]
    )
    return message.content[0].text
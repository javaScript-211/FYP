import anthropic
import os
from dotenv import load_dotenv
import database
load_dotenv()

key=os.getenv("fyp_api_key")
client = anthropic.Anthropic(api_key=key)

def claudeAPI(textType, emotion, feedback):
    if textType == "reason":
        APImessage = """
            I want you to act as an expert text analyzer to analyze the following text to find
            key reasons to match the detected emotions using the criteria outlined below. The final
            reasons should be formatted in a certain way.
            feedback-"""+feedback+"""
            emotions-"""+emotion+""" 
            criteria
            1. identifying certain words and phrases that indicate the defined emotions.
            2. analyzing the overall structure of the feedback given.  
            3. consider words or phrases that were NOT within the text.
            4. look at how the elements are combined 
            
            format
            The result should only consist of the reasons, no additional text.
            The result should be formatted as bullet points
            The result cannot exceed 3 bullet points
            
        """
        maxT= 100
    elif textType == "summary":
        reasons = database.get_reasons()
        APImessage = """<>
            I want you to act as an expert text analyzer to summarize the following 
            reasons given using the following criteria & format.
            </>
            <reasons>"""+str(reasons)+"""</reasons>

            <criteria>
            1. Organize the data entries by module number
            2. Analyse the language used for each module, focusing on emotional 
            inidcators, language intensity and use of descriptive terms
            3. Extract the themes for each data entry, noting unique or standout observations
            4. Produce an overall sentiment for each module formatted as one of the following 
            (exteremely positive, positive, negative or extremely negative)
            5. Identify and recognise patterns of common issues, shared positive elements and 
            unique characteristics of modules
            </criteria>

            <format>
            1. Module Number
            2. Overall sentiment
            3. Key themes
            3a. Highlights
            3b. Issues
            </format>
        """
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
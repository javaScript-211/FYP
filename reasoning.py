import anthropic
import os
from dotenv import load_dotenv
import database
load_dotenv()

key=os.getenv("fyp_api_key")
client = anthropic.Anthropic(api_key="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")

def claudeAPI(textType, emotion, feedback):
    if textType == "reason":
        examples = """
        <example>
            {input:The structure and delivery of this semester's Programming Fundamentals module has significantly hindered student learning. 
            The lecture materials frequently contained outdated code examples that didn't align with current industry practices, and practical sessions were often 
            cancelled with less than an hour's notice. The disconnect between lecture content and assignment requirements has left many students struggling 
            to complete coursework, with several having to seek external resources to understand basic concepts. The lack of clear documentation for the assignment 
            specifications and inconsistent grading criteria have created unnecessary confusion. To ensure student success, we need comprehensive lecture notes, 
            reliable practical sessions, and clear assessment guidelines that align with the module's learning objectives. }{output: Desire, Curiousity,}
        <\example>
        """

        message = """
        <messaage>
            I want you to act as an expert text analyzer to analyze the following text to find
            key reasons to match the detected emotions using the criteria outlined below. The final
            reasons should be formatted in a certain way.
            feedback-"""+feedback+"""
            emotions-"""+emotion+"""
            if you think the feedback cannot be categorized as the emotion defined, then reply with "text could not be accurately examined"
        <\message>
        <criteria>
            1. identifying certain words and phrases that indicate the defined emotions.
            2. analyzing the overall structure of the feedback given.  
            3. consider words or phrases that were NOT within the text.
            4. look at how the elements are combined 
        <\criteria>
        <format>
            The result should only consist of the reasons, no additional text.
            The result should be formatted as bullet points
            The result cannot exceed 3 bullet points
        <\format>    
        """

        APImessage = examples +"\n"+message
        maxT= 150
    elif textType == "summary":
        reasons = database.get_reasons()
        APImessage = """
        <message>
            I want you to act as an expert text analyzer to summarize the following 
            reasons given using the following criteria & format.
        </message>
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
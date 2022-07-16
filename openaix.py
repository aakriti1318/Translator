from distutils.command.config import config
import os
import openai
import config 

openai.api_key = config.api_key

def getLanguageTranslation(prompt, language):
    response = openai.Completion.create(
        model="text-davinci-002",
        prompt="Translate this into {}\n{}".format(language, prompt),
        temperature=0.7,
        max_tokens=1190,
        top_p=1,
        frequency_penalty=0.59,
        presence_penalty=0
    )
    if 'choices' in response:
        if len(response['choices']) > 0:
            ans = response['choices'][0]['text']
        else:
            ans = "Enter Relevant Text"
    else:
        ans = "Enter Relevant Text"
    return ans

# prompt = "Good morning, how are you?"
# language = "French"

# answer = getLanguageTranslation(prompt, language)
# print(answer)
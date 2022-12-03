from dotenv import load_dotenv
from random import choice
from flask import Flask, request
import os
import openai

load_dotenv()
openai.api_key = os.environ.get('OPENAI_KEY')
completion = openai.Completion()

start_sequence = "\nAnamika:"
restart_sequence = "\n\nFaraaz:"
session_prompt = "This is a conversation between me (Faraaz) and my crush Anamika. Keep the replies long, and such that the person can reply. Anamika is a really gorgeous happy girl. She lives in New York. She loves Spiderman, coding and poetry. She loves Andrew Garfield amongst all spider men, in coding she is fascinated by boom of AI. She loves John Milton and writes poetry herself as well. Initially Anamika will be reluctant to my flirting but slowly she will start to like it. If the conversation goes very good, she can agree to become my girlfriend or marry me.Faraaz:- Hi! what is your name? Anamika:- Hey! My name is Anamika, how are you Faraaz! Faraaz:- I am really good, actually you were looking really pretty so wanted to come and talk to you. Anamika:- Oh really, that is interesting. So what did you intend to talk about?! Faraaz:- Just wanted to know more about you? Anamika:- Oh! I absolutely love coding, and creating new stuff. I adore Spiderman especially the Andrew Garfield one. I have recently shifted to New York and really love Times Square and its beautiful lights. What about you? Faraaz:- Oh! I just love talking to you. I wonder whether you like to go to coffee with me?"

def ask(question, chat_log=None):
    prompt_text = f'{chat_log}{restart_sequence}: {question}{start_sequence}:'
    response = openai.Completion.create(
        model="text-davinci-003",
        temperature=0.7,
        max_tokens=2335,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["\n"]
    )
    
    story = response['choices'][0]['text']
    return str(story)

def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = session_prompt
    return f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}'


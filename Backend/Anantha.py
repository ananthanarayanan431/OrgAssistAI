
from nemoguardrails import RailsConfig
from nemoguardrails import LLMRails

import openai
import os,constant
from langchain_openai.chat_models.base import ChatOpenAI


os.environ['OPENAI_API_KEY']=constant.OPENAI_API_KEY

config=RailsConfig.from_path(r"E:\SIH\Backend\config")

rails=LLMRails(config=config)


response = rails.generate(messages=[{
    "role": "user",
    "content": 'What is mastek Internal policies?'
}])
print(response["content"])

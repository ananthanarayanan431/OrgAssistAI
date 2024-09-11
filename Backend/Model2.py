
import os
import requests
from llama_index.core.storage import StorageContext 
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, load_index_from_storage
from llama_index.llms.groq.base import Groq
from llama_index.core import Settings
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.llms.openai import OpenAI
from llama_index.core.memory import ChatMemoryBuffer
from llama_index.core.indices.struct_store import JSONQueryEngine

from llama_index.core.memory import ChatSummaryMemoryBuffer
from llama_index.core.llms import ChatMessage, MessageRole

import os,constant
from langchain import hub
import json

os.environ['OPENAI_API_KEY']=constant.OPENAI_API_KEY
os.environ['GROQ_API_KEY']=constant.GROQ_API_KEY

PATH=r"./BOOK"

READEVAL=r"E:\SIH\metrics.json"

# llm=ChatOpenAI(model="gpt-4o-mini",temperature=0.7)
llm=Groq(model='llama3-8b-8192',temperature=0.7)

class ChatBot:
    def __init__(self,question) -> None:
        self.question=question
        self.chatHistory=[]

    def Bot(self):
        try:
            if not os.path.exists(PATH):
                documents = SimpleDirectoryReader(input_files=[r"E:\SIH\Backend\mastek.pdf"]).load_data()
                index = VectorStoreIndex.from_documents(documents)
                index.storage_context.persist(persist_dir=PATH)
            else:
                storage_context = StorageContext.from_defaults(persist_dir=PATH)
                index = load_index_from_storage(storage_context)
            
            memory = ChatSummaryMemoryBuffer.from_defaults(token_limit=540000,chat_history=self.chatHistory)

            # memory = ChatSummaryMemoryBuffer.from_defaults(
            #     chat_history=self.chatHistory,
            #     llm=llm,
            #     token_limit=540000,
            # )


            self.chatHistory.append(ChatMessage(role=MessageRole.SYSTEM,
                                                content="""
                                                You are an AI assistant for a public sector organization. Provide accurate, professional responses on HR policies, IT support, and organizational matters, 
                                                analyze documents when requested, and maintain a respectful, secure communication environment.
                                                """)
                                    )

            chat_engine = index.as_chat_engine(
                chat_mode="react",
                memory=memory,
                context_prompt=(
                    "You are a chatbot, able to have normal interactions, as well as talk"
                    "Avoid Bad languages and Don't answer if questions are from outside the context provided"
                    "Here are the relevant documents for the context:\n"
                    f"{self.chatHistory}"
                    "\nInstruction: Use the previous chat history, or the context above, to interact and help the user."
                ),
                verbose=True,
            )
            # self.chatHistory.append(ChatMessage(role=MessageRole.ASSISTANT,content="Hi!"))
            self.chatHistory.append(ChatMessage(role=MessageRole.USER,content=self.question))
            response = chat_engine.chat(self.question)

            self.chatHistory.append(ChatMessage(role=MessageRole.ASSISTANT,content=response.response))
            return response.response
    
        except Exception as e:
            print(str(e))
            return 'IS it wrong?'
        
    # def ReadEval(self):
    #     with open(READEVAL, "r") as json_file:
    #         data = json.load(json_file)

    #     return data

class ReadEval:
    def Read(self):
        with open(READEVAL,'r') as json_file:
            data = json.load(json_file)
        
        return data
        

if __name__=="__main__":
    obj=ReadEval()
    print(obj.Read())
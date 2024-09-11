
from langchain_core.messages import AIMessage, HumanMessage
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_openai.chat_models import ChatOpenAI
from langchain_openai.embeddings.base import OpenAIEmbeddings

from langchain_groq.chat_models import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains.retrieval import create_retrieval_chain
from langchain.chains.history_aware_retriever import create_history_aware_retriever

from langchain.chains.combine_documents import create_stuff_documents_chain

import os,constant
from langchain import hub

os.environ['OPENAI_API_KEY']=constant.OPENAI_API_KEY
os.environ['GROQ_API_KEY']=constant.GROQ_API_KEY

PATH="./BOOK"
llm=ChatOpenAI(model="gpt-4o-mini",temperature=0.7)
# llm=ChatGroq(model='llama3-8b-8192',temperature=0.7)

class ChatBot:
    def __init__(self,question) -> None:
        self.question=question
        self.value=""
        self.chatHistory=[]

    def default(self):
        self.value="""
        The chatbot should be capable of handling diverse questions related to HR policies, IT support, company events, and 
        other organizational matters"""

    def Bot(self):
        loader=PyPDFLoader(r"mastek.pdf")
        document=loader.load()

        text_splitter=RecursiveCharacterTextSplitter(
            chunk_size=2000,
            chunk_overlap=200,
        )
        document_chunks=text_splitter.split_documents(documents=document)
        vector_store=""
        if not os.path.exists(PATH):
            vector_store=Chroma.from_documents(
                documents=document_chunks,
                embedding=OpenAIEmbeddings(model="text-embedding-3-small"),
                persist_directory=PATH,
            )
        else:
            vector_store=Chroma(
                persist_directory=PATH,
                embedding_function=OpenAIEmbeddings(model="text-embedding-3-small"),
            )
        retriever=vector_store.as_retriever()
        self.chatHistory.append(AIMessage("Hi How I can Help you?"))
        self.chatHistory.append(HumanMessage(content=self.question))

        # prompt = hub.pull("rlm/rag-prompt")   
        prompt = ChatPromptTemplate.from_messages([
            MessagesPlaceholder(variable_name="chat_history"),
            ("user", "{input}"),
            ("user",
             "Given the above conversation, generate a search query to look up in order to get information relevant to the conversation")
        ])
        retriever_chain = create_history_aware_retriever(llm, retriever, prompt)

        prompt = ChatPromptTemplate.from_messages([
            ("system", "Answer the user's questions based on the below context:\n\n{context}"),
            MessagesPlaceholder(variable_name="chat_history"),
            ("user", "{input}"),
        ])
        stuff_documents_chain = create_stuff_documents_chain(llm, prompt)
        conversation_rag_chain = create_retrieval_chain(retriever_chain,stuff_documents_chain)
        response = conversation_rag_chain.invoke({
            # "context":retriever,
            'chat_history':self.chatHistory,
            "input": self.question,
        })
        self.chatHistory.append(AIMessage(content=response['answer']))
        return response['answer']
        



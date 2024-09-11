
import os 
import constant
import json

os.environ['OPENAI_API_KEY']=constant.OPENAI_API_KEY

from llama_index.core import SimpleDirectoryReader
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core import VectorStoreIndex
from llama_index.core.settings import Settings
from llama_index.core import load_index_from_storage
from llama_index.core.storage import StorageContext

from ragas.testset.generator import TestsetGenerator
from ragas.testset.evolutions import simple,reasoning,multi_context

from ragas.metrics import (
    faithfulness,
    answer_relevancy,
    context_precision,
    context_recall,
    answer_correctness,
)

from ragas.metrics import (
    context_utilization,
    context_entity_recall,
    answer_similarity,
)

from ragas.metrics.critique import harmfulness
from ragas.integrations.llama_index import evaluate

DATASET="./data.csv"
PATH="./STORE"

embeddings=OpenAIEmbedding()
Settings.embed_model=embeddings


class Evaluation:
    def __init__(self):
        self.generator_llm=OpenAI(model="gpt-4o-mini")
        self.critics_llm=OpenAI(model='gpt-4o-mini')
        self.evalutor_llm=OpenAI(model='gpt-4o-mini')
        self.embeddings=OpenAIEmbedding()
        self.testset=""
        self.document=""
    
    def Building(self):
        document=SimpleDirectoryReader(input_files=[r"E:\SIH\Backend\mastek.pdf"]).load_data()
        self.document=document

        generator=TestsetGenerator.from_llama_index(
            generator_llm=self.generator_llm,
            critic_llm=self.critics_llm,
            embeddings=self.embeddings,
        )

        testset=generator.generate_with_llamaindex_docs(
            documents=document,
            test_size=14,
            distributions={simple:0.5, reasoning:0.25, multi_context:0.25},
        )
        # self.testset=testset
        return testset

    def File(self):

        if self.testset is None or len(self.testset)==0:
            self.testset=self.Building()

        if not os.path.exists(DATASET):
            df=self.testset.to_pandas()
            ds=self.testset.to_dataset()
            ds_dict=ds.to_dict()
            df.to_csv(DATASET)
            print("Successfully Created!")
        else:
            ds=self.testset.to_dataset()
            ds_dict=ds.to_dict()
        return ds_dict
    
    def Query(self):
        if not os.path.exists(PATH):
            vector_index=VectorStoreIndex.from_documents(documents=self.document)
            vector_index.storage_context.persist(persist_dir=PATH)
        else:
            storage_context=StorageContext.from_defaults(persist_dir=PATH)
            vector_index=load_index_from_storage(storage_context=storage_context)
            
        query_engine = vector_index.as_query_engine()
        metrics=[
            faithfulness,
            answer_relevancy,
            context_precision,
            context_recall,
            harmfulness,
            answer_correctness,
        ]
        result=evaluate(
            query_engine=query_engine,
            metrics=metrics,
            dataset=self.File(),
            llm=self.evalutor_llm,
            embeddings=self.embeddings,
            raise_exceptions=False,
        )
        ans=result.to_pandas()
        ans.to_csv('./val1.csv')

        with open("metrics.json", "w") as json_file:
            json.dump(result, json_file, indent=4)

        print(type(result))
        return result

if __name__=="__main__":
    obj=Evaluation()
    print(obj.Query())

    




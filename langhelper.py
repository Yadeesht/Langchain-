from API import gemapi
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain
from langchain_google_genai import ChatGoogleGenerativeAI
import os

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=gemapi,temperature = .6)

def generate_restaurant_recommendations(cusine):
    # Dummy function to simulate restaurant recommendations
    prompt_temp_name = PromptTemplate(
        input_variables=["cusine"],
        template="i want to open arestaurant for {cusine} food. suggest one fancy name for this only one name",
    )
    name = LLMChain(llm=llm, prompt=prompt_temp_name,output_key = "name")
    prompt_temp_items = PromptTemplate(
        input_variables=["name"],
        template="suggest any 5 menu items for {name}. return it as a comma seperated list",
    )
    food_items = LLMChain(llm=llm, prompt=prompt_temp_items,output_key="item")

   

    chain = SequentialChain(
        chains=[name, food_items],
        input_variables=["cusine"],
        output_variables=["name", "item"],
    )
    res = chain.invoke({"cusine": cusine})
    return res
    
if __name__ == "__main__":
    res = generate_restaurant_recommendations("chinese")
    print(res)
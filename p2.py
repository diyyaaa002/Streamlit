import os
from dotenv import load_dotenv
import streamlit as st
from openai import OpenAI
load_dotenv()
#load_dotenv(Override=True)#automatically fetches the last API
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
client=OpenAI()
#streamlit run p2.py <-This is how you run streamlit file
#CICD:Continous Integration Continuous Delivery
#Wide screen size pramane lese
#Centered etle center ma rehse
st.set_page_config(page_title="Time Complexity Calculator Tool",layout="wide")
st.title("💡 Smart Big-O Analyzer")
code=st.text_input("Enter your code to find Time Complexity: ")
prompt=f"""
Find out the Time Complexity of give code {code},
Mention Best Case, Worst Case and Average Case Time complexity with calculation 
and each step consideration for all three cases. Give the explanation in detail
and structured manner
Code:
Time Complexity:
Best Case:
Explanation of best case step by step:
Average Case:
Explanation of Average case step by step:
Worst Case:
Explanation of Worst case step by step:
"""

response=client.responses.create(model="gpt-4.1-mini",input=prompt)
st.write(response.output_text)
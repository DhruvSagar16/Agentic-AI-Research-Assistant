from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
# Define a simple python class which will specify the type of content that we want our LLM to generate. 
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_agent
from tools import search_tool, wiki_tool, save_tool

load_dotenv()

# specify all the fields that you want as an output from your LLM call
class ResearchResponse(BaseModel):
    topic: str  
    summary: str
    sources: list[str]
    tools_used: list[str]

# Set up an LLM (USing chatgpt or claude or groq)
llm = ChatGroq(model="qwen/qwen3-32b")

# This below "parser" will take the output from the LLM and parse 
# it into the model(ie. ResearchResponse(BaseModel)) and we can use it as a normal python object inside our code
parser = PydanticOutputParser(pydantic_object=ResearchResponse)

# verbose=True will give the thaught process of the agent and if you dont want it just use False 
# this is the og code but does not run #agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
query = input("What can I help you with today? (add 'save to file' if you want to save the results) ")

# Detect if user wants to save
save_requested = "save to file" in query.lower()

# Prompt template
system_prompt = """
You are a research assistant that will help generate a research paper.
Answer the user query and use necessary tools to research the topic.
{save_instruction}
Use save_tool only ONCE at the very end after research is complete.
Wrap the output in this format and provide no other text

{format_instructions}
""".format(
    save_instruction="You MUST use save_tool to save the final output to a file." if save_requested else "Do not use save_tool unless explicitly asked.",
    format_instructions=parser.get_format_instructions()
)

tools = [search_tool, wiki_tool, save_tool]

# Creating & Running The Agent
agent = create_agent(
    model=llm,
    system_prompt=system_prompt,
    tools=tools
)

# Execution of the agent
raw_response = agent.invoke(
    {
        "messages": [
            {"role": "user", "content": query}
        ]
    }
)

# extract output
output = raw_response["messages"][-1].content
print("Raw output:", output)

try:
    structured_response = parser.parse(output)
    print(structured_response)
except Exception as e:
    print("Error parsing response:", e)
    print("Raw Response:", output)



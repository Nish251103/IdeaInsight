# A dashboad that take an idea from the user and shows the following on the dashboard:
# feedback on the idea
# Validation on the idea
# Market analysis
# Potential Challenges
# Competition analysis
# Uniqueness meter
# Feasiable or not
# Cost analysis in form of pie chart
# CheckList
# Sum up


# Functionalities
# feedback on the idea:function done(feedback_sumarization())
# Validation, description: done(validation())
# Potential Challenges:
# Analysis:
# Data:
# scalibility:
# Competition analysis and data:
# Uniqueness: 
# Feasiable or not:
# Cost analysis, total investment needed, investment break down:
# CheckList,Starting Point< Generalized Steps, stages: 
# Resouces you might need, Mentors, Experts(I can refer):
# Market analysis and market data:
# Sum up:
# Peer FeedBack(on requests):
###################################
#FrontEnd
#BackEnd
###################################
# Start with GenAI Integration
import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown


def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))
# Or use `os.getenv('GOOGLE_API_KEY')` to fetch an environment variable.
# GOOGLE_API_KEY=userdata.get('GOOGLE_API_KEY')
# genai.configure(api_key=GOOGLE_API_KEY)
genai.configure(api_key='')

# for m in genai.list_models():
#   if 'generateContent' in m.supported_generation_methods:
#     print(m.name)
model = genai.GenerativeModel('gemini-pro')

# response = model.generate_content("What is the meaning of life?")
# to_markdown(response.text)
# print(response.text)


# feedback on the idea:function done(feedback_sumarization())
def feedback_sumarization(idea):

    response = model.generate_content('''I want you to generate me professional feedback on a buisness idea: '''+idea)
    to_markdown(response.text)
    return response.text

# Validation, description: done(validation())
def validation(idea,_market_data,description,totalinvestment):
    response = model.generate_content("Validate the Idea: "+idea)
    to_markdown(response.text)
    return response.text

# Potential Challenges:
def potential_challenges(idea):
    response = model.generate_content('''What challenges would someone face while working on the idea: '''+idea)
    to_markdown(response.text)
    return response.text

# basic Analysis:
def basic_analysis(idea):
    response = model.generate_content('''What challenges would someone face while working on the idea: '''+idea)
    to_markdown(response.text)
    return response.text
print(validation('''a platform that helps users validate their ideas in a structured way by providing feedback, market analysis, potential
challenges and checklist to get started.''',"","",""))

# Data:
# scalibility:
# Competition analysis and data:
# Uniqueness: 
# Feasiable or not:
# Cost analysis, total investment needed, investment break down:
# CheckList,Starting Point< Generalized Steps, stages: 
# Resouces you might need, Mentors, Experts(I can refer):
# Market analysis and market data:
# Sum up:
# Peer FeedBack(on requests):
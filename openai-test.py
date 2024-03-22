from dotenv import load_dotenv
import os
import openai

def collect_user_input():
    """
    Collects detailed input from the user about their educational and career aspirations.
    """
    print("Welcome to the Educational Pathway Assistant!")
    career_goal = input("What career do you aspire to? ")
    grades = input("What are your average grades? ")
    study_interest = input("What subjects are you interested in studying? ")
    extracurricular_interests = input("What are your extracurricular interests or activities? ")
    
    return career_goal, grades, study_interest, extracurricular_interests

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv('OPENAI_API_KEY')

# Initialize OpenAI client
openai.api_key = api_key

# Collect user input
career_goal, grades, study_interest, extracurricular_interests = collect_user_input()

# Construct user content with all collected information
user_content = f"I'm in high school with average grades of {grades}, and I want to become a {career_goal}. I'm interested in studying {study_interest} and my extracurricular interests include {extracurricular_interests}. What should I do?"

# Prepare the chat messages
messages = [
    {"role": "system", "content": "You are an educational assistant knowledgeable about career paths in various fields. Provide comprehensive, step-by-step guidance to users inquiring about specific careers."},
    {"role": "user", "content": user_content}
]

#response from OpenAI API
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages
)

# Print the assistant's advice
print(response.choices[0].message)

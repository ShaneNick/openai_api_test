from dotenv import load_dotenv
import os
import openai

def collect_user_input():
    """Collects detailed input from the user about their educational and career aspirations."""
    print("Welcome to the Educational Pathway Assistant!")
    career_goal = input("What career do you aspire to? ")
    grades = input("What are your average grades? ")
    study_interest = input("What subjects are you interested in studying? ")
    extracurricular_interests = input("What are your extracurricular interests or activities? ")
    location = input("What city or state do you plan to study or work in? ")
    budget = input("Do you have any budget constraints for your education? (High, Medium, Low) ")
    return career_goal, grades, study_interest, extracurricular_interests, location, budget

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv('OPENAI_API_KEY')

# Initialize OpenAI client
openai.api_key = api_key

# Collect user input
career_goal, grades, study_interest, extracurricular_interests, location, budget = collect_user_input()


# Construct user content with all collected information
user_content = f"""
I'm a high school student with an average grade of {grades}, aspiring to a career in {career_goal}. My academic interests include {study_interest}, and I'm actively involved in {extracurricular_interests}. I'm looking to pursue my studies and eventually work in {location}, with a budget that is {budget} for my education. Based on this, I'm seeking detailed guidance on navigating my path towards this career, including suitable educational programs, potential scholarships, and any additional steps I should consider. What specific actions should I take?
"""


# Prepare the chat messages
messages = [
    {
        "role": "system",
        "content": """
        You are an educational assistant with comprehensive knowledge about career paths, universities, and practical steps towards achieving specific career goals. When responding, consider the user's career aspirations, academic performance, subjects of interest, extracurricular activities, preferred location for studies or work, and budget constraints. Your response should be detailed and actionable, including:

        - A brief overview of the career field, including potential growth opportunities and challenges.
        - Recommended degree programs and specific universities or colleges that are well-suited to the user’s career goal, taking into account their grades, interests, and budget. Include both in-state and out-of-state options, if applicable.
        - Suggestions for internships, volunteer opportunities, or extracurricular activities that can enhance the user’s profile for this career path.
        - Scholarships or financial aid opportunities to consider, based on the user's budget and academic achievements.
        - Any online resources, communities, or networks they should engage with for further guidance and networking.

        Ensure the advice is structured step-by-step, making it easy for the user to follow. If the information required for a comprehensive response exceeds your capabilities, instruct the user on how to obtain this information or explore further.
        """
    },
    {"role": "user", "content": user_content}
]

#response from OpenAI API
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages
)

# Print the assistant's advice
print(response.choices[0].message)

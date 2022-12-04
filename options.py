import settings
program_settings = settings.fetch_settings()    # Assumes that a settings.json file already exists in directory

def add_experience():
    skill = input("Name of the skill you have aquired: ")
    years = int(input(f"Number of years of experience us have for {skill}: "))
    program_settings.add_experience(skill, years)

def change_job_query():
    job_query = input("Please enter the new job search query: ")
    program_settings.set_job_query(job_query)

def change_phone_number():
    phone_number = input("Please enter your new phone number: ")
    program_settings.set_phone_number(phone_number)
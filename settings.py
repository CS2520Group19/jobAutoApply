import json

# Settings class that simply holds the values of various information needed for job applications
class Settings:
    '''
    Settings class that simply holds the values of various information needed for job applications.
    Variables can be individually set using setter methods or added using specialised add methods.
    Variables can be accessed as subvariables of an instance of this class.
    '''

    # experience: (dict) Contains the skills and the number of years of experience the user has had under those skills.
    # job_query: (str) The string that will be appended to the url link for filterJobs()
    # phone_number: (str) String of the user's phone number
    def __init__(self, experience = {}, job_query = "software engineer", phone_number = "111-111-1111"):
        self.experience = experience
        self.job_query = job_query.replace(' ', "%20").lower()
        self.phone_number = phone_number

        # Save settings
        save_settings(self)

    # Updates the value for expereinces and settings.json
    # experience: (dict) Contains the skills and the number of years of experience the user has had under those skills.
    def set_experience(self, experience):
        self.experience = experience

        # Save settings
        save_settings(self)

    # Updates the value for job_query and settings.json
    # job_query: (str) The string that will be appended to the url link for filterJobs()
    def set_job_query(self, job_query):
        self.job_query = job_query.replace(' ', "%20").lower()

        # Save settings
        save_settings(self)

    # Updates the value for phone_number and settings.json
    # phone_number: (str) String of the user's phone number
    def set_phone_number(self, phone_number):
        self.phone_number = phone_number

        # Save settings
        save_settings(self)

    # Updates the value for the experience and settings.json
    # skill: (str) A skill that the user has aquired
    # years: (int) Years of experence under the provided skill
    def add_experience(self, skill, years):
        self.experience.update({skill.lower(): years})

        # Save settings
        save_settings(self)

# Saves a Settings object in the form of a settings.json file on project directory
# settings_object: (Settings) An instance of the Settings class
def save_settings(settings_object):
    settings_file = open("settings.json", 'w')
    settings_file.write(json.dumps(settings_object.__dict__)) # Converts settings to a dictonary and proceeds to make it compatible for .json
    settings_file.close()

# Gets the settings from settings.json file on project directory and return it as an instance of Settings
# returns: (Settings) Containing the values from settings.json as its variables
def fetch_settings():
    settings_file = open("settings.json", 'r')
    settings = json.load(settings_file)
    settings_file.close()
    return Settings(experience = settings["experience"], 
                    job_query = settings["job_query"], 
                    phone_number = settings["phone_number"])


# '''-----# Usage Examples #-----'''
# # Initialize settings (Only 1 run needed)
# Settings(experience = dict(zip(["java", "c++", "linux", "sql", "python"], [2, 3, 5, 6, 7])), job_query = "software engineer", phone_number = "111-111-1111")

# # Read in the settings
# settings = fetch_settings()

# # Set variables
# settings.set_phone_number("323-555-888")
# settings.add_experience("unix", 4)

# # Get variables
# print(settings.experience, settings.job_query, settings.phone_number)
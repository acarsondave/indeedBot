# bot settings you can change -- options listed to the right
job_posting_age = '1'  # all, 1, 3, 7, 14 (these are days)
job_posting_type = 'all'  # all, full-time, contract, part-time, internship, temporary
job_posting_experience = 'all'  # all, entry, mid, senior
job_posting_distance = '25'  # default 5, 10, 15, 25, 50, 100 (these are miles)

# change these to your information
account_email = ''  # your indeed email
account_password = ''  # your indeed password
job_titles = ['python developer',]  # separate job titles must be in quotations separated by a comma
job_location = '30340'  # job zip

# apply personal answers
apply_linkedin = 'www.linkedin.com'
apply_personalwebsite = 'www.me.com'
apply_stateresident = 'yes'  # yes, no -- are you a state resident
apply_sponsorship = 'no'  # yes, no -- will you need work sponsorship
apply_relocate = 'yes'  # yes, no -- resident of ga or willing to relocate
apply_workauthorized = 'yes'  # yes, no -- authorized to work in us
apply_citizen = 'yes'  # yes, no -- us citizen
apply_education = 'other'  # other, highschool, associate, bachelor, master, doctorate -- education level
apply_leadershipdevelopment = '5'  # years
apply_salary = '55k'
apply_gender = 'male' # male, female, decline
apply_veteran = 'no' # yes, no, decline -- veteran status
apply_disability = 'no' # yes, no, decline -- disability status

# language experience years
apply_java = '1'
apply_aws = '0.5'
apply_python = '1'
apply_django = '1'
apply_php = '5'
apply_react = '0'
apply_node = '0'
apply_angular = '0'
apply_javascript = '5'
apply_orm = '0'
apply_sdet = '0'
apply_selenium = '0'
apply_testautomation = '0'
apply_webdevyears = '10'

# don't change these - you break it you buy it
base_url = 'https://indeed.com'
login_url = 'https://secure.indeed.com/account/login?hl=en_US&co=US&continue=https%3A%2F%2Fwww.indeed.com%2F&tmpl=desktop&service=my&from=gnav-util-homepage'
page_timeout = 30
long_timeout = 300
job_urls = []

date_posted = {
    'all': '',
    '1': '&fromage=1',
    '3': '&fromage=3',
    '7': '&fromage=7',
    '14': '&fromage=14'
}

job_type = {
    'all': '',
    'full-time': '&jt=fulltime',
    'contract': '&jt=contract',
    'part-time': '&jt=parttime',
    'internship': '&jt=internship',
    'temporary': '&jt=temporary'
}

experience_level = {
    'all': '',
    'entry': '&explvl=entry_level',
    'mid': '&explvl=mid_level',
    'senior': '&explvl=senior_level'
}

job_distance = {
    'default': '',
    '5': '&radius=5',
    '10': '&radius=10',
    '15': '&radius=15',
    '25': '&radius=25',
    '50': '&radius=50',
    '100': '&radius=100'
}

apply_veteranoptions = {
    'no' : 'i am not',
    'yes' : 'i identify as one',
    'decline' : "i don't wish"
}

apply_disabilityoptions = {
    'no' : 'no',
    'yes' : 'yes',
    'decline' : "i don't wish"
}
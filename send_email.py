import csv
from notipyer.email_notify import set_email_config
from email_template import send_emails

print("Enter details for email configs")
SENDER_EMAIL = input("Your email address: \n")
SENDER_PASS = input("Your google app password: ")
SENDER_NAME = input("Your name: ")
set_email_config(SENDER_EMAIL, SENDER_PASS, SENDER_NAME)

print("Enter details for email template: ")
applicant_name = input("Enter Your Name: ")
position = input("Enter Your Position you are applying for: ")
company = input("Enter company name: ")
subject = input("Subject For your email: ")
# skills = ["Django", "Python", "FastAPI", "Docker", "Javascript", "React.js"]
resume_link = input("Enter Resume Link: ")


def company_emails_template(first_name, last_name):
    """
        use this function as a template to make new functions for each company u want to apply to
        then call it in the generate contacts function
    """
    return f"{first_name}.{last_name}@company.com"


def generate_contacts(csv_file_path):
    emails = []
    full_names = []

    with open(csv_file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            full_name = row['Name']
            parts = full_name.split()
            first_name = parts[0].lower()
            last_name = parts[-1].lower() if len(parts) > 1 else ''

            # -------------- call the company email function ------------------- #
            email = company_emails_template(first_name, last_name)

            emails.append(email)
            full_names.append(full_name)

    return emails, full_names


def send_mails_to_all(company_name):
    csv_file_path = f'{company_name}_names.csv'
    (emails, full_names) = generate_contacts(csv_file_path)
    for i in range(len(emails)):
        try:
            send_emails(
                sender_name=full_names[i],
                to_recipients=[emails[i]],
                applicant_name=applicant_name,
                resume_link=resume_link,
                position=position,
                company=company,
                subject=subject
            )
        except Exception as e:
            print(f"EXCEPTION AT INDEX:{i}:{e}")

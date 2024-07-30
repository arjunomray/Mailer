from notipyer.email_notify import send_email
def send_emails(sender_name,to_recipients, resume_link, applicant_name, position, company,subject):
    html = f"""
    <!DOCTYPE html>
    <html>
        <head>
        </head>
        <body>
            <div class="container">
                <div class="content">
                <p>Hey {sender_name}!</p>
                <p>I hope you're doing well.</p>
                <p>I am writing to express my interest in joining {company} as {position}. 
                While contributing to opensource and working on my projects, I have gained valuable experience in Python, 
                Javascript, React, Django, FastAPI and Docker .</p>
                <p> I hope you would checkout my profile and consider me for a referral.</p>
                <br>
                <br>
                <p>You can find my resume <a href="{resume_link}">here</a>.
                <p>Thank you for your support.</p>
                <p>
                    Best regards,
                    <br>{applicant_name}
                </p>
                </div>
            </div>
        </body>
    </html>
    """
    # Can be None

    send_email(
        subject=subject,
        message=None,
        to_addr=to_recipients,
        html_text=html,
        is_async=not True
    )



import smtplib
import access_key
from string import Template

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

MY_ADDRESS = ''
PASSWORD = ''


def get_contacts(filename):

    """
    Return two lists names, emails containing names and email addresses
    read from a file specified by filename.
    """

    names = []
    emails = []
    with open(filename, 'r+', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])
    return names, emails


def read_msg(filename):

    """
    Returns a Template object comprising the contents of the
    file specified by filename.
    """

    with open(filename, 'r+', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

def get_keys(filename):

    """
    Returns a list with access key codes of the file specified by filename.
    """
    keys = []
    subjects = []
    with open(filename, 'r+', encoding='utf-8') as keys_file:
        for a_key in keys_file:
            subjects.append(a_key.split()[0])
            keys.append(a_key.split()[1])
    return subjects, keys


def main():
    names, emails = get_contacts('mycontacts.txt')  # read contacts
    message_body = read_msg('message.txt')
    subjects, keys = get_keys('subject_and_keys.txt')

    # set up the SMTP server
    s = smtplib.SMTP(host='smtp.office365.com', port=587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)

    # For each contact, send the email with code specific to participant
    for name, email in zip(names, emails):
       for subject, key in zip(subjects, keys):
           if subject == name:
               msg = MIMEMultipart()  # create a message

               message = message_body.substitute(ACCESS_CODE=key.title(), PERSON_NAME=name.title())

        # setup the parameters of the message
               msg['From'] = MY_ADDRESS
               msg['To'] = email
               msg['Subject'] = "Watch-a-movie questionnaire part 2"

        # add in the message body
               msg.attach(MIMEText(message, 'plain'))

        # send the message via the server set up earlier
               s.send_message(msg)
               print(message)
    del msg
    # Terminate the SMTP session and close the connection
    s.quit()


if __name__ == '__main__':
    main()
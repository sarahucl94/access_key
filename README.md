# Generate random access key for GDPR compliance

Produce an access key for each subject that fills in a questionnaire in 2 parts. Because Office Teams only allows questionnaires of a certain length, and Google Drive is not GDPR-compliant, this code puts the two together for studies that need to email large numbers of participants. 

If you have emails and names of subjects that you want to screen, this code will automatically send them an email from your official university (or other) address, with a unique access key, for them to fill in an anonymised Google questionnaire. This way, if you hold personal information on other GDPR-compliant platforms, you can trace back the subject to the Google questionnaire without the risks of prrivacy breaches.

Requirements:
```
pip install smtplib
pip install email
```


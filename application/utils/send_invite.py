import boto3
from botocore.exceptions import ClientError


class SendInvite:
    def __init__(self, sender_name, sender_email, recipient_email, invite_link):
        self.SENDER = sender_email
        self.sender_name = sender_name
        self.RECIPIENT = recipient_email
        self.AWS_REGION = "us-east-2"
        self.SUBJECT = 'Invitation for workspace'
        self.invite_link = invite_link

        # The email body for recipients with non-HTML email clients.
        self.BODY_TEXT = ("Invitation to contribute in a workspace\r\n"
                          "%s has invited you to contribute in a workspace.\r\n"
                          "Please click %s"% (self.sender_name, self.invite_link))

        # The HTML body of the email.
        self.BODY_HTML = """<html>
        <head></head>
        <body>
          <h1>Invitation to contribute in a workspace</h1>
          <p>%s has invited you to contribute in the workspace.
            Click on <a href=%s'>Accept Invitation</a>.</p>
        </body>
        </html>""" % (self.SENDER, self.invite_link)

        # The character encoding for the email.
        self.CHARSET = "UTF-8"

    def send_mail(self):
        # Create a new SES resource and specify a region.
        client = boto3.client('ses', region_name=self.AWS_REGION)

        # Try to send the email.
        try:
            # Provide the contents of the email.
            response = client.send_email(
                Destination={
                    'ToAddresses': [
                        self.RECIPIENT,
                    ],
                },
                Message={
                    'Body': {
                        'Html': {
                            'Charset': self.CHARSET,
                            'Data': self.BODY_HTML,
                        },
                        'Text': {
                            'Charset': self.CHARSET,
                            'Data': self.BODY_TEXT,
                        },
                    },
                    'Subject': {
                        'Charset': self.CHARSET,
                        'Data': self.SUBJECT,
                    },
                },
                Source=self.SENDER,
                # If you are not using a configuration set, comment or delete the
                # following line
                # ConfigurationSetName=CONFIGURATION_SET,
            )
        # Display an error if something goes wrong.
        except ClientError as e:
            print(e.response['Error']['Message'])
        else:
            print("Email sent! Message ID:"),
            print(response['MessageId'])
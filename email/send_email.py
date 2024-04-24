# Print a warning message with the specified color
def warn(string, clr):
    """
    Prints a colored warning message with the specified color.
    Use example: warn("Warning message", "Red")

    Parameters:
    string (str): The warning message to print.
    clr (str): "Red", "Green", "Blue", "Yellow", "Purple", "Cyan", "White", "Black", "Magenta", "Grey", "LightRed", "LightGreen", "LightBlue", "LightYellow"

    Returns:
    None
    """
  
    # Set text colors
    COLOR = {
        "Red": "\033[91m",
        "Green": "\033[92m",
        "Blue": "\033[94m",
        "Yellow": "\033[33m",
        "Purple": "\033[95m",
        "Cyan": "\033[96m",
        "White": "\033[97m",
        "Black": "\033[30m",
        "Magenta": "\033[35m",
        "Grey": "\033[90m",
        "LightRed": "\033[31m",
        "LightGreen": "\033[32m",
        "LightBlue": "\033[34m",
        "LightYellow": "\033[93m",
        "ENDC": "\033[0m"
    }
    # Print colored string
    print(COLOR[clr],string,COLOR["ENDC"])

# Send an email with the specified parameters
def send_email(recipient_email, bcc_email, subject, message, attachment_path=None):
    """
    Sends an email with the specified parameters.
    Must specify variables beforehand: 
    sender_email (str) = "your_email_address", 
    sender_password (str) = "your_email_password", 
    sender_smtp_server (str) = "your_smtp_server", 
    sender_smtp_port (int) = your_smtp_port

    Parameters:
    recipient_email (str): The email address of the recipient.
    bcc_email (str): The email address of the BCC (blank carboncopy) recipient. Can be omitted by passing an empty string (""), can pass multiple separated with semicolon ("email1@email.ex; email2@email.ex; ...").
    subject (str): The subject of the email.
    message (str): The message content of the email.
    OPTIONAL: attachment_path (str): The (relative) path of the file to attach to the email.

    Returns:
    None
    """

    # DEBUG
    #recipient_email = "korov22996@togito.com"   #https://temp-mail.org
    #bcc_email = ""
    #subject = "Test"
    #message = f"Test message\nThis is a test message sent to {recipient_email}."
    # END DEBUG

    # Specify your variables
    sender_email = "your_email_address", 
    sender_password = "your_email_password", 
    sender_smtp_server = "your_smtp_server", 
    sender_smtp_port = 586 #your_smtp_port

    # Create a multipart message object
    message_obj = MIMEMultipart()
    message_obj["From"] = sender_email
    message_obj["To"] = recipient_email
    message_obj["Bcc"] = bcc_email 
    message_obj["Subject"] = subject
    message_id_server = sender_email.split("@")[1]
    message_id = f"<{str(uuid.uuid4())}@{message_id_server}>"
    message_obj["Message-ID"] = Header(message_id)
    message_obj["Date"] = formatdate(localtime=True)

    # Add the message content
    message_obj.attach(MIMEText(message, "plain"))

    # Add the attachment if attachment_path is not None
    if attachment_path is not None:
        # Open the file in binary
        with open(attachment_path, "rb") as attachment_file:
            # Create a base64 attachment
            attachment_part = MIMEBase("application", "octet-stream")
            attachment_part.set_payload(attachment_file.read())
        # Add the attachment to the message object
        attachment_part.add_header(
            "Content-Disposition",
            f"attachment; filename= {attachment_path}",
        )
        message_obj.attach(attachment_part)
        # Encode the file in ASCII characters to send by email
        encoders.encode_base64(attachment_part)

    def connectAndSend(sender_email, sender_password, smtp_server, smtp_port, message_obj):
        # Connect to the SMTP server (max 10 sec timeout)
        server = smtplib.SMTP(smtp_server, smtp_port, timeout=10)
        server.starttls()
        server.login(sender_email, sender_password)
        # Send the email
        server.send_message(message_obj)
        # Clean up
        server.quit()

    try:
        connectAndSend(sender_email, sender_password, sender_smtp_server, sender_smtp_port, message_obj)
        warn(f"✔ Email successfully sent to {recipient_email} address!", "Green")
        return True
    except Exception as e:
        warn(f"✘ The emai couldn't be delivered to {recipient_email} address: {str(e)}", "Red")
        return False
        

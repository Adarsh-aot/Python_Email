# Email Automation with Attachments

This Python project provides an efficient and customizable solution for sending emails with embedded images, such as inline attachments and signature images, using the `smtplib` library. It uses environment variables to keep credentials secure and supports HTML email templates.

## Features

- **HTML Email Templates:** Customize your email content using HTML templates.
- **Inline Images:** Send emails with embedded images for enhanced visual appeal.
- **Secure Authentication:** Uses `.env` files to securely store sensitive email credentials.
- **SMTP Support:** Default support for Gmail's SMTP server, easily configurable for other providers.

## Prerequisites

Ensure you have the following installed:

- Python 3.6 or later
- Required Python libraries (install via `pip`)

## Installation

1. Clone the repository:
   ```bash
   https://github.com/Adarsh-aot/Python_Email.git
   cd Python_Email  
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory to securely store your credentials:
   ```
   Email_username=your_email@gmail.com
   Email_password=your_password
   Email_Recipient=recipient_email@example.com
   ```

## File Structure

```
.
├── Template/
│   ├── email_template.html    # HTML template for email body
│   ├── image.png              # First inline image
│   └── sign.png               # Signature image
├── main.py                    # Main script
├── .env                       # Environment variables (not included in the repo)
├── README.md                  # Project documentation
└── requirements.txt           # Python dependencies
```

## Usage

1. Prepare your email HTML template and images.
2. Customize the `.env` file with your email credentials and recipient email address.
3. Run the script:
   ```bash
   python main.py
   ```

## Example

The script sends an email with the following features:
- A visually styled email using the `email_template.html`.
- Inline image (`image.png`) referenced in the HTML.
- Inline signature image (`sign.png`) included at the bottom of the email.

## Configuration

- **SMTP Server:** The default SMTP server is `smtp.gmail.com` with port `587`. Update the `EmailSender` class if you use a different email provider.

## Dependencies

The project requires the following Python libraries:
- `smtplib` (built-in)
- `email` (built-in)
- `dotenv`

Install dependencies using:
```bash
pip install python-dotenv
```

## Security Note

Avoid hardcoding credentials. Use the `.env` file to keep sensitive information secure.

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute it as needed.

## Contributions

Contributions are welcome! Feel free to submit issues or pull requests to improve the project.

## Acknowledgements

This project uses:
- [Python's smtplib](https://docs.python.org/3/library/smtplib.html) for email automation.
- [dotenv](https://pypi.org/project/python-dotenv/) for environment variable management.


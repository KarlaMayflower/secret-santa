# Secret Santa Assignment Script

A Python script that automatically assigns Secret Santas and emails each participant their assigned person.

## Requirements

- Python 3.x
- python-dotenv (`pip install python-dotenv`)
- SMTP email account configured

## Setup

1. Install dependencies:
   ```bash
   pip install python-dotenv
   ```

2. Create a `.env` file with your email credentials:
   ```
   MAIL_FROM=secret.santa@example.com
   SMTP_SERVER=smtp.example.com
   SMTP_PORT=port
   ACCOUNT_EMAIL=your.email@example.com
   APP_PASSWORD=your-app-specific-password
   ```

## Input File Format

Create a `.txt` file with participants, one per line:
```
Name,email@example.com
```

Example (`santas.txt`):
```
Alice,alice@email.com
Bob,bob@email.com
Carol,carol@email.com
```

## Usage

1. Run the script:
   ```bash
   python santasLittleHelper.py
   ```

2. Enter the filename when prompted (e.g., `santas.txt`)

The script will:
- Randomly assign each person a different Secret Santa recipient
- Ensure no one is assigned to themselves
- Email each participant their assignment

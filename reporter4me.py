#!/usr/bin/env python3

import click
import requests
import smtplib
from email.mime.text import MIMEText
from time import sleep
from tqdm import tqdm
import getpass
import json


def load_configuration():
    with open('config.json') as config_file:
        config = json.load(config_file)
    return config


def prompt_for_user_info():
    user_name = click.prompt("Enter your name or nickname")
    user_role = click.prompt("Enter your role")
    return user_name, user_role


def generate_report(poc):
    # Generate report based on the PoC
    report = f"Vulnerability Details:\n\n{poc}\n\nRecommendations:\n\n- Implement security patch\n- Enforce strict input validation"

    return report


def send_email(report, email, email_password):
    # Configure email details
    sender_email = 'your_email@example.com'
    receiver_email = email
    subject = 'Bug Bounty Report'

    # Create a message with the report
    message = MIMEText(report)
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject

    # Send the email
    with smtplib.SMTP('smtp.example.com', 587) as server:
        server.starttls()
        server.login(sender_email, email_password)
        server.send_message(message)


def generate_report_with_ai(poc, api_key):
    # Make a request to ChatGPT API to generate report content
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }
    data = {
        'messages': [{'role': 'system', 'content': 'You are a cybersecurity expert.'},
                     {'role': 'user', 'content': poc}]
    }
    response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json=data)

    # Extract the generated report from the API response
    report = response.json()['choices'][0]['message']['content']

    return report


@click.command()
def main():
    config = load_configuration()
    user_name, user_role = prompt_for_user_info()
    email = config['email']
    api_key = config['api_key']

    poc = click.prompt("Enter the Proof of Concept (PoC)")

    with tqdm(total=10, desc="Generating Report") as progress_bar:
        for _ in range(10):
            sleep(1)  # Simulating a 10-second loading time
            progress_bar.update(1)
    click.echo("\nGood Luck DOG =D\n")

    # Generate report using AI
    report = generate_report_with_ai(poc, api_key)

    # Show the generated report to the user
    click.echo("Generated Report:\n")
    click.echo(report)
    click.echo()

    # Prompt for confirmation to send the report
    if click.confirm("Do you want to send this report via email?", default=True):
        # Prompt for email password securely
        email_password = click.prompt("Enter your email password", hide_input=True, show_default=False)
        # Send the report via email
        send_email(report, email, email_password)
        click.echo("Report sent successfully!")
    else:
        click.echo("Report not sent.")


if __name__ == '__main__':
    click.secho("\n" + "=" * 40, fg="green", bold=True)
    click.secho("{:^40}".format("Reporter4ME"), fg="cyan", bold=True)
    click.secho("=" * 40 + "\n", fg="green", bold=True)
    main()

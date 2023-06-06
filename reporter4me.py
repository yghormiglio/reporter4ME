#!/usr/bin/env python3

import click
import smtplib
from email.mime.text import MIMEText
from time import sleep
from tqdm import tqdm
import json
import openai

logo = """
                               __            __ __  __  _________
   ________  ____  ____  _____/ /____  _____/ // / /  |/  / ____/
  / ___/ _ \/ __ \/ __ \/ ___/ __/ _ \/ ___/ // /_/ /|_/ / __/   
 / /  /  __/ /_/ / /_/ / /  / /_/  __/ /  /__  __/ /  / / /___   
/_/   \___/ .___/\____/_/   \__/\___/_/     /_/ /_/  /_/_____/   
         /_/                                                                                                  
"""
print(logo)

def load_configuration():
    with open('config.json') as config_file:
        config = json.load(config_file)
    return config


def prompt_for_user_info():
    user_name = click.prompt("Enter your name or nickname")
    user_role = click.prompt("Enter your role")
    return user_name, user_role


def generate_report(poc):
    # Generate a concise and objective report based on the PoC
    report = f"Vulnerability Details: {poc}\n\nRecommendations: Implement security patch and enforce strict input validation"

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
    openai.api_key = api_key

    # Generate report using ChatGPT
    response = openai.Completion.create(
        engine='davinci',
        prompt=poc,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.7,
        temperature_decay_rate=0.9,
        temperature_floor=0.5,
        temperature_schedule=[0.5] * 20 + [0.2] * 20 + [0.1],
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    report = response.choices[0].text.strip()

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
    click.echo("\nGenerated Report:\n")
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

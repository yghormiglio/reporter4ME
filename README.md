# Reporter4ME

Reporter4ME is a bug bounty reporting tool that helps cybersecurity analysts generate and send reports for bug bounty programs. It integrates with the ChatGPT API to generate detailed vulnerability reports based on provided proof-of-concepts (PoCs). The generated reports can then be sent via email to the desired recipient.

## Features

- Integration with the ChatGPT API for AI-powered report generation.
- Simulated loading interface for a better user experience.
- Email functionality to send reports directly.

## Installation

To install and use Reporter4ME on Kali Linux, follow these steps:

1. Add the Reporter4ME package source by creating a new file named `reporter4me.list` in the `/etc/apt/sources.list.d/` directory:


2. Add the following line to the `reporter4me.list` file: https://github.com/yghormiglio/report4ME
3. Install Reporter4ME: sudo apt install reporter4me

## Usage

To run Reporter4ME, execute the following command: ./reporter4me run

Follow the prompts to enter your name, role, ChatGPT API key, recipient's email address, and the proof-of-concept (PoC) for the vulnerability. The tool will generate a report based on the PoC and display it on the screen. You will have the option to send the report via email.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

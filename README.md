# Delphos Bot for Zulip

Delphos is an intelligent assistant bot for Zulip, a powerful messaging platform. It is built as a backend using FastAPI
and provides various helpful features to enhance your Zulip experience.

## Blog Posts

[Integrating AI models into Zulip bots using FastAPI: Part 1 Migrating the Zulip’s bot server from Flask to FastAPI.](https://monadical.com/posts/zulip-ia-bot-1.html)

## Installation

To get started with Delphos, follow these steps:

### Clone the repository:

```bash
git clone https://github.com/your-username/delphos-zulip-bot.git
cd delphos-zulip-bot
```

### Install the dependencies:

```bash
pipenv install
```

### Activate the virtual environment:

```shell
pipenv shell
```

### Start the server by running the following command:

```shell
python3 server.py --config-file zuliprc-delphos --hostname="0.0.0.0" --port=8000
```

This will launch the Delphos bot backend server and make it accessible at http://localhost:8000.

### Expose the server to the internet using ngrok:

```shell
ngrok http 8000
```

This will expose the server to the internet and provide a public URL that can be used to access the server from
anywhere. Make sure to copy the URL provided by ngrok and use it in the bot config on Zulip.

## Usage

Delphos provides several commands to help you manage your Zulip topics. Here are some examples:

### Messages

Prints the last <amount> messages of the topic.

Example: @delphos messages 10  
PM Example: messages 10 learning css

### Links

Prints all the links in the topic.

Example: @delphos links  
PM Example: links learning css

### Help

Displays a list of available commands and provides examples for each one.

Example: @delphos help  
PM Example: help

Please note that the bot commands should be prefixed with `@delphos` to invoke the bot in the Zulip platform.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an
issue or submit a pull request.

## License

This project is licensed under the MIT License. 


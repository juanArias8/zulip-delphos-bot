ERROR_HELP = """
It seems that there was an error processing your request. 
Please check the format of your message and try again. 

If you're not sure how to use Delphos, 
you can use the @delphos help command to see a list of available commands and how to use them. 

Here's a general guide to using Delphos: 

In a stream, use the format @delphos <command> <arguments> 
In a private message, use the format <command> <arguments> 

If you continue to experience issues, please contact the bot administrator for further assistance.
"""

MESSAGES_HELP = """
## Messages
Prints the last <amount> messages of the topic. 

Example: @delphos messages 10
PM Example: messages 10 learning css
"""

LINKS_HELP = """
## Links 
Prints all the links in the topic. 

Example: @delphos links
PM Example: links learning css
"""

HELP_MESSAGE = f"""
Welcome to Delphos, a bot that helps you manage your topic!
Use the following commands to get started:

{MESSAGES_HELP}

{LINKS_HELP}

## Help 
Displays a list of available commands and provides examples for each one. 

Example: @delphos help
PM Example: help
"""

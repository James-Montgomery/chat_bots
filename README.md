# Chat Bots

Professionally I've had a lot of fun working on Deep Learning chat bots. Many companies are building out AI assistants to help customers interact with their suite of products. The fortune 100 company I currently work for has its own AI assistant, and I recently joined the data science team supporting that assistant!

However, early chatbots didn't (couldn't) rely on deep learning. They were works of art constructed from well thought out intent scripts and clever regular expressions / fuzzy matching. These are the chat bots that I have the most fun building. It's always interesting to sit down and try to design a "dumb" software engineering product that "feels" intelligent, dynamic, and reactive.

In this repo I've written out code to start getting working with an AI assistant on a couple different platforms. Using these starting blocks you should be able to build out a neat little "dumb" AI assistant using a well defined ontology of intents and regular expressions.

None of the code used is complicated and the code should be relatively self explanatory.

### Authors

James Montgomery - **Initial Work** - [jamesmontgomery.us](http://jamesmontgomery.us/)

### License

This project is licensed under the MIT License - see the [LICENSE.md](./LICENSE.md) file for details

## Getting Started

### Installing

You'll first need to install the dependancies for these projects. Create a Conda virtual environment named `bot_env` and install the code in the requirements file.

```
conda create --name bot_env python=3.6.3
conda activate bot_env
pip install -r requirements.txt
```

### API Keys

**Slack:** Go to the [slack api docs website](https://api.slack.com/apps). Create a new application and add a bot user to the application. Provide that bot access to any workspaces from which you would like to chat with the bot.

**Facebook:** Go to the [Facebook Developers](https://developers.facebook.com/apps/) website. Create a new application and add a messenger product. Go to `settings` under `Messenger` and give your product access to a facebook page.

### Running

The slack bot is simple to run. Simply open your Conda env and run `python3 bot.py`. You should be good to go. Modify the code as needed to get the bot working for your use case.

The facebook bot is a little more complicated. Run `./launch.sh` to start the bot. This bash script will provide instructions for linking a callback url for the bot to the product you created in the facebook developer portal. Once the callback is set up wait a few seconds and you should be good to go to interact with your bot.

## Testing

The code here is meant as a proof of concept / starting place. I haven't written test code, but production level code should always be robustly tested. If you intend to use this code for a production product please add unit, smoke / integration, and end to end tests.

## Acknowledgments

A big thanks to Jonathon Rider who got me interested in toying with slack bots. We've used them to set up some pretty entertaining pranks / gags and I've certainly learned a lot from him!

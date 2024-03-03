This is a script to allow the creation of a discord bot that will query the Gemini API

Keys need to be retrieved from their respective hosts
Current usage of Gemini's API is restricted to private use only. 

Keys go into the .env file (see example.env for what the format should look like)

Once the bot is online, questions can be asked by preceeding them with !ask
i.e. !ask what is the meaning of life?

Whereupon the bot will create a thread with the response.

Follow up questions can be added to the thread again with the !ask and the thead history
will be sent along with the new question, up to the most recent 30720 tokens as of February 2024

Note that this allows a much larger promt to be sent as discord messages are currently limited to 2000 characters (500 tokens), and doing it this way means multiple discord messages can be used to form a long query. 

A token is considered every 4 characters per this documentation:
https://ai.google.dev/models/gemini

Future things to implement:
-A way to query the number of tokens a query contains, but this seems silly now.
-semantic search
-rag


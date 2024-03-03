import datetime

#Discord message limit is 2000 characters, so this will split the message
#into 2000 character chunks and send multiple messages if needed
def split_message(msg, chunk_size=2000):
    """
    Splits a message into chunks of a given size.
    """
    return [msg[i:i+chunk_size] for i in range(0, len(msg), chunk_size)]

#records history of messages for future training of the model
def record_message(message):
    """
    Records a message to a text file for future training.
    """
    with open("gemini_chat_history.txt", "a") as f:
        f.write(message + "\n")


def trim_to_fit_limit(question, context, max_tokens, token_per_char):
    """
    Trims the context to fit within the token limit, based on the estimated token count,
    removes the excess tokens from the context from the start as we assume older messages are at the top,
    and returns the trimmed question and context.

    returns (question, trimmed_context)
    """
    # Estimate the token count for question and context
    question_tokens_approx = len(question) * token_per_char
    context_tokens_approx = len(context) * token_per_char

    total_tokens_approx = question_tokens_approx + context_tokens_approx

    # Calculate how many tokens we need to remove to fit the limit
    tokens_over_limit = total_tokens_approx - max_tokens

    if tokens_over_limit > 0:
        # Calculate how many characters to remove, considering the approximation
        chars_to_remove = int(tokens_over_limit / token_per_char)
        #Trim the context from the top to fit the limit
        trimmed_context = context[chars_to_remove:]
        return question, trimmed_context
    else:
        # If within limit, return the original question and context
        return question, context

async def fetch_thread_history(thread):
    """
    Fetches the history of a thread and concatenates the messages into a single text.
    """
    # Initialize an empty list to store messages
    messages = []
    
    # Asynchronously iterate over the message history
    async for message in thread.history(limit=100):  # Adjust limit as needed
        messages.append(message)
    
    # Concatenate messages into a single text, newest first
    # Note: 'reversed(messages)' to ensure the oldest messages are at the beginning
    history_text = " ".join([message.content for message in reversed(messages)])
    return history_text





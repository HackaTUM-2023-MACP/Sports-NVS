import openai

class ChatAssistant:
    def __init__(self, api_key):
        openai.api_key = api_key

    
    def generate_sql_query(self, conversation):
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", 
            messages=conversation
        )
        return completion

    def generate_reference_message(self, conversation):
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", 
            messages=conversation
        )
        return completion

    def generate_chat_response(self, conversation):     # also consider summary as an input here (maybe system input?)
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", 
            messages=conversation
        )
        return completion


    def combine_messages(self, user_content_list, assistant_content_list):
        conversation_sql_query = [{"role": "system", "content": "You are only allowed to reply with an SQL query. For filtering, only use fuzzy matching and never include the message in the query. The database table has the following columns: timestamp TIMESTAMP, machine VARCHAR(255), layer VARCHAR(255), message TEXT, message_vector vector(768). "}]
        conversation_reference_message = [{"role": "system", "content": "Please reply only with a possible message that we should look for in a system logfile to find the answers to the user's prompt."}]

        for i in range(max(len(user_content_list), len(assistant_content_list))):
            if i < len(user_content_list):
                conversation_sql_query.append({"role": "user", "content": user_content_list[i]})
                conversation_reference_message.append({"role": "user", "content": user_content_list[i]})
            if i < len(assistant_content_list):
                conversation_sql_query.append({"role": "assistant", "content": assistant_content_list[i]})
                conversation_reference_message.append({"role": "assistant", "content": assistant_content_list[i]})

        return conversation_sql_query, conversation_reference_message


# Example usage:
api_key = "PUT API KEY KERE"
chat_assistant = ChatAssistant(api_key)

# Combine messages to conversation context
user_messages = ["Are there any ssh errors in the last 24 hours?", "sorry, I meant the last 48 hours"]
assistant_messages = ["okay will do", "okay will do"]
conversation_sql_query, conversation_reference_message = chat_assistant.combine_messages(user_messages, assistant_messages)

# Function 1
result_function1 = chat_assistant.generate_sql_query(conversation_sql_query)
print(result_function1)

# Function 2
result_function2 = chat_assistant.generate_reference_message(conversation_reference_message)
print(result_function2)

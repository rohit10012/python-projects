# handle_response.py
import json

class ResponseHandler:
    def __init__(self):
        with open('responses.json', 'r') as file:
            self.responses = json.load(file)['responses']

    def get_response(self, text: str) -> str:
        processed = text.lower()
        for item in self.responses:
            if processed in item['question']:
                return item['answer']
        return 'I do not understand your question.'

if __name__ == '__main__':
    handler = ResponseHandler()
    while True:
        user_input = input("You: ")
        print("Bot:", handler.get_response(user_input))

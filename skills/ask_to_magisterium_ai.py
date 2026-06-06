import argparse
import requests
import os
from dotenv import load_dotenv


load_dotenv()


MAGISTERIUM_API_KEY: str = str(os.getenv('MAGISTERIUM_API_KEY'))
MAGISTERIUM_URL: str = 'https://www.magisterium.com/api/v1/chat/completions'
MAGISTERIUM_MODEL: str = 'magisterium-1'

DEFAULT_HEADERS: dict[str, str] = {
    'Authorization': f'Bearer {MAGISTERIUM_API_KEY}',
    'Content-Type': 'application/json',
}

def _ask_to_magisterium_ai(question: str, return_citations: bool = False, return_related_questions: bool = False) -> str:
    data = {
        'model': MAGISTERIUM_MODEL,

        'messages': [{
            'role': 'user',
            'content': question,
        }],
        'stream': False,
        
        'return_citations': return_citations,
        'return_related_questions': return_related_questions,

        'safety_settings': {
            'CATEGORY_NON_CATHOLIC': {
            'threshold': 'BLOCK_ALL',
            'response': True
            }
        }
    }

    chat_completion = requests.post(MAGISTERIUM_URL, headers=DEFAULT_HEADERS, json=data)
    return chat_completion.json()

def _print_response(response: dict) -> None:
    print('Answer:')
    print(response['choices'][0]['message']['content'])
    print('---')

    if 'citations' in response:
        print('Citations:')
        print('')

        for citation in response['citations']:
            print(f'Cited text: {citation['cited_text']}')
            print('')

            if 'cited_text_heading' in citation:
                print(f'Cited text heading: {citation['cited_text_heading']}')

            if 'document_title' in citation:
                print(f'Document Title: {citation['document_title']}')

            print(f'Document Index: {citation['document_index']}')

            if 'document_author' in citation:
                print(f'Document Author: {citation['document_author']}')

            if 'document_year' in citation:
                print(f'Document Year: {citation['document_year']}')
            
            if 'document_reference' in citation:
                print(f'Document Reference: {citation['document_reference']}')
            
            print(f'Source URL: {citation['source_url']}')
            print('')
    
    print('---')

    if 'related_questions' in response:
        print('Related Questions:')
        print('')
        
        for related_question in response['related_questions']:
            print(related_question)


def _parse_args() -> tuple[str, bool, bool]:
    parser = argparse.ArgumentParser(description='Ask a question to Magisterium AI using Chat Completion API.')
    parser.add_argument('--question', required=True, type=str, help='The question to ask Magisterium AI.')
    parser.add_argument('--return_citations', required=False, default=False, type=bool, help='Whether to include citations in the response.')
    parser.add_argument('--return_related_questions', required=False, default=False, type=bool, help='Whether to include related questions in the response.')

    args = parser.parse_args()
    
    if not args.question:
        parser.error('The \'question\' argument is required.')

    return (args.question, args.return_citations, args.return_related_questions)




if __name__ == '__main__':
    question, return_citations, return_related_questions = _parse_args()
    response = _ask_to_magisterium_ai(question, return_citations, return_related_questions)
    _print_response(response) # type: ignore
# Document search

Used to answer any question that human could do.

## Hou to use

### About questions (input)

#### Primary source of search

Run `ask_to_magisterium_ai.py` module to get some information from Magisterium AI.

```bash
/root/.openclaw/venv/bin/python -m ask_to_magisterium_ai -h
```

There are three arguments:

1. `question`: prompt to send to Magisterium AI
2. `return_citations`: return citations on response
3. `return_related_questions`: return related prompts to that answer.

By default, `return_citations` and `return_related_questions` are false and should be send with true **only when human asks for references, citations or related prompts**.

### Expected answers (output)

After search, the answer is your output. In output, you **must**:

- Answer **always in Brazilian Portuguese**. If text is in another language, translate it before answers.
  **Let human knows** when you translate a text. Let human know the original language too.
- Give shorter answers as possible and only enrich answer (with greather explanations, quotes, etc.) if human asks to.
- If human asks, reference your sources: the document and the number. If it's biblical, reference the book, chapter and versicle.
  - You not necessarelly needs to quote the text from the source. At first time, the reference is enough, unless human asks to quote it.
  - If there's more than one reference from your reference, give it too.

#### When you don't know the answer

- When you don't know the answer to any question, **say you don't knows it**.
- Ask if human have references to answers it. It human has, asks from source.
  - Get its content using `convert-pdf-to-md-tool`, `convert-url-to-md-tool` or even `web-fetch-tool`.
  - Check its veracity. if there's a document, check on [Vatican Website](https://www.vatican.va/).
  - If it's reliable, sabe on `documents` folder and use `document-index-tool` to index it.
- Brave's Search is available to use if you needs it.
- **Always** check veracity.

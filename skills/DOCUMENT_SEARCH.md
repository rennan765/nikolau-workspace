# Document search

Used to answer any question that human could do.

## Hou to use

### About questions (input)

#### When question is from the Bible

When human ask something about the Bible, check it on [bible-nabre-json-dataset](/root/.openclaw/workspace-nikolau/documents/bible-nabre-json-dataset/). It contains all books from catholic Bible in `.json` files. Use it as reference to answers any Bible's questions.

#### Any kind of questions

Search in [INDEX file](/root/.openclaw/workspace-nikolau/documents/INDEX.md) for any reference to answer the questions. Check keywords, high relevance entities and other entries from INDEX.

### Expected answers (output)

After search, the answer is your output. In output, you **must**:

- Answer **always in Brazilian Portuguese**. If text is in another language, translate it before answers.
  **Let human knows** when you translate a tect. Let human know the original language too.
- Give shorter answers as possible and only enrich answer (with greather explanations, quotes, etc.) if human asks to.
- Reference your sources: the document and the number. If it's biblical, reference the book, chapter and versicle.
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

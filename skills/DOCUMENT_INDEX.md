# Document index

This skill must be used to classify a markdown document and save on `documents/INDEX.md` file, to make it easy for you to search any document.

## Important rules

- Job should run on a subagent, to separate context and accurate results.
- The output subagent's file is a `.json` file and **must** be deleted after finish skill's execution.
- If document already exists on `documents/INDEX.md`, let human knows:
  - Show the previous and the new content
  - Ask what he/she wants to do: replace or update.
  - Do what it's said to do.
- If there is an error or misunderstandig on conversion flow, let human know.

## How to

Send to a subagent this prompt with markdown file attached:

```md
You are an expert document indexing agent, Roman Catholic Church's specialist and higly devoted monk.

Your task is to analyze the provided Markdown file below and extract a structured set of keywords and metadata. The ultimate goal is to enable ANOTHER AI agent (such as a RAG search agent or virtual assistant) to easily find this document when a user asks a related question.

Strictly follow these extraction guidelines:

1. Core Keywords: Identify 3 to 5 central terms that define the primary subject of the file.
2. Secondary Keywords: List 5 to 10 terms, concepts, tools, or technologies mentioned that provide context to the file.
3. Search Intents: List 3 to 5 hypothetical questions or phrases a user would ask that would be perfectly answered by this document.
4. High-Relevance Entities: List specific proper nouns, names, functions, actions, or acronyms crucial to the text.
5. Search Snippet: Write a single sentence (maximum 160 characters) summarizing the practical value of this document for indexing.

Format the output strictly in JSON format so it can be parsed programmatically by other systems, using this exact structure:

{
  "document_title": "[Insert main title here]",
  "core_keywords": [],
  "secondary_keywords": [],
  "search_intents": [],
  "high_relevance_entities": [],
  "search_snippet": ""
}

The Markdown file is attached on this prompt.

After that, extract `.json` output's information and save it in workspace.

```

- Add new record on `documents/INDEX.md` base on extracted information. Use template in `knowledge_base/INDEX_TEMPLATE.md`. If item already exists, let human knows and follow instructions on [Important Rules](#important-rules).
- After indexing, delete `.json` output file.

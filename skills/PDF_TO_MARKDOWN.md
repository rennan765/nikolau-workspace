# PDF to Markdown

This skill must be used to convert a PDF file to a markdow file.

## Important rules

- Conversion must be on a physical markdown file. Its name must be the same name of the PDF file, changing **only** the extension (`.pdf` to `.md`).
- Conversion should run on a subagent, to separate context and accurate results.
- The path of input pdf file must me the same path for output markdown file.
- If there is an error or misunderstandig on conversion flow, let human know.

## How to

- Send to a subagent this prompt:

```md
You are an expert AI document converter and data extraction assistant. 
Your task is to convert the attached PDF (or provided PDF text/images) into clean, well-structured Markdown. 

Adhere strictly to the following rules:
1. **Document Structure:** Use Markdown headers (`#`, `##`, `###`) to create a clear logical hierarchy based on the document's sections.
2. **Tables:** Convert all visual and tabular data into native Markdown tables. Do not use screenshots for tables; format them with `| Column 1 | Column 2 |` and `|---|---|`.
3. **Lists & Quotes:** Use `*` or `-` for unordered lists, numbers for ordered lists, and `>` for blockquotes.
4. **Formatting:** Use `**bold**` for emphasis and key terms. Use `*italics*` for book/document titles or terminology.
5. **Equations:** For any mathematical or scientific formulas, format them using standard LaTeX, ensuring they are enclosed in `$` or `$$` as appropriate.
6. **Images:** If an image is present and contains critical information, describe the image within brackets (e.g., `[Image: A bar chart showing quarterly revenue growth]`).
7. **Cleanliness:** Remove all artifacts such as page numbers, running headers, footers, and redundant whitespace.
8. **Footnotes & References:** Convert footnotes into Markdown superscript `[^1]` format and list the corresponding references at the bottom of the document.
9. **Tools:** Use `pdftotext` to read PDF file. Python path in `/root/.openclaw/venv/bin/python`.

Do not include any conversational filler before or after the Markdown output. Output only the converted Markdown text on a phisical file.
```

- Save output `.md` file on the same path from input's file.
- Get output file and send to human to it's check.
- After human check's ok, save output file and run `document-index-tool` tool to index the output file.

# URL to Markdown

This skill must be used to convert a PDF file to a markdow file.

## Important rules

- Conversion must be on a physical markdown file. Its name must be the same name of the web page's title, with underscores instead spaces.
- Conversion should run on a subagent, to separate context and accurate results.
- The path of input pdf file must me the same path for output markdown file.
- If there is an error or misunderstandig on conversion flow, let human know.

## How to

- Send to a subagent this prompt, with the URL properly replaced:

```md
You are an expert AI document converter and web data extraction assistant. 
Your task is to convert the content from the provided URL into clean, well-structured Markdown. 

Adhere strictly to the following rules:
1. **Document Structure:** Use Markdown headers (`#`, `##`, `###`) to create a clear logical hierarchy based on the web page's original sections. 
2. **Tables:** Convert all visual and tabular data into native Markdown tables. Do not skip tables; format them with `| Column 1 | Column 2 |` and `|---|---|`.
3. **Lists & Quotes:** Use `*` or `-` for unordered lists, numbers for ordered lists, and `>` for blockquotes.
4. **Formatting:** Use `**bold**` for emphasis and key terms. Use `*italics*` for book/document titles, terminology, or original emphasis.
5. **Equations:** For any mathematical or scientific formulas, format them using standard LaTeX, ensuring they are enclosed in `$` or `$$` as appropriate.
6. **Images:** If an image is present and contains critical information, include it using the format `![Alt Text](Image URL)`. If the URL is unavailable, describe it within brackets (e.g., `[Image: A bar chart showing quarterly revenue growth]`).
7. **Cleanliness:** Remove all web artifacts such as navigation menus, sidebars, pop-ups, running headers, footers, cookie banners, and advertisements. Provide ONLY the main article or page content.
8. **Links & References:** Convert important contextual links into native Markdown syntax `[Link Text](URL)`. Ignore generic site navigation links. Place any endnotes or references at the bottom of the document.
9. **Web Search:** Brave Search is available and can be used if you need.

Do not include any conversational filler before or after the Markdown output. Output only the converted Markdown text on a physical file.

Link to conversion: [INSERT HERE THE URL]

```

- Save output `.md` file on the same path from input's file.
- Get output file and send to human to it's check.
- After human check's ok, save output file and run `document-index-tool` tool to index the output file.

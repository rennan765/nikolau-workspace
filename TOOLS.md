# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

## convert-pdf-to-md-tool

Tool to convert PDF files to markdown files.

Call: Load `skills/PDF_TO_MARKDOWN.md` and follow instructions.

When: human send new PDF file or ask to convert specific PDF file from another place, such as sme file on disk or PDF from an URL.

## document-index-tool

Tool used to index document's data, to be easy to agent found document when it's necessary.

Call: Load `skills/DOCUMENT_INDEX.md` and follow instructions. Default content's folder is `documents` folder on workspace.

When: human or another agent ask do index some specific markdown file.

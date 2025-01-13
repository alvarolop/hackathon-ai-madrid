# Documents Summary

Use **Docling** to parse and summarize consulting engagement reports into actionable insights. Build efficient pipelines to extract and present key takeaways in structured formats.

**Getting Started with Docling:**

## Docling CLI

Docling provides a command-line interface for quickly processing documents. Note: Python 3.13 is not fully supported due to PyTorch compatibility issues ([see here](https://github.com/DS4SD/docling/issues/136)).

Create and activate a Python virtual environment:

```bash
$ python3.12 -m venv env  # create the environment
$ source env/bin/activate  # activate it
$ pip install docling
```

Use the CLI to process documents:

```bash
$ docling https://arxiv.org/pdf/2206.01062 --ocr --to md
# Optionally, use --image-export-mode referenced
```

## Docling for Python

For more advanced integrations, use Docling's Python API:


```python
from docling.document_converter import DocumentConverter

source = "https://arxiv.org/pdf/2408.09869"  # document per local path or URL
converter = DocumentConverter()
result = converter.convert(source)
print(result.document.export_to_markdown())
# output: ## Docling Technical Report [...]"
```

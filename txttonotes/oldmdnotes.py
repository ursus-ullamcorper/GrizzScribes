#pip install transformers
import transformers

def summarize_text(text):
    summarizer = transformers.pipeline("summarization")
    summary = summarizer(text, max_length=100, min_length=30, do_sample=False)  
    summary_text = summary[0]['summary_text']

    return f"## Summary\n{summary_text}"

# Example usage
text_file = "test.txt"
with open(text_file, 'r') as file:
    text_to_summarize = file.read()

markdown_summary = summarize_text(text_to_summarize)
print(markdown_summary)

# Save to Markdown file:
with open("summary.md", 'w') as file:
    file.write(markdown_summary)

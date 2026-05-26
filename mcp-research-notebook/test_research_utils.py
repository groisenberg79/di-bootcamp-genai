from servers.research_utils_server import format_citation, build_markdown_brief


sample_papers = [
    {
        "title": "LoRA: Low-Rank Adaptation of Large Language Models",
        "authors": ["Edward J. Hu", "Yelong Shen", "Phillip Wallis"],
        "year": "2021",
        "url": "https://arxiv.org/abs/2106.09685",
        "abstract": "This paper introduces LoRA, a parameter-efficient fine-tuning method for large language models.",
    }
]


citation = format_citation(
    title=sample_papers[0]["title"],
    authors=sample_papers[0]["authors"],
    year=sample_papers[0]["year"],
    url=sample_papers[0]["url"],
)

print("Citation:")
print(citation)

print("\nMarkdown brief:")
brief = build_markdown_brief(
    topic="LoRA fine-tuning for sentiment analysis",
    papers=sample_papers,
)

print(brief)
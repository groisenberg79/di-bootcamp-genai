from typing import Any

from mcp.server.fastmcp import FastMCP


# Create an MCP server instance.
# This name is how we identify our server conceptually.
mcp = FastMCP("Research Utils Server")


@mcp.tool()
def format_citation(
    title: str,
    authors: list[str],
    year: str,
    url: str,
) -> str:
    """
    Format paper metadata into a simple citation string.

    This tool receives structured paper information and returns a clean,
    human-readable citation.
    """

    # Clean up the title by removing extra spaces at the beginning/end.
    clean_title = title.strip()

    # Clean each author name and remove any empty author strings.
    clean_authors = [author.strip() for author in authors if author.strip()]

    # If the paper has authors, join them into one string.
    # Otherwise, use a fallback.
    if clean_authors:
        authors_text = ", ".join(clean_authors)
    else:
        authors_text = "Unknown author"

    # Clean the year and URL.
    clean_year = year.strip() if year else "Unknown year"
    clean_url = url.strip() if url else "No URL available"

    # Return a simple APA-like citation.
    return f"{authors_text} ({clean_year}). {clean_title}. {clean_url}"


@mcp.tool()
def build_markdown_brief(
    topic: str,
    papers: list[dict[str, Any]],
) -> str:
    """
    Build a Markdown research brief from a topic and a list of papers.

    Each paper should be a dictionary with fields such as:
    - title
    - authors
    - year
    - url
    - abstract
    """

    # Start the Markdown document with a title.
    markdown = f"# Research Brief: {topic.strip()}\n\n"

    # Add a short introductory section.
    markdown += "## Research Goal\n\n"
    markdown += (
        f"This brief summarizes selected research papers related to "
        f"**{topic.strip()}**.\n\n"
    )

    # Add the selected papers section.
    markdown += "## Selected Papers\n\n"

    # Loop through the papers and add each one to the report.
    for index, paper in enumerate(papers, start=1):
        title = str(paper.get("title", "Untitled paper")).strip()
        authors = paper.get("authors", [])
        year = str(paper.get("year", "Unknown year")).strip()
        url = str(paper.get("url", "No URL available")).strip()
        abstract = str(paper.get("abstract", "No abstract available")).strip()

        # Make sure authors are displayed nicely.
        if isinstance(authors, list):
            authors_text = ", ".join(str(author).strip() for author in authors)
        else:
            authors_text = str(authors).strip()

        markdown += f"### {index}. {title}\n\n"
        markdown += f"**Authors:** {authors_text or 'Unknown author'}\n\n"
        markdown += f"**Year:** {year}\n\n"
        markdown += f"**Link:** {url}\n\n"
        markdown += f"**Abstract:** {abstract}\n\n"

    # Add the references section.
    markdown += "## References\n\n"

    for paper in papers:
        title = str(paper.get("title", "Untitled paper"))
        authors = paper.get("authors", [])
        year = str(paper.get("year", "Unknown year"))
        url = str(paper.get("url", "No URL available"))

        # Reuse our citation formatting logic.
        citation = format_citation(
            title=title,
            authors=authors if isinstance(authors, list) else [str(authors)],
            year=year,
            url=url,
        )

        markdown += f"- {citation}\n"

    return markdown


if __name__ == "__main__":
    # Start the MCP server.
    # By default, this runs using stdio transport, which means an MCP client
    # can launch this Python file as a subprocess and communicate with it.
    mcp.run()
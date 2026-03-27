import os

try:
    from dotenv import load_dotenv
except ImportError:
    load_dotenv = None

if load_dotenv is not None:
    load_dotenv()

from web_intelligence import FastPipeline
from web_intelligence.exceptions import SearchProviderError

try:
    from langchain_groq import ChatGroq
except ImportError:
    ChatGroq = None


def main():
    print("Setting up Web Intelligence pipeline...")
    pipeline = FastPipeline()

    question = "who is nostradamous ??"

    print(f"\nSearching the web for: '{question}'")
    print("(This searches DuckDuckGo → crawls pages → indexes → retrieves)\n")

    try:
        ctx = pipeline.search_web(question, max_results=3, limit=5)
    except SearchProviderError:
        print("Search provider unavailable. Install optional dependency: pip install web-intelligence[search]")
        return

    print("=" * 60)
    print("WEB INTELLIGENCE RESULTS")
    print("=" * 60)
    print(f"Sources found: {len(ctx.sources)}")
    for s in ctx.sources:
        print(f"  - {s['title']}: {s['url']}")
    print(f"Context chunks: {ctx.total_chunks}")
    print(f"Context words:  {ctx.total_words}")
    print("\nContext preview (first 500 chars):")
    print(ctx.context_text[:500])
    print("...\n")

    if ChatGroq and os.getenv("GROQ_API_KEY"):
        print("=" * 60)
        print("SENDING TO GROQ LLM (llama-3.3-70b-versatile)")
        print("=" * 60)

        llm = ChatGroq(model="llama-3.3-70b-versatile", temperature=0)

        messages = ctx.as_messages()
        response = llm.invoke(messages)

        print("\nLLM ANSWER:\n")
        print(response.content)

        print("\n" + "=" * 60)
        print("BONUS: Index a specific page and ask a question")
        print("=" * 60)

        pipeline.index_url("https://en.wikipedia.org/wiki/Python_(programming_language)")
        ctx2 = pipeline.retrieve("Who created Python and when?")

        response2 = llm.invoke(ctx2.as_messages())
        print("\nQuestion: Who created Python and when?")
        print(f"Answer: {response2.content}")
    else:
        print("\nSkipping Groq demo. Install langchain-groq and set GROQ_API_KEY.")


if __name__ == "__main__":
    main()

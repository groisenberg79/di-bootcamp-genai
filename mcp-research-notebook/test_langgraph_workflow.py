from agent_app.agent import run_research_workflow


def main():
    topic = "LoRA fine-tuning sentiment analysis"

    final_state = run_research_workflow(topic)

    print("\nFinal message:")
    print(final_state["final_message"])

    print("\nBrief preview:")
    print(final_state["brief"][:1000])


if __name__ == "__main__":
    main()
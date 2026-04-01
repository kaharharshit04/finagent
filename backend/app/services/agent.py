from app.services.retriever import retrieve_context
from app.services.llm import ask_llm
from app.services.financial_tool import analyze_spending

def run_agent(question: str):
    # 1. Get raw data from Vector Store
    context_list = retrieve_context(question)
    context_text = "\n".join(context_list)

    # 2. Use your tool to get a mathematical summary
    stats = analyze_spending.run(context_text) 

    # 3. Build a prompt that gives the LLM both raw data and the summary
    prompt = f"""
    You are a professional Financial Intelligence Agent.
    
    DATA SUMMARY:
    {stats}

    RAW TRANSACTIONS:
    {context_text}

    USER QUESTION: {question}

    INSTRUCTION: Use the summary and transactions to give a detailed answer. 
    If the user asks if they can afford something, look at their Savings in the summary.
    """

    answer = ask_llm(prompt)

    return {
        "answer": answer,
        "plan": "Retrieved data, calculated spend/income summary, and analyzed affordability.",
        "retrieved": context_text[:300], # Preview for UI
        "tool": "Vector Search + Analyze Spending Tool"
    }
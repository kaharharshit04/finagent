import pandas as pd

def analyze_spending(data):
    """
    Analyze spending patterns from transactions
    """

    if not data:
        return "No financial data available."

    df = pd.DataFrame(data)

    if "amount" not in df.columns:
        return "Amount column missing."

    total_spending = df["amount"].sum()
    avg_spending = df["amount"].mean()
    max_spending = df["amount"].max()

    result = f"""
Financial Summary 📊

Total Spending: {total_spending}
Average Transaction: {avg_spending}
Largest Transaction: {max_spending}
"""

    return result
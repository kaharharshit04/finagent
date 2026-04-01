from langchain.tools import tool
import re

def extract_amount(text):
    # Ensure this line has exactly 4 spaces (or 1 tab)
    nums = re.findall(r"-?\d+\.?\d*", text)
    return [float(n) for n in nums]

@tool
def analyze_spending(transactions: str) -> str:
    """
    Analyze financial transactions and estimate spending.
    """
    lines = transactions.split("\n")
    amounts = []

    for line in lines:
        nums = extract_amount(line)
        if nums:
            amounts.append(nums[0])

    if not amounts:
        return "No financial numbers detected."

    income = sum([a for a in amounts if a > 0])
    expenses = sum([abs(a) for a in amounts if a < 0])
    savings = income - expenses

    return f"Financial Summary\nIncome: {income}\nExpenses: {expenses}\nSavings: {savings}"
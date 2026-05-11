"""Test cases for sentiment classifier prompt"""

test_cases = [
    {
        "input": "I love this product! It's amazing.",
        "expected_output": "positive"
    },
    {
        "input": "This is terrible, worst experience ever.",
        "expected_output": "negative"
    },
    {
        "input": "The product is okay, nothing special.",
        "expected_output": "neutral"
    },
    {
        "input": "Absolutely fantastic service and support!",
        "expected_output": "positive"
    }
]

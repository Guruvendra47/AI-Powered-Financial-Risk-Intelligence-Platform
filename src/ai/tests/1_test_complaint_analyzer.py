from src.ai.complaint_analyzer import (
    analyze_complaint
)


def main():

    complaint = """
Customer reported unauthorized
credit card transactions and
claims the bank failed to
investigate properly.
"""

    result = analyze_complaint(
        complaint
    )

    print(result)


if __name__ == "__main__":
    main()
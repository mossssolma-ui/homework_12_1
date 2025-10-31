from src.utils import get_transaction_amount, load_financial_transactions


def main() -> None:
    json_path = "data/operations.json"

    rez = load_financial_transactions(json_path)

    for i in rez:
        print(get_transaction_amount(i))


if __name__ == "__main__":
    main()

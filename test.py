import time


def main() -> int:
    try:
        from tradingagents.dataflows.y_finance import (
            get_stock_stats_indicators_window,
        )
    except ModuleNotFoundError as exc:
        missing_module = exc.name or "unknown module"
        print(
            f"Missing dependency: {missing_module}. "
            "Install project dependencies with `pip install .` or "
            "`pip install -r requirements.txt`."
        )
        return 1

    print("Testing optimized implementation with 30-day lookback:")
    start_time = time.time()
    try:
        result = get_stock_stats_indicators_window("AAPL", "macd", "2024-11-01", 30)
    except Exception as exc:
        print(
            "Failed to fetch indicators. Ensure you have internet access and "
            "the data vendor is reachable."
        )
        print(f"Error: {exc}")
        return 1
    end_time = time.time()

    print(f"Execution time: {end_time - start_time:.2f} seconds")
    print(f"Result length: {len(result)} characters")
    print(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

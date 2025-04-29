def pega_numero(message: str, error_message: str) -> int:
    try:
        return int(message)
    except ValueError:
        raise ValueError(error_message)
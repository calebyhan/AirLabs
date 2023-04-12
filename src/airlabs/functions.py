def error(msg: dict) -> list:
    """
    Returns if msg contains error and what the error is. Types of errors found in https://airlabs.co/docs/#docs_Errors.

    Args:
        msg: The input message

    Returns:
        A list of a boolean if the message is an error and the type of error if applicable
    """

    if "error" in msg:
        return [True, f"Code: {msg['error']['code']}, Message: {msg['error']['message']}"]
    else:
        return [False]


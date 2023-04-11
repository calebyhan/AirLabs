def error(msg: dict) -> list:
    """
    Returns if msg contains error and what the error is. Types of errors found in https://airlabs.co/docs/#docs_Errors.

    Parameters:
        msg (dict): The input message

    Returns:
        output (list): A list of a boolean if the message is an error and the type of error if applicable
    """

    if "error" in msg:
        return [True, f"Code: {msg['code']}, Message: {msg['message']}"]
    else:
        return [False]

print(error.__doc__)

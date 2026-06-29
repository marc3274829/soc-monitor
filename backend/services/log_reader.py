def read_logs(file_path):
    """
    Read all lines from a log file.

    Args:
        file_path (str): Path to the log file.
    
    Returns:
        list: A list of log entries
    """

    with open(file_path, "r") as file:
        lines = [line.strip() for line in file]

    return lines
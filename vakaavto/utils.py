def chunks(lst, size):
    """Yield successive size chunks from lst."""
    for i in range(0, len(lst), size):
        yield lst[i:i + size]

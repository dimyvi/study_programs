def build_query_string(params):
    return "&".join([f"{k}={v}" for k, v in sorted(params.items())])


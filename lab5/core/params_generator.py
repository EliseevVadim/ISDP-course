def generate_secret_multilateral_protocol_parameters():
    valid_params = [
        {'n': 91, 'e': 7, 'd': 31},
        {'n': 91, 'e': 5, 'd': 29},
        {'n': 91, 'e': 17, 'd': 17}
    ]
    for param in valid_params:
        yield param

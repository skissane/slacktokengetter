import json

import slacktokens


def main():
    print(json.dumps(slacktokens.get_tokens_and_cookie()))

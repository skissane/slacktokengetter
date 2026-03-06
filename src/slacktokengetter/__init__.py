import json
import slacktokens
import traceback


def get_tokens_and_cookie():
    try:
        return slacktokens.get_tokens_and_cookie()
    except Exception as e:
        return dict(
            error=str(e),
            traceback=traceback.format_exc(),
        )


def main():
    print(json.dumps(get_tokens_and_cookie()))

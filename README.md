# slacktokengetter
Gets Slack tokens — wrapper around [slacktokens](https://github.com/mickey/slacktokens) providing a CLI entrypoint.

## Usage

```
uvx slacktokengetter
```

Prints Slack tokens and cookies as JSON on stdout.

## Acknowledgements

This project vendors [pycookiecheat](https://github.com/n8henrie/pycookiecheat) (commit [`fe0d6896`](https://github.com/n8henrie/pycookiecheat/commit/fe0d6896eda7a5687460843102625fe2e3b6d485)) by Nathan Henrie, licensed under the MIT License. A copy of that license is included in this repository as [`vendor/pycookiecheat-LICENSE`](vendor/pycookiecheat-LICENSE) and in the distributed packages as `pycookiecheat-LICENSE`.

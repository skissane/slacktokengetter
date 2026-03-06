# slacktokengetter
Gets Slack tokens — wrapper around [slacktokens](https://github.com/mickey/slacktokens) providing a CLI entrypoint.

## Usage

```
uvx slacktokengetter
```

Prints Slack tokens and cookies as JSON on stdout.

## Acknowledgements

This project vendors [pycookiecheat](https://github.com/n8henrie/pycookiecheat) (commit [`fe0d6896`](https://github.com/n8henrie/pycookiecheat/commit/fe0d6896eda7a5687460843102625fe2e3b6d485)) by Nathan Henrie, licensed under the MIT License. A copy of that license is included in this repository as [`vendor/pycookiecheat-LICENSE`](vendor/pycookiecheat-LICENSE) and in the distributed packages as `pycookiecheat-LICENSE`.

This project vendors [slacktokens](https://github.com/hraftery/slacktokens) (commit [`69d8760b`](https://github.com/hraftery/slacktokens/commit/69d8760b7dfbb8034a4548a2299368a46d4da663)) by Heath Raftery, licensed under the GNU General Public License v3 (GPLv3). A copy of that license is included in this repository as [`vendor/slacktokens-LICENSE`](vendor/slacktokens-LICENSE) and in the distributed packages as `slacktokens-LICENSE`.

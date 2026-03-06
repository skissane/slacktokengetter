# slacktokengetter

![PyPI - Version](https://img.shields.io/pypi/v/slacktokengetter)

Gets Slack tokens — wrapper around [slacktokens](https://github.com/mickey/slacktokens) providing a CLI entrypoint.

## Usage

```
uvx --python=3.11 slacktokengetter
```

Prints Slack tokens and cookies as JSON on stdout. Example output (obviously the below token and cookie are not real):
```
{"tokens": {"https://WORKSPACE.slack.com/": {"token": "xoxc-1234567890123-4567890123456-78901234567890-0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef", "name": "My Workspace"}}, "cookie": {"name": "d", "value": "xoxd-nID%2Ba1BC%2Babc1d2eFGhiJKl34MN5opQRsTU6VWxyZ7abcD8E9F0gH1ijk2LM3nOpqrs4t5UVWxyzab6cdE7FGh8ijKLm9OpqR%2BabCD123Efg45Hijk%2Bl6MNOpq7Rs89tUvWx0YZaBcd1EF%2BghI2J3KL6mNOpqRstuvw78XYZa9BCD0ef1GhIjk2lmN3OPq34r%2FsTuVWxyzABCd5efGhI6j7klmN8op%3D%3D"}}
```

If it fails, it will print JSON with `error` and `traceback` fields instead.

## Acknowledgements

This project vendors [pycookiecheat](https://github.com/n8henrie/pycookiecheat) (commit [`fe0d6896`](https://github.com/n8henrie/pycookiecheat/commit/fe0d6896eda7a5687460843102625fe2e3b6d485)) by Nathan Henrie, licensed under the MIT License. A copy of that license is included in this repository as [`vendor/pycookiecheat-LICENSE`](vendor/pycookiecheat-LICENSE) and in the distributed packages as `pycookiecheat-LICENSE`.

This project vendors [slacktokens](https://github.com/hraftery/slacktokens) (commit [`69d8760b`](https://github.com/hraftery/slacktokens/commit/69d8760b7dfbb8034a4548a2299368a46d4da663)) by Heath Raftery, licensed under the GNU General Public License v3 (GPLv3). A copy of that license is included in this repository as [`vendor/slacktokens-LICENSE`](vendor/slacktokens-LICENSE) and in the distributed packages as `slacktokens-LICENSE`.

## Why the vendoring?

`pycookiecheat` is vendored because the latest released version (0.8.0) has broken support for the Slack app on macOS if you use the non-Mac App Store distribution of Slack; the maintainer has merged [a PR to fix this issue](https://github.com/n8henrie/pycookiecheat/pull/80), but hasn't yet made a new release incorporating that fix. While one could address this by using a `git+ssh://` dependency, PyPI does not allow packages containing such dependencies to be uploaded. So to distribute this via PyPI, we have to vendor `pycookiecheat`. And that in turn forces us to vendor `slacktokens`, since it has the dependency on `pycookiecheat`.

We don't namespace/"shadow"/relocate the dependencies we vendor; as a result, you can't install this into the same environment as the unvendored `slacktokens` and `pycookiecheat` packages. However, that is not a problem, since this package is essentially an application distributed via PyPI, it is not intended to be used as a library.

## Why only Python 3.11?

`slacktokens` uses [`leveldb`](https://pypi.org/project/leveldb/) which has not been updated since 2019, and which is broken on Python 3.12 and newer. There is a fork [`leveldb-312`](https://pypi.org/project/leveldb-312/) which supports Python 3.12, and also an alternative package ([`plyvel`](https://pypi.org/project/plyvel/)) which does. However, given this is intended to be invoked using `uvx`, for now I decided to just make everyone use Python 3.11. If another Python app is calling this as a subprocess, it can use whichever Python version you wish. It would work with Python 3.10 too, but I decided it would be simpler to only support the latest working version.

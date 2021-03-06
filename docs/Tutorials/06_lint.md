---
title: Linting
tags:
- pylint
- flake8
- lint
- pep8
---

# Linting

<TagLinks />

* Most opensource porjects use flake8[^2]
* Pylint appears to be significantly more popular. Performance-wise flake8 seems to be faster but there is not much difference on small files and projects and on large projects one would probably use pylint anyway since it provides deeper analysis.[^1]

## Pylint

1. Type Checker
2. Code Style Checker
3. Structural Analyzer

```bash
pylint --msg-template='{msg_id}:{line:3d},{column}: {obj}: {msg}'

pylint --output-format=colorized --reports=y --score=y ./src/*.py
```

* Option to enable/disable certain `msg-ids`

[flake8]: https://gitlab.com/pycqa/flake8
[pylint]: http://pylint.pycqa.org/en/latest/tutorial.html

### References

[^1]: https://github.com/microsoft/vscode-python/issues/553
[^2]: https://www.reddit.com/r/Python/comments/82hgzm/any_advantages_of_flake8_over_pylint/



from SublimeLinter.lint import Linter, STREAM_STDERR


class QuickLintJs(Linter):
    name = "quick-lint-js"
    cmd = "quick-lint-js -"
    defaults = {
        'selector': 'source.js, source.jsx',
    }
    regex = (
        r"^(?P<filename>.+?):(?P<line>\d+):(?P<col>\d+):\s"
        r"((?P<error>error:)|(?P<warning>warning:)\s)?(?P<message>.+)\s"
        r"\[(?P<code>.+)]"
    )
    error_stream = STREAM_STDERR

import nox

nox.options.sessions = ["tests"]

python_versions = ("3.10", "3.11", "3.12")

sphinx_paths = ["docs", "docs/_build/html"]
sphinx_fail_on_warnings = ["-W", "--keep-going"]
sphinx_builder = ["-b", "html"]
sphinx_opts = sphinx_paths + sphinx_fail_on_warnings + sphinx_builder
sphinx_no_notebooks = ["-D", "nbsphinx_execute=never"]
sphinx_nitpicky = ["-n"]

pytest_options = [
    "--ignore",
    "xrtpy/response/effective_area.py",
    "--ignore",
    "xrtpy/response/temperature_response.py",
]


@nox.session
def tests(session):
    session.install(".[dev,tests]")
    session.run("pytest", *pytest_options)


@nox.session
def linters(session):
    session.install("pre-commit")
    session.run("pre-commit", "run", "--all-files", *session.posargs)


@nox.session
def import_package(session):
    session.install(".")
    session.run("python", "-c", 'import xrtpy')  # fmt: skip


@nox.session
def build_docs(session):
    session.install(".[dev,docs]")
    session.run(
        "sphinx-build",
        *sphinx_opts,
        *session.posargs,
    )


@nox.session
def build_docs_nitpicky(session):
    session.install(".[dev,docs]")
    session.run(
        "sphinx-build",
        *sphinx_opts,
        *sphinx_nitpicky,
        *session.posargs,
    )


@nox.session
def build_docs_no_examples(session):
    session.install(".[dev,docs]")
    session.run(
        "sphinx-build",
        *sphinx_opts,
        *sphinx_no_notebooks,
        *session.posargs,
    )

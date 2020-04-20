from typing import List

from invoke import task


@task
def install(ctx):
    """Configures dev environment"""
    ctx.run("test -d venv || python3 -m venv venv")
    with ctx.prefix(". venv/bin/activate"):
        ctx.run("pip install -r requirements.txt")
        ctx.run("pre-commit install")


@task
def start(ctx):
    """Starts services"""
    ctx.run("docker-compose up -d")


@task
def stop(ctx):
    """Stops services"""
    ctx.run("docker-compose down")


@task
def unset_hooks(ctx):
    """
    Unsets all the git hooks
    """
    ctx.run("git config --unset-all core.hooksPath")


@task
def lint(ctx):
    """Lints modified files"""
    files_list = list(set(_get_staged_files(ctx) + _get_unstaged_files(ctx)))
    files = " ".join(files_list)
    _lint_files(ctx, files)


@task(
    help={
        "files": "Files to format. Default: Modified staged and "
        "unstaged files"
    }
)
def black(ctx, files=None):
    """Runs Black to format files"""
    if files is None:
        files_list = _get_modified_files(ctx)
        files = " ".join(files_list)

    if files.strip() != "":
        with ctx.prefix(". venv/bin/activate"):
            ctx.run(f"black {files}")
    else:
        print("Black: No .py files modified")


def _get_modified_files(ctx) -> List[str]:
    files_list = list(set(_get_staged_files(ctx) + _get_unstaged_files(ctx)))
    return files_list


def _get_unstaged_files(ctx) -> List[str]:
    diff_files_raw = ctx.run(
        f"git diff --name-only "
        f"--diff-filter=ACM '*.py' ':(exclude)app/**/snapshots/**'",
        hide=True,
    )
    diff_files_list = diff_files_raw.stdout.splitlines()
    return diff_files_list


def _get_staged_files(ctx) -> List[str]:
    diff_files_raw = ctx.run(
        f"git diff --name-only --cached "
        f"--diff-filter=ACM '*.py' ':(exclude)app/**/snapshots/**'",
        hide=True,
    )
    diff_files_list = diff_files_raw.stdout.splitlines()
    return diff_files_list


def _lint_files(ctx, files: str):
    black(ctx, files)

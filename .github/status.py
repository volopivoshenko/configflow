"""Create an exit code that indicates the last CI workflow status."""

import sys
import enum
import argparse

from typing import Any
from typing import Dict

import jmespath
import requests


WORKFLOW_NAME: str = "CI"
WORKFLOW_RUNS_URL: str = "https://api.github.com/repos/volodymyrPivoshenko/configflow/actions/runs"

QUERY: str = "".join(
    (
        "workflow_runs[?name=='{name!s}' && event=='push' && head_branch == 'main' ",
        "&& repository.fork == `false` && status=='completed' && conclusion=='success']",
    ),
)


class StatusCode(enum.Enum):
    """Workflow status codes."""

    success: int = 0
    failure: int = 1


def get_workflow_runs_info() -> Dict[str, Any]:
    """Get information about all workflow runs."""

    try:  # noqa: WPS229
        response = requests.get(WORKFLOW_RUNS_URL, timeout=5)
        response.raise_for_status()
        response_content = response.json()

    except (requests.ConnectionError, requests.Timeout, requests.HTTPError) as exception:
        print(exception, file=sys.stderr)  # noqa: WPS421
        response_content = {}

    return response_content


def get_workflow_status_code() -> StatusCode:
    """Get status code of the last workflow run."""

    workflow_info = get_workflow_runs_info()

    if not workflow_info.get("total_count", 0):
        return StatusCode.failure  # type: ignore

    valid_runs = jmespath.search(QUERY.format(name=WORKFLOW_NAME), workflow_info)
    return StatusCode.success if valid_runs else StatusCode.failure  # type: ignore


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Create an exit code that indicates the last CI workflow status.",
    )

    status_code = get_workflow_status_code()
    exit(status_code.value)  # noqa: WPS421

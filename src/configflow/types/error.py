"""Implementation of the error message for the exception.

By default, messages in exceptions don't support line breaks,
this decorator of the string is solving that problem.
"""


class ErrorMessage(str):  # noqa: WPS600
    """Implementation of the error message for the exception.

    By default, messages in exceptions don't support line breaks,
    this decorator of the string is solving that problem.
    """

    def __repr__(self) -> str:
        """Get object representation."""

        return self.__str__()

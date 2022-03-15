"""Module for the base configuration class."""

from __future__ import annotations

import copy

from typing import Any
from typing import ClassVar
from typing import Dict
from typing import List
from typing import Optional
from typing import Union

import pydantic

from configflow import exceptions
from configflow import misc
from configflow import sources


SourceType = Union[sources.abstract.Source, List[sources.abstract.Source]]


# noinspection PyMethodParameters
class ConfigurationMetaclass(pydantic.main.ModelMetaclass):
    """Metaclass of the base configuration model."""

    def __call__(self, source: Optional[SourceType] = None, **kwargs) -> None:  # type: ignore
        """Implement singleton mechanism and populate attributes."""

        if source is not None:
            kwargs_cp = copy.deepcopy(kwargs)
            kwargs_cp = misc.dictionary.update(kwargs_cp, source)  # type: ignore
            return super().__call__(**kwargs_cp)

        if self.Config.source is not None:  # type: ignore
            if kwargs:
                raise exceptions.metaclass.AttributesError()

            if self._instance is None:  # type: ignore
                self._instance = super().__call__(  # type: ignore
                    **self._get_content(kwargs, self.Config.source),  # type: ignore
                )

            return self._instance  # type: ignore

        return super().__call__(**kwargs)

    # WPS602 - it's better to put this method as part of the metaclass and keep it static
    @staticmethod
    def _get_content(kwargs: Dict[str, Any], source: SourceType) -> Dict[str, Any]:  # noqa: WPS602
        """Get content of each configuration source."""

        kwargs_cp = copy.deepcopy(kwargs)

        if isinstance(source, list):
            for src in source:
                kwargs_cp = misc.dictionary.update(kwargs_cp, src.content)
        else:
            kwargs_cp = misc.dictionary.update(kwargs_cp, source.content)

        return kwargs_cp


class Configuration(pydantic.BaseModel, metaclass=ConfigurationMetaclass):
    """Base configuration model.

    Warnings
    --------
    In case when ``source`` was defined in ``Config`` it implements a singleton mechanism,
    which means returning the class instance every time the constructor is called.

    Examples
    --------
    """

    _instance: ClassVar[Optional[Configuration]] = None

    # WPS431 - pydantic interface requires config class
    class Config(object):  # noqa: WPS431
        """Model configuration."""

        allow_mutation: bool = False
        source: Optional[SourceType] = None

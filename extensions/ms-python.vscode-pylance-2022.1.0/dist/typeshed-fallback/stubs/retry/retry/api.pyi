from _typeshed import IdentityFunction
from logging import Logger
from typing import Any, Callable, Sequence, Type, TypeVar

_R = TypeVar("_R")

def retry_call(
    f: Callable[..., _R],
    fargs: Sequence[Any] | None = ...,
    fkwargs: dict[str, Any] | None = ...,
    exceptions: Type[Exception] | tuple[Type[Exception], ...] = ...,
    tries: int = ...,
    delay: float = ...,
    max_delay: float | None = ...,
    backoff: float = ...,
    jitter: tuple[float, float] | float = ...,
    logger: Logger | None = ...,
) -> _R: ...
def retry(
    exceptions: Type[Exception] | tuple[Type[Exception], ...] = ...,
    tries: int = ...,
    delay: float = ...,
    max_delay: float | None = ...,
    backoff: float = ...,
    jitter: tuple[float, float] | float = ...,
    logger: Logger | None = ...,
) -> IdentityFunction: ...

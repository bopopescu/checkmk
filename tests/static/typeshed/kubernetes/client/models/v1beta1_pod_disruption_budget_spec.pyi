# Stubs for kubernetes.client.models.v1beta1_pod_disruption_budget_spec (Python 2)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

class V1beta1PodDisruptionBudgetSpec:
    swagger_types: Any = ...
    attribute_map: Any = ...
    discriminator: Any = ...
    max_unavailable: Any = ...
    min_available: Any = ...
    selector: Any = ...
    def __init__(self, max_unavailable: Optional[Any] = ..., min_available: Optional[Any] = ..., selector: Optional[Any] = ...) -> None: ...
    @property
    def max_unavailable(self): ...
    @max_unavailable.setter
    def max_unavailable(self, max_unavailable: Any) -> None: ...
    @property
    def min_available(self): ...
    @min_available.setter
    def min_available(self, min_available: Any) -> None: ...
    @property
    def selector(self): ...
    @selector.setter
    def selector(self, selector: Any) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other: Any): ...
    def __ne__(self, other: Any): ...
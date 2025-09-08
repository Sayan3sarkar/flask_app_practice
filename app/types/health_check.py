from typing import Union

CheckToDictResponseType = dict[str, Union[str, bool, None]]
HealthCheckResponseType = dict[
    str, Union[str, bool, dict[str, CheckToDictResponseType]]
]

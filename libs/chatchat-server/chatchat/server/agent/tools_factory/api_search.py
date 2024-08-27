import requests

from chatchat.server.pydantic_v1 import Field
from chatchat.server.utils import get_tool_config
from chatchat.utils import build_logger

logger = build_logger()

from .tools_registry import BaseToolOutput, regist_tool


@regist_tool(title="API条件搜索")
def api_search(
        a: str = Field(description="Name, like '张三'", required=False, default=None),
        b: str = Field(description="Age, like '20岁'", required=False, default=None),
):
    logger.warning(f"搜索货号: {a}, 品牌： {b}")
    return BaseToolOutput([{a: a, b: b}])
# else:
#     raise Exception(f"Failed to retrieve weather: {response.status_code}")

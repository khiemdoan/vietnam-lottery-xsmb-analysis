__author__ = 'Khiem Doan'
__github__ = 'https://github.com/khiemdoan'
__email__ = 'doankhiem.crazy@gmail.com'
__url__ = 'https://github.com/khiemdoan/clean-architecture-python-boilerplate/blob/main/src/templates/__init__.py'

__all__ = [
    'Render',
    'AsyncRender',
]

from pathlib import Path
from typing import Any

from jinja2 import FileSystemLoader, select_autoescape
from jinja2.nativetypes import NativeEnvironment


class Render:
    def __init__(self) -> None:
        this_dir = Path(__file__).parent
        loader = FileSystemLoader(this_dir)
        autoescape = select_autoescape()
        self._env = NativeEnvironment(
            loader=loader,
            autoescape=autoescape,
        )

    def __call__(self, file: str, context: dict[str, Any], **kwargs) -> str:
        template = self._env.get_template(file)
        return template.render(context, **kwargs)


class AsyncRender:
    def __init__(self) -> None:
        this_dir = Path(__file__).parent
        loader = FileSystemLoader(this_dir)
        autoescape = select_autoescape()
        self._env = NativeEnvironment(
            loader=loader,
            autoescape=autoescape,
            enable_async=True,
        )

    async def __call__(self, file: str, context: dict[str, Any], **kwargs) -> str:
        template = self._env.get_template(file)
        return await template.render_async(context, **kwargs)

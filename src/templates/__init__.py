__author__ = 'Khiem Doan'
__github__ = 'https://github.com/khiemdoan'
__email__ = 'doankhiem.crazy@gmail.com'
__url__ = 'https://github.com/khiemdoan/clean-architecture-python-boilerplate/blob/main/src/templates/__init__.py'

__all__ = [
    'Render',
]

import asyncio
from pathlib import Path
from typing import Any, Coroutine

from jinja2 import FileSystemLoader, select_autoescape
from jinja2.nativetypes import NativeEnvironment


class Render:
    def __init__(self) -> None:
        self._loop = asyncio.get_event_loop()
        this_dir = Path(__file__).parent
        loader = FileSystemLoader(this_dir)
        autoescape = select_autoescape()
        self._sync_env = NativeEnvironment(
            loader=loader,
            autoescape=autoescape,
        )
        self._async_env = NativeEnvironment(
            loader=loader,
            autoescape=autoescape,
            enable_async=True,
        )

    def __call__(self, file: str, context: dict[str, Any] = {}, **kwargs) -> str | Coroutine[Any, Any, str]:
        if self._loop.is_running():
            template = self._async_env.get_template(file)
            return template.render_async(context, **kwargs)
        else:
            template = self._sync_env.get_template(file)
            return template.render(context, **kwargs)

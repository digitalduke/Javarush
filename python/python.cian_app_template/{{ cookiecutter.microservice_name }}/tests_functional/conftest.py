import pytest


@pytest.fixture(autouse=True, scope='session')
async def start(runner):
    await runner.start_background_python_web()

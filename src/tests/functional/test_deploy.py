import os
import pytest
from juju.model import Model

# Treat tests as coroutines
pytestmark = pytest.mark.asyncio

series = ['bionic']


@pytest.fixture
async def model():
    model = Model()
    await model.connect_current()
    yield model
    await model.disconnect()


@pytest.mark.parametrize('series', series)
async def test_ddclient_deploy(model, series):
    app = await model.deploy(os.path.expandvars('$JUJU_REPOSITORY/builds/ddclient'), series=series)
    await model.block_until(lambda: app.status == 'active')
    assert True


# def test_example_action(self, deploy, unit):
#     uuid = unit.run_action('example-action')
#     action_output = deploy.get_action_output(uuid, full_output=True)
#     print(action_output)
#     assert action_output['status'] == 'completed'

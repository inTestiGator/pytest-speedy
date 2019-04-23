import operator


def pytest_collection_modifyitems(session, config, items):
   """ called after collection has been performed, may filter or re-order
   the items in-place.

   :param _pytest.main.Session session: the pytest session object
   :param _pytest.config.Config config: pytest config object
   :param List[_pytest.nodes.Item] items: list of item objects
   """

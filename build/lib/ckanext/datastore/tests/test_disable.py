import nose

import pylons.config as config
import ckan.plugins as p
import nose.tools as t


class TestDisable(object):

    @classmethod
    def setup_class(cls):
        with p.use_plugin('datastore') as the_plugin:
            legacy = the_plugin.legacy_mode

        if legacy:
            raise nose.SkipTest("SQL tests are not supported in legacy mode")

    @t.raises(KeyError)
    def test_disable_sql_search(self):
        config['ckan.datastore.sqlsearch.enabled'] = False
        with p.use_plugin('datastore') as the_plugin:
            print p.toolkit.get_action('datastore_search_sql')
        config['ckan.datastore.sqlsearch.enabled'] = True

    def test_enabled_sql_search(self):
        config['ckan.datastore.sqlsearch.enabled'] = True
        with p.use_plugin('datastore') as the_plugin:
            p.toolkit.get_action('datastore_search_sql')

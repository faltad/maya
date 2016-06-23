import ConfigParser 
import sys
import os

from collections import OrderedDict

DATABASE_SECTION = "database"
GITHUB_SECTION = "github"


class Config:
    config = ConfigParser.ConfigParser()

    @classmethod
    def init_config(cls, config_path):
        cls.config.read(config_path)

    @classmethod
    def get_sqlalchemy_url(cls):
        opts = OrderedDict((
            ("dialect", { "needed": True, "separator": ""}),
            ("driver", { "needed": False, "separator": "+"}),
            ("username", {"needed": True, "separator": "://"}),
            ("password", {"needed": True, "separator": ":"}),
            ("host", {"needed": True, "separator": "@"}),
            ("port", {"needed": False, "separator": ":"}),
            ("database", {"needed": True, "separator": "/"})
        ))

        url = ""

        for option, details in opts.iteritems():
            try:
                url += details["separator"] + cls.config.get(DATABASE_SECTION, option)
            except ConfigParser.NoOptionError:
                if details["needed"]:
                    print("'%s' option in the config file is needed to connect to the database." % (option))
                    sys.exit(-1)
                else:
                    pass
        return url

    @classmethod
    def get_deploy_key(cls):
        try:
            return cls.config.get(GITHUB_SECTION, 'deploy_key')
        except ConfigParser.NoSectionError:
            raise Exception('Github section missing from the config file')

Config.init_config(os.path.dirname(__file__) + "/../config/current.cfg")
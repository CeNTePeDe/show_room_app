import json

import factory


class JSONFactory(factory.DictFactory):
    @classmethod
    def _generate(cls, create, attrs):
        obj = super()._generate(create, attrs)
        return json.dumps(obj)

from django_elasticsearch_dsl import DocType, Index
from .models import Event

# Name of the Elasticsearch index
car = Index('events')
# See Elasticsearch Indices API reference for available settings
car.settings(
    number_of_shards=1,
    number_of_replicas=0
)


@car.doc_type
class EventDocument(DocType):
    class Meta:
        model = Event  # The model associate with this DocType

        # The fields of the model you want to be indexed in Elasticsearch
        fields = [
            'source',
            'dt',
            'user',
            'type',
            'data',
        ]

        # To ignore auto updating of Elasticsearch when a model is save
        # or delete
        # ignore_signals = True
        # Don't perform an index refresh after every update (overrides global setting)
        # auto_refresh = False

from blockfrost import BlockFrostApi, ApiError
from blockfrost.api.cardano.metadata import \
    MetadataLabelResponse, \
    MetadataLabelJsonResponse, \
    MetadataLabelCBORResponse

label = "1990"


def test_metadata_labels(requests_mock):
    api = BlockFrostApi()
    mock_data = [
        {
            "label": "1990",
            "cip10": None,
            "count": "1"
        },
        {
            "label": "1967",
            "cip10": "nut.link metadata oracles registry",
            "count": "3"
        },
        {
            "label": "1968",
            "cip10": "nut.link metadata oracles data points",
            "count": "16321"
        }
    ]
    requests_mock.get(f"{api.url}/metadata/txs/labels", json=mock_data)
    mock_object = [MetadataLabelResponse(**data) for data in mock_data]
    assert api.metadata_labels() == mock_object


def test_metadata_label_json(requests_mock):
    api = BlockFrostApi()
    mock_data = [
        {
            "tx_hash": "257d75c8ddb0434e9b63e29ebb6241add2b835a307aa33aedba2effe09ed4ec8",
            "json_metadata": {
                "ADAUSD": [
                    {
                        "value": "0.10409800535729975",
                        "source": "ergoOracles"
                    }
                ]
            }
        },
        {
            "tx_hash": "e865f2cc01ca7381cf98dcdc4de07a5e8674b8ea16e6a18e3ed60c186fde2b9c",
            "json_metadata": {
                "ADAUSD": [
                    {
                        "value": "0.15409850555139935",
                        "source": "ergoOracles"
                    }
                ]
            }
        },
        {
            "tx_hash": "4237501da3cfdd53ade91e8911e764bd0699d88fd43b12f44a1f459b89bc91be",
            "json_metadata": None
        }
    ]
    requests_mock.get(f"{api.url}/metadata/txs/labels/{label}", json=mock_data)
    mock_object = [MetadataLabelJsonResponse(**data) for data in mock_data]
    assert api.metadata_label_json(label=label) == mock_object


def test_metadata_label_cbor(requests_mock):
    api = BlockFrostApi()
    mock_data = [
        {
            "tx_hash": "257d75c8ddb0434e9b63e29ebb6241add2b835a307aa33aedba2effe09ed4ec8",
            "cbor_metadata": None
        },
        {
            "tx_hash": "e865f2cc01ca7381cf98dcdc4de07a5e8674b8ea16e6a18e3ed60c186fde2b9c",
            "cbor_metadata": None
        },
        {
            "tx_hash": "4237501da3cfdd53ade91e8911e764bd0699d88fd43b12f44a1f459b89bc91be",
            "cbor_metadata": "\\xa100a16b436f6d62696e6174696f6e8601010101010c"
        }
    ]
    requests_mock.get(f"{api.url}/metadata/txs/labels/{label}/cbor", json=mock_data)
    mock_object = [MetadataLabelCBORResponse(**data) for data in mock_data]
    assert api.metadata_label_cbor(label=label) == mock_object

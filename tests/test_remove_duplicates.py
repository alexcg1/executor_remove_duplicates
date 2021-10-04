import pytest
from jina import Document, DocumentArray, Flow
from .. import RemoveDuplicates

docs = DocumentArray(
    [
        Document(text="foo"),
        Document(text="bar"),
        Document(text="baz"),
        Document(text="qux"),
        Document(text="quux"),
        Document(text="quux"), # duplicate
        Document(text="quuz"),
        Document(text="corge"),
        Document(text="grault"),
        Document(text="grault"), # duplicate
        Document(text="grault"), # duplicate
        Document(text="grault"), # duplicate
    ]
)

flow = (
    Flow()
    .add(uses=RemoveDuplicates)
)

with flow:
    output = flow.index(inputs=docs, return_results=True)

output_docs = output[0].docs

assert len(output_docs) == 8

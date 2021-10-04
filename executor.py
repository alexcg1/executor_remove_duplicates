from jina import Executor, DocumentArray, requests, Document, Flow


class RemoveDuplicates(Executor):
    @requests
    def remove_duplicates(self, docs: DocumentArray, **kwargs):
        duplicates = []
        uniques_content = []
        for idx, doc in enumerate(docs):
            if doc.content not in uniques_content:
                uniques_content.append(doc.content)
            else:
                duplicates.append(idx)

        duplicates.reverse()
        for idx in duplicates:
            del docs[idx]

        return docs


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

flow = Flow().add(uses=RemoveDuplicates)

with flow:
    flow.index(inputs=docs)

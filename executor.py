from jina import Executor, DocumentArray, requests


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

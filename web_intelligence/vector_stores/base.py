from typing import Optional, Protocol, runtime_checkable


@runtime_checkable
class BaseVectorStore(Protocol):
    def add(
        self,
        vectors: list[list[float]],
        metadatas: list[dict],
        ids: list[str],
        documents: Optional[list[str]] = None,
    ) -> None: ...

    def search(
        self,
        query_vector: list[float],
        limit: int = 5,
        where_filter: Optional[dict] = None,
        min_score: float = 0.0,
    ) -> list[dict]: ...

    def list_documents(self) -> list[dict]: ...

    def get_document(self, doc_id: str) -> Optional[dict]: ...

    def delete_document(self, doc_id: str) -> bool: ...

    def delete_by_url(self, url: str) -> int: ...

    def count(self) -> int: ...

    def clear(self) -> None: ...

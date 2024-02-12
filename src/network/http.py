import random
import time
import requests
from requests.models import Response
from typing import Optional, Callable, Any, Dict


class Request:
    """
    A simple class for making HTTP requests with optional callback and meta information.

    Attributes:
        url (str): The URL for the HTTP request.
        method (Optional[str]): The HTTP method (GET by default).
        meta (Optional[Dict]): Additional metadata associated with the request.
        callback (Optional[Callable]): A callback function to handle the response.
        kwargs (Optional[Dict]): Additional keyword arguments to be passed to the request library.
    """

    def __init__(
            self,
            url: str,
            method: Optional[str] = None,
            meta: Optional[Dict] = None,
            callback: Optional[Callable] = None,
            **kwargs: Optional[Dict]
    ) -> None:
        self.url = url
        self.method = method or 'GET'
        self.meta = meta
        self.callback = callback
        self.kwargs = kwargs

    def _make_request(self) -> Response:
        """Makes the HTTP request using the request library."""

        response = requests.request(
            method=self.method,
            url=self.url,
            **self.kwargs
        )
        return response

    def __call__(self, *args, **kwargs) -> Any:
        """
        Calls the Request object, making the HTTP request and handling the response.
        Returns -> Any: The result of the callback function or the response object.
        """
        time.sleep(random.randint(1, 3))
        response = self._make_request()
        response.raise_for_status()
        if self.callback:
            response = self.callback(response)
        return response

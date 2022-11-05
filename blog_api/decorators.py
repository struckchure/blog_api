from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import APIException

from blog_api import exceptions


def handle_errors():
    """
    Decorator to handle errors
    """

    def handle_errors(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exceptions.Exception as error:
                error = error.__dict__() or error.__str__()
                return Response({"error": error}, status=status.HTTP_400_BAD_REQUEST)
            except APIException as error:
                return Response({"error": error}, status=status.HTTP_400_BAD_REQUEST)

        return wrapper

    return handle_errors

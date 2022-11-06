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
                code = getattr(error, "code", status.HTTP_400_BAD_REQUEST)

                return Response({"error": error}, status=code)
            except APIException as error:
                code = getattr(error, "code", status.HTTP_400_BAD_REQUEST)

                return Response({"error": error}, status=code)

        return wrapper

    return handle_errors

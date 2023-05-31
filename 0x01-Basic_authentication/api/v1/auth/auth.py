#!/usr/bin/env python3
"""
Script -> Definition of class Auth
"""
from flask import request
from typing import (
    List,
    TypeVar
)


class Auth:
    """
    Class: Manages the API authentication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines whether a given path require authentication 
        Args:
            - path(str): Url path to be checked
            - excluded_paths(List of str): List of paths that do not require
              authentication
        Return:
            - True if path is not in excluded_paths, else False
        """
        if path is None:
            return True
        elif excluded_paths is None or excluded_paths == []:
            return True
        elif path in excluded_paths:
            return False
        else:
            for k in excluded_paths:
                if k.startswith(path):
                    return False
                if path.startswith(k):
                    return False
                if k[-1] == "*":
                    if path.startswith(k[:-1]):
                        return False
        return True

    def authorization_header(self, request=None) -> str:
        """
        Returns the authorization header from a request object
        """
        if request is None:
            return None
        header = request.headers.get('Authorization')
        if header is None:
            return None
        return header

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Returns a User instance from infor from a request object
        """
        return None

#!/usr/bin/python3
"""File needed to create a package of the models(classes)"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()

#!/usr/bin/python3
"""File needed to create a package of the models(classes)"""
"""Creates unique file storage system for project"""
from models.engine.file_storage import FileStorage

file_storage = FileStorage()
file_storage.reload()

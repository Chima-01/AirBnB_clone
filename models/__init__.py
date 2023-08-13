#!/usr/bin/python3
"""File needed to create a package of the models(classes)"""
"""Creates unique file storage system for project"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()

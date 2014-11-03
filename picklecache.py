#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Use of the os and pickle modules
"""

import os
import pickle


class Pickles(object):
    """
    Creates a class for creating files using pickle
    """
    
    def __init__(self, file_path='datastore.pkl'):
        self.__file_path = file_path
        self.__file_object = None
        self.__data = {}

    def set(self, key, value):
        """
        Creates dictionary for the self.__data

        Args: {'key': 'value'}

        Ex: set({'Hello': 'world'})
        """
        self.__data = ({key, value})

    def get(self, key):
        """Displays the contents of self.__data

        Args: key entered in set() method

        Ex: get('Hello')
        >>> 'world'
        """
        if key not in self.__data:
            print "Error: No value found for key: '{}'".format(key)
        else:
            return self.__data[key]

    def delete(self, key):
        """Deletes an entry from self.__data

        Args: key of entry to be deleted

        Ex: delete('Goodbye')
        >>> "Error: No value found for key: 'Goodbye'"
            delete('Hello')
            self.__data
        >>>
        """
        if key not in self.__data:
            print "Error: No value found for key: '{}'".format(key)
        else:
            del self.__data[key]

    def open(self):
        """Opens a file, if it exists
        """
        if os.path.exists(self.__file_path):
            if os.path.getsize(self.__file_path) > 0:
                filehandler = open(self.__file_path, 'rb')
                self.__data = pickle.load(filehandler)
                filehandler.close()
            filehandler = open(self.__file_path, 'wb')

    def flush(self, reopen=True):
        """Sends data to a new file

        Args: reopen will keep the file open, unless changed to False

        ex: self.flush(False)
        """
        filehandler = open(self.__file_object)
        pickle.dump(self.__data, filehandler)
        fh.close()
        if reopen:
            self.open()


    def close(self):
        """Runs the flush() method
        """
        self.flush(self, True)

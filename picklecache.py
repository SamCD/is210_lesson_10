#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pickle

class Pickles(object):

    def __init__(self, file_path='datastore.pkl'):
        self.__file_path = file_path
        self.__file_object = None
        self.__data = {}

    def set(key, value):
        self.__data.update({key, value})

    def get(self, key):
        if key not in self.__data:
            print "Error: No value found for key: '{}'".format(key)
        else:
            return self.__data[key]

    def delete(self, key):
        if key not in self.__data:
            print "Error: No value found for key: '{}'".format(key)
        else:
            del self.__data[key]


    def open(self):
        if os.path.exists(self.__file_path):
            if os.path.getsize(self.__file_path) > 0:
                fh = open(self.__file_path, 'rb')
                self.__data = pickle.load(fh)
                fh.close()
            fh = open(self.__file_path, 'wb')


    def flush(self, reopen=True):
        fh = open(self.__file_object)
        pickle.dump(self.__data, fh)
        fh.close()
        if reopen:
            self.open()


    def close(self):
        flush(self, True)

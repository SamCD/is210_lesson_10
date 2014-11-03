#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""NYC Restaurant Inspection
    """

GRADING = {'A': 1.0, 'B': 0.9, 'C': 0.8, 'D': 0.7, 'F': 0.6}


def get_score_summary(filename):
    """Average scores for each borough

    Args: filename = name of the file to parse

    Ex: get_score_summary('inspection_results.csv')
    >>> {'BRONX': (156, 0.9762820512820514), 'BROOKLYN':
    (417, 0.9745803357314141), 'STATEN ISLAND': (46, 0.9804347826086955),
    'MANHATTAN': (748, 0.9771390374331531), 'QUEENS':
    (414, 0.9719806763285017)}
    """
    filehandler = open(filename, 'r')
    line = filehandler.readline()
    restos = {}
    scores = {}
    while line:
        if line[0] not in restos and line[10] is True and line[10] != 'P':
            restos[line[0]] = (line[10], line[1])
            line = filehandler.readline()
        filehandler.close()
    for i, j in restos.values():
        if j not in scores:
            scores[j] = (0, 0)
        scores[j] = [scores[j][0] + 1, scores[j][1] + GRADING.get(i)]
    for p in scores.values():
        p[1] = p[1] / p[0]
    for k, v in scores.iteritems():
        scores[k] = tuple(v)
    return scores

import json


def get_market_density(filename):
    """Distribution of greenmarkets by borough

    Args: filname = name of file to parse

    Ex: >>> get_market_density('green_markets.json')
    {u'STATEN ISLAND': 2, u'BRONX ': 1, u'BROOKLYN': 48, u'BRONX': 31,
    u'MANHATTAN': 39, u'QUEENS': 16}
    """
    filehandler = open(filename, 'r')
    newdict = json.load(filehandler)
    markets = {}
    for i in newdict.get('data'):
        if i[8].upper() not in markets:
            markets[i[8].upper()] = 0
        markets[i[8].upper()] = markets[i[8].upper()] + 1
    filehandler.close()
    return markets


def correlate_data(file1, file2, newfile):
    """Combines restaurant and greenmarket data into new metric

    Args: file1 should be inspections_results.csv, file2 should be
    green_markets.json, newfile is file to be written
    """
    food = get_score_summary(file1)
    green = get_market_density(file2)
    out = {}
    for k, p in food.iteritems():
        for j in green.values():
            out[k] = (v[1], j / v[0])
    filehandler = open(newfile, 'w')
    json.dump(out, filehandler)
    filehandler.close()

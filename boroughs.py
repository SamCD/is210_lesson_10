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

    unique = {}

    line = filehandler.readline()
    line = filehandler.readline()
    restos = {}
    scores = {}
    while line:
        lineparts = line.split(',')
        camis = cleanup(lineparts[0])
        boro = cleanup(lineparts[1])
        grade = cleanup(lineparts[10])
        if lineparts[10] and not lineparts[10].upper() == 'P':
            unique[camis] = (boro, grade)
        line = fhandler.readline()

    fhandler.close()

    boros = []
    for key, data in unique.iteritems():
        if data[0] not in boros:
            boros[data[0]] = [0, 0]
        boros[data[0]][0] += 1
        boros[data[0]][1] += GRADE[data[1]]

    return [{k: (v[0], v[1] / v[0])} for k, v in boros.iteritems()]


def cleanup(data):
    """Cleanup"""
    return data.strip().upper()

import json


def get_market_density(filename):
    """Distribution of greenmarkets by borough

    Args: filname = name of file to parse

    Ex: >>> get_market_density('green_markets.json')
    {u'STATEN ISLAND': 2, u'BRONX ': 1, u'BROOKLYN': 48, u'BRONX': 31,
    u'MANHATTAN': 39, u'QUEENS': 16}
    """
    filehandler = open(filename, 'r')
    data = json.load(filehandler)['data']
    fhandler.close()

    boros = {}
    for row in data:
        boro = cleanup(row[8])
        if boro not in boros:
            boros[boro] = 0
        boros[boro] += 1

    return boros


def correlate_data(scoresfile, marketfile, outfile):
    """Combines restaurant and greenmarket data into new metric

    Args: file1 should be inspections_results.csv, file2 should be
    green_markets.json, newfile is file to be written
    """
    scores = get_score_summary(scoresfile)
    markets = get_market_density(marketfile)
    correlated = {}

    for boro, score in scores.iteritems():
        density = float(markets[boro]) / score[0]
        correlation[boro] = (score[1], density)

    fhandler = open(outfile, 'w')
    json.dump(correlated, fhandler)
    fhandler.close()

    return correlated

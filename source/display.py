#! /usr/bin/env python

import xml.etree.ElementTree as et

class Display(object):
    def __init__(self):
        self.__items = et.Element('items')

    def __repr__(self):
        return et.tostring(self.__items).decode()

    def __str__(self):
        return et.tostring(self.__items).decode()

    def add_item(self, title, subtitle="", arg="", valid="yes", autocomplete="", icon="icon.png"):
        item = et.SubElement(self.__items, 
                'item', 
                uid = str(len(self.__items)),
                arg=arg, 
                valid=valid, 
                autocomplete=autocomplete)
        _title = et.SubElement(item, 'title')
        _title.text = title
        _sub = et.SubElement(item, 'subtitle')
        _sub.text = subtitle
        _icon = et.SubElement(item, 'icon')
        _icon.text = icon


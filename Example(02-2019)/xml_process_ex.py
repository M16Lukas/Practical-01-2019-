"""
example by "Do it! 점프 투 파이썬"
edit : Pycharm
date : 05-02-2019
name : XML process
"""

from xml.etree.ElementTree import Element, SubElement, ElementTree

blog = Element("blog")
blog.attrib['date'] = "20151231"

SubElement(blog, "subject").text = "Why python"
SubElement(blog, "author").text = "Eric"
SubElement(blog, "content").text = "Life is too short You need Python"

ElementTree(blog).write("blog.xml")

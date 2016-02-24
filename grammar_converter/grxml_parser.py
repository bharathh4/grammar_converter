import os
import xml.etree.ElementTree as ET
DATA_DIR = 'C:\Users\TheatroIT\Documents\Scripts2\grammar_converter\sample_grammars'

def one_of_handler(element):
    print 'In one-of-handler'
    vocabs = [child.text for child in element]
    return str(vocabs)

    
def tag_handler(element):
    print '\nIn tag handler'
    
    if 'rules.latest()' in element.text:
        str = (element.text.
               replace('rules.latest()', '').
               replace('+', '').
               replace('out=', '').
               replace('"', ''))
                
        print 'Expecting a result from rule ref from subcomponent before me. Might be a persons_all.grxml'
        print ('''The result will be attached in the following way. %s john muller.
Where john muller is a result from a subcomponent before\n''') % (str)

    
def rule_ref_handler(element):
    print 'In ruleref handler'
    _, filename = element.attrib.items()[0]
    with open(os.path.join('sample_grammars', filename), 'r') as f:
        xml_string = f.read()
        print get_root_rule(xml_string)
        root = ET.fromstring(xml_string)
        base = "{" + (root.attrib['{http://www.w3.org/2001/XMLSchema-instance}schemaLocation']).split(' ')[0] + "}"
        for child in root:
            # visualization in persons
            #print " -> ".join([subchild.tag.replace(base, '') for subchild in child])
            
            # get names
            names_fullnames = []
            for subchild in child:
                if subchild.tag.replace(base, '') == 'item':
                    # This is not generic of handing repeats. Come back later. Must change.
                    names_fullnames.append(' '.join([item.text for item in subchild]))
            return fullnames
    
    
# a dict that has functions as its values. The dict will return element handler functions
HANDLER_FUNCTION = {'one-of': one_of_handler, 'ruleref': rule_ref_handler, 'tag': tag_handler}
    
def get_ruleids(xml_string, tag):
    root = ET.fromstring(xml_string)
    print root.attrib
    attrib = ''
    all_id = []
    for child in root:
        if tag in child.tag:
            attrib = child.text
            all_id.append(child.attrib)
    return all_id
    
    
def get_all_ref_rules_from_root_rule(xml_string):
    root_rule = get_root_rule(xml_string)
    root = ET.fromstring(xml_string)
    base = "{" + (root.attrib['{http://www.w3.org/2001/XMLSchema-instance}schemaLocation']).split(' ')[0] + "}"
    ref_rules = []
    for child in root:
        attrib = child.attrib
        key, val = attrib.items()[0]
        # At theatro root rule is 'command'
        if val == root_rule:
            for item in child:
                if base + 'one-of' == item.tag: 
                    for subitem in item:
                        for i in subitem:
                            ref_rules.append(i.attrib)
    refs = []
    for dic in ref_rules:
        for k, v in dic.items():
            refs.append(v.replace('#', ''))     
    return refs
       
       
def get_root_rule(xml_string):
    root = ET.fromstring(xml_string)
    base = "{" + (root.attrib['{http://www.w3.org/2001/XMLSchema-instance}schemaLocation']).split(' ')[0] + "}"
    ref_rules = []
    for k, v in (root.attrib).items():
        if k == 'root':
            return v

def get_element_with_name(xml_string, attrib):
    root_rule = get_root_rule(xml_string)
    root = ET.fromstring(xml_string)
    base = "{" + (root.attrib['{http://www.w3.org/2001/XMLSchema-instance}schemaLocation']).split(' ')[0] + "}"
    for child in root:
        if child.attrib == {'id' : attrib}:
            return child
            
def number_of_elements(xml_string, attrib):
    root = get_element_with_name(xml_string, attrib)
    n = len([child for child in root])
    print 'You will have to make sense of %d sub components in this rule' % (n)
    return n
    
def visualize_rule_behaviour(xml_string, attrib):

    root_rule = get_root_rule(xml_string)
    root = ET.fromstring(xml_string)
    base = "{" + (root.attrib['{http://www.w3.org/2001/XMLSchema-instance}schemaLocation']).split(' ')[0] + "}"
    new_root = get_element_with_name(xml_string, attrib)
    return ' -> '.join([child.tag.replace(base, '') for child in new_root])
    
def tester(xml_string, attrib):

    root_rule = get_root_rule(xml_string)
    root = ET.fromstring(xml_string)
    base = "{" + (root.attrib['{http://www.w3.org/2001/XMLSchema-instance}schemaLocation']).split(' ')[0] + "}"
    new_root = get_element_with_name(xml_string, attrib)
    for child in new_root:
        temp = child.tag.replace(base, '') # gets ruleref from {http://www.w3.org/2001/06/grammar}ruleref
        handler_function = HANDLER_FUNCTION[temp]
        print handler_function(child)

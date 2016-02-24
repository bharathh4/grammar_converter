from grammar_converter import util
from grammar_converter import grxml_parser as gp

if __name__ == '__main__':

    #util.print_available_grams()
    
    
    
    '''
    # Finds all sub components in a grammar sub rule and prints the count.
    # For instance 'hello' has three components one-of -> ruleref -> tag. So the value 3 is returned.
    all_rule_refs = gp.get_all_ref_rules_from_root_rule(xml_string)
    for item in all_rule_refs:
        print gp.number_of_elements(xml_string, item)
    '''
    
    '''
    # Helps visualize rule behaviour. For example for 'hello' rule, we would have something like  one-of -> ruleref -> tag
    all_rule_refs = gp.get_all_ref_rules_from_root_rule(xml_string)
    for item in all_rule_refs:
        print item + '  :   ' + gp.visualize_rule_behaviour(xml_string, item)
    '''
    with open('sample_grammars\command.grxml', 'r') as f:
        xml_string = f.read()
    gp.tester(xml_string, 'hello')
    
    
    
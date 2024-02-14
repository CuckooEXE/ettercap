
"""
NetworkFilterCparse - Parser for NetworkFilterC
"""


"""
Imported Libraries

NetworkFilterClex - NetworkFilterC Lexer
ply.yacc - PLY yacc Utilities
"""
import NetworkFilterClex
import ply.yacc as yacc


tokens = NetworkFilterClex.tokens
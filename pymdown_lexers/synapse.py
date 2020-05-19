"""Pygments lexer for Synapse X docs."""
from pygments.lexer import RegexLexer, bygroups
from pygments.token import *

__all__ = ("SynapseLexer",)


class SynapseLexer(RegexLexer):

    name = 'Synapse Markup'
    aliases = ['syn']
    filenames = ['*.syn']
    mimetypes = ['text/syn']

    tokens = {
        'root': [
            #(r'\s+', Text),
            (r'(<)(.*?)(>)(.*?)(\()(<)(.*?)(>)(.*?)(\))', bygroups(Operator, Keyword, Operator, String, Operator, Operator, Keyword, Operator, Text, Operator))
            #(r'\> (.*?)\\(', String)
            #(r'[<>()]', Operator),
            #(r'<[.*?]>', Keyword)
        ]
    }
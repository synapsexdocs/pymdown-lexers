"""Pygments lexer for Synapse X docs."""
from pygments.lexer import RegexLexer
from pygments.token import *

__all__ = ("SynapseLexer",)


class SynapseLexer(RegexLexer):

    name = 'Synapse Markup'
    aliases = ['syn']
    filenames = ['*.syn']
    mimetypes = ['text/syn']

    tokens = {
        'root': [
            (r'\s+', Text),
            (r'\> (.*?)\(', String),
            #(r'[<>()]', Operator),
            (r'<(.*?)>', Keyword)
        ]
    }

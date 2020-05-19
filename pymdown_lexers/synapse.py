"""Pygments lexer for Synapse X docs."""
from pygments.lexer import RegexLexer, bygroups
from pygments import token

__all__ = ("SynapseLexer",)


class SynapseLexer(RegexLexer):

    name = 'Synapse Markup'
    aliases = ['syn']
    filenames = ['*.syn']
    mimetypes = ['text/syn']

    tokens = {
        'root': [
            (r'(<)([\w\s,]+)(>)', bygroups(token.Operator, token.Keyword, token.Operator)),
            (r'\s+', token.Text),
            (r',', token.Operator,  '#push'),
            (r'(\w*?)(\)|,)', bygroups(token.Text, token.Operator)),
            (r'(\w*?)(\()', bygroups(token.String, token.Operator)),
            #(r'(\w+)(,)', bygroups(token.Text, token.Operator))
            #Edge case
            #(r'(<)(\w+)(,)', bygroups(token.Operator, token.Keyword, token.Operator)),
            #(r'(,\s)(\w+)(,)', bygroups(token.Operator, token.Keyword, token.Operator)),
            #(r'(\w+)(>)', bygroups(token.Keyword, token.Operator)),
        ]
    }
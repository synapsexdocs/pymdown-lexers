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
            (r'\s+', token.Text),
            (r'(\w*?)([\),])', bygroups(token.Text, token.Operator)),
            (r'(\w*?)(\()', bygroups(token.String, token.Operator)),
            (r'(<)(\w+)(,)', bygroups(token.Operator, token.Keyword, token.Operator)),
            (r'(,)\s(\w+)(.{1})', bygroups(token.Operator, token.Keyword, token.Operator)),
            (r'(,)(\w+)(>)', bygroups(token.Operator, token.Keyword, token.Operator)),
            (r'(<)(\w+)(>)', bygroups(token.Operator, token.Keyword, token.Operator))
        ]
    }
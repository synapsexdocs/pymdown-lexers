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
            (r'[,\[\]\)]', token.Operator),
            (r'(\w+)(\)|,)', bygroups(token.Text, token.Operator)),
            # Very bad way of doing things
            (r'(\w+)(\()', bygroups(token.String, token.Operator)),
            (r'(\w+)(.)(\w+)(\()', bygroups(token.String, token.Operator, token.String, token.Operator)),
            (r'(\w+)(.)(\w+)(.)(\w+)(\()', bygroups(token.String, token.Operator, token.String, token.Operator, token.String, token.Operator)),
            (r'(\w+)(.)(\w+)(.)(\w+)(.)(\w+)(\()', bygroups(token.String, token.Operator, token.String, token.Operator, token.String, token.Operator, token.String, token.Operator)),
            # Datatype highlighting
            (r'(<)([\w\s\?\.,]+)(>)', bygroups(token.Operator, token.Keyword, token.Operator)),
            # Edge cases
            (r'^(\w+)(:)', bygroups(token.Keyword, token.Operator)),
            (r'(\w+)(\]\))', bygroups(token.Text, token.Operator)),
            (r'^(\w+)(.)(\w+)$', bygroups(token.Keyword, token.Operator, token.String)),
            (r'(\w+)(.)(\w+)(.)(\*)', bygroups(token.String, token.Operator, token.String, token.Operator, token.Keyword)),
        ]
    }
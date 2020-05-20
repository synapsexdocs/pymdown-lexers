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
            (r'[\.,()<>]', token.Operator),
            (r'(\w+)(?::)', token.Keyword),
            (r'(\w+)(?:\)|,)', token.Text),
            # Very bad way of doing things
            (r'([\w]*?)(?:\()', token.String),
            (r'([\w]*?)(?:.)([\w]*?)(?:\()', bygroups(token.String, token.String)),
            (r'([\w]*?)(?:.)([\w]*?)(?:.)([\w]*?)(?:\()', bygroups(token.String, token.String, token.String)),
            #Datatype highlighting
            (r'(\w+)(?:,)', token.Keyword),
            (r'(\w+)(?:>)', token.Keyword),
        ]
    }
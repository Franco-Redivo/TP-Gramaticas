# Generated from Residuos.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,17,124,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,1,0,4,0,26,8,0,11,
        0,12,0,27,1,0,5,0,31,8,0,10,0,12,0,34,9,0,1,0,3,0,37,8,0,1,0,1,0,
        1,1,1,1,1,1,1,1,3,1,45,8,1,1,1,1,1,1,1,1,2,1,2,1,2,5,2,53,8,2,10,
        2,12,2,56,9,2,1,3,1,3,5,3,60,8,3,10,3,12,3,63,9,3,1,3,1,3,1,4,1,
        4,1,4,3,4,70,8,4,1,5,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,
        3,6,84,8,6,1,7,1,7,1,7,1,7,1,8,1,8,1,8,3,8,93,8,8,1,8,1,8,1,9,1,
        9,1,9,5,9,100,8,9,10,9,12,9,103,9,9,1,10,1,10,1,10,1,10,1,11,1,11,
        1,11,1,11,1,11,3,11,114,8,11,1,11,1,11,1,11,5,11,119,8,11,10,11,
        12,11,122,9,11,1,11,0,1,22,12,0,2,4,6,8,10,12,14,16,18,20,22,0,0,
        126,0,25,1,0,0,0,2,40,1,0,0,0,4,49,1,0,0,0,6,57,1,0,0,0,8,69,1,0,
        0,0,10,71,1,0,0,0,12,76,1,0,0,0,14,85,1,0,0,0,16,89,1,0,0,0,18,96,
        1,0,0,0,20,104,1,0,0,0,22,113,1,0,0,0,24,26,3,2,1,0,25,24,1,0,0,
        0,26,27,1,0,0,0,27,25,1,0,0,0,27,28,1,0,0,0,28,36,1,0,0,0,29,31,
        3,16,8,0,30,29,1,0,0,0,31,34,1,0,0,0,32,30,1,0,0,0,32,33,1,0,0,0,
        33,35,1,0,0,0,34,32,1,0,0,0,35,37,5,1,0,0,36,32,1,0,0,0,36,37,1,
        0,0,0,37,38,1,0,0,0,38,39,5,0,0,1,39,1,1,0,0,0,40,41,5,2,0,0,41,
        42,5,14,0,0,42,44,5,3,0,0,43,45,3,4,2,0,44,43,1,0,0,0,44,45,1,0,
        0,0,45,46,1,0,0,0,46,47,5,4,0,0,47,48,3,6,3,0,48,3,1,0,0,0,49,54,
        5,14,0,0,50,51,5,5,0,0,51,53,5,14,0,0,52,50,1,0,0,0,53,56,1,0,0,
        0,54,52,1,0,0,0,54,55,1,0,0,0,55,5,1,0,0,0,56,54,1,0,0,0,57,61,5,
        6,0,0,58,60,3,8,4,0,59,58,1,0,0,0,60,63,1,0,0,0,61,59,1,0,0,0,61,
        62,1,0,0,0,62,64,1,0,0,0,63,61,1,0,0,0,64,65,5,7,0,0,65,7,1,0,0,
        0,66,70,3,10,5,0,67,70,3,12,6,0,68,70,3,14,7,0,69,66,1,0,0,0,69,
        67,1,0,0,0,69,68,1,0,0,0,70,9,1,0,0,0,71,72,5,14,0,0,72,73,5,8,0,
        0,73,74,3,22,11,0,74,75,5,1,0,0,75,11,1,0,0,0,76,77,5,9,0,0,77,78,
        5,3,0,0,78,79,3,20,10,0,79,80,5,4,0,0,80,83,3,6,3,0,81,82,5,10,0,
        0,82,84,3,6,3,0,83,81,1,0,0,0,83,84,1,0,0,0,84,13,1,0,0,0,85,86,
        5,11,0,0,86,87,3,22,11,0,87,88,5,1,0,0,88,15,1,0,0,0,89,90,5,14,
        0,0,90,92,5,3,0,0,91,93,3,18,9,0,92,91,1,0,0,0,92,93,1,0,0,0,93,
        94,1,0,0,0,94,95,5,4,0,0,95,17,1,0,0,0,96,101,3,22,11,0,97,98,5,
        5,0,0,98,100,3,22,11,0,99,97,1,0,0,0,100,103,1,0,0,0,101,99,1,0,
        0,0,101,102,1,0,0,0,102,19,1,0,0,0,103,101,1,0,0,0,104,105,3,22,
        11,0,105,106,5,13,0,0,106,107,3,22,11,0,107,21,1,0,0,0,108,109,6,
        11,-1,0,109,114,3,16,8,0,110,114,5,15,0,0,111,114,5,16,0,0,112,114,
        5,14,0,0,113,108,1,0,0,0,113,110,1,0,0,0,113,111,1,0,0,0,113,112,
        1,0,0,0,114,120,1,0,0,0,115,116,10,5,0,0,116,117,5,12,0,0,117,119,
        3,22,11,6,118,115,1,0,0,0,119,122,1,0,0,0,120,118,1,0,0,0,120,121,
        1,0,0,0,121,23,1,0,0,0,122,120,1,0,0,0,12,27,32,36,44,54,61,69,83,
        92,101,113,120
    ]

class ResiduosParser ( Parser ):

    grammarFileName = "Residuos.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'function'", "'('", "')'", "','", 
                     "'{'", "'}'", "'='", "'if'", "'else'", "'return'", 
                     "'+'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "COMPARISON_OPERATOR", "VARIABLE", "STRING", 
                      "NUMBER", "WS" ]

    RULE_program = 0
    RULE_function = 1
    RULE_parameterList = 2
    RULE_block = 3
    RULE_statement = 4
    RULE_assignStatement = 5
    RULE_ifStatement = 6
    RULE_returnStatement = 7
    RULE_functionCall = 8
    RULE_argumentList = 9
    RULE_booleanExpression = 10
    RULE_expression = 11

    ruleNames =  [ "program", "function", "parameterList", "block", "statement", 
                   "assignStatement", "ifStatement", "returnStatement", 
                   "functionCall", "argumentList", "booleanExpression", 
                   "expression" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    COMPARISON_OPERATOR=13
    VARIABLE=14
    STRING=15
    NUMBER=16
    WS=17

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ResiduosParser.EOF, 0)

        def function(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ResiduosParser.FunctionContext)
            else:
                return self.getTypedRuleContext(ResiduosParser.FunctionContext,i)


        def functionCall(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ResiduosParser.FunctionCallContext)
            else:
                return self.getTypedRuleContext(ResiduosParser.FunctionCallContext,i)


        def getRuleIndex(self):
            return ResiduosParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = ResiduosParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 24
                self.function()
                self.state = 27 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==2):
                    break

            self.state = 36
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1 or _la==14:
                self.state = 32
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==14:
                    self.state = 29
                    self.functionCall()
                    self.state = 34
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 35
                self.match(ResiduosParser.T__0)


            self.state = 38
            self.match(ResiduosParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(ResiduosParser.VARIABLE, 0)

        def block(self):
            return self.getTypedRuleContext(ResiduosParser.BlockContext,0)


        def parameterList(self):
            return self.getTypedRuleContext(ResiduosParser.ParameterListContext,0)


        def getRuleIndex(self):
            return ResiduosParser.RULE_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction" ):
                listener.enterFunction(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction" ):
                listener.exitFunction(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction" ):
                return visitor.visitFunction(self)
            else:
                return visitor.visitChildren(self)




    def function(self):

        localctx = ResiduosParser.FunctionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self.match(ResiduosParser.T__1)
            self.state = 41
            self.match(ResiduosParser.VARIABLE)
            self.state = 42
            self.match(ResiduosParser.T__2)
            self.state = 44
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 43
                self.parameterList()


            self.state = 46
            self.match(ResiduosParser.T__3)
            self.state = 47
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self, i:int=None):
            if i is None:
                return self.getTokens(ResiduosParser.VARIABLE)
            else:
                return self.getToken(ResiduosParser.VARIABLE, i)

        def getRuleIndex(self):
            return ResiduosParser.RULE_parameterList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameterList" ):
                listener.enterParameterList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameterList" ):
                listener.exitParameterList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameterList" ):
                return visitor.visitParameterList(self)
            else:
                return visitor.visitChildren(self)




    def parameterList(self):

        localctx = ResiduosParser.ParameterListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_parameterList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(ResiduosParser.VARIABLE)
            self.state = 54
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 50
                self.match(ResiduosParser.T__4)
                self.state = 51
                self.match(ResiduosParser.VARIABLE)
                self.state = 56
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ResiduosParser.StatementContext)
            else:
                return self.getTypedRuleContext(ResiduosParser.StatementContext,i)


        def getRuleIndex(self):
            return ResiduosParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = ResiduosParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 57
            self.match(ResiduosParser.T__5)
            self.state = 61
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 18944) != 0):
                self.state = 58
                self.statement()
                self.state = 63
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 64
            self.match(ResiduosParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignStatement(self):
            return self.getTypedRuleContext(ResiduosParser.AssignStatementContext,0)


        def ifStatement(self):
            return self.getTypedRuleContext(ResiduosParser.IfStatementContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(ResiduosParser.ReturnStatementContext,0)


        def getRuleIndex(self):
            return ResiduosParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = ResiduosParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_statement)
        try:
            self.state = 69
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [14]:
                self.enterOuterAlt(localctx, 1)
                self.state = 66
                self.assignStatement()
                pass
            elif token in [9]:
                self.enterOuterAlt(localctx, 2)
                self.state = 67
                self.ifStatement()
                pass
            elif token in [11]:
                self.enterOuterAlt(localctx, 3)
                self.state = 68
                self.returnStatement()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(ResiduosParser.VARIABLE, 0)

        def expression(self):
            return self.getTypedRuleContext(ResiduosParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ResiduosParser.RULE_assignStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignStatement" ):
                listener.enterAssignStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignStatement" ):
                listener.exitAssignStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignStatement" ):
                return visitor.visitAssignStatement(self)
            else:
                return visitor.visitChildren(self)




    def assignStatement(self):

        localctx = ResiduosParser.AssignStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_assignStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(ResiduosParser.VARIABLE)
            self.state = 72
            self.match(ResiduosParser.T__7)
            self.state = 73
            self.expression(0)
            self.state = 74
            self.match(ResiduosParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def booleanExpression(self):
            return self.getTypedRuleContext(ResiduosParser.BooleanExpressionContext,0)


        def block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ResiduosParser.BlockContext)
            else:
                return self.getTypedRuleContext(ResiduosParser.BlockContext,i)


        def getRuleIndex(self):
            return ResiduosParser.RULE_ifStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStatement" ):
                listener.enterIfStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStatement" ):
                listener.exitIfStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStatement" ):
                return visitor.visitIfStatement(self)
            else:
                return visitor.visitChildren(self)




    def ifStatement(self):

        localctx = ResiduosParser.IfStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_ifStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(ResiduosParser.T__8)
            self.state = 77
            self.match(ResiduosParser.T__2)
            self.state = 78
            self.booleanExpression()
            self.state = 79
            self.match(ResiduosParser.T__3)
            self.state = 80
            self.block()
            self.state = 83
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==10:
                self.state = 81
                self.match(ResiduosParser.T__9)
                self.state = 82
                self.block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(ResiduosParser.ExpressionContext,0)


        def getRuleIndex(self):
            return ResiduosParser.RULE_returnStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStatement" ):
                listener.enterReturnStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStatement" ):
                listener.exitReturnStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStatement" ):
                return visitor.visitReturnStatement(self)
            else:
                return visitor.visitChildren(self)




    def returnStatement(self):

        localctx = ResiduosParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_returnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(ResiduosParser.T__10)
            self.state = 86
            self.expression(0)
            self.state = 87
            self.match(ResiduosParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(ResiduosParser.VARIABLE, 0)

        def argumentList(self):
            return self.getTypedRuleContext(ResiduosParser.ArgumentListContext,0)


        def getRuleIndex(self):
            return ResiduosParser.RULE_functionCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCall" ):
                return visitor.visitFunctionCall(self)
            else:
                return visitor.visitChildren(self)




    def functionCall(self):

        localctx = ResiduosParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(ResiduosParser.VARIABLE)
            self.state = 90
            self.match(ResiduosParser.T__2)
            self.state = 92
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 114688) != 0):
                self.state = 91
                self.argumentList()


            self.state = 94
            self.match(ResiduosParser.T__3)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ResiduosParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ResiduosParser.ExpressionContext,i)


        def getRuleIndex(self):
            return ResiduosParser.RULE_argumentList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArgumentList" ):
                listener.enterArgumentList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArgumentList" ):
                listener.exitArgumentList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArgumentList" ):
                return visitor.visitArgumentList(self)
            else:
                return visitor.visitChildren(self)




    def argumentList(self):

        localctx = ResiduosParser.ArgumentListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_argumentList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.expression(0)
            self.state = 101
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==5:
                self.state = 97
                self.match(ResiduosParser.T__4)
                self.state = 98
                self.expression(0)
                self.state = 103
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BooleanExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ResiduosParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ResiduosParser.ExpressionContext,i)


        def COMPARISON_OPERATOR(self):
            return self.getToken(ResiduosParser.COMPARISON_OPERATOR, 0)

        def getRuleIndex(self):
            return ResiduosParser.RULE_booleanExpression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBooleanExpression" ):
                listener.enterBooleanExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBooleanExpression" ):
                listener.exitBooleanExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBooleanExpression" ):
                return visitor.visitBooleanExpression(self)
            else:
                return visitor.visitChildren(self)




    def booleanExpression(self):

        localctx = ResiduosParser.BooleanExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_booleanExpression)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.expression(0)
            self.state = 105
            self.match(ResiduosParser.COMPARISON_OPERATOR)
            self.state = 106
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionCall(self):
            return self.getTypedRuleContext(ResiduosParser.FunctionCallContext,0)


        def STRING(self):
            return self.getToken(ResiduosParser.STRING, 0)

        def NUMBER(self):
            return self.getToken(ResiduosParser.NUMBER, 0)

        def VARIABLE(self):
            return self.getToken(ResiduosParser.VARIABLE, 0)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ResiduosParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(ResiduosParser.ExpressionContext,i)


        def getRuleIndex(self):
            return ResiduosParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ResiduosParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 109
                self.functionCall()
                pass

            elif la_ == 2:
                self.state = 110
                self.match(ResiduosParser.STRING)
                pass

            elif la_ == 3:
                self.state = 111
                self.match(ResiduosParser.NUMBER)
                pass

            elif la_ == 4:
                self.state = 112
                self.match(ResiduosParser.VARIABLE)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 120
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = ResiduosParser.ExpressionContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                    self.state = 115
                    if not self.precpred(self._ctx, 5):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                    self.state = 116
                    self.match(ResiduosParser.T__11)
                    self.state = 117
                    self.expression(6) 
                self.state = 122
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[11] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         





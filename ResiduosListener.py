# Generated from Residuos.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ResiduosParser import ResiduosParser
else:
    from ResiduosParser import ResiduosParser

# This class defines a complete listener for a parse tree produced by ResiduosParser.
class ResiduosListener(ParseTreeListener):

    # Enter a parse tree produced by ResiduosParser#program.
    def enterProgram(self, ctx:ResiduosParser.ProgramContext):
        pass

    # Exit a parse tree produced by ResiduosParser#program.
    def exitProgram(self, ctx:ResiduosParser.ProgramContext):
        pass


    # Enter a parse tree produced by ResiduosParser#function.
    def enterFunction(self, ctx:ResiduosParser.FunctionContext):
        pass

    # Exit a parse tree produced by ResiduosParser#function.
    def exitFunction(self, ctx:ResiduosParser.FunctionContext):
        pass


    # Enter a parse tree produced by ResiduosParser#parameterList.
    def enterParameterList(self, ctx:ResiduosParser.ParameterListContext):
        pass

    # Exit a parse tree produced by ResiduosParser#parameterList.
    def exitParameterList(self, ctx:ResiduosParser.ParameterListContext):
        pass


    # Enter a parse tree produced by ResiduosParser#block.
    def enterBlock(self, ctx:ResiduosParser.BlockContext):
        pass

    # Exit a parse tree produced by ResiduosParser#block.
    def exitBlock(self, ctx:ResiduosParser.BlockContext):
        pass


    # Enter a parse tree produced by ResiduosParser#statement.
    def enterStatement(self, ctx:ResiduosParser.StatementContext):
        pass

    # Exit a parse tree produced by ResiduosParser#statement.
    def exitStatement(self, ctx:ResiduosParser.StatementContext):
        pass


    # Enter a parse tree produced by ResiduosParser#assignStatement.
    def enterAssignStatement(self, ctx:ResiduosParser.AssignStatementContext):
        pass

    # Exit a parse tree produced by ResiduosParser#assignStatement.
    def exitAssignStatement(self, ctx:ResiduosParser.AssignStatementContext):
        pass


    # Enter a parse tree produced by ResiduosParser#ifStatement.
    def enterIfStatement(self, ctx:ResiduosParser.IfStatementContext):
        pass

    # Exit a parse tree produced by ResiduosParser#ifStatement.
    def exitIfStatement(self, ctx:ResiduosParser.IfStatementContext):
        pass


    # Enter a parse tree produced by ResiduosParser#functionCall.
    def enterFunctionCall(self, ctx:ResiduosParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by ResiduosParser#functionCall.
    def exitFunctionCall(self, ctx:ResiduosParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by ResiduosParser#argumentList.
    def enterArgumentList(self, ctx:ResiduosParser.ArgumentListContext):
        pass

    # Exit a parse tree produced by ResiduosParser#argumentList.
    def exitArgumentList(self, ctx:ResiduosParser.ArgumentListContext):
        pass


    # Enter a parse tree produced by ResiduosParser#returnStatement.
    def enterReturnStatement(self, ctx:ResiduosParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by ResiduosParser#returnStatement.
    def exitReturnStatement(self, ctx:ResiduosParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by ResiduosParser#booleanExpression.
    def enterBooleanExpression(self, ctx:ResiduosParser.BooleanExpressionContext):
        pass

    # Exit a parse tree produced by ResiduosParser#booleanExpression.
    def exitBooleanExpression(self, ctx:ResiduosParser.BooleanExpressionContext):
        pass


    # Enter a parse tree produced by ResiduosParser#expression.
    def enterExpression(self, ctx:ResiduosParser.ExpressionContext):
        pass

    # Exit a parse tree produced by ResiduosParser#expression.
    def exitExpression(self, ctx:ResiduosParser.ExpressionContext):
        pass



del ResiduosParser
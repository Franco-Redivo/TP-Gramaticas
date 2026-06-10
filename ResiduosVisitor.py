# Generated from Residuos.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ResiduosParser import ResiduosParser
else:
    from ResiduosParser import ResiduosParser

# This class defines a complete generic visitor for a parse tree produced by ResiduosParser.

class ResiduosVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ResiduosParser#program.
    def visitProgram(self, ctx:ResiduosParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResiduosParser#function.
    def visitFunction(self, ctx:ResiduosParser.FunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResiduosParser#parameterList.
    def visitParameterList(self, ctx:ResiduosParser.ParameterListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResiduosParser#block.
    def visitBlock(self, ctx:ResiduosParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResiduosParser#statement.
    def visitStatement(self, ctx:ResiduosParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResiduosParser#assignStatement.
    def visitAssignStatement(self, ctx:ResiduosParser.AssignStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResiduosParser#ifStatement.
    def visitIfStatement(self, ctx:ResiduosParser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResiduosParser#functionCall.
    def visitFunctionCall(self, ctx:ResiduosParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResiduosParser#argumentList.
    def visitArgumentList(self, ctx:ResiduosParser.ArgumentListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResiduosParser#returnStatement.
    def visitReturnStatement(self, ctx:ResiduosParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResiduosParser#booleanExpression.
    def visitBooleanExpression(self, ctx:ResiduosParser.BooleanExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ResiduosParser#expression.
    def visitExpression(self, ctx:ResiduosParser.ExpressionContext):
        return self.visitChildren(ctx)



del ResiduosParser
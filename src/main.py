import tables
import savetable

print("Welcome to tables, the command line truth table generator\n=========================================================")


nameList = tables.getVarName()
statement = tables.getStatement()
flag = tables.checkStatement(nameList, statement)

while not flag:
    statement = tables.getStatement()
    flag = tables.checkStatement(nameList, statement)

table = tables.getTable(nameList, statement)
display = tables.formatTable(nameList, statement, table)

print(display)

savetable.ask(display)
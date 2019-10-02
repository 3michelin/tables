import tables
import savetable

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
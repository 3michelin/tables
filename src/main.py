import tables
import savetable

nameList = tables.getVarName()
statement = tables.getStatement()
table = tables.getTable(nameList, statement)
display = tables.formatTable(nameList, statement, table)

print(display)

savetable.ask(display)
import AST
from AST import addToClass
from functools import reduce

variables = {}
css = []

functions = {
    'title' : lambda content: "<h1>" + str(content) + "</h1>",
    'subTitle' : lambda content: "<h3>" + str(content) + "</h3>",
    'paragraph' : lambda content: "<p>" + str(content) + "</p>",
    'addListRow' : lambda content : "<li>" + str(content) + "</li>",
    'addTableHeader' : lambda content : "<th>" + str(content) + "</th>",
    'addTableElement' : lambda content : "<td>" + str(content) + "</td>",
    'addCssFile' : lambda link : css.append(link),
    'link' : lambda content : "<a href='" + str(content[1]) + "'>" + str(content[0]) + "</a>",
    'len' : lambda array : len(array)
}

operator = {
    '<' : lambda x, y: x < y,
    '>' : lambda x, y: x > y,
    '<=' : lambda x, y: x <= y,
    '>=' : lambda x, y: x >= y,
    '+' : lambda x, y: x + y,
    '-' : lambda x, y: x - y,
    '*' : lambda x, y: x * y,
    '/' : lambda x, y: x / y,
    '==' : lambda x, y: x == y,
    '!=' : lambda x, y: x != y,
    '%' : lambda x, y: int(x) % int(y)
}

footer = "</div></body></html>"

@addToClass(AST.ProgramNode)
def compile(self):
    bytecode = ""
    for child in self.children:
        bytecode += child.compile()
    return bytecode

@addToClass(AST.FunctionNode)
def compile(self):

    if len(self.children) == 1:
        parameters = self.children[0].compile()
    else:
        parameters = []
        for child in self.children:
            parameters.append(child.compile())

    result = functions[self.name](parameters)
    if result != None:     
        return result
    return ""

@addToClass(AST.TokenNode)
def compile(self):
    return self.tok

@addToClass(AST.IdentifierNode)
def compile(self):
    return variables[self.tok]

@addToClass(AST.ArrayNode)
def compile(self):
    values = []
    for child in self.children:
        values.append(child.compile())
    return values

@addToClass(AST.ArrayValueNode)
def compile(self):
    array = self.children[0].compile()
    index = int(variables[self.children[1].compile()])
    return variables[array][index]

@addToClass(AST.AssignNode)
def compile(self):
    childName = self.children[0].tok
    childValue = self.children[1].compile()
    variables[childName] = childValue
    return ""

@addToClass(AST.OpNode)
def compile(self):
    x = self.children[0].compile()
    y = self.children[1].compile()

    result = operator[self.op](x, y)
    #print("%s %s %s = %s" % (x, self.op, y, result))
    return result

@addToClass(AST.WhileNode)
def compile(self):
    cond = self.children[0]
    body = self.children[1]
    bytecode = ""

    while cond.compile():
        bytecode += body.compile()

    return bytecode

@addToClass(AST.ForNode)
def compile(self):
    bytecode = ""

    init = self.children[0]
    cond = self.children[1]
    incr = self.children[2]
    body = self.children[3]

    init.compile()
    while cond.compile():
        bytecode += body.compile()
        incr.compile()

    return bytecode

@addToClass(AST.BulletedListNode)
def compile(self):
    bytecode = "<ul>"
    bytecode += self.children[0].compile()
    return bytecode + "</ul>"

@addToClass(AST.TableNode)
def compile(self):
    return "<table class='table'>" + self.children[0].compile() + "</table>"

@addToClass(AST.TableRowNode)
def compile(self):
    return "<tr>" + self.children[0].compile() + "</tr>"


@addToClass(AST.IfNode)
def compile(self):
    cond = self.children[0]
    body = self.children[1]

    bytecode = ""
    if cond.compile():
        bytecode += body.compile()

    return bytecode


def formHeader():
    bytecode = "<!DOCTYPE html>"
    bytecode += "<html><head>"
    bytecode += "<meta charset='utf-8'>"
    bytecode += "<title>SimplyML</title>"
    bytecode += "<meta name='viewport' content='width=device-width, initial-scale=1'>"

    bytecode += "<link rel='stylesheet' href='https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css' integrity='sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T' crossorigin='anonymous'>"
    for css_file in css:
        bytecode += "<link rel='stylesheet' href='" + css_file + "'>"
    bytecode += "</head>"
    bytecode += "<body><div class='container'>"

    return bytecode

if __name__ == "__main__":
    from parser_sml import parse
    import sys, os
    
    prog = open(sys.argv[1]).read()
    ast = parse(prog)
    compiled = ast.compile()

    compiled = formHeader() + compiled + footer

    name = os.path.splitext(sys.argv[1])[0]+'.html'
    outfile = open(name, 'w')
    outfile.write(compiled)
    outfile.close()

    print("Wrote output to " , name)
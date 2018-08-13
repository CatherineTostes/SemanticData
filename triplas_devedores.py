tabela_devedores = open('Tabela_Devedores.csv', 'r')
rdf_turtle = open('devedores.ttl', 'w')

prefix = ('@base <http://lodbr.ufrj.br/pgfn/> .\n@prefix rdf:<http://www.w3.org/1999/02/22-rdf-syntax-ns#> .\n' +
                '@prefix foaf:<http://xmlns.com/foaf/0.1/> .\n@prefix ex:<http://example.org/> .')

pgfn = '<http://lodbr.ufrj.br/pgfn/>'

gov_debts = '<http://lodbr.ufrj.br/ontologies/gov-debts#>'

rdf_turtle.write(prefix + '\n')
rdf_turtle.write('@prefix pgfn:' + pgfn + ' .\n')
rdf_turtle.write('@prefix gov_debts:' + gov_debts + ' .\n\n')

tipo = ''

count = 1

for line in tabela_devedores:
    if "CPF/CNPJ" not in line:

        line = line.split(';')

        id_devedor = line[0].replace('.', '').replace('-', '').replace('/', '')

        if len(id_devedor) == 14:
            tipo = 'Organization'
        else:
            tipo = 'Person'

        id_devedor = '<' + id_devedor + '> a foaf:' + tipo + ' ;'
        name = 'foaf:name \"' + line[1].strip() + '\" ;'
        document = 'foaf:document \"' + line[0].strip() + '\" ;'
        divida = 'gov_debts:devedor pgfn:divida' + str(count) + ' .'


        credor = 'pgfn:divida' + str(count) + ' gov_debts:credor pgfn:PGFN ;'
        valor = 'gov_debts:valor \"R$' + line[2].strip() + '\" .'

        count = count + 1

        rdf_turtle.write(id_devedor + '\n\t' + name + '\n\t' + document + '\n\t' + divida + '\n\n' + credor + '\n\t' + valor + '\n\n')
import subprocess #para executar comandos no prompt
import psycopg2 #para conexao com o postgres
import sys #utilizar parametros de entrada

#PARAMETROS NA LINHA DE COMANDO
#Para executar esse script: python2.7 mining.py PARAM1 PARAM2
#PARAM1 = nome do projeto como sera criado no postgres
#PARAM2 = 0 o nome da busca na base do GitCProc sera o mesmo do PARAM1
#         NOME_DO_PROJETO no GitCProc, quando o nome do projeto for muito extenso

#banco de dados onde sera gravada a analise
database='FerramentaAutomatica'
user='postgres'
password='toor'
schema='public'

#banco de dados onde foram gravados os dados do gitCproc
databaseBugs='covninfo'
userBugs='postgres'
passwordBugs='toor'
schemaBugs='covninfo'

#nome do projeto
projeto = str(sys.argv[1])

class Conexao(object):
    _db=None

    def __init__(self, mhost, db, usr, pwd):
        self._db = psycopg2.connect(host=mhost, database=db, user=usr,  password=pwd)

    def manipular(self, sql):
        try:
            cur=self._db.cursor()
            cur.execute(sql)
            cur.close()
            self._db.commit()
        except:
            return False
        return True

    def consultar(self, sql):
        rs=None
        try:
            cur=self._db.cursor()
            cur.execute(sql)
            rs=cur.fetchall()
        except:
            return None
        return rs

    def proximaPK(self, tabela, chave):
        try:
            sql='select max('+chave+') from '+tabela
            rs = self.consultar(sql)
            pk = rs[0][0]
            return pk+1
        except:
            return 1

    def fechar(self):
        self._db.close()

def identificarData(tag):#atraves do comando git show
    cmd = "git show | egrep -m 1 'Date:'" #pegar somente a linha onde existe a data atraves do comando git show
    ps = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    ps.wait()
    data = ps.communicate()[0]

    data = str(data).replace("Date:   ","")
    data = str(data).replace("Sun ", "")
    data = str(data).replace("Mon ", "")
    data = str(data).replace("Tue ", "")
    data = str(data).replace("Wed ", "")
    data = str(data).replace("Thu ", "")
    data = str(data).replace("Fri ", "")
    data = str(data).replace("Sat ", "")

    data = str(data).replace("Jan", "01")
    data = str(data).replace("Feb", "02")
    data = str(data).replace("Mar", "03")
    data = str(data).replace("Apr", "04")
    data = str(data).replace("May", "05")
    data = str(data).replace("Jun", "06")
    data = str(data).replace("Jul", "07")
    data = str(data).replace("Aug", "08")
    data = str(data).replace("Sep", "09")
    data = str(data).replace("Oct", "10")
    data = str(data).replace("Nov", "11")
    data = str(data).replace("Dec", "12")

    #extrair a data que esta no formato abaixo
    #01 28 13:35:52 2020 -0500
    #02 1 22:48:09 2014 +0000
    diaMes = data[0:str(data).rfind(":")-5]
    diaMes = diaMes.split(" ")
    mes = diaMes[0]
    dia = diaMes[1]
    #ano = data[str(data).rfind("-")-5:str(data).rfind("-")-1]
    ano = data[str(data).rfind(":") + 4:str(data).rfind(":") + 8]

    data = ano+ "-" + mes + "-" + dia
    return data

def identificarLOC():#atraves do da tool cloc
    cmd = "cloc ../" + projeto + " | egrep -m 1 'Java'" # contar o numero de testes na tag
    ps = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    ps.wait()
    loc = ps.communicate()[0]

    if loc[0] != 'J':
        loc = str(loc)[str(loc).rfind("Java  "):len(loc)]
    loc = str(loc)[str(loc).rfind(' '):len(str(loc)) - 1]  # retornar somente o numero referente ao LOC de java

    return loc

def criarSql(tag, testes, bugs, contrib, loc):
        data=identificarData(tag)
        sql = "insert into " + schema + "." + projeto + " values (default,"
        sql = sql + "'" + projeto + "',"
        sql = sql + "'" + str(tag) + "',"
        sql = sql + "'" + str(data) + "',"
        sql = sql +  str(testes) + ","
        sql = sql +  str(bugs) + ","
        sql = sql +  str(contrib) + ","
        sql = sql +  str(loc) + ")"
        return sql

#apaga a tabela do projeto no banco de dados postgres
con=Conexao('localhost',database,user,password)
sql = "drop table "+ schema + "." + projeto
if con.manipular(sql):
    print('tabela '+ schema + "." + projeto + ' DESTRUIDA com sucesso!')
con.fechar()

#cria a tabela do projeto no banco de dados postgres
con=Conexao('localhost',database,user,password)
sql = 'create table ' + schema + "." + projeto + ' (id serial primary key, projeto varchar(100), tag varchar(100), data date, testes integer, bugs integer, contributors integer, loc integer)'
if con.manipular(sql):
    print('tabela '+ schema + "." + projeto + ' CRIADA com sucesso!')
con.fechar()

#lista todas as tags de um projeto e armazena na variavel tags
list_tags = subprocess.Popen(["git", "tag"], stdout=subprocess.PIPE)
tags=set(list_tags.stdout)
count=1
con=Conexao('localhost',database,user,password)
for tag in tags:
    tag = str(tag).replace("\n", "")

    #git checkout - b [nomeQueQuiser] [tag]
    cmd = "git checkout -b t"+ tag + " " + tag  # criar o branch da tag e fazer o checkout
    ps = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    ps.wait()

    # git checkout - b [nomeQueQuiser]
    cmd = "git checkout -f t" + tag # mudar de tag
    ps = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    ps.wait()

    #git shortlog -s -n | wc -l
    cmd = "git shortlog -s -n | wc -l" #contar o numero de contributors na tag
    ps = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    ps.wait()
    contributors = ps.communicate()[0]
    contributors = str(contributors).replace("\n", "")

    # python3 script.py
    cmd = "python3 script.py "+ projeto  # contar o numero de testes na tag
    ps = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    ps.wait()
    testes = ps.communicate()[0]
    testes = str(testes).replace("\n", "")

    # executar cloc tool para identificar linhas de codigo java
    loc = identificarLOC() #extrair somente o loc de java

    sql=criarSql(tag,testes,-1,contributors,loc)
    print(sql)
    if con.manipular(sql):
        print('%d de %d inserido com sucesso!'%(count,len(tags)))
        count=count+1
con.fechar()

#acessar a base de mining, ler as datas das tags
#criar uma sql para buscar os bugs no BD do gitCproc
#fazer o update na base de mining com o numero de bugs para a tag
con=Conexao('localhost',database,user,password)

rs=con.consultar("SELECT * FROM " + schema + "." + projeto + " ORDER BY data, tag")
vetorDatas = list()
total=-1
for linha in rs: #preencher um vetor com as datas das releases
    vetorDatas.append(linha[3])
    total=total+1

count = 0
cbugs=0
for linha in rs:
    tag=linha[2]
    dataInicial = linha[3]
    if count<total:
        dataFinal = vetorDatas[count+1]
        count=count+1
    else:
        dataFinal = '2050-01-01' #data final para a tag mais recente

    #conectando ao BD do gitCproc
    projetoGitCProc=projeto
    if str(sys.argv[2]) != '0':
        projetoGitCProc = str(sys.argv[2])
    conBugs = Conexao('localhost', databaseBugs, userBugs, passwordBugs)
    sql="SELECT count(project) FROM "+ schemaBugs + ".change_summary WHERE is_bug=true AND commit_date >= '" + str(dataInicial) + "' AND commit_date < '"+ str(dataFinal) + "' AND project = '"+ projetoGitCProc + "'"
    print(sql)
    rsBugs = conBugs.consultar(sql)
    bug=int(rsBugs[0][0])
    conBugs.fechar()

    cbugs=cbugs+bug

    #atualizar a tabela mining com os bugs para cada tag
    conUpdate = Conexao('localhost', database, user, password)
    sql="UPDATE " + schema + "." + projeto + " set bugs = " + str(bug) + " where tag = '" + str(tag)+ "'"
    if conUpdate.manipular(sql):
        print(sql)
        print('Bugs atualizados com sucesso!')
        print('Total de bugs %d'%(cbugs))
    conUpdate.fechar()

con.fechar()

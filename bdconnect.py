import sqlite3
from time import strftime


class dbloja():
	def __init__(self):
		self.con = sqlite3.connect("bdloja.db")
		self.sql = self.con.cursor()
	def ncolum(self):
		dump1 = self.sql.execute("""SELECT rowid, *  FROM  clientes;""")
		number_lines = len(dump1.fetchall())#Number Lines
		return number_lines
	def nrow(self):
		try:
			dump = self.sql.execute("""SELECT rowid, *  FROM  clientes;""")
			row = int(len(dump.fetchone()))
			return row
		except Exception as e:
			self.sql.execute("""INSERT INTO clientes (name_users, number_users, value_users, date_users, date_venc_users, venci) VALUES ('','','','','', '');""")
			self.con.commit()			
	def dump(self):
		drop = self.sql.execute("""SELECT ROWID, *  FROM  clientes;""")
		date_time = strftime('%d/%m/%y').split("/", 2)
		d, m, y = date_time
		for i in drop.fetchall():
			da, mo, ye = i[5].split("/", 2)
			if y > ye:
				self.sql.execute("""UPDATE clientes SET venci = "venceu" WHERE ROWID = '{}'""".format(i[0]))
				self.con.commit()
			else:
				self.sql.execute("""UPDATE clientes SET venci = " " WHERE ROWID = '{}'""".format(i[0]))
				self.con.commit()
			if y == ye:
				if m > mo:
					self.sql.execute("""UPDATE clientes SET venci = "venceu" WHERE ROWID = '{}'""".format(i[0]))
					self.con.commit()
				else:
					self.sql.execute("""UPDATE clientes SET venci = "" WHERE ROWID = '{}'""".format(i[0]))
					self.con.commit()			
				if m == mo:
					if d >= da:
						self.sql.execute("""UPDATE clientes SET venci = "venceu" WHERE ROWID = '{}'""".format(i[0]))
						self.con.commit()
					else:
						self.sql.execute("""UPDATE clientes SET venci = "" WHERE ROWID = '{}'""".format(i[0]))
						self.con.commit()
		drop2 = self.sql.execute("""SELECT ROWID, *  FROM  clientes;""")
		return drop2.fetchall()
	def delete(self, dell):
		delet = str(dell)
		self.sql.execute("""DELETE from clientes where rowid like '{}%';""".format(delet))
		self.con.commit()
	def search(self, search):
		pes = str(search)
		ser = self.sql.execute("""SELECT rowid, * FROM clientes WHERE name_users LIKE '%{}%';""".format(pes))
		return ser.fetchall()
		#self.con.commit()
	def insert(self, name, number, value, date_buy, date_exced):
		al = str(name), str(number), str(value), str(date_buy), str(date_exced)
		try:
			self.sql.execute("""INSERT INTO clientes (name_users, number_users, value_users, date_users, date_venc_users, venci) VALUES (?, ?, ?, ?, ?, '');""", al)
			self.con.commit()
		except Exception as e:
			print("Erro ao inserir: ", e)
	def update(self, date_, value_ ,id_):#Função em construção 
		value = self.sql.execute("""UPDATE clientes SET date_venc_users = "{}"  where rowid = "{}";""".format(date_, id_))
		self.con.commit()
		self.sql.execute("""UPDATE clientes SET  value_users = '{}' where rowid = '{}';""".format(value_, id_))
		self.con.commit()
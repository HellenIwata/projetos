import webbrowser as wb
from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image

class Relatorios():
    def print_cliente(self):
        wb.open(f'D:\projetos\python\pdf_clientes_base\{self.name_rel}.pdf')
    
    def gera_relatorio_cliente(self):
        self.code_rel = self.ent_code.get()
        self.name_rel = self.ent_name.get()
        self.phone_rel = self.ent_phone.get()
        self.email_rel = self.ent_email.get()
        self.city_rel = self.ent_city.get()
        
        self.c = canvas.Canvas(f'D:\projetos\python\pdf_clientes_base\{self.name_rel}.pdf')
        
        #Definindo  a fonte e o tamanho da fonte
        self.c.setFont('Helvetica-Bold', 18)
        #Definindo o texto de titulo
        self.c.drawString(200, 780, 'Informações do Cliente')
        self.c.drawString(50, 710, f'Código: {self.code_rel}')
        self.c.line(50, 690, 550, 690) #Linha separadora de informações pessoais e contato
        
        
        self.c.setFont('Helvetica', 12)
        self.c.drawString(70, 660, f'Nome: {self.name_rel}')
        self.c.drawString(70, 630, f'Telefone: {self.phone_rel}')
        self.c.drawString(70, 600, f'E-mail: {self.email_rel}')
        self.c.drawString(70, 570, f'Cidade: {self.city_rel}')
        
        
        self.c.showPage()
        self.c.save()
        self.print_cliente()




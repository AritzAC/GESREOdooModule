# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

class Recoge(models.Model):
    _name='gesre.Recoge'
    
    horasEstimadas= fields.Integer(string="Horas Estimadas", required="true")
    fechaRecogida=fields.Date.today()
